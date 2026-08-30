// ============================================================
// MODIFIED: SCIENCE DIRECT EMAIL EXTRACTOR - SHOWS EMAILS
// ============================================================
// Shows extracted emails in each tab and total count in progress.
// ============================================================

// ============================================================
// GENERATE UNIQUE SESSION ID FOR THIS WINDOW
// ============================================================
function generateSessionId() {
    return 'session_' + Date.now() + '_' + Math.random().toString(36).substr(2, 6);
}

const SESSION_ID = generateSessionId();
const STORAGE_PREFIX = 'extractor_' + SESSION_ID + '_';

console.log(`🆔 Session ID: ${SESSION_ID}`);
console.log(`📁 This window uses isolated storage: ${STORAGE_PREFIX}`);

// ============================================================
// ISOLATED STORAGE FUNCTIONS
// ============================================================
function getStorageKey(key) {
    return STORAGE_PREFIX + key;
}

function setStorage(key, value) {
    localStorage.setItem(getStorageKey(key), JSON.stringify(value));
}

function getStorage(key) {
    const data = localStorage.getItem(getStorageKey(key));
    return data ? JSON.parse(data) : null;
}

function removeStorage(key) {
    localStorage.removeItem(getStorageKey(key));
}

function clearAllStorage() {
    const keysToRemove = [];
    for (let i = 0; i < localStorage.length; i++) {
        const key = localStorage.key(i);
        if (key && key.startsWith(STORAGE_PREFIX)) {
            keysToRemove.push(key);
        }
    }
    keysToRemove.forEach(key => localStorage.removeItem(key));
    console.log(`🗑️ Cleared all data for session: ${SESSION_ID}`);
}

// ============================================================
// OPEN REAL TAB IN BACKGROUND - NO FOCUS
// ============================================================
function openTabInBackground(url) {
    const newTab = window.open(url, '_blank');
    
    if (newTab) {
        try {
            newTab.blur();
            window.focus();
            setTimeout(() => { try { window.focus(); } catch(e) {} }, 50);
            setTimeout(() => { try { window.focus(); } catch(e) {} }, 200);
        } catch(e) {}
    }
    
    return newTab;
}

