/*
 * save_all_articles_onclick.js
 *
 * Paste into DevTools console on a ScienceDirect SEARCH RESULTS page.
 * Opens every article in the list as a background tab, waits for each
 * to render, saves its HTML to Downloads, then closes the tab.
 *
 * Prerequisites in Chrome Site Settings for sciencedirect.com:
 *   - Pop-ups and redirects: Allow
 *   - Automatic downloads:  Allow
 *   (otherwise Chrome silently drops all but the first download)
 */
(async () => {
  'use strict';

  // ---- Config ----
  const MAX_TABS_AT_ONCE = 6;          // parallel tabs (don't slam the server)
  const PER_TAB_TIMEOUT_MS = 30000;    // max wait per tab
  const POST_READY_SETTLE_MS = 1500;   // MathJax / lazy-content settle
  const DELAY_BETWEEN_DOWNLOADS_MS = 800; // Chrome throttles >~10/sec
  const DOWNLOAD_PREFIX = 'sd_article_';

  // ---- 1. Collect article links ----
  const links = [...new Set(
    [...document.querySelectorAll('a[href*="/science/article/pii/"]')]
      .map(a => a.href.split('#')[0].split('?')[0])
      .filter(h => /\/science\/article\/pii\/[A-Z0-9]+$/i.test(h))
  )];

  console.log(`Found ${links.length} article link(s).`);
  if (!links.length) {
    console.warn('No article links. Are you on a search results page?');
    return;
  }

  if (!confirm(
    `Open ${links.length} article(s) in background tabs and save all HTML?`
  )) return;

  // ---- 2. Helpers ----
  const sleep = (ms) => new Promise(r => setTimeout(r, ms));

  function triggerDownload(html, filename) {
    const blob = new Blob([html], { type: 'text/html;charset=utf-8' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = filename;
    a.style.display = 'none';
    document.body.appendChild(a);
    a.click();
    a.remove();
    setTimeout(() => URL.revokeObjectURL(url), 10000);
  }

  async function waitForTabReady(tab, timeoutMs) {
    const deadline = Date.now() + timeoutMs;
    while (Date.now() < deadline) {
      if (!tab || tab.closed) return null;
      try {
        const doc = tab.document;
        if (
          doc &&
          doc.readyState === 'complete' &&
          doc.body &&
          doc.body.innerText.length > 200
        ) {
          return doc;
        }
      } catch (e) {
        // cross-origin / not navigated yet — keep waiting
      }
      await sleep(400);
    }
    return null;
  }

  // ---- 3. Worker: open → wait → read → close, return HTML ----
  async function fetchOneArticle(url, index, total) {
    const pii = (url.match(/\/pii\/([A-Z0-9]+)$/i) || [, `a${index}`])[1];
    console.log(`[${index + 1}/${total}] open ${pii}`);

    let tab;
    try {
      tab = window.open(url, '_blank');
      if (!tab) throw new Error('popup blocked');
    } catch (e) {
      console.warn(`  ${pii}: window.open failed — ${e.message}`);
      return { pii, ok: false, error: e.message };
    }

    const doc = await waitForTabReady(tab, PER_TAB_TIMEOUT_MS);
    if (!doc) {
      try { tab.close(); } catch (_) {}
      console.warn(`  ${pii}: tab never became ready`);
      return { pii, ok: false, error: 'timeout / not ready' };
    }

    await sleep(POST_READY_SETTLE_MS);

    let html = null;
    let title = '';
    try {
      title = doc.title || '';
      html = '<!DOCTYPE html>\n' + doc.documentElement.outerHTML;
    } catch (e) {
      try { tab.close(); } catch (_) {}
      console.warn(`  ${pii}: read failed — ${e.message}`);
      return { pii, ok: false, error: 'read: ' + e.message };
    }

    try { tab.close(); } catch (_) {}
    return { pii, ok: true, html, title };
  }

  // ---- 4. Run with limited parallelism ----
  const results = { saved: 0, failed: 0, failures: [] };
  let cursor = 0;

  async function worker() {
    while (cursor < links.length) {
      const i = cursor++;
      const url = links[i];
      const r = await fetchOneArticle(url, i, links.length);

      if (r.ok) {
        const filename = `${DOWNLOAD_PREFIX}${r.pii}.html`;
        try {
          triggerDownload(r.html, filename);
          results.saved++;
          console.log(
            `  ${r.pii}: saved ${filename} (${r.html.length.toLocaleString()} bytes)`
          );
        } catch (e) {
          results.failed++;
          results.failures.push({ pii: r.pii, reason: 'download: ' + e.message });
          console.warn(`  ${r.pii}: download failed — ${e.message}`);
        }
      } else {
        results.failed++;
        results.failures.push({ pii: r.pii, reason: r.error });
      }

      await sleep(DELAY_BETWEEN_DOWNLOADS_MS);
    }
  }

  console.log(
    `\nStarting ${MAX_TABS_AT_ONCE} parallel workers for ${links.length} articles…\n`
  );

  const workers = Array.from({ length: MAX_TABS_AT_ONCE }, () => worker());
  await Promise.all(workers);

  // ---- 5. Summary ----
  console.log('\n──────── Summary ────────');
  console.log(`Saved:  ${results.saved}`);
  console.log(`Failed: ${results.failed}`);
  if (results.failures.length) {
    console.log('\nFailures:');
    for (const f of results.failures) console.log(`  ${f.pii} — ${f.reason}`);
  }
  console.log(`\nFiles landed in your Downloads folder as ${DOWNLOAD_PREFIX}<PII>.html`);
})();
