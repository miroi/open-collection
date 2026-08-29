import requests
from bs4 import BeautifulSoup
import time
import re
from urllib.parse import urljoin, urlparse, quote
import random
import logging
from typing import List, Optional, Dict
from dataclasses import dataclass
from datetime import datetime
import hashlib
import json
import os

# Try to import selenium, but provide fallback
try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.chrome.service import Service
    from selenium.common.exceptions import TimeoutException, NoSuchElementException
    from webdriver_manager.chrome import ChromeDriverManager
    SELENIUM_AVAILABLE = True
except ImportError:
    SELENIUM_AVAILABLE = False
    print("⚠️  Selenium not installed. Install with: pip install selenium webdriver-manager")

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)


@dataclass
class SearchConfig:
    """Configuration for the MDPI search"""
    query: str = "First-principles calculations DFT"
    page_no: int = 3
    page_count: int = 50
    year_from: int = 1996
    year_to: int = 2026
    sort: str = "pubdate"
    view: str = "default"
    
    # Delay configuration (in seconds)
    min_delay: float = 3.0
    max_delay: float = 8.0
    retry_delay: float = 15.0
    max_retries: int = 3
    
    # Request configuration
    timeout: int = 30
    use_selenium: bool = False  # Set to True if requests fail
    headless: bool = True
    use_proxy: bool = False  # Optional: use proxy
    
    user_agents: List[str] = None
    
    def __post_init__(self):
        if self.user_agents is None:
            self.user_agents = [
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/121.0",
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Safari/605.1.15"
            ]