// ============================================================
// MAIN FUNCTION - ISOLATED WITH BACKGROUND TABS
// ============================================================
function openArticlesWithDetector(count = 0) {
    clearAllStorage();
    
    setStorage('totalArticles', 0);
    setStorage('processedArticles', 0);
    setStorage('totalEmails', 0);
    setStorage('tabsStatus', {});
    setStorage('collectedEmails', []);
    
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
    
    setStorage('totalArticles', totalToOpen);
    setStorage('startTime', Date.now());
    
    console.log(`🆔 Session: ${SESSION_ID}`);
    console.log(`📝 Found ${links.length} articles total`);
    console.log(`📌 Opening ${totalToOpen} article(s) in BACKGROUND tabs`);
    console.log(`💡 Tabs open in background - focus stays here!`);
    console.log(`📊 This window's data is ISOLATED from other windows`);
    console.log(`🤖 Auto-download when all tabs reach 100%`);
    
    const batchSize = 5;
    let openedCount = 0;
    
    function openNextBatch() {
        const endIndex = Math.min(openedCount + batchSize, totalToOpen);
        
        for (let i = openedCount; i < endIndex; i++) {
            const tabId = `tab_${i + 1}`;
            const articleUrl = links[i];
            
            const newTab = openTabInBackground(articleUrl);
            
            console.log(`  📌 Opened ${i + 1}/${totalToOpen} (background)`);
            
            if (newTab) {
                const progress = getStorage('tabsStatus') || {};
                progress[tabId] = {
                    url: articleUrl,
                    status: 'opening',
                    emailsFound: 0,
                    startTime: Date.now(),
                    percent: 0,
                    foundEmails: []
                };
                setStorage('tabsStatus', progress);
                
                setTimeout(() => {
                    try {
                        const script = newTab.document.createElement('script');
                        script.textContent = `
                            // ============================================================
                            // TAB SCRIPT - ISOLATED BY SESSION ID
                            // ============================================================
                            (function() {
                                const SESSION_ID = '${SESSION_ID}';
                                const STORAGE_PREFIX = 'extractor_' + SESSION_ID + '_';
                                const tabId = '${tabId}';
                                let tabPercent = 0;
                                const foundEmails = [];
                                
                                function getStorageKey(key) {
                                    return STORAGE_PREFIX + key;
                                }
                                
                                function getStorage(key) {
                                    const data = localStorage.getItem(getStorageKey(key));
                                    return data ? JSON.parse(data) : null;
                                }
                                
                                function setStorage(key, value) {
                                    localStorage.setItem(getStorageKey(key), JSON.stringify(value));
                                }
                                
                                function reportProgress(status, detail, percent, email) {
                                    const tabsStatus = getStorage('tabsStatus') || {};
                                    tabsStatus[tabId] = { 
                                        status, 
                                        detail, 
                                        percent: percent || 0, 
                                        email: email || null, 
                                        lastUpdate: Date.now(),
                                        foundEmails: foundEmails
                                    };
                                    setStorage('tabsStatus', tabsStatus);
                                    
                                    let totalEmails = 0, processed = 0;
                                    for (const key in tabsStatus) {
                                        if (tabsStatus[key].emailsFound) totalEmails += tabsStatus[key].emailsFound;
                                        if (tabsStatus[key].status === 'complete' || tabsStatus[key].status === 'error') processed++;
                                    }
                                    setStorage('totalEmails', totalEmails);
                                    setStorage('processedArticles', processed);
                                }
                                
                                function reportEmailFound(email) {
                                    const tabsStatus = getStorage('tabsStatus') || {};
                                    if (!tabsStatus[tabId]) tabsStatus[tabId] = {};
                                    if (!tabsStatus[tabId].emailsFound) tabsStatus[tabId].emailsFound = 0;
                                    tabsStatus[tabId].emailsFound++;
                                    tabsStatus[tabId].lastEmail = email;
                                    if (!foundEmails.includes(email)) {
                                        foundEmails.push(email);
                                        // Print the email in the tab console
                                        console.log(\`  ✅ Found email: \${email}\`);
                                    }
                                    tabsStatus[tabId].foundEmails = foundEmails;
                                    setStorage('tabsStatus', tabsStatus);
                                    
                                    let totalEmails = 0;
                                    for (const key in tabsStatus) {
                                        if (tabsStatus[key].emailsFound) totalEmails += tabsStatus[key].emailsFound;
                                    }
                                    setStorage('totalEmails', totalEmails);
                                    
                                    const collected = getStorage('collectedEmails') || [];
                                    if (!collected.includes(email)) {
                                        collected.push(email);
                                        setStorage('collectedEmails', collected);
                                    }
                                }
                                
                                function createProgressUI() {
                                    const container = document.createElement('div');
                                    container.id = 'extractorProgress_' + SESSION_ID;
                                    container.style.cssText = \`
                                        position: fixed; top: 20px; right: 20px; z-index: 9999999;
                                        background: rgba(0,0,0,0.85); color: white; padding: 16px 20px;
                                        border-radius: 12px; font-family: Arial, sans-serif; font-size: 14px;
                                        min-width: 280px; max-width: 350px; box-shadow: 0 8px 32px rgba(0,0,0,0.5);
                                        border: 1px solid rgba(255,255,255,0.1);
                                        max-height: 500px; overflow-y: auto;
                                    \`;
                                    container.innerHTML = \`
                                        <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 8px;">
                                            <span style="font-size: 20px;">📧</span>
                                            <span style="font-weight: bold; font-size: 16px;">Tab \${tabId}</span>
                                            <span style="font-size: 10px; color: #888; margin-left: 5px;">[\${SESSION_ID.slice(0, 8)}]</span>
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
                                        <div id="emailList" style="margin-top: 8px; font-size: 11px; color: #4CAF50; max-height: 100px; overflow-y: auto; border-top: 1px solid #333; padding-top: 6px; display: none;"></div>
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
                                    const emailListEl = document.getElementById('emailList');
                                    
                                    if (statusEl) statusEl.textContent = status;
                                    if (detailEl) detailEl.textContent = detail;
                                    if (barEl) barEl.style.width = (percent || 0) + '%';
                                    if (percentEl) percentEl.textContent = Math.round(percent || 0) + '%';
                                    if (emailCountEl) emailCountEl.textContent = foundEmails.length;
                                    
                                    if (emailListEl) {
                                        if (foundEmails.length > 0) {
                                            emailListEl.style.display = 'block';
                                            emailListEl.style.color = '#aaa';
                                            emailListEl.style.fontSize = '11px';
                                            emailListEl.innerHTML = foundEmails.map(e => \`📧 \${e}\`).join('<br>');
                                        } else {
                                            emailListEl.style.display = 'none';
                                        }
                                    }
                                    
                                    reportProgress(status, detail, percent, email);
                                    tabPercent = percent || 0;
                                }
                                
                                function showComplete(emailsFound) {
                                    const badge = document.getElementById('tabStatusBadge');
                                    if (badge) { 
                                        badge.textContent = '✅ DONE (' + emailsFound + ' emails)'; 
                                        badge.style.background = 'rgba(76,175,80,0.3)'; 
                                        badge.style.color = '#4CAF50'; 
                                    }
                                    const emailListEl = document.getElementById('emailList');
                                    if (emailListEl) {
                                        if (foundEmails.length > 0) {
                                            emailListEl.style.display = 'block';
                                            emailListEl.style.color = '#4CAF50';
                                            emailListEl.style.fontSize = '12px';
                                            emailListEl.innerHTML = foundEmails.map(e => \`📧 \${e}\`).join('<br>');
                                        } else {
                                            emailListEl.style.display = 'none';
                                        }
                                    }
                                    // Print all found emails in the tab console
                                    if (foundEmails.length > 0) {
                                        console.log(\`\\n✅ Found \${foundEmails.length} email(s) in this tab:\`);
                                        foundEmails.forEach((email, i) => {
                                            console.log(\`  \${i+1}. \${email}\`);
                                        });
                                    }
                                    reportProgress('complete', 'Found ' + emailsFound + ' email(s)', 100);
                                }
                                
                                function showError(message) {
                                    const badge = document.getElementById('tabStatusBadge');
                                    if (badge) { badge.textContent = '❌ ERROR'; badge.style.background = 'rgba(244,67,54,0.2)'; badge.style.color = '#f44336'; }
                                    reportProgress('error', message, 0);
                                }
                                
                                function cleanMailtoEmail(email) {
                                    if (!email) return null;
                                    let cleaned = email.replace(/^mailto:/i, '').split('?')[0];
                                    const prefixes = ['author.', 'authors.', 'China.', 'UK.', 'US.', 'Europe.', 'Asia.'];
                                    for (const prefix of prefixes) { if (cleaned.toLowerCase().startsWith(prefix.toLowerCase())) { cleaned = cleaned.substring(prefix.length); } }
                                    const suffixes = ['More', 'Laboratory', 'University', 'Institute', 'College', 'Department', 'Lab', 'Group', 'Team', 'Research', 'Center', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'];
                                    for (const suffix of suffixes) { if (cleaned.endsWith(suffix)) { cleaned = cleaned.substring(0, cleaned.length - suffix.length); } }
                                    const validPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$/;
                                    return validPattern.test(cleaned) ? cleaned : null;
                                }
                                
                                function findEmailIcons() {
                                    const icons = [];
                                    const actionBars = document.querySelectorAll('.article-actions, .article-toolbar, .action-bar, [class*="action"], [class*="toolbar"]');
                                    for (const bar of actionBars) {
                                        const buttons = bar.querySelectorAll('button, a, [role="button"]');
                                        for (const btn of buttons) {
                                            const ariaLabel = btn.getAttribute('aria-label') || '';
                                            const title = btn.getAttribute('title') || '';
                                            const className = btn.className || '';
                                            const dataTrack = btn.getAttribute('data-track-action') || '';
                                            const isEmailAction = ariaLabel.toLowerCase().includes('email') || ariaLabel.toLowerCase().includes('share') || title.toLowerCase().includes('email') || title.toLowerCase().includes('share') || className.toLowerCase().includes('email') || dataTrack.toLowerCase().includes('email') || dataTrack.toLowerCase().includes('share');
                                            if (isEmailAction && btn.offsetParent !== null) { icons.push(btn); }
                                        }
                                    }
                                    const sdSelectors = ['.article-actions__email', '.action-email', '.email-icon', '.envelope-icon', 'button[data-track-action="email"]', 'a[data-track-action="email"]', '.js-email-article', '.action-share', 'button[aria-label*="Email" i]', 'a[aria-label*="Email" i]'];
                                    for (const selector of sdSelectors) {
                                        const elements = document.querySelectorAll(selector);
                                        for (const el of elements) { if (el.offsetParent !== null && !icons.includes(el)) { icons.push(el); } }
                                    }
                                    const allButtons = document.querySelectorAll('button, a');
                                    for (const btn of allButtons) {
                                        const innerHTML = btn.innerHTML || '';
                                        const ariaLabel = btn.getAttribute('aria-label') || '';
                                        const hasEnvelopeSvg = innerHTML.includes('envelope') || innerHTML.includes('M2 4.5C2 3.12 3.12 2 4.5 2h15');
                                        const hasPersonSvg = innerHTML.includes('person') || innerHTML.includes('M12 12c2.21 0 4-1.79 4-4');
                                        if ((hasEnvelopeSvg || ariaLabel.toLowerCase().includes('email')) && btn.offsetParent !== null && !icons.includes(btn)) { icons.push(btn); }
                                    }
                                    return [...new Set(icons)];
                                }
                                
                                function waitForPanel(timeout = 10000) {
                                    return new Promise((resolve) => {
                                        let attempts = 0, maxAttempts = 40;
                                        const checkInterval = setInterval(() => {
                                            attempts++;
                                            const panelSelectors = ['.action-panel', '.popup', '.modal', '.dialog', '.sidebar', '[role="dialog"]', '[role="popup"]', '.flyout', '[class*="panel"]', '.right-panel', '.side-panel', '.action-sidebar', '.action-sheet'];
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
                                            if (attempts >= maxAttempts) { clearInterval(checkInterval); resolve(null); }
                                        }, 300);
                                    });
                                }
                                
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
                                
                                function closePanel() {
                                    const closeBtns = document.querySelectorAll('[aria-label*="close" i], .close, .btn-close, [class*="close"]');
                                    for (const btn of closeBtns) { try { btn.click(); } catch(e) {} }
                                }
                                
                                async function autoExtractAll() {
                                    const progress = createProgressUI();
                                    updateProgress('⏳ Loading page...', 'Waiting for content to load', 5);
                                    await new Promise(resolve => setTimeout(resolve, 3000));
                                    updateProgress('🔍 Searching for email icons...', 'Scanning the page', 10);
                                    
                                    let icons = [], attempts = 0, maxAttempts = 6;
                                    while (icons.length === 0 && attempts < maxAttempts) {
                                        attempts++;
                                        updateProgress('Searching... (' + attempts + '/' + maxAttempts + ')', 'Looking for email icons', 10 + attempts * 5);
                                        icons = findEmailIcons();
                                        if (icons.length === 0 && attempts < maxAttempts) { await new Promise(resolve => setTimeout(resolve, 2000)); }
                                    }
                                    
                                    if (icons.length === 0) { updateProgress('❌ No email icons found', 'This article may not have email icons', 100); showError('No email icons found'); return; }
                                    
                                    updateProgress('Found ' + icons.length + ' icon(s)', 'Starting extraction...', 30);
                                    let extractedCount = 0, totalIcons = icons.length;
                                    
                                    for (let i = 0; i < icons.length; i++) {
                                        const icon = icons[i];
                                        const percent = 30 + ((i + 1) / totalIcons) * 60;
                                        updateProgress('Clicking icon ' + (i + 1) + '/' + totalIcons, 'Processing email icon ' + (i + 1) + ' of ' + totalIcons, percent);
                                        icon.scrollIntoView({ behavior: 'smooth', block: 'center' });
                                        await new Promise(resolve => setTimeout(resolve, 800));
                                        try { icon.click(); } catch(e) { icon.dispatchEvent(new MouseEvent('click', { view: window, bubbles: true, cancelable: true })); }
                                        
                                        updateProgress('Waiting for panel... (' + (i + 1) + '/' + totalIcons + ')', 'The email panel is opening', Math.min(percent + 10, 90));
                                        const panel = await waitForPanel(10000);
                                        
                                        if (panel) {
                                            updateProgress('Extracting... (' + (i + 1) + '/' + totalIcons + ')', 'Reading email from panel', Math.min(percent + 20, 95));
                                            const email = extractEmailFromPanel(panel);
                                            closePanel();
                                            if (email) {
                                                const collected = getStorage('collectedEmails') || [];
                                                if (!collected.includes(email)) {
                                                    collected.push(email);
                                                    setStorage('collectedEmails', collected);
                                                    extractedCount++;
                                                    reportEmailFound(email);
                                                    updateProgress('✅ Saved: ' + email, 'Extracted ' + extractedCount + ' email(s) so far', Math.min(percent + 30, 100));
                                                    console.log('  ✅ Saved: ' + email);
                                                } else {
                                                    updateProgress('⚠️ Duplicate: ' + email, 'Already collected', Math.min(percent + 30, 100));
                                                }
                                            } else {
                                                updateProgress('❌ No email in panel', 'No mailto link found', Math.min(percent + 20, 95));
                                            }
                                        } else {
                                            updateProgress('⏰ Panel timeout', 'No panel appeared after clicking', Math.min(percent + 10, 90));
                                        }
                                        await new Promise(resolve => setTimeout(resolve, 1000));
                                    }
                                    
                                    const totalStored = getStorage('collectedEmails') || [];
                                    updateProgress('✅ Complete! Found ' + extractedCount + ' email(s)', 'Total collected: ' + totalStored.length + ' emails across all tabs', 100);
                                    showComplete(extractedCount);
                                    console.log('✅ Extracted ' + extractedCount + ' new email(s) from this article');
                                }
                                
                                if (document.readyState === 'complete') {
                                    setTimeout(autoExtractAll, 2000);
                                } else {
                                    window.addEventListener('load', function() { setTimeout(autoExtractAll, 3000); });
                                }
                                console.log("👤 Auto-extractor started with progress UI!");
                            })();
                        `;
                        newTab.document.body.appendChild(script);
                    } catch(e) {}
                }, 6000);
            }
        }
        
        openedCount = endIndex;
        
        if (openedCount < totalToOpen) {
            console.log(`  ⏳ Waiting 4s before opening next batch...`);
            setTimeout(openNextBatch, 4000);
        } else {
            console.log(`\n✅ Opened ${totalToOpen} article(s) in BACKGROUND tabs!`);
            console.log(`📊 Auto-monitoring progress for session: ${SESSION_ID}`);
            console.log("🤖 Will auto-download when all tabs reach 100%");
            startProgressMonitor();
        }
    }
    
    openNextBatch();
}

