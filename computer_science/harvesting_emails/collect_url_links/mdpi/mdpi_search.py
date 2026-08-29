import re
import json
from datetime import datetime
from typing import List

class MDPILinkExtractor:
    """Helper class for processing manually extracted links"""
    
    @staticmethod
    def process_extracted_links(raw_links: str) -> List[str]:
        """
        Process links extracted from the browser console
        
        Args:
            raw_links: String containing links (one per line)
        
        Returns:
            Cleaned list of PDF links
        """
        # Split by newlines and clean
        links = [link.strip() for link in raw_links.split('\n') if link.strip()]
        
        # Filter for MDPI PDF links
        pdf_links = []
        for link in links:
            if 'mdpi.com' in link and ('pdf' in link.lower() or '/article/' in link.lower()):
                # Convert article links to PDF links
                if '/article/' in link:
                    pdf_link = link.replace('/article/', '/pdf/')
                    if not pdf_link.endswith('/'):
                        pdf_link = pdf_link + '/'
                    pdf_links.append(pdf_link)
                else:
                    pdf_links.append(link)
        
        # Remove duplicates while preserving order
        seen = set()
        unique_links = []
        for link in pdf_links:
            if link not in seen:
                seen.add(link)
                unique_links.append(link)
        
        return unique_links
    
    @staticmethod
    def save_links(links: List[str], filename: str = None):
        """Save links to file"""
        if not filename:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = f"mdpi_pdf_links_{timestamp}.txt"
        
        with open(filename, 'w') as f:
            f.write(f"# MDPI PDF Links\n")
            f.write(f"# Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"# Total: {len(links)}\n")
            f.write("#" + "="*79 + "\n\n")
            for link in links:
                f.write(link + "\n")
        
        print(f"✅ Saved {len(links)} links to {filename}")
        return filename


def print_javascript_extractor():
    """Print the JavaScript code to extract links from the browser"""
    print("""
================================================================================
📋 JAVASCRIPT EXTRACTOR - Copy and paste this into your browser's DevTools
================================================================================

// Enhanced PDF link extractor for MDPI
(function() {
    console.log('🔍 Extracting PDF links from MDPI...');
    
    const pdfLinks = new Set();
    const articleLinks = new Set();
    
    // Method 1: Direct PDF links
    document.querySelectorAll('a[href*="pdf"]').forEach(a => {
        if (a.href && a.href.includes('mdpi.com')) {
            pdfLinks.add(a.href);
        }
    });
    
    // Method 2: Article links (convert to PDF)
    document.querySelectorAll('a[href*="/article/"]').forEach(a => {
        if (a.href && a.href.includes('mdpi.com')) {
            const pdfUrl = a.href.replace('/article/', '/pdf/');
            articleLinks.add(pdfUrl.endsWith('/') ? pdfUrl : pdfUrl + '/');
        }
    });
    
    // Method 3: Links within article items
    document.querySelectorAll('.article-item a, .search-result a, .result-item a').forEach(a => {
        if (a.href && a.href.includes('mdpi.com')) {
            if (a.href.includes('pdf')) {
                pdfLinks.add(a.href);
            } else if (a.href.includes('/article/')) {
                const pdfUrl = a.href.replace('/article/', '/pdf/');
                articleLinks.add(pdfUrl.endsWith('/') ? pdfUrl : pdfUrl + '/');
            }
        }
    });
    
    // Combine all links
    const allLinks = [...pdfLinks, ...articleLinks];
    const uniqueLinks = [...new Set(allLinks)];
    
    // Display results
    console.log(`\\n✅ Found ${uniqueLinks.length} PDF links:`);
    console.log('='.repeat(60));
    uniqueLinks.forEach((link, i) => {
        console.log(`${i+1}. ${link}`);
    });
    
    // Copy to clipboard
    const linkText = uniqueLinks.join('\\n');
    navigator.clipboard.writeText(linkText).then(() => {
        console.log(`\\n📋 Copied ${uniqueLinks.length} links to clipboard!`);
        console.log('Paste them into a text file.');
    }).catch(err => {
        console.error('Failed to copy:', err);
        console.log('\\nCopy the links manually from the console output above.');
    });
    
    // Return for further processing
    return uniqueLinks;
})();

================================================================================
📝 INSTRUCTIONS:
1. Open the MDPI search page in your browser
2. Press F12 to open DevTools
3. Go to the Console tab
4. Paste the JavaScript code above
5. Press Enter to run it
6. The links will be copied to your clipboard
7. Paste them into a text file

================================================================================
""")


def main():
    """Main function"""
    print("\n" + "="*80)
    print("🔍 MDPI PDF LINK EXTRACTOR")
    print("="*80)
    
    print("\nSince MDPI is blocking automated requests, use this semi-automated method:")
    
    while True:
        print("\n" + "-"*80)
        print("Options:")
        print("  1. Show JavaScript extractor code")
        print("  2. Process links from clipboard/file")
        print("  3. Exit")
        
        choice = input("\nSelect option (1-3): ").strip()
        
        if choice == '1':
            print_javascript_extractor()
        
        elif choice == '2':
            print("\n📋 Paste the links (one per line, press Ctrl+D when done):")
            lines = []
            try:
                while True:
                    line = input()
                    lines.append(line)
            except EOFError:
                pass
            
            if lines:
                raw_text = '\n'.join(lines)
                extractor = MDPILinkExtractor()
                links = extractor.process_extracted_links(raw_text)
                
                if links:
                    print(f"\n✅ Processed {len(links)} unique PDF links:")
                    print("-"*80)
                    for i, link in enumerate(links, 1):
                        print(f"{i:3d}. {link}")
                    
                    filename = extractor.save_links(links)
                    print(f"\n💾 Links saved to {filename}")
                else:
                    print("\n❌ No valid PDF links found. Make sure you copied the links correctly.")
            else:
                print("\n❌ No input provided.")
        
        elif choice == '3':
            print("\nGoodbye!")
            break
        
        else:
            print("\n❌ Invalid option. Please choose 1, 2, or 3.")


if __name__ == "__main__":
    main()