class MDPIScraper:
    """MDPI web scraper with multiple methods to bypass blocks"""
    
    def __init__(self, config: SearchConfig):
        self.config = config
        self.session = requests.Session()
        self.last_request_time = 0
        self.request_count = 0
        self.total_requests = 0
        self.driver = None
        
        # Setup session
        self._setup_session()
    
    def _setup_session(self):
        """Setup session with cookies and headers"""
        # Add cookies to appear more like a real browser
        self.session.cookies.set('MDPI_Language', 'en')
        self.session.cookies.set('MDPI_Currency', 'USD')
        
        # Headers with more realistic browser behavior
        self.session.headers.update({
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Cache-Control': 'max-age=0',
            'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        })
    
    def _get_random_user_agent(self) -> str:
        """Get a random user agent from the list"""
        return random.choice(self.config.user_agents)
    
    def _respect_rate_limit(self):
        """Implement rate limiting with jitter"""
        current_time = time.time()
        time_since_last = current_time - self.last_request_time
        
        if self.last_request_time > 0:
            delay = random.uniform(self.config.min_delay, self.config.max_delay)
            if time_since_last < delay:
                sleep_time = delay - time_since_last + random.uniform(0, 1.0)
                logger.debug(f"Rate limiting: sleeping for {sleep_time:.2f} seconds")
                time.sleep(sleep_time)
        
        self.last_request_time = time.time()
        self.request_count += 1
        self.total_requests += 1
        
        if self.request_count % 5 == 0:
            logger.info(f"Total requests made: {self.total_requests}")
    
    def _make_request(self, url: str, retry_count: int = 0) -> Optional[requests.Response]:
        """Make HTTP request with retries and exponential backoff"""
        headers = {
            'User-Agent': self._get_random_user_agent(),
            'Referer': 'https://www.mdpi.com/',
        }
        
        # Add proxy if configured
        proxies = None
        if self.config.use_proxy:
            proxies = {
                'http': 'http://proxy:8080',
                'https': 'https://proxy:8080'
            }
        
        try:
            self._respect_rate_limit()
            
            logger.debug(f"Making request to: {url}")
            response = self.session.get(
                url,
                headers=headers,
                timeout=self.config.timeout,
                allow_redirects=True,
                proxies=proxies
            )
            
            # Check for rate limiting (HTTP 429)
            if response.status_code == 429:
                logger.warning(f"Rate limited (429) on attempt {retry_count + 1}")
                if retry_count < self.config.max_retries:
                    wait_time = self.config.retry_delay * (2 ** retry_count) + random.uniform(0, 5)
                    logger.info(f"Waiting {wait_time:.2f} seconds before retry")
                    time.sleep(wait_time)
                    return self._make_request(url, retry_count + 1)
                else:
                    logger.error(f"Max retries reached for {url}")
                    return None
            
            # Check for 403 (Forbidden)
            if response.status_code == 403:
                logger.warning(f"Forbidden (403) on attempt {retry_count + 1}")
                if retry_count < self.config.max_retries:
                    # Try with different user agent and cookies
                    logger.info("Refreshing session and trying with different headers...")
                    self._refresh_session()
                    wait_time = self.config.retry_delay * (1.5 ** retry_count) + random.uniform(0, 5)
                    logger.info(f"Waiting {wait_time:.2f} seconds before retry")
                    time.sleep(wait_time)
                    return self._make_request(url, retry_count + 1)
                else:
                    logger.error(f"Max retries reached for {url}")
                    return None
            
            response.raise_for_status()
            return response
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Request failed: {e}")
            if retry_count < self.config.max_retries:
                wait_time = self.config.retry_delay * (2 ** retry_count) + random.uniform(0, 3)
                logger.info(f"Retrying in {wait_time:.2f} seconds (attempt {retry_count + 1}/{self.config.max_retries})")
                time.sleep(wait_time)
                return self._make_request(url, retry_count + 1)
            return None
    
    def _refresh_session(self):
        """Refresh session with new cookies and headers"""
        self.session = requests.Session()
        self._setup_session()
        # Add some random cookies
        random_cookie = hashlib.md5(str(random.random()).encode()).hexdigest()[:16]
        self.session.cookies.set('MDPI_Session', random_cookie)
    
    def search_with_selenium(self) -> List[str]:
        """Use Selenium to fetch the page (more reliable for JavaScript-heavy sites)"""
        if not SELENIUM_AVAILABLE:
            logger.error("Selenium is not installed. Install with: pip install selenium webdriver-manager")
            return []
        
        logger.info("Using Selenium to fetch page...")
        
        if not self._setup_selenium():
            logger.error("Failed to setup Selenium. Falling back to requests.")
            return self.search()
        
        try:
            url = self._build_search_url()
            logger.info(f"Loading URL with Selenium: {url}")
            
            self.driver.get(url)
            
            # Wait for content to load
            wait = WebDriverWait(self.driver, 20)
            
            # Wait for the search results to appear
            try:
                wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".article-item, .search-result, .article-entry")))
            except TimeoutException:
                logger.warning("Timeout waiting for search results, trying alternative selectors...")
                # Try to wait for any content
                time.sleep(5)
            
            # Get page source and parse
            html = self.driver.page_source
            soup = BeautifulSoup(html, 'html.parser')
            
            # Extract PDF links
            pdf_links = self._extract_pdf_links_selenium(soup)
            
            # Remove duplicates
            seen = set()
            unique_pdf_links = []
            for link in pdf_links:
                if link not in seen:
                    seen.add(link)
                    unique_pdf_links.append(link)
            
            logger.info(f"Extracted {len(unique_pdf_links)} unique PDF links with Selenium")
            return unique_pdf_links
            
        except Exception as e:
            logger.error(f"Error with Selenium: {e}")
            return []
        finally:
            if self.driver:
                self.driver.quit()
                self.driver = None
    
    def _setup_selenium(self) -> bool:
        """Setup Selenium WebDriver"""
        if not SELENIUM_AVAILABLE:
            return False
            
        try:
            chrome_options = Options()
            if self.config.headless:
                chrome_options.add_argument("--headless")
            
            # Add arguments to avoid detection
            chrome_options.add_argument("--disable-blink-features=AutomationControlled")
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-gpu")
            chrome_options.add_argument("--disable-web-security")
            chrome_options.add_argument("--disable-features=VizDisplayCompositor")
            chrome_options.add_argument("--disable-features=IsolateOrigins,site-per-process")
            
            # Add user agent
            user_agent = self._get_random_user_agent()
            chrome_options.add_argument(f"--user-agent={user_agent}")
            
            # Exclude automation flags
            chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
            chrome_options.add_experimental_option('useAutomationExtension', False)
            
            # Initialize driver with webdriver-manager
            service = Service(ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=service, options=chrome_options)
            self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
            
            logger.info("Selenium WebDriver setup successful")
            return True
            
        except Exception as e:
            logger.error(f"Failed to setup Selenium: {e}")
            logger.info("Please install ChromeDriver: https://chromedriver.chromium.org/")
            logger.info("Or install webdriver-manager: pip install webdriver-manager")
            return False
    
    def _build_search_url(self) -> str:
        """Build the search URL"""
        encoded_query = quote(self.config.query)
        return (f"https://www.mdpi.com/search?"
                f"sort={self.config.sort}"
                f"&page_no={self.config.page_no}"
                f"&page_count={self.config.page_count}"
                f"&year_from={self.config.year_from}"
                f"&year_to={self.config.year_to}"
                f"&q={encoded_query}"
                f"&view={self.config.view}")
    
    def search(self) -> List[str]:
        """Execute the search and extract PDF links"""
        search_url = self._build_search_url()
        logger.info(f"Search URL: {search_url}")
        
        # Try with requests first
        response = self._make_request(search_url)
        if not response:
            logger.warning("Requests failed. Trying Selenium...")
            return self.search_with_selenium()
        
        logger.info(f"Response status: {response.status_code}")
        logger.info(f"Response size: {len(response.content)} bytes")
        
        # Check if response is too small (might be blocked or captcha)
        if len(response.content) < 5000:
            logger.warning("Response size is very small. Might be blocked or captcha. Trying Selenium...")
            return self.search_with_selenium()
        
        # Parse HTML
        try:
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Check for captcha or blocked page
            if "captcha" in str(soup).lower() or "blocked" in str(soup).lower():
                logger.warning("Captcha or block detected. Trying Selenium...")
                return self.search_with_selenium()
            
            pdf_links = self._extract_pdf_links(soup)
            
            # Remove duplicates while preserving order
            seen = set()
            unique_pdf_links = []
            for link in pdf_links:
                if link not in seen:
                    seen.add(link)
                    unique_pdf_links.append(link)
            
            logger.info(f"Extracted {len(unique_pdf_links)} unique PDF links")
            return unique_pdf_links
            
        except Exception as e:
            logger.error(f"Error parsing HTML: {e}")
            return []
    
    def _extract_pdf_links(self, soup: BeautifulSoup) -> List[str]:
        """Extract PDF links from BeautifulSoup object"""
        pdf_links = []
        all_links = soup.find_all('a', href=True)
        
        # MDPI specific patterns
        patterns = [
            r'/\d+-\d+/\d+/\d+/pdf\?',  # PDF with version
            r'/\d+-\d+/\d+/\d+/pdf$',   # PDF without version
            r'/pdf\?version=\d+',       # Simple PDF with version
            r'\.pdf\?version=\d+',      # PDF file with version
            r'\.pdf$',                  # Direct PDF file
        ]
        
        combined_pattern = re.compile('|'.join(patterns), re.IGNORECASE)
        
        for link in all_links:
            href = link.get('href', '')
            if href and combined_pattern.search(href):
                absolute_url = urljoin("https://www.mdpi.com", href)
                if self._is_valid_pdf_url(absolute_url):
                    pdf_links.append(absolute_url)
                    logger.debug(f"Found PDF link: {absolute_url}")
        
        return pdf_links
    
    def _extract_pdf_links_selenium(self, soup: BeautifulSoup) -> List[str]:
        """Extract PDF links with Selenium (different approach)"""
        pdf_links = []
        
        # Find all article containers
        article_selectors = [
            '.article-item',
            '.search-result',
            '.article-entry',
            '.result-item',
            'article',
            '.item'
        ]
        
        for selector in article_selectors:
            articles = soup.select(selector)
            if articles:
                logger.info(f"Found {len(articles)} articles with selector: {selector}")
                break
        
        # Look for PDF links in each article
        all_links = soup.find_all('a', href=True)
        
        for link in all_links:
            href = link.get('href', '')
            # Look for PDF links or links that might lead to PDFs
            if 'pdf' in href.lower() or href.endswith('.pdf'):
                absolute_url = urljoin("https://www.mdpi.com", href)
                if self._is_valid_pdf_url(absolute_url):
                    pdf_links.append(absolute_url)
            elif 'article' in href.lower() and 'pdf' not in href.lower():
                # Try to construct PDF URL from article URL
                absolute_url = urljoin("https://www.mdpi.com", href)
                if '/html' in absolute_url:
                    pdf_url = absolute_url.replace('/html', '/pdf')
                    if self._is_valid_pdf_url(pdf_url):
                        pdf_links.append(pdf_url)
                elif absolute_url.endswith('/'):
                    pdf_url = absolute_url + 'pdf'
                    if self._is_valid_pdf_url(pdf_url):
                        pdf_links.append(pdf_url)
        
        return pdf_links
    
    def _is_valid_pdf_url(self, url: str) -> bool:
        """Check if the URL is a valid PDF URL"""
        # MDPI PDF URLs typically contain these patterns
        valid_patterns = [
            r'https://www\.mdpi\.com/\d+-\d+/\d+/\d+/pdf',
            r'https://www\.mdpi\.com/\d+-\d+/\d+/\d+/pdf\?',
            r'https://www\.mdpi\.com/\d+-\d+/\d+/\d+/pdf\?version=',
        ]
        
        for pattern in valid_patterns:
            if re.match(pattern, url):
                return True
        return False
    
    def get_statistics(self) -> Dict:
        """Get scraping statistics"""
        return {
            'total_requests': self.total_requests,
            'request_count': self.request_count,
            'last_request_time': self.last_request_time,
            'min_delay': self.config.min_delay,
            'max_delay': self.config.max_delay,
            'user_agents_count': len(self.config.user_agents),
            'using_selenium': self.config.use_selenium,
            'headless': self.config.headless,
            'selenium_available': SELENIUM_AVAILABLE
        }