// ============================================================
// OPEN ALL ARTICLES
// ============================================================
function openAllArticles() {
    console.log(`📌 Opening ALL articles (Session: ${SESSION_ID})...`);
    openArticlesWithDetector(0);
}

// ============================================================
// SHOW PROGRESS - WITH EMAIL COUNT
// ============================================================
function showProgress() {
    const tabsStatus = getStorage('tabsStatus') || {};
    const totalArticles = getStorage('totalArticles') || 0;
    const processedArticles = getStorage('processedArticles') || 0;
    const totalEmails = getStorage('totalEmails') || 0;
    const startTime = getStorage('startTime');
    const collected = getStorage('collectedEmails') || [];
    
    console.log("\n" + "=".repeat(60));
    console.log(`📊 EXTRACTION PROGRESS (Session: ${SESSION_ID})`);
    console.log("=".repeat(60));
    console.log(`🆔 Session: ${SESSION_ID}`);
    console.log(`📄 Total articles: ${totalArticles}`);
    console.log(`✅ Processed: ${processedArticles}`);
    console.log(`📧 Total emails found: ${totalEmails}`);
    console.log(`⏱️  Started: ${startTime ? new Date(startTime).toLocaleTimeString() : 'N/A'}`);
    
    if (collected.length > 0) {
        console.log(`\n📧 All collected emails (${collected.length}):`);
        collected.forEach((email, i) => {
            console.log(`  ${i+1}. ${email}`);
        });
    }
    
    if (Object.keys(tabsStatus).length > 0) {
        console.log("\n📋 Tab Status:");
        let tabIndex = 0;
        for (const [tabId, status] of Object.entries(tabsStatus)) {
            tabIndex++;
            const statusText = status.status || 'unknown';
            const percentInfo = status.percent ? ` ${Math.round(status.percent)}%` : '';
            const emailCount = status.foundEmails ? status.foundEmails.length : 0;
            const emailInfo = emailCount > 0 ? ` 📧 ${emailCount} emails` : '';
            const emails = status.foundEmails && status.foundEmails.length > 0 ? ` [${status.foundEmails.join(', ')}]` : '';
            console.log(`  ${tabIndex}. ${statusText}${percentInfo}${emailInfo}${emails}`);
        }
    }
    console.log("=".repeat(60));
    return { tabsStatus, totalArticles, processedArticles, totalEmails, collected };
}

