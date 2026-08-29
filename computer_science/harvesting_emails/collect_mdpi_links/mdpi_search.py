import requests
from bs4 import BeautifulSoup
import time
import re
from urllib.parse import urljoin, urlparse
import random
import logging
from typing import List, Optional, Dict
from dataclasses import dataclass
from datetime import datetime

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
    min_delay: float = 2.0
    max_delay: float = 5.0
    retry_delay: float = 10.0
    max_retries: int = 3
    
    # Request configuration
    timeout: int = 30
    user_agents: List[str] = None
    
    def __post_init__(self):
        if self.user_agents is None:
            self.user_agents = [
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/121.0",
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                "Mozilla/5.0 (iPhone; CPU iPhone OS 17_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Mobile/15E148 Safari/604.1"
            ]


class MDPIScraper:
    """MDPI web scraper with built-in delays and rate limiting"""
    
    def __init__(self, config: SearchConfig):
        self.config = config
        self.session = requests.Session()
        self.last_request_time = 0
        self.request_count = 0
        self.total_requests = 0
        
        # Set default headers
        self.session.headers.update({
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
        })
    
    def _get_random_user_agent(self) -> str:
        """Get a random user agent from the list"""
        return random.choice(self.config.user_agents)
    
    def _respect_rate_limit(self):
        """Implement rate limiting with jitter"""
        current_time = time.time()
        time_since_last = current_time - self.last_request_time
        
        # Add random jitter to avoid predictable patterns
        delay = random.uniform(self.config.min_delay, self.config.max_delay)
        
        if time_since_last < delay:
            sleep_time = delay - time_since_last + random.uniform(0, 0.5)
            logger.debug(f"Rate limiting: sleeping for {sleep_time:.2f} seconds")
            time.sleep(sleep_time)
        
        self.last_request_time = time.time()
        self.request_count += 1
        self.total_requests += 1
        
        # Log request count periodically
        if self.request_count % 10 == 0:
            logger.info(f"Total requests made: {self.total_requests}")
    
    def _make_request(self, url: str, retry_count: int = 0) -> Optional[requests.Response]:
        """Make HTTP request with retries and exponential backoff"""
        headers = {
            'User-Agent': self._get_random_user_agent(),
            'Referer': 'https://www.mdpi.com/'
        }
        
        try:
            self._respect_rate_limit()
            
            logger.debug(f"Making request to: {url}")
            response = self.session.get(
                url,
                headers=headers,
                timeout=self.config.timeout,
                allow_redirects=True
            )
            
            # Check for rate limiting (HTTP 429)
            if response.status_code == 429:
                logger.warning(f"Rate limited (429) on attempt {retry_count + 1}")
                if retry_count < self.config.max_retries:
                    wait_time = self.config.retry_delay * (2 ** retry_count) + random.uniform(0, 2)
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
                wait_time = self.config.retry_delay * (2 ** retry_count) + random.uniform(0, 2)
                logger.info(f"Retrying in {wait_time:.2f} seconds (attempt {retry_count + 1}/{self.config.max_retries})")
                time.sleep(wait_time)
                return self._make_request(url, retry_count + 1)
            return None
    
    def search(self) -> List[str]:
        """Execute the search and extract PDF links"""
        # Build the search URL
        import urllib.parse
        encoded_query = urllib.parse.quote(self.config.query)
        
        params = {
            "sort": self.config.sort,
            "page_no": self.config.page_no,
            "page_count": self.config.page_count,
            "year_from": self.config.year_from,
            "year_to": self.config.year_to,
            "q": encoded_query,
            "view": self.config.view
        }
        
        search_url = f"https://www.mdpi.com/search?{urllib.parse.urlencode(params)}"
        logger.info(f"Search URL: {search_url}")
        
        # Fetch the search results
        response = self._make_request(search_url)
        if not response:
            logger.error("Failed to fetch search results")
            return []
        
        logger.info(f"Response status: {response.status_code}")
        logger.info(f"Response size: {len(response.content)} bytes")
        
        # Parse HTML
        try:
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Find all PDF links
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
        
        # Method 1: Look for explicit PDF links
        for link in all_links:
            href = link.get('href', '')
            if href and ('pdf' in href.lower() or href.endswith('.pdf')):
                absolute_url = urljoin("https://www.mdpi.com", href)
                pdf_links.append(absolute_url)
                logger.debug(f"Found PDF link: {absolute_url}")
        
        # Method 2: Look for links with PDF pattern
        pdf_pattern = re.compile(r'\.pdf$|/pdf\?|/pdf$', re.IGNORECASE)
        for link in all_links:
            href = link.get('href', '')
            if href and pdf_pattern.search(href):
                absolute_url = urljoin("https://www.mdpi.com", href)
                if absolute_url not in pdf_links:
                    pdf_links.append(absolute_url)
                    logger.debug(f"Found PDF link (pattern): {absolute_url}")
        
        # Method 3: Look for article links that might have PDF versions
        article_pattern = re.compile(r'/\d+-\d+/\d+/\d+/\d+', re.IGNORECASE)
        for link in all_links:
            href = link.get('href', '')
            if href and article_pattern.search(href) and 'pdf' not in href:
                # This might be an article page that could have a PDF
                pdf_url = urljoin("https://www.mdpi.com", href)
                if pdf_url not in pdf_links:
                    # Try to construct PDF URL
                    if pdf_url.endswith('/'):
                        pdf_url = pdf_url.rstrip('/')
                    pdf_links.append(f"{pdf_url}/pdf")
                    logger.debug(f"Constructed PDF link: {pdf_links[-1]}")
        
        return pdf_links
    
    def get_statistics(self) -> Dict:
        """Get scraping statistics"""
        return {
            'total_requests': self.total_requests,
            'request_count': self.request_count,
            'last_request_time': self.last_request_time,
            'min_delay': self.config.min_delay,
            'max_delay': self.config.max_delay,
            'user_agents_count': len(self.config.user_agents)
        }


def main():
    """Main function to run the scraper"""
    # Create configuration with custom delays
    config = SearchConfig(
        query="First-principles calculations DFT",
        page_no=3,
        page_count=50,
        year_from=1996,
        year_to=2026,
        min_delay=2.0,  # Minimum 2 seconds between requests
        max_delay=5.0,  # Maximum 5 seconds between requests
        retry_delay=10.0,  # 10 seconds wait before retry
        max_retries=3
    )
    
    # Initialize scraper
    scraper = MDPIScraper(config)
    
    logger.info("Starting MDPI search...")
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
    print(f"Elapsed time: {elapsed_time:.2f}s")
    
    # Optional: Show sample user agents used
    print(f"\nSample user agents:")
    for ua in config.user_agents[:2]:
        print(f"  - {ua[:60]}...")


if __name__ == "__main__":
    main()
