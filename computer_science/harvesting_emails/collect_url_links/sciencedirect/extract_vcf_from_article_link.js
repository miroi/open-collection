// ============================================================
// FIXED: EMAIL EXTRACTOR WITH AUTO-DOWNLOAD
// ============================================================
// This version fixes the filename issue.
// ============================================================

async function extractAllEmails() {
    console.log("🔍 Extracting all valid emails from this page...");
    
    const allEmails = new Set();
    
    // Function to find ALL email icons on the page
    function findAllEmailIcons() {
        const icons = [];
        const seenIcons = new Set();
        
        const potentialIcons = document.querySelectorAll('button, a, [role="button"], [class*="email"], [class*="envelope"]');
        
        for (const icon of potentialIcons) {
            const isEmailIcon = 
                icon.querySelector('svg[data-icon="envelope"]') ||
                icon.querySelector('svg[data-icon="email"]') ||
                icon.querySelector('.fa-envelope') ||
                icon.getAttribute('aria-label')?.toLowerCase().includes('email') ||
                icon.getAttribute('title')?.toLowerCase().includes('email') ||
                icon.classList.contains('email-icon') ||
                icon.classList.contains('envelope-icon') ||
                icon.innerHTML?.toLowerCase().includes('envelope') ||
                icon.getAttribute('data-track-action') === 'email' ||
                icon.getAttribute('data-track')?.includes('email');
            
            if (isEmailIcon && icon.offsetParent !== null) {
                const rect = icon.getBoundingClientRect();
                const key = `${Math.round(rect.left / 10)},${Math.round(rect.top / 10)}`;
                
                if (!seenIcons.has(key)) {
                    seenIcons.add(key);
                    icons.push({
                        icon: icon,
                        position: { left: rect.left, top: rect.top },
                        key: key
                    });
                }
            }
        }
        
        return icons;
    }
    
    // Function to wait for panel
    function waitForPanel(timeout = 5000) {
        return new Promise((resolve) => {
            const startTime = Date.now();
            const checkInterval = setInterval(() => {
                const panelSelectors = [
                    '.action-panel',
                    '.popup',
                    '.modal',
                    '.dialog',
                    '.sidebar',
                    '[role="dialog"]',
                    '[role="popup"]',
                    '.flyout',
                    '[class*="panel"]',
                    '[class*="overlay"]',
                    '.action-sidebar',
                    '.right-panel',
                    '.side-panel'
                ];
                
                for (const selector of panelSelectors) {
                    const panels = document.querySelectorAll(selector);
                    for (const panel of panels) {
                        const style = window.getComputedStyle(panel);
                        if (style.display !== 'none' && 
                            style.visibility !== 'hidden' && 
                            panel.offsetParent !== null &&
                            panel.offsetWidth > 50) {
                            const text = panel.innerText || '';
                            const hasEmail = text.includes('@') || 
                                           panel.querySelector('a[href^="mailto:"]');
                            if (hasEmail) {
                                clearInterval(checkInterval);
                                resolve(panel);
                                return;
                            }
                        }
                    }
                }
                
                const mailtoLinks = document.querySelectorAll('a[href^="mailto:"]');
                for (const link of mailtoLinks) {
                    if (link.offsetParent !== null) {
                        clearInterval(checkInterval);
                        resolve(link);
                        return;
                    }
                }
                
                if (Date.now() - startTime > timeout) {
                    clearInterval(checkInterval);
                    resolve(null);
                }
            }, 200);
        });
    }
    
    // Function to extract and validate email from panel
    function extractEmailFromPanel(panel) {
        if (!panel) return null;
        
        const emails = [];
        
        // Check mailto links (most reliable)
        const mailtoLinks = panel.querySelectorAll('a[href^="mailto:"]');
        mailtoLinks.forEach(link => {
            const href = link.getAttribute('href');
            if (href) {
                let email = href.replace('mailto:', '').split('?')[0];
                email = cleanAndValidateEmail(email);
                if (email) {
                    emails.push(email);
                }
            }
        });
        
        // Check text content
        const text = panel.innerText || panel.textContent || '';
        const emailRegex = /[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}/g;
        const matches = text.match(emailRegex);
        if (matches) {
            matches.forEach(email => {
                const cleaned = cleanAndValidateEmail(email);
                if (cleaned) {
                    emails.push(cleaned);
                }
            });
        }
        
        // Remove duplicates
        return [...new Set(emails)];
    }
    
    // Function to clean and validate email addresses
    function cleanAndValidateEmail(email) {
        if (!email) return null;
        
        // Remove common artifacts
        let cleaned = email
            .replace(/More$/i, '')           // Remove "More" suffix
            .replace(/^[^@]*?\./, '')        // Remove prefixes like "China."
            .replace(/^[^@]*?\./, '')        // Remove multiple prefixes
            .replace(/^[^@]*?\./, '')        // Remove up to 3 prefixes
            .trim();
        
        // Remove any trailing punctuation
        cleaned = cleaned.replace(/[.,;!?]$/, '');
        
        // Validate email format
        const validPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
        if (validPattern.test(cleaned)) {
            return cleaned;
        }
        
        return null;
    }
    
    // ============================================================
    // FIXED: AUTO-DOWNLOAD FUNCTION
    // ============================================================
    function autoDownloadVCF(emails) {
        if (!emails || emails.length === 0) {
            console.log("❌ No emails to download");
            return;
        }
        
        const uniqueEmails = [...new Set(emails)];
        
        // Create VCF contacts
        const vcfContacts = uniqueEmails.map((email) => {
            const name = email.split('@')[0].replace(/[._-]/g, ' ').replace(/\b\w/g, l => l.toUpperCase());
            const nameParts = name.split(' ');
            const firstName = nameParts[0] || 'Unknown';
            const lastName = nameParts.slice(1).join(' ') || 'Researcher';
            
            return `BEGIN:VCARD
VERSION:3.0
FN:${firstName} ${lastName}
N:${lastName};${firstName};;;
EMAIL;TYPE=INTERNET,WORK:${email}
SOURCE:ScienceDirect Article
REV:${new Date().toISOString().replace(/[-:]/g, '').split('.')[0]}Z
END:VCARD`;
        });
        
        const allVCF = vcfContacts.join('\n\n');
        
        // FIXED: Generate safe filename
        const timestamp = new Date().toISOString().replace(/[:.]/g, '-').slice(0, 19);
        
        // Get article title safely - if it's the script itself, use a default
        let articleTitle = 'article';
        try {
            if (document.title && document.title.length > 0 && document.title.length < 200) {
                // Only use valid title, not the script content
                const title = document.title.replace(/[^a-zA-Z0-9]/g, '_').slice(0, 30);
                if (title.length > 2 && !title.includes('=')) {
                    articleTitle = title;
                }
            }
        } catch(e) {
            // Fallback to default
        }
        
        // Ensure filename is safe
        const filename = `emails_${articleTitle}_${timestamp}.vcf`;
        // Remove any special characters that might cause issues
        const safeFilename = filename.replace(/[^a-zA-Z0-9._-]/g, '_');
        
        // Store in localStorage
        localStorage.setItem('lastExtractedEmails', JSON.stringify(uniqueEmails));
        localStorage.setItem('lastVCFContent', allVCF);
        
        // Create and download the file
        const blob = new Blob([allVCF], {type: 'text/vcard;charset=utf-8'});
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = safeFilename;
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
        URL.revokeObjectURL(url);
        
        console.log(`📥 Auto-downloaded: ${safeFilename}`);
        console.log(`📧 Contains ${uniqueEmails.length} email(s)`);
        
        return uniqueEmails;
    }
    
    // ============================================================
    // MAIN EXTRACTION LOGIC
    // ============================================================
    
    // Find ALL email icons
    let allIcons = findAllEmailIcons();
    
    // Remove duplicates
    const uniqueIcons = [];
    const seenPositions = new Set();
    for (const item of allIcons) {
        if (!seenPositions.has(item.key)) {
            seenPositions.add(item.key);
            uniqueIcons.push(item);
        }
    }
    allIcons = uniqueIcons;
    
    console.log(`📝 Found ${allIcons.length} unique email icons`);
    
    if (allIcons.length === 0) {
        console.log("❌ No email icons found.");
        console.log("\n💡 Try the manual approach:");
        console.log("  1. Click the envelope icon next to an author name");
        console.log("  2. Run: extractFromOpenPanel()");
        return [];
    }
    
    // Process each icon
    for (let i = 0; i < allIcons.length; i++) {
        const item = allIcons[i];
        
        console.log(`\n📌 Processing icon ${i + 1}/${allIcons.length}`);
        
        item.icon.scrollIntoView({ behavior: 'smooth', block: 'center' });
        await new Promise(resolve => setTimeout(resolve, 500));
        
        console.log("  🖱️ Clicking email icon...");
        try {
            if (typeof item.icon.click === 'function') {
                item.icon.click();
            } else {
                const event = new MouseEvent('click', {
                    view: window,
                    bubbles: true,
                    cancelable: true
                });
                item.icon.dispatchEvent(event);
            }
        } catch (e) {
            console.log(`  ❌ Failed to click: ${e.message}`);
            continue;
        }
        
        console.log("  ⏳ Waiting for panel...");
        const panel = await waitForPanel(5000);
        
        if (panel) {
            console.log("  ✅ Panel opened!");
            const emails = extractEmailFromPanel(panel);
            
            if (emails && emails.length > 0) {
                emails.forEach(email => {
                    if (!allEmails.has(email)) {
                        allEmails.add(email);
                        console.log(`  ✅ Found valid email: ${email}`);
                    } else {
                        console.log(`  ⚠️ Email ${email} already found`);
                    }
                });
            } else {
                console.log("  ❌ No valid email found in the panel");
            }
            
            // Close the panel
            const closeBtns = panel.querySelectorAll('[aria-label*="close" i], .close, .btn-close, [class*="close"]');
            let closed = false;
            for (const btn of closeBtns) {
                try {
                    btn.click();
                    closed = true;
                    break;
                } catch (e) {}
            }
            if (!closed) {
                document.body.click();
            }
            await new Promise(resolve => setTimeout(resolve, 500));
            
        } else {
            console.log("  ⏰ No panel appeared");
        }
        
        if (i < allIcons.length - 1) {
            const waitTime = 2000 + Math.random() * 1000;
            console.log(`  ⏳ Waiting ${Math.round(waitTime/1000)}s...`);
            await new Promise(resolve => setTimeout(resolve, waitTime));
        }
    }
    
    // ============================================================
    // RESULTS AND AUTO-DOWNLOAD
    // ============================================================
    console.log("\n" + "=".repeat(80));
    console.log("📊 EXTRACTION COMPLETE");
    console.log("=".repeat(80));
    
    const uniqueEmails = Array.from(allEmails);
    
    if (uniqueEmails.length > 0) {
        console.log(`✅ Found ${uniqueEmails.length} valid unique email(s):\n`);
        uniqueEmails.forEach((email, index) => {
            console.log(`${index + 1}. ${email}`);
        });
        
        console.log("\n📧 EMAIL LIST (copy this):");
        console.log("-".repeat(60));
        console.log(uniqueEmails.join('\n'));
        console.log("-".repeat(60));
        
        // ============================================================
        // AUTO-DOWNLOAD VCF
        // ============================================================
        console.log("\n📥 Auto-downloading VCF file...");
        autoDownloadVCF(uniqueEmails);
        
        console.log("\n📁 To download again, run: downloadEmails()");
        
    } else {
        console.log("❌ No valid emails were found.");
        console.log("\n💡 Try the manual approach:");
        console.log("  1. Click the envelope icon next to an author name");
        console.log("  2. Run: extractFromOpenPanel()");
    }
    
    return uniqueEmails;
}