def main():
    """Main function to run the scraper"""
    print("\n" + "="*80)
    print("MDPI PDF LINK SCRAPER")
    print("="*80)
    print(f"Selenium available: {SELENIUM_AVAILABLE}")
    
    # First try with enhanced requests
    config = SearchConfig(
        query="First-principles calculations DFT",
        page_no=3,
        page_count=50,
        year_from=1996,
        year_to=2026,
        min_delay=3.0,
        max_delay=8.0,
        retry_delay=15.0,
        max_retries=3,
        use_selenium=False,  # Start with requests, fallback to Selenium if needed
        headless=True
    )
    
    # Initialize scraper
    scraper = MDPIScraper(config)
    
    logger.info("Starting MDPI search with enhanced anti-blocking measures...")
    logger.info(f"Query: {config.query}")
    logger.info(f"Page: {config.page_no}, Results per page: {config.page_count}")
    logger.info(f"Year range: {config.year_from}-{config.year_to}")
    logger.info(f"Delay range: {config.min_delay}-{config.max_delay} seconds")
    
    # Perform search
    start_time = time.time()
    pdf_links = scraper.search()
    elapsed_time = time.time() - start_time
    
    # Print results
    print("\n" + "="*80)
    print(f"SEARCH RESULTS")
    print("="*80)
    
    if pdf_links:
        print(f"\n✅ Found {len(pdf_links)} PDF links (took {elapsed_time:.2f} seconds):")
        print("-"*80)
        for i, link in enumerate(pdf_links, 1):
            print(f"{i:3d}. {link}")
        
        # Save to file with timestamp
        filename = f"mdpi_pdf_links_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(filename, "w") as f:
            f.write(f"# MDPI PDF Links\n")
            f.write(f"# Query: {config.query}\n")
            f.write(f"# Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"# Total: {len(pdf_links)}\n")
            f.write("#" + "="*79 + "\n\n")
            for link in pdf_links:
                f.write(link + "\n")
        
        print(f"\n💾 Links saved to: {filename}")
        
    else:
        print("\n❌ No PDF links found.")
        print("Possible reasons:")
        print("  - The search returned no results")
        print("  - The website structure has changed")
        print("  - You might be rate-limited or blocked")
        print("  - The page might require JavaScript to render")
        if SELENIUM_AVAILABLE:
            print("\n💡 Try forcing Selenium with:")
            print("  config.use_selenium = True")
        else:
            print("\n💡 Install Selenium to bypass blocks:")
            print("  pip install selenium webdriver-manager")
            print("  Then set config.use_selenium = True")
    
    # Print statistics
    stats = scraper.get_statistics()
    print("\n" + "="*80)
    print("SCRAPING STATISTICS")
    print("="*80)
    print(f"Total requests made: {stats['total_requests']}")
    print(f"Requests in this session: {stats['request_count']}")
    print(f"Minimum delay: {stats['min_delay']:.1f}s")
    print(f"Maximum delay: {stats['max_delay']:.1f}s")
    print(f"User agents available: {stats['user_agents_count']}")
    print(f"Selenium available: {stats['selenium_available']}")
    print(f"Using Selenium: {stats['using_selenium']}")
    print(f"Headless mode: {stats['headless']}")
    print(f"Elapsed time: {elapsed_time:.2f}s")


if __name__ == "__main__":
    main()