// ============================================================
// PROGRESS MONITOR - WITH EMAIL COUNT IN PROGRESS BAR
// ============================================================
let progressInterval = null;
let monitorActive = false;
let autoDownloadDone = false;

function startProgressMonitor() {
    if (progressInterval) { clearInterval(progressInterval); }
    monitorActive = true;
    autoDownloadDone = false;
    console.log(`📊 Starting progress monitor (updates every 5 seconds)`);
    console.log("   Will auto-download when all tabs complete");
    showProgressSummary();
    progressInterval = setInterval(() => {
        if (!monitorActive) { clearInterval(progressInterval); return; }
        showProgressSummary();
        
        if (!autoDownloadDone) {
            const total = getStorage('totalArticles') || 0;
            const processed = getStorage('processedArticles') || 0;
            const tabsStatus = getStorage('tabsStatus') || {};
            const totalEmails = getStorage('totalEmails') || 0;
            let allComplete = true;
            
            for (const [tabId, status] of Object.entries(tabsStatus)) {
                if (status.percent < 100 && status.status !== 'error') {
                    allComplete = false;
                    break;
                }
            }
            
            if (allComplete && total > 0 && processed >= total) {
                autoDownloadDone = true;
                console.log(`\n🎉 ALL TABS COMPLETE! Auto-downloading VCF...`);
                stopProgressMonitor();
                setTimeout(() => {
                    downloadEmails();
                }, 1000);
            }
        }
    }, 5000);
}