// ============================================================
// DOWNLOAD FUNCTION (can be called manually)
// ============================================================
function downloadEmails(emailsArray) {
    // If no emails provided, try to get from localStorage or the last extraction
    if (!emailsArray || emailsArray.length === 0) {
        // Try to get from the last extraction result
        const stored = localStorage.getItem('lastExtractedEmails');
        if (stored) {
            try {
                emailsArray = JSON.parse(stored);
            } catch(e) {}
        }
    }
    
    if (!emailsArray || emailsArray.length === 0) {
        console.log("❌ No emails to download. Run extractAllEmails() first.");
        return;
    }
    
    const uniqueEmails = [...new Set(emailsArray)];
    
    // Create VCF contacts
    const vcfContacts = uniqueEmails.map((email) => {
        const name = email.split('@')[0].replace(/[._-]/g, ' ').replace(/\b\w/g, l => l.toUpperCase());
        const nameParts = name.split(' ');
        const firstName = nameParts[0] || 'Unknown';
        const lastName = nameParts.slice(1).join(' ') || 'Researcher';
        
        return `BEGIN:VCARD
VERSION:3.0
FN:${firstName} ${lastName}
N:${lastName};${firstName};;;
EMAIL;TYPE=INTERNET,WORK:${email}
SOURCE:ScienceDirect Article
REV:${new Date().toISOString().replace(/[-:]/g, '').split('.')[0]}Z
END:VCARD`;
    });
    
    const allVCF = vcfContacts.join('\n\n');
    
    // FIXED: Generate safe filename
    const timestamp = new Date().toISOString().replace(/[:.]/g, '-').slice(0, 19);
    
    // Get article title safely
    let articleTitle = 'article';
    try {
        if (document.title && document.title.length > 0 && document.title.length < 200) {
            const title = document.title.replace(/[^a-zA-Z0-9]/g, '_').slice(0, 30);
            if (title.length > 2 && !title.includes('=')) {
                articleTitle = title;
            }
        }
    } catch(e) {}
    
    // Ensure filename is safe
    const filename = `emails_${articleTitle}_${timestamp}.vcf`;
    const safeFilename = filename.replace(/[^a-zA-Z0-9._-]/g, '_');
    
    // Download
    const blob = new Blob([allVCF], {type: 'text/vcard;charset=utf-8'});
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = safeFilename;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
    
    console.log(`📥 Downloaded: ${safeFilename}`);
    console.log(`📧 Contains ${uniqueEmails.length} email(s)`);
    
    return uniqueEmails;
}

