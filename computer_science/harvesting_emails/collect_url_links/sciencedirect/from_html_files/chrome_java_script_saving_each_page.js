/*
 * save_articles_manual_browser.js
 *
 * Paste into DevTools console on a ScienceDirect SEARCH RESULTS page
 * (e.g. https://www.sciencedirect.com/search?qs=Zn12O12) after logging in.
 *
 * For each article: opens a new tab, waits for you to confirm via a dialog,
 * then downloads the article's HTML to your Downloads folder.
 */
(async () => {
  'use strict';

  // ---- Config ----
  const DELAY_AFTER_LOAD_MS = 3000;   // let page render before prompting
  const DELAY_BEFORE_NEXT_MS = 1000;  // pause between articles
  const DOWNLOAD_PREFIX = 'sd_article_';

  // ---- Collect article links on the current search page ----
  const links = [...new Set(
    [...document.querySelectorAll('a[href*="/science/article/pii/"]')]
      .map(a => a.href.split('#')[0].split('?')[0])
      .filter(h => /\/science\/article\/pii\/[A-Z0-9]+/i.test(h))
  )];

  console.log(`Found ${links.length} article link(s).`);
  if (!links.length) {
    console.warn('No article links on this page. Are you on a search results page?');
    return;
  }

  const proceed = confirm(
    `Found ${links.length} article(s).\n\n` +
    `For each one, a new tab will open. You'll be asked to confirm saving.\n\n` +
    `Continue?`
  );
  if (!proceed) return;

  // ---- Helper: prompt user in the opener window ----
  function askSave(pii, index, total) {
    // The tab title is set to the prompt so you can see it in the tab bar too.
    return confirm(
      `[${index + 1}/${total}] Article: ${pii}\n\n` +
      `Check the article tab that just opened.\n\n` +
      `OK = save this article's HTML\n` +
      `Cancel = skip (don't save)`
    );
  }

  // ---- Helper: download a string as a file ----
  function downloadHtml(html, filename) {
    const blob = new Blob([html], { type: 'text/html;charset=utf-8' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = filename;
    document.body.appendChild(a);
    a.click();
    a.remove();
    setTimeout(() => URL.revokeObjectURL(url), 5000);
  }

  // ---- Main loop ----
  const stats = { saved: 0, skipped: 0, failed: 0 };

  for (let i = 0; i < links.length; i++) {
    const url = links[i];
    const pii = (url.match(/\/pii\/([A-Z0-9]+)/i) || [, `article_${i}`])[1];
    const filename = `${DOWNLOAD_PREFIX}${pii}.html`;

    console.log(`\n[${i + 1}/${links.length}] ${url}`);

    // Open the article in a new tab. We use window.open so we can
    // reference it and close it after saving.
    const tab = window.open(url, '_blank');
    if (!tab) {
      console.warn('Popup blocked — please allow popups for this site and retry.');
      stats.failed++;
      continue;
    }

    // Give the tab time to load. We can't read its DOM cross-origin
    // (sciencedirect.com is same-origin as opener, so actually we CAN,
    // but the tab may still be on a captcha — hence the human confirm step).
    await new Promise(r => setTimeout(r, DELAY_AFTER_LOAD_MS));

    // Ask the user — human-in-the-loop
    const wantsSave = askSave(pii, i, links.length);

    if (!wantsSave) {
      console.log(`  skipped`);
      stats.skipped++;
      try { tab.close(); } catch (_) {}
      await new Promise(r => setTimeout(r, DELAY_BEFORE_NEXT_MS));
      continue;
    }

    // Read the HTML from the child tab (same-origin, so allowed).
    // If ScienceDirect loaded a login/captcha page, we'll still save whatever
    // is currently displayed — check the tab visually before confirming.
    let html = null;
    let titleForLog = '';
    try {
      // Try the article tab's document
      const childDoc = tab.document;
      if (childDoc) {
        // Ensure it's fully parsed
        if (childDoc.readyState !== 'complete') {
          await new Promise(r => {
            const check = () => childDoc.readyState === 'complete' ? r() : setTimeout(check, 250);
            check();
          });
        }
        html = '<!DOCTYPE html>\n' + childDoc.documentElement.outerHTML;
        titleForLog = childDoc.title || '';
      }
    } catch (e) {
      console.warn('  could not read child tab DOM:', e.message);
    }

    // Fallback: if reading child DOM failed, refetch via fetch().
    // This also helps if the tab was closed or is cross-origin for some reason.
    if (!html) {
      try {
        const res = await fetch(url, { credentials: 'include' });
        if (!res.ok) throw new Error('HTTP ' + res.status);
        html = await res.text();
        console.log('  (used fetch fallback)');
      } catch (e) {
        console.warn('  fetch fallback failed:', e.message);
        stats.failed++;
        try { tab.close(); } catch (_) {}
        await new Promise(r => setTimeout(r, DELAY_BEFORE_NEXT_MS));
        continue;
      }
    }

    // Sanity check: make sure we didn't save a block page
    const looksBlocked = /just a moment|captcha|access denied|verify you are human/i
      .test(titleForLog) || /just a moment|captcha|access denied/i.test(html.slice(0, 5000));
    if (looksBlocked) {
      const reallySave = confirm(
        `[${i + 1}/${links.length}] ${pii}\n\n` +
        `WARNING: this looks like a block/captcha page (title="${titleForLog}").\n\n` +
        `Save anyway?`
      );
      if (!reallySave) {
        console.log('  skipped (blocked page)');
        stats.skipped++;
        try { tab.close(); } catch (_) {}
        await new Promise(r => setTimeout(r, DELAY_BEFORE_NEXT_MS));
        continue;
      }
    }

    // Trigger download
    try {
      downloadHtml(html, filename);
      console.log(`  saved: ${filename} (${html.length.toLocaleString()} bytes) title="${titleForLog}"`);
      stats.saved++;
    } catch (e) {
      console.warn('  download failed:', e.message);
      stats.failed++;
    }

    try { tab.close(); } catch (_) {}
    await new Promise(r => setTimeout(r, DELAY_BEFORE_NEXT_MS));
  }

  // ---- Summary ----
  console.log('\n──────── Summary ────────');
  console.log(`Saved:   ${stats.saved}`);
  console.log(`Skipped: ${stats.skipped}`);
  console.log(`Failed:  ${stats.failed}`);
  console.log(`Files in your Downloads folder, prefixed "${DOWNLOAD_PREFIX}".`);
})();