function showProgressSummary() {
    const total = getStorage('totalArticles') || 0;
    const processed = getStorage('processedArticles') || 0;
    const totalEmails = getStorage('totalEmails') || 0;
    const tabsStatus = getStorage('tabsStatus') || {};
    const collected = getStorage('collectedEmails') || [];
    
    if (total > 0) {
        const percent = total > 0 ? Math.round((processed / total) * 100) : 0;
        
        let statusStr = '';
        let percentStr = '';
        if (Object.keys(tabsStatus).length > 0) {
            const statuses = [];
            const percents = [];
            for (const [tabId, status] of Object.entries(tabsStatus)) {
                const s = status.status || 'unknown';
                const p = status.percent || 0;
                if (s === 'complete') { statuses.push('✅'); }
                else if (s === 'error') { statuses.push('❌'); }
                else if (s === 'processing') { statuses.push('🔄'); }
                else if (s === 'opening') { statuses.push('📂'); }
                else { statuses.push('⏳'); }
                percents.push(Math.round(p) + '%');
            }
            statusStr = statuses.join(' ');
            percentStr = percents.join(' ');
        }
        
        // Show total emails count in the progress bar
        console.log(`📊 [${new Date().toLocaleTimeString()}] ${processed}/${total} articles (${percent}%) | 📧 ${totalEmails} emails [${SESSION_ID.slice(0, 8)}]`);
        if (percentStr) {
            console.log(`   └─ Tab progress: ${percentStr}`);
        }
        if (collected.length > 0 && collected.length <= 10) {
            console.log(`   └─ Emails: ${collected.join(', ')}`);
        } else if (collected.length > 10) {
            console.log(`   └─ Emails (${collected.length} total): ${collected.slice(0, 5).join(', ')} ... and ${collected.length - 5} more`);
        }
    }
}

