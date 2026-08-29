// ============================================================
// IMPROVED: PROGRESS TRACKING ACROSS TABS
// ============================================================

function openArticlesWithDetector(count = 0) {
    clearEmails();
    
    // Initialize progress tracking
    localStorage.setItem('extractorProgress', JSON.stringify({
        totalArticles: 0,
        processedArticles: 0,
        totalEmails: 0,
        tabsStatus: {}
    }));
    
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
    
    // Store total articles for progress tracking
    const progress = JSON.parse(localStorage.getItem('extractorProgress') || '{}');
    progress.totalArticles = totalToOpen;
    progress.processedArticles = 0;
    progress.totalEmails = 0;
    progress.startTime = Date.now();
    progress.tabsStatus = {};
    localStorage.setItem('extractorProgress', JSON.stringify(progress));
    
    console.log(`📝 Found ${links.length} articles total`);
    console.log(`📌 Opening ${totalToOpen} article(s)`);
    console.log(`📊 Progress will be tracked across all tabs`);
    
    const batchSize = 3;
    let openedCount = 0;
    
    function openNextBatch() {
        const endIndex = Math.min(openedCount + batchSize, totalToOpen);
        
        for (let i = openedCount; i < endIndex; i++) {
            const tabId = `tab_${i + 1}`;
            const newTab = window.open(links[i], '_blank');
            console.log(`  📌 Opened ${i + 1}/${totalToOpen}`);
            
            if (newTab) {
                // Initialize tab status
                const progress = JSON.parse(localStorage.getItem('extractorProgress') || '{}');
                progress.tabsStatus[tabId] = {
                    url: links[i],
                    status: 'opening',
                    emailsFound: 0,
                    startTime: Date.now()
                };
                localStorage.setItem('extractorProgress', JSON.stringify(progress));
                
                setTimeout(() => {
                    try {
                        const script = newTab.document.createElement('script');
                        script.textContent = `
                            // ============================================================
                            // TAB SCRIPT WITH PROGRESS REPORTING
                            // ============================================================
                            (function() {
                                const tabId = '${tabId}';
                                
                                // ============================================================
                                // REPORT PROGRESS TO MAIN TAB
                                // ============================================================
                                function reportProgress(status, detail, percent, email) {
                                    const progress = JSON.parse(localStorage.getItem('extractorProgress') || '{}');
                                    if (!progress.tabsStatus) progress.tabsStatus = {};
                                    
                                    progress.tabsStatus[tabId] = {
                                        status: status,
                                        detail: detail,
                                        percent: percent || 0,
                                        email: email || null,
                                        lastUpdate: Date.now()
                                    };
                                    
                                    // Calculate total emails
                                    let totalEmails = 0;
                                    let processed = 0;
                                    for (const key in progress.tabsStatus) {
                                        if (progress.tabsStatus[key].emailsFound) {
                                            totalEmails += progress.tabsStatus[key].emailsFound;
                                        }
                                        if (progress.tabsStatus[key].status === 'complete' || 
                                            progress.tabsStatus[key].status === 'error') {
                                            processed++;
                                        }
                                    }
                                    progress.totalEmails = totalEmails;
                                    progress.processedArticles = processed;
                                    
                                    localStorage.setItem('extractorProgress', JSON.stringify(progress));
                                }
                                
                                function reportEmailFound(email) {
                                    const progress = JSON.parse(localStorage.getItem('extractorProgress') || '{}');
                                    if (!progress.tabsStatus) progress.tabsStatus = {};
                                    
                                    if (!progress.tabsStatus[tabId].emailsFound) {
                                        progress.tabsStatus[tabId].emailsFound = 0;
                                    }
                                    progress.tabsStatus[tabId].emailsFound++;
                                    progress.tabsStatus[tabId].lastEmail = email;
                                    
                                    let totalEmails = 0;
                                    for (const key in progress.tabsStatus) {
                                        if (progress.tabsStatus[key].emailsFound) {
                                            totalEmails += progress.tabsStatus[key].emailsFound;
                                        }
                                    }
                                    progress.totalEmails = totalEmails;
                                    
                                    localStorage.setItem('extractorProgress', JSON.stringify(progress));
                                }
                                
                                // ============================================================
                                // CREATE PROGRESS UI
                                // ============================================================
                                function createProgressUI() {
                                    const container = document.createElement('div');
                                    container.id = 'extractorProgress';
                                    container.style.cssText = \`
                                        position: fixed;
                                        top: 20px;
                                        right: 20px;
                                        z-index: 9999999;
                                        background: rgba(0,0,0,0.85);
                                        color: white;
                                        padding: 16px 20px;
                                        border-radius: 12px;
                                        font-family: Arial, sans-serif;
                                        font-size: 14px;
                                        min-width: 280px;
                                        max-width: 350px;
                                        box-shadow: 0 8px 32px rgba(0,0,0,0.5);
                                        border: 1px solid rgba(255,255,255,0.1);
                                    \`;
                                    
                                    container.innerHTML = \`
                                        <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 8px;">
                                            <span style="font-size: 20px;">📧</span>
                                            <span style="font-weight: bold; font-size: 16px;">Tab \${tabId}</span>
                                            <span id="tabStatusBadge" style="margin-left: auto; font-size: 11px; color: #4CAF50; background: rgba(76,175,80,0.2); padding: 2px 10px; border-radius: 12px;">● ACTIVE</span>
                                        </div>
                                        <div id="progressStatus" style="color: #aaa; font-size: 13px; margin-bottom: 4px;">⏳ Initializing...</div>
                                        <div id="progressDetail" style="color: #888; font-size: 12px;">Waiting for page to load</div>
                                        <div style="margin-top: 10px; height: 3px; background: #333; border-radius: 2px; overflow: hidden;">
                                            <div id="progressBar" style="height: 100%; width: 0%; background: linear-gradient(90deg, #4CAF50, #8BC34A); transition: width 0.5s ease; border-radius: 2px;"></div>
                                        </div>
                                        <div style="margin-top: 6px; font-size: 11px; color: #666; text-align: right;">
                                            <span id="progressPercent">0%</span>
                                            <span style="margin-left: 10px;">📧 <span id="emailCount">0</span></span>
                                        </div>
                                    \`;
                                    
                                    document.body.appendChild(container);
                                    return container;
                                }
                                
                                function updateProgress(status, detail, percent, email) {
                                    const statusEl = document.getElementById('progressStatus');
                                    const detailEl = document.getElementById('progressDetail');
                                    const barEl = document.getElementById('progressBar');
                                    const percentEl = document.getElementById('progressPercent');
                                    const emailCountEl = document.getElementById('emailCount');
                                    
                                    if (statusEl) statusEl.textContent = status;
                                    if (detailEl) detailEl.textContent = detail;
                                    if (barEl) barEl.style.width = (percent || 0) + '%';
                                    if (percentEl) percentEl.textContent = Math.round(percent || 0) + '%';
                                    if (emailCountEl) emailCountEl.textContent = document.querySelectorAll('.email-saved').length;
                                    
                                    reportProgress(status, detail, percent, email);
                                }
                                
                                function showComplete(emailsFound) {
                                    const container = document.getElementById('extractorProgress');
                                    const badge = document.getElementById('tabStatusBadge');
                                    if (badge) {
                                        badge.textContent = '✅ DONE';
                                        badge.style.background = 'rgba(76,175,80,0.3)';
                                        badge.style.color = '#4CAF50';
                                    }
                                    if (container) {
                                        container.style.border = '1px solid rgba(76,175,80,0.3)';
                                    }
                                    reportProgress('complete', \`Found \${emailsFound} email(s)\`, 100);
                                }
                                
                                function showError(message) {
                                    const badge = document.getElementById('tabStatusBadge');
                                    if (badge) {
                                        badge.textContent = '❌ ERROR';
                                        badge.style.background = 'rgba(244,67,54,0.2)';
                                        badge.style.color = '#f44336';
                                    }
                                    reportProgress('error', message, 0);
                                }
                                
                                // ============================================================
                                // CLEAN EMAIL FUNCTION
                                // ============================================================
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
                                    return validPattern.test(cleaned) ? cleaned : null;
                                }
                                
                                // ============================================================
                                // FIND EMAIL ICONS
                                // ============================================================
                                function findEmailIcons() {
                                    const icons = [];
                                    
                                    // Method 1: Article actions toolbar
                                    const actionBars = document.querySelectorAll('.article-actions, .article-toolbar, .action-bar, [class*="action"], [class*="toolbar"]');
                                    for (const bar of actionBars) {
                                        const buttons = bar.querySelectorAll('button, a, [role="button"]');
                                        for (const btn of buttons) {
                                            const ariaLabel = btn.getAttribute('aria-label') || '';
                                            const title = btn.getAttribute('title') || '';
                                            const className = btn.className || '';
                                            const dataTrack = btn.getAttribute('data-track-action') || '';
                                            const isEmailAction = 
                                                ariaLabel.toLowerCase().includes('email') ||
                                                ariaLabel.toLowerCase().includes('share') ||
                                                title.toLowerCase().includes('email') ||
                                                title.toLowerCase().includes('share') ||
                                                className.toLowerCase().includes('email') ||
                                                dataTrack.toLowerCase().includes('email') ||
                                                dataTrack.toLowerCase().includes('share');
                                            if (isEmailAction && btn.offsetParent !== null) {
                                                icons.push(btn);
                                            }
                                        }
                                    }
                                    
                                    // Method 2: ScienceDirect specific selectors
                                    const sdSelectors = [
                                        '.article-actions__email', '.action-email', '.email-icon',
                                        '.envelope-icon', 'button[data-track-action="email"]',
                                        'a[data-track-action="email"]', '.js-email-article',
                                        '.action-share', 'button[aria-label*="Email" i]',
                                        'a[aria-label*="Email" i]'
                                    ];
                                    for (const selector of sdSelectors) {
                                        const elements = document.querySelectorAll(selector);
                                        for (const el of elements) {
                                            if (el.offsetParent !== null && !icons.includes(el)) {
                                                icons.push(el);
                                            }
                                        }
                                    }
                                    
                                    // Method 3: SVG detection
                                    const allButtons = document.querySelectorAll('button, a');
                                    for (const btn of allButtons) {
                                        const innerHTML = btn.innerHTML || '';
                                        const ariaLabel = btn.getAttribute('aria-label') || '';
                                        const hasEnvelopeSvg = innerHTML.includes('envelope') || innerHTML.includes('M2 4.5C2 3.12 3.12 2 4.5 2h15');
                                        const hasPersonSvg = innerHTML.includes('person') || innerHTML.includes('M12 12c2.21 0 4-1.79 4-4');
                                        if ((hasEnvelopeSvg || ariaLabel.toLowerCase().includes('email')) && btn.offsetParent !== null && !icons.includes(btn)) {
                                            icons.push(btn);
                                        }
                                    }
                                    
                                    return [...new Set(icons)];
                                }
                                
                                // ============================================================
                                // WAIT FOR PANEL
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
                                                    if (style.display !== 'none' && style.visibility !== 'hidden' && panel.offsetParent !== null && panel.offsetWidth > 50) {
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
                                // EXTRACT EMAIL FROM PANEL
                                // ============================================================
                                function extractEmailFromPanel(panel) {
                                    if (!panel) return null;
                                    const mailtoLinks = panel.querySelectorAll('a[href^="mailto:"]');
                                    for (const link of mailtoLinks) {
                                        const href = link.getAttribute('href');
                                        if (href) {
                                            const cleaned = cleanMailtoEmail(href);
                                            if (cleaned) return cleaned;
                                        }
                                    }
                                    return null;
                                }
                                
                                // ============================================================
                                // CLOSE PANEL
                                // ============================================================
                                function closePanel() {
                                    const closeBtns = document.querySelectorAll('[aria-label*="close" i], .close, .btn-close, [class*="close"]');
                                    for (const btn of closeBtns) {
                                        try { btn.click(); } catch(e) {}
                                    }
                                }
                                
                                // ============================================================
                                // AUTO-EXTRACT ALL WITH PROGRESS
                                // ============================================================
                                async function autoExtractAll() {
                                    const progress = createProgressUI();
                                    updateProgress('⏳ Loading page...', 'Waiting for content to load', 5);
                                    
                                    await new Promise(resolve => setTimeout(resolve, 3000));
                                    updateProgress('🔍 Searching for email icons...', 'Scanning the page', 10);
                                    
                                    let icons = [];
                                    let attempts = 0;
                                    const maxAttempts = 6;
                                    
                                    while (icons.length === 0 && attempts < maxAttempts) {
                                        attempts++;
                                        updateProgress(\`🔍 Searching... (\${attempts}/\${maxAttempts})\`, 'Looking for email icons', 10 + attempts * 5);
                                        icons = findEmailIcons();
                                        if (icons.length === 0 && attempts < maxAttempts) {
                                            await new Promise(resolve => setTimeout(resolve, 2000));
                                        }
                                    }
                                    
                                    if (icons.length === 0) {
                                        updateProgress('❌ No email icons found', 'This article may not have email icons', 100);
                                        showError('No email icons found');
                                        return;
                                    }
                                    
                                    updateProgress(\`📧 Found \${icons.length} icon(s)\`, 'Starting extraction...', 30);
                                    
                                    let extractedCount = 0;
                                    const totalIcons = icons.length;
                                    
                                    for (let i = 0; i < icons.length; i++) {
                                        const icon = icons[i];
                                        const percent = 30 + ((i + 1) / totalIcons) * 60;
                                        
                                        updateProgress(
                                            \`🖱️ Clicking icon \${i + 1}/\${totalIcons}\`,
                                            \`Processing email icon \${i + 1} of \${totalIcons}\`,
                                            percent
                                        );
                                        
                                        icon.scrollIntoView({ behavior: 'smooth', block: 'center' });
                                        await new Promise(resolve => setTimeout(resolve, 800));
                                        
                                        try {
                                            icon.click();
                                        } catch(e) {
                                            icon.dispatchEvent(new MouseEvent('click', { view: window, bubbles: true, cancelable: true }));
                                        }
                                        
                                        updateProgress(
                                            \`⏳ Waiting for panel... (\${i + 1}/\${totalIcons})\`,
                                            'The email panel is opening',
                                            percent + 10
                                        );
                                        
                                        const panel = await waitForPanel(10000);
                                        
                                        if (panel) {
                                            updateProgress(
                                                \`📧 Extracting... (\${i + 1}/\${totalIcons})\`,
                                                'Reading email from panel',
                                                percent + 20
                                            );
                                            const email = extractEmailFromPanel(panel);
                                            closePanel();
                                            
                                            if (email) {
                                                const stored = JSON.parse(localStorage.getItem('collectedEmails') || '[]');
                                                if (!stored.includes(email)) {
                                                    stored.push(email);
                                                    localStorage.setItem('collectedEmails', JSON.stringify(stored));
                                                    extractedCount++;
                                                    reportEmailFound(email);
                                                    updateProgress(
                                                        \`✅ Saved: \${email}\`,
                                                        \`Extracted \${extractedCount} email(s) so far\`,
                                                        percent + 30
                                                    );
                                                    console.log(\`  ✅ Saved: \${email}\`);
                                                } else {
                                                    updateProgress(
                                                        \`⚠️ Duplicate: \${email}\`,
                                                        \`Already collected\`,
                                                        percent + 30
                                                    );
                                                }
                                            } else {
                                            updateProgress(
                                                    \`❌ No email in panel\`,
                                                    \`No mailto link found\`,
                                                    percent + 30
                                                );
                                            }
                                        } else {
                                            updateProgress(
                                              \`⏰ Panel timeout\`,
                                                \`No panel appeared after clicking\`,
                                                percent + 20
                                            );
                                        }
                                        
                                        await new Promise(resolve => setTimeout(resolve, 1000));
                                    }
                                    
                                  const totalStored = JSON.parse(localStorage.getItem('collectedEmails') || '[]');
                                    updateProgress(
                                        \`✅ Complete! Found \${extractedCount} email(s)\`,
                                        \`Total collected: \${totalStored.length} emails across all tabs\`,
                                        100
                                    );
                                    
                                    showColete(extractedCount);
                                    console.log(\`✅ Extracted \${extractedCount} new email(s) from this article\`);
                                }
                                
                                // ============================================================
                                // START
                                // ============================================================
                                console.log("👤 Auto-extractor startedh progress UI!");
                                
                                if (document.readyState === 'complete') {
                                    setTimeout(autoExtractAll, 2000);
                                } else {
                                    window.addEventListener('load', function() {
                                        setTimeout(autoExtractAll, 3000);
                                    });
                                }
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
            console.log("📊 Track progress in the main tab with: showProgress()");
            console.log("📥 After all taplete, run: downloadEmails()");
        }
    }
    
    openNextBatch();
}

// ============================================================
// SHOW PROGRESS IN MAIN TAB
// ============================================================
function showProgress() {
    const progress = JSON.parse(localStorage.getItem('extractorProgress') || '{}');
    
    console.log("\n" + "=".repeat(60));
    console.log("📊 EXTRACTION PROGRESS");
    console.log("=".repeat(60));
    console.log(`📄 Total articles: ${progrtotalArticles || 0}`);
    console.log(`✅ Processed: ${progress.processedArticles || 0}`);
    console.log(`📧 Emails found: ${progress.totalEmails || 0}`);
    console.log(`⏱️  Started: ${progress.startTime ? new Date(progress.startTime).toLocaleTimeString() : 'N/A'}`);
    
    if (progress.tabsStatus) {
        console.log("\n📋 Tab Status:");
        let tabIndex = 0;
        for (const [tabId, status] of Object.entries(progress.tabsStatus)) {
            tabIndex++;
            const statusTes.status || 'unknown';
            const emailInfo = status.lastEmail ? ` 📧 ${status.lastEmail}` : '';
            const percentInfo = status.percent ? ` ${Math.round(status.percent)}%` : '';
            console.log(`  ${tabIndex}. ${statusText}${percentInfo}${emailInfo}`);
        }
    }
    
    console.log("=".repeat(60));
    return progress;
}

// ============================================================
// AUTO-REFRESH PROGRESS (runs every 5 seconds)
// ==========================================================
let progressInterval = null;

function startProgressMonitor() {
    if (progressInterval) {
        clearInterval(progressInterval);
    }
    console.log("📊 Starting progress monitor (updates every 5 seconds)");
    console.log("   Press Ctrl+C to stop monitoring");
    progressInterval = setInterval(() => {
        const progress = JSON.parse(localStorage.getItem('extractorProgress') || '{}');
        if (progress.totalArticles > 0) {
            const total = progress.totalArticles || 0;
            const processed = progress.processedArticles || 0;
            const emails = progress.totalEmails || 0;
            const percent = total > 0 ? Math.round((processed / total) * 100) : 0;
            console.log(`📊 [${new Date().toLocaleTimeString()}] ${processed}/${total} articles (${percent}%) | 📧 ${emails} emails`);
        }
    }, 5000);
}

function stopProgressMonitor() {
    if (progressInterval) {
        clearInterval(progressInterval);
        progressInterval = null;
      nsole.log("📊 Progress monitor stopped");
    }
}

// ============================================================
// CLEAR OLD EMAILS
// ============================================================
function clearEmails() {
    localStorage.removeItem('collectedEmails');
    localStorage.removeItem('extractorProgress');
    localStorage.removeItem('lastProcessed');
    console.log("🗑️ Cleared all collected emails and progress data");
}

// ============================================================
NLOAD UNIQUE EMAILS
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
// CHECK PROGRESS (basic)
// ============================================================
function checkProgress() {
    const stored = JSON.parse(localStorage.getItem('collectedEmails') || '[]');
    const unique = [...new Set(stored)];
    console.log(`📊 Progre${unique.length} unique emails collected`);
    if (unique.length > 0) {
        console.log(`   ${unique.join(', ')}`);
    }
    return unique;
}

// ============================================================
// START
// ============================================================
console.log("\n" + "=".repeat(60));
console.log("📧 SCIENCE DIRECT EMAIL EXTRACTOR - WITH CROSS-TAB PROGRESS");
console.log("=".repeat(60));
console.log("\n📌 Commands:");
console.log("  openArticlesWithDetector(3)  - Openarticles");
console.log("  showProgress()              - Show detailed progress");
console.log("  startProgressMonitor()      - Auto-refresh progress every 5s");
console.log("  stopProgressMonitor()       - Stop auto-refresh");
console.log("  downloadEmails()            - Download VCF");
console.log("=".repeat(60));
