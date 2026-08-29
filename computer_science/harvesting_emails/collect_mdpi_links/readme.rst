Python tool to harvest links of specific MDPI pdf papers
========================================================

  pip install requests beautifulsoup4
 pip install selenium webdriver-manager


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
    console.log(`\n✅ Found ${uniqueLinks.length} PDF links:`);
    console.log('='.repeat(60));
    uniqueLinks.forEach((link, i) => {
        console.log(`${i+1}. ${link}`);
    });

    // Copy to clipboard
    const linkText = uniqueLinks.join('\n');
    navigator.clipboard.writeText(linkText).then(() => {
        console.log(`\n📋 Copied ${uniqueLinks.length} links to clipboard!`);
        console.log('Paste them into a text file.');
    }).catch(err => {
        console.error('Failed to copy:', err);
        console.log('\nCopy the links manually from the console output above.');
    });

    // Return for further processing
    return uniqueLinks;
})();