function stopProgressMonitor() {
    if (progressInterval) {
        clearInterval(progressInterval);
        progressInterval = null;
        monitorActive = false;
        console.log(`📊 Progress monitor stopped for session ${SESSION_ID}`);
    }
}

// ============================================================
// DOWNLOAD EMAILS
// ============================================================
function downloadEmails() {
    const stored = getStorage('collectedEmails') || [];
    
    if (stored.length === 0) {
        console.log(`❌ No emails collected yet (Session: ${SESSION_ID})`);
        return;
    }
    
    const uniqueEmails = [...new Set(stored)];
    const emailCount = uniqueEmails.length;
    
    console.log(`\n📧 Unique emails (${emailCount}) - Session: ${SESSION_ID}:`);
    uniqueEmails.forEach((email, i) => {
        console.log(`  ${i+1}. ${email}`);
    });
    
    if (emailCount === 0) {
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
    
    const timestamp = new Date().toISOString().replace(/[:.]/g, '-').slice(0, 19);
    const filename = `emails_${emailCount}_${SESSION_ID.slice(0, 8)}_${timestamp}.vcf`;
    
    const blob = new Blob([allVCF], {type: 'text/vcard;charset=utf-8'});
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = filename;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
    
    console.log(`\n📥 Downloaded: ${filename}`);
    console.log(`📧 Contains ${emailCount} unique emails`);
}

// ============================================================
// CLEAR EMAILS
// ============================================================
function clearEmails() {
    clearAllStorage();
}

// ============================================================
// CHECK PROGRESS
// ============================================================
function checkProgress() {
    const stored = getStorage('collectedEmails') || [];
    const unique = [...new Set(stored)];
    console.log(`📊 Progress (Session ${SESSION_ID}): ${unique.length} unique emails collected`);
    if (unique.length > 0) { console.log(`   ${unique.join(', ')}`); }
    return unique;
}

// ============================================================
// SHOW SESSION INFO
// ============================================================
function showSessionInfo() {
    console.log(`\n🆔 Session ID: ${SESSION_ID}`);
    console.log(`📁 Storage prefix: ${STORAGE_PREFIX}`);
    return { sessionId: SESSION_ID, storagePrefix: STORAGE_PREFIX };
}

// ============================================================
// START
// ============================================================
console.log("\n" + "=".repeat(60));
console.log("📧 SCIENCE DIRECT EMAIL EXTRACTOR - SHOWS EMAILS");
console.log("=".repeat(60));
console.log(`🆔 Session ID: ${SESSION_ID}`);
console.log(`💡 Tabs open in BACKGROUND - focus stays here!`);
console.log(`📁 This window's data is ISOLATED from other windows`);
console.log(`📧 Emails will be shown in each tab's console and progress bar`);
console.log("\n📌 Commands:");
console.log("  openAllArticles()           - Open ALL articles");
console.log("  openArticlesWithDetector(3)  - Open 3 articles");
console.log("  showProgress()              - Show progress with emails");
console.log("  showSessionInfo()           - Show session details");
console.log("  stopProgressMonitor()       - Stop auto-refresh");
console.log("  downloadEmails()            - Manual download VCF");
console.log("=".repeat(60));