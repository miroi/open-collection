// ============================================================
// TARGETED: Find and click the Person+Envelope icon
// ============================================================

function openArticlesWithDetector(count = 0) {
    // AUTO-CLEAR: Clear old emails before starting
    clearEmails();
    
    const links = [];
    const selectors = [
        'a[href*="/science/article/pii/"]',
        'a[href*="/science/article/abs/"]',
        'a[href*="/science/article/"]',
        'a[href*="pii/"]',
        '.result-item a[href*="/science/article/"]',
        '.search-result a[href*="/science/article/"]',
        '.article-link',
        '.title a',
        '.result-title a',
        'h2 a',
        '.js-article-title a'
    ];
    
    for (const selector of selectors) {
        const elements = document.querySelectorAll(selector);
        for (const el of elements) {
            let href = el.getAttribute('href');
            if (href && (href.includes('/science/article/') || href.includes('pii/'))) {
                const fullUrl = href.startsWith('http') ? href : `https://www.sciencedirect.com${href}`;
                if (!links.includes(fullUrl)) {
                    links.push(fullUrl);
                }
            }
        }
    }
    
    let totalToOpen = count;
    if (totalToOpen === 0 || totalToOpen > links.length) {
        totalToOpen = links.length;
    }
    
    console.log(`📝 Found ${links.length} articles total`);
    console.log(`📌 Opening ${totalToOpen} article(s)`);
    console.log(`👤 Looking for Person+Envelope icons...`);
    
    const batchSize = 3;
    let openedCount = 0;
    
    function openNextBatch() {
        const endIndex = Math.min(openedCount + batchSize, totalToOpen);
        
        for (let i = openedCount; i < endIndex; i++) {
            const newTab = window.open(links[i], '_blank');
            console.log(`  📌 Opened ${i + 1}/${totalToOpen}`);
            
            if (newTab) {
                setTimeout(() => {
                    try {
                        const script = newTab.document.createElement('script');
                        script.textContent = `
                            // ============================================================
                            // TARGETED: Find Person+Envelope icon
                            // ============================================================
                            (function() {
                                console.log("👤 Looking for Person+Envelope email icon...");
                                
                                // Clean email function
                                function cleanMailtoEmail(email) {
                                    if (!email) return null;
                                    let cleaned = email.replace(/^mailto:/i, '').split('?')[0];
                                    
                                    const prefixes = ['author.', 'authors.', 'China.', 'UK.', 'US.', 'Europe.', 'Asia.'];
                                    for (const prefix of prefixes) {
                                        if (cleaned.toLowerCase().startsWith(prefix.toLowerCase())) {
                                            cleaned = cleaned.substring(prefix.length);
                                        }
                                    }
                                    
                                    const suffixes = ['More', 'Laboratory', 'University', 'Institute', 'College', 'Department', 'Lab', 'Group', 'Team', 'Research', 'Center', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'];
                                    for (const suffix of suffixes) {
                                        if (cleaned.endsWith(suffix)) {
                                            cleaned = cleaned.substring(0, cleaned.length - suffix.length);
                                        }
                                    }
                                    
                                    const validPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$/;
                                    if (validPattern.test(cleaned)) {
                                        return cleaned;
                                    }
                                    return null;
                                }
                                
                                // ============================================================
                                // TARGETED: Find Person+Envelope icon
                                // ============================================================
                                function findEmailIcons() {
                                    const icons = [];
                                    
                                    console.log("  🔍 Searching for Person+Envelope icons...");
                                    
                                    // Method 1: Look for the article actions toolbar
                                    const actionBars = document.querySelectorAll(
                                        '.article-actions, .article-toolbar, .action-bar, ' +
                                        '[class*="action"], [class*="toolbar"]'
                                    );
                                    
                                    for (const bar of actionBars) {
                                        // Look for buttons inside the action bar
                                        const buttons = bar.querySelectorAll('button, a, [role="button"]');
                                        for (const btn of buttons) {
                                            const ariaLabel = btn.getAttribute('aria-label') || '';
                                            const title = btn.getAttribute('title') || '';
                                            const className = btn.className || '';
                                            const dataTrack = btn.getAttribute('data-track-action') || '';
                                            
                                            // Check if it's the email action (person+envelope icon)
                                            const isEmailAction = 
                                                ariaLabel.toLowerCase().includes('email') ||
                                                ariaLabel.toLowerCase().includes('share') ||
                                                title.toLowerCase().includes('email') ||
                                                title.toLowerCase().includes('share') ||
                                                className.toLowerCase().includes('email') ||
                                                dataTrack.toLowerCase().includes('email') ||
                                                dataTrack.toLowerCase().includes('share');
                                            
                                            if (isEmailAction && btn.offsetParent !== null) {
                                                console.log(\`  ✅ Found Person+Envelope icon: \${ariaLabel || title}\`);
                                                icons.push(btn);
                                            }
                                        }
                                    }
                                    
                                    // Method 2: Look for the specific person+envelope icon by SVG
                                    const allElements = document.querySelectorAll('*');
                                    for (const el of allElements) {
                                        // Look for SVG that might contain both person and envelope
                                        const svgs = el.querySelectorAll('svg');
                                        for (const svg of svgs) {
                                            const svgContent = svg.innerHTML || '';
                                            const hasPerson = svgContent.includes('person') || 
                                                             svgContent.includes('user') ||
                                                             svgContent.includes('M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z');
                                            const hasEnvelope = svgContent.includes('envelope') || 
                                                               svgContent.includes('M2 4.5C2 3.12 3.12 2 4.5 2h15');
                                            
                                            if (hasPerson && hasEnvelope) {
                                                // Find the clickable parent
                                                let parent = el;
                                                while (parent && !['button', 'a'].includes(parent.tagName.toLowerCase())) {
                                                    parent = parent.parentElement;
                                                }
                                                if (parent && parent.offsetParent !== null && !icons.includes(parent)) {
                                                    console.log(\`  ✅ Found Person+Envelope icon (SVG combo)\`);
                                                    icons.push(parent);
                                                }
                                            }
                                        }
                                    }
                                    
                                    // Method 3: Look for the specific ScienceDirect email button
                                    const sdSelectors = [
                                        '.article-actions__email',
                                        '.action-email',
                                        '.email-icon',
                                        '.envelope-icon',
                                        'button[data-track-action="email"]',
                                        'a[data-track-action="email"]',
                                        '.js-email-article',
                                        '.action-share',
                                        'button[aria-label*="Email" i]',
                                        'a[aria-label*="Email" i]'
                                    ];
                                    
                                    for (const selector of sdSelectors) {
                                        const elements = document.querySelectorAll(selector);
                                        for (const el of elements) {
                                            if (el.offsetParent !== null && !icons.includes(el)) {
                                                console.log(\`  ✅ Found by selector: \${selector}\`);
                                                icons.push(el);
                                            }
                                        }
                                    }
                                    
                                    // Method 4: Look for any button with email-related text or icon
                                    const allButtons = document.querySelectorAll('button, a');
                                    for (const btn of allButtons) {
                                        const innerHTML = btn.innerHTML || '';
                                        const ariaLabel = btn.getAttribute('aria-label') || '';
                                        
                                        // Check if it contains an envelope SVG
                                        const hasEnvelopeSvg = innerHTML.includes('envelope') || 
                                                              innerHTML.includes('M2 4.5C2 3.12 3.12 2 4.5 2h15');
                                        
                                        // Check if it contains a person SVG
                                        const hasPersonSvg = innerHTML.includes('person') || 
                                                            innerHTML.includes('M12 12c2.21 0 4-1.79 4-4');
                                        
                                        if ((hasEnvelopeSvg || ariaLabel.toLowerCase().includes('email')) && 
                                            btn.offsetParent !== null && !icons.includes(btn)) {
                                            console.log(\`  ✅ Found email icon by SVG/content\`);
                                            icons.push(btn);
                                        }
                                    }
                                    
                                    // Remove duplicates
                                    const uniqueIcons = [...new Set(icons)];
                                    console.log(\`  📧 Found \${uniqueIcons.length} email icon(s)\`);
                                    return uniqueIcons;
                                }
                                
                                // ============================================================
                                // Wait for panel
                                // ============================================================
                                function waitForPanel(timeout = 10000) {
                                    return new Promise((resolve) => {
                                        let attempts = 0;
                                        const maxAttempts = 40;
                                        const checkInterval = setInterval(() => {
                                            attempts++;
                                            const panelSelectors = [
                                                '.action-panel', '.popup', '.modal', '.dialog', '.sidebar',
                                                '[role="dialog"]', '[role="popup"]', '.flyout',
                                                '[class*="panel"]', '.right-panel', '.side-panel',
                                                '.action-sidebar', '.action-sheet'
                                            ];
                                            for (const selector of panelSelectors) {
                                                const panels = document.querySelectorAll(selector);
                                                for (const panel of panels) {
                                                    const style = window.getComputedStyle(panel);
                                                    if (style.display !== 'none' && 
                                                        style.visibility !== 'hidden' && 
                                                        panel.offsetParent !== null &&
                                                        panel.offsetWidth > 50) {
                                                        clearInterval(checkInterval);
                                                        resolve(panel);
                                                        return;
                                                    }
                                                }
                                            }
                                            if (attempts >= maxAttempts) {
                                                clearInterval(checkInterval);
                                                resolve(null);
                                            }
                                        }, 300);
                                    });
                                }
                                
                                // ============================================================
                                // Extract email from panel
                                // ============================================================
                                function extractEmailFromPanel(panel) {
                                    if (!panel) return null;
                                    
                                    const mailtoLinks = panel.querySelectorAll('a[href^="mailto:"]');
                                    for (const link of mailtoLinks) {
                                        const href = link.getAttribute('href');
                                        if (href) {
                                            const cleaned = cleanMailtoEmail(href);
                                            if (cleaned) {
                                                return cleaned;
                                            }
                                        }
                                    }
                                    return null;
                                }
                                
                                // ============================================================
                                // Close panel
                                // ============================================================
                                function closePanel() {
                                    const closeBtns = document.querySelectorAll('[aria-label*="close" i], .close, .btn-close, [class*="close"]');
                                    for (const btn of closeBtns) {
                                        try { btn.click(); } catch(e) {}
                                    }
                                }
                                
                                // ============================================================
                                // Auto-extract
                                // ============================================================
                                async function autoExtractAll() {
                                    console.log("⏳ Waiting for page to load...");
                                    await new Promise(resolve => setTimeout(resolve, 5000));
                                    
                                    let icons = [];
                                    let attempts = 0;
                                    const maxAttempts = 6;
                                    
                                    while (icons.length === 0 && attempts < maxAttempts) {
                                        attempts++;
                                        console.log(\`  🔄 Attempt \${attempts}/\${maxAttempts}...\`);
                                        icons = findEmailIcons();
                                        if (icons.length === 0 && attempts < maxAttempts) {
                                            await new Promise(resolve => setTimeout(resolve, 2000));
                                        }
                                    }
                                    
                                    console.log(\`📧 Found \${icons.length} icon(s) after \${attempts} attempt(s)\`);
                                    
                                    if (icons.length === 0) {
                                        console.log("❌ No email icons found");
                                        return;
                                    }
                                    
                                    let extractedCount = 0;
                                    
                                    for (let i = 0; i < icons.length; i++) {
                                        const icon = icons[i];
                                        console.log(\`  🖱️ Clicking icon \${i + 1}/\${icons.length}...\`);
                                        
                                        icon.scrollIntoView({ behavior: 'smooth', block: 'center' });
                                        await new Promise(resolve => setTimeout(resolve, 800));
                                        
                                        try {
                                            icon.click();
                                        } catch(e) {
                                            const event = new MouseEvent('click', {
                                                view: window,
                                                bubbles: true,
                                                cancelable: true
                                            });
                                            icon.dispatchEvent(event);
                                        }
                                        
                                        const panel = await waitForPanel(10000);
                                        
                                        if (panel) {
                                            const email = extractEmailFromPanel(panel);
                                            closePanel();
                                            
                                            if (email) {
                                                const stored = JSON.parse(localStorage.getItem('collectedEmails') || '[]');
                                                if (!stored.includes(email)) {
                                                    stored.push(email);
                                                    localStorage.setItem('collectedEmails', JSON.stringify(stored));
                                                    extractedCount++;
                                                    console.log(\`    ✅ Saved: \${email}\`);
                                                } else {
                                                    console.log(\`    ⚠️ Already saved: \${email}\`);
                                                }
                                            }
                                        }
                                        
                                        await new Promise(resolve => setTimeout(resolve, 1500));
                                    }
                                    
                                    console.log(\`✅ Found \${extractedCount} new email(s)\`);
                                }
                                
                                // Run
                                if (document.readyState === 'complete') {
                                    setTimeout(autoExtractAll, 3000);
                                } else {
                                    window.addEventListener('load', function() {
                                        setTimeout(autoExtractAll, 4000);
                                    });
                                }
                                
                                console.log("👤 Auto-extractor started!");
                            })();
                        `;
                        newTab.document.body.appendChild(script);
                    } catch(e) {}
                }, 6000);
            }
        }
        
        openedCount = endIndex;
        
        if (openedCount < totalToOpen) {
            setTimeout(openNextBatch, 4000);
        } else {
            console.log(`\n✅ Opened ${totalToOpen} article(s)!`);
            console.log("📊 After all tabs complete, run: downloadEmails()");
        }
    }
    
    openNextBatch();
}

// ============================================================
// CLEAR OLD EMAILS
// ============================================================
function clearEmails() {
    localStorage.removeItem('collectedEmails');
    localStorage.removeItem('lastProcessed');
    console.log("🗑️ Cleared all collected emails");
}

// ============================================================
// DOWNLOAD UNIQUE EMAILS
// ============================================================
function downloadEmails() {
    let stored = JSON.parse(localStorage.getItem('collectedEmails') || '[]');
    
    if (stored.length === 0) {
        console.log("❌ No emails collected yet");
        return;
    }
    
    const uniqueEmails = [...new Set(stored)];
    
    console.log(`\n📧 Unique emails (${uniqueEmails.length}):`);
    uniqueEmails.forEach((email, i) => {
        console.log(`  ${i+1}. ${email}`);
    });
    
    if (uniqueEmails.length === 0) {
        console.log("❌ No valid emails found");
        return;
    }
    
    const vcfContacts = uniqueEmails.map((email) => {
        let name = email.split('@')[0]
            .replace(/[._-]/g, ' ')
            .replace(/\b\w/g, l => l.toUpperCase());
        
        let firstName = 'Unknown';
        let lastName = 'Researcher';
        
        const nameParts = name.split(' ');
        if (nameParts.length >= 2) {
            firstName = nameParts[0];
            lastName = nameParts.slice(1).join(' ');
        } else if (nameParts.length === 1 && nameParts[0].length > 2) {
            const single = nameParts[0];
            if (single.length > 4) {
                const mid = Math.ceil(single.length / 2);
                firstName = single.substring(0, mid);
                lastName = single.substring(mid);
            } else {
                firstName = single;
            }
        }
        
        return `BEGIN:VCARD
VERSION:3.0
FN:${firstName} ${lastName}
N:${lastName};${firstName};;;
EMAIL;TYPE=INTERNET,WORK:${email}
SOURCE:ScienceDirect
REV:${new Date().toISOString().replace(/[-:]/g, '').split('.')[0]}Z
END:VCARD`;
    });
    
    const allVCF = vcfContacts.join('\n\n');
    
    const blob = new Blob([allVCF], {type: 'text/vcard;charset=utf-8'});
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `unique_emails_${new Date().toISOString().slice(0,10)}.vcf`;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
    
    console.log(`\n📥 Downloaded VCF with ${uniqueEmails.length} unique emails`);
}

// ============================================================
// CHECK PROGRESS
// ============================================================
function checkProgress() {
    const stored = JSON.parse(localStorage.getItem('collectedEmails') || '[]');
    const unique = [...new Set(stored)];
    console.log(`📊 Progress: ${unique.length} unique emails collected`);
    if (unique.length > 0) {
        console.log(`   ${unique.join(', ')}`);
    }
    return unique;
}

// ============================================================
// START
// ============================================================
console.log("\n" + "=".repeat(60));
console.log("📧 SCIENCE DIRECT EMAIL EXTRACTOR");
console.log("=".repeat(60));
console.log("\n📌 Run: openArticlesWithDetector(3)");
console.log("📌 After all tabs finish: downloadEmails()");
console.log("=".repeat(60));