// ============================================================
// HELPER: Extract from an already open panel
// ============================================================
function extractFromOpenPanel() {
    console.log("🔍 Looking for valid email in open panel...");
    
    const panelSelectors = [
        '.action-panel',
        '.popup',
        '.modal',
        '.dialog',
        '.sidebar',
        '[role="dialog"]',
        '[role="popup"]',
        '[class*="panel"]'
    ];
    
    let panel = null;
    for (const selector of panelSelectors) {
        const p = document.querySelector(selector);
        if (p && p.offsetParent !== null && p.offsetWidth > 50) {
            panel = p;
            break;
        }
    }
    
    if (!panel) {
        console.log("❌ No open panel found. Make sure the panel is open.");
        console.log("💡 Click the envelope icon next to an author name first.");
        return;
    }
    
    console.log("✅ Panel found!");
    const text = panel.innerText || panel.textContent || '';
    
    // Check mailto links
    const mailtoLinks = panel.querySelectorAll('a[href^="mailto:"]');
    const emails = [];
    
    mailtoLinks.forEach(link => {
        const href = link.getAttribute('href');
        if (href) {
            let email = href.replace('mailto:', '').split('?')[0];
            email = email.replace(/More$/i, '').trim();
            if (email && email.includes('@')) {
                emails.push(email);
                console.log(`📧 Found mailto email: ${email}`);
            }
        }
    });
    
    // Check text content
    const emailRegex = /[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}/g;
    const matches = text.match(emailRegex);
    if (matches) {
        matches.forEach(email => {
            let cleaned = email.replace(/More$/i, '').trim();
            cleaned = cleaned.replace(/^[^@]*?\./, '');
            if (cleaned && cleaned.includes('@') && !emails.includes(cleaned)) {
                emails.push(cleaned);
                console.log(`📧 Found text email: ${cleaned}`);
            }
        });
    }
    
    if (emails.length === 0) {
        console.log("❌ No valid email found in the panel.");
        console.log("📝 Full panel content:", text);
        return;
    }
    
    const uniqueEmails = [...new Set(emails)];
    
    console.log(`\n📧 Found ${uniqueEmails.length} valid email(s):`);
    uniqueEmails.forEach((email, i) => {
        console.log(`  ${i+1}. ${email}`);
    });
    
    // Create VCF
    const email = uniqueEmails[0];
    const name = email.split('@')[0].replace(/[._-]/g, ' ').replace(/\b\w/g, l => l.toUpperCase());
    const nameParts = name.split(' ');
    const firstName = nameParts[0] || 'Unknown';
    const lastName = nameParts.slice(1).join(' ') || 'Researcher';
    
    const vcf = `BEGIN:VCARD
VERSION:3.0
FN:${firstName} ${lastName}
N:${lastName};${firstName};;;
EMAIL;TYPE=INTERNET,WORK:${email}
SOURCE:ScienceDirect Article
REV:${new Date().toISOString().replace(/[-:]/g, '').split('.')[0]}Z
END:VCARD`;
    
    console.log("\n📇 VCF CONTACT:");
    console.log("-".repeat(60));
    console.log(vcf);
    console.log("-".repeat(60));
    
    navigator.clipboard.writeText(vcf).then(() => {
        console.log("✅ VCF copied to clipboard!");
    }).catch(() => {
        console.log("⚠️ Could not copy. Please copy manually.");
    });
    
    return uniqueEmails;
}

// ============================================================
// AUTO-RUN: Extract and download
// ============================================================
console.log("\n" + "=".repeat(80));
console.log("📧 EMAIL EXTRACTOR WITH AUTO-DOWNLOAD (FIXED)");
console.log("=".repeat(80));
console.log("\nCommands:");
console.log("  extractAllEmails()  - Extract emails and auto-download VCF");
console.log("  downloadEmails()    - Download VCF from last extraction");
console.log("  extractFromOpenPanel() - Extract from already open panel");
console.log("=".repeat(80));

// Run the extraction
extractAllEmails();
