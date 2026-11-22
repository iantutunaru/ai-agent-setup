// measure.js: numbers from the open page, for the web-check skill.
// Pass this whole file as the text of the browser's JavaScript tool; the last expression is the result (JSON).
// To measure one part of the page, put a line before it: window.WEB_CHECK_ROOT = "<css selector>";
// After a reload or a resize of the same site, this one line runs it again: eval(sessionStorage.getItem('webCheckMeasure'))
// The result's page.script must read 2026-11-21b: an older value means the browser kept a copy of an earlier
// version (its cache, or the sessionStorage key of an earlier chat), so pass or load this file again.
// It reads and reports; the only thing it leaves behind is that sessionStorage key. What a number should be is in
// the rulebook, not here: each section's "find" gives words for `rb.py find`.
(() => { const measure = async () => {
  if (!innerWidth || !innerHeight) return { error: 'The window has no size (a hidden browser pane lays the page out at width 0), so nothing can be measured. Set a size with the browser\'s resize tool or show the pane, reload, and run again.' };
  const root = document.querySelector(window.WEB_CHECK_ROOT || 'body') || document.body;
  const cut = (s, n = 60) => { s = (s || '').replace(/\s+/g, ' ').trim(); return s.length > n ? s.slice(0, n - 1) + '…' : s; };
  const r1 = x => Math.round(x * 10) / 10;
  const cut2 = x => Math.floor(x * 100 + 1e-9) / 100;   // cut, not rounded: 4.49 must not read as 4.5
  const kb =bytes => Math.round(bytes / 102.4) / 10;
  const style = el => getComputedStyle(el);
  const shown = el => {
    const r = el.getBoundingClientRect(), cs = style(el);
    return r.width > 0 && r.height > 0 && cs.visibility !== 'hidden' && cs.display !== 'none' && parseFloat(cs.opacity) > 0.05;
  };
  const all = sel => [...root.querySelectorAll(sel)];
  const median = a => { if (!a.length) return null; const s = [...a].sort((x, y) => x - y); return s[Math.floor(s.length / 2)]; };
  const ownText = el => [...el.childNodes].filter(n => n.nodeType === 3).map(n => n.nodeValue).join('').replace(/\s+/g, ' ').trim();
  const inSentence = el => el.tagName === 'A' && style(el).display === 'inline' && !el.querySelector('img, svg') && !!el.parentElement && ownText(el.parentElement).length >= 20;
  const tail = url => { if (/^data:/i.test(url)) return url.slice(0, url.indexOf(';') > 0 ? url.indexOf(';') : 20) + ' (inline)'; try { const u = new URL(url, location.href); return cut(u.pathname.split('/').slice(-2).join('/'), 50); } catch (e) { return cut(url, 50); } };

  // ---- colour: any CSS colour to [r, g, b, a] through a canvas
  const ctx = Object.assign(document.createElement('canvas'), { width: 1, height: 1 }).getContext('2d', { willReadFrequently: true });
  const rgbaCache = new Map();
  const rgba = colour => {
    if (!rgbaCache.has(colour)) {
      ctx.clearRect(0, 0, 1, 1); ctx.fillStyle = '#000'; ctx.fillStyle = colour; ctx.fillRect(0, 0, 1, 1);
      const d = ctx.getImageData(0, 0, 1, 1).data;
      rgbaCache.set(colour, [d[0], d[1], d[2], d[3] / 255]);
    }
    return rgbaCache.get(colour);
  };
  const over = (top, under) => top.slice(0, 3).map((c, i) => c * top[3] + under[i] * (1 - top[3]));
  const lum = c => { const [r, g, b] = c.map(v => { v /= 255; return v <= 0.04045 ? v / 12.92 : ((v + 0.055) / 1.055) ** 2.4; }); return 0.2126 * r + 0.7152 * g + 0.0722 * b; };
  const ratio = (a, b) => { const [hi, lo] = [lum(a), lum(b)].sort((x, y) => y - x); return (hi + 0.05) / (lo + 0.05); };
  const hex = c => '#' + c.slice(0, 3).map(v => Math.round(v).toString(16).padStart(2, '0')).join('');
  const background = el => {   // the colour behind an element, and whether a picture lies behind it
    const layers = []; let image = false;
    for (let e = el; e; e = e.parentElement) {
      const cs = style(e);
      if (cs.backgroundImage && cs.backgroundImage !== 'none') image = true;
      const c = rgba(cs.backgroundColor);
      if (c[3] > 0) { layers.push(c); if (c[3] >= 0.999) break; }
    }
    let colour = [255, 255, 255];
    for (const layer of layers.reverse()) colour = over(layer, colour);
    return { colour, image };
  };

  // ---- text: every visible run of text, grouped by how it is set
  const groups = new Map(); const underlined = [];
  const walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT);
  let seen = 0;
  for (let n = walker.nextNode(); n && seen < 6000; n = walker.nextNode()) {
    const text = n.nodeValue.replace(/\s+/g, ' ').trim(); const el = n.parentElement;
    if (!text || !el || /^(SCRIPT|STYLE|NOSCRIPT|TEMPLATE)$/.test(el.tagName) || !shown(el)) continue;
    seen++;
    const cs = style(el), bg = background(el), fg = over(rgba(cs.color), bg.colour);
    const size = r1(parseFloat(cs.fontSize)), weight = parseInt(cs.fontWeight, 10) || 400;
    const family = cs.fontFamily.split(',')[0].replace(/["']/g, '').trim();
    const key = [size, weight, family, hex(fg), hex(bg.colour), bg.image].join('|');
    const g = groups.get(key) || { size, weight, family, colour: hex(fg), background: hex(bg.colour), overPicture: bg.image, contrast: cut2(ratio(fg, bg.colour)), chars: 0, sample: cut(text, 50) };
    g.chars += text.length; groups.set(key, g);
    if (cs.textDecorationLine.includes('underline') && !el.closest('a, button, [role=link]') && underlined.length < 6) underlined.push(cut(text, 40));
  }
  const gs = [...groups.values()]; const chars = gs.reduce((s, g) => s + g.chars, 0);
  const tally = field => { const m = new Map(); gs.forEach(g => m.set(g[field], (m.get(g[field]) || 0) + g.chars)); return [...m].sort((a, b) => b[1] - a[1]); };
  const sizes = tally('size');
  const large = g => g.size >= 24 || (g.size >= 18.66 && g.weight >= 700);
  const text = {
    find: 'size, small print, typefaces, emphasis',
    characters: chars,
    bodySizePx: sizes.length ? sizes[0][0] : null,
    sizesPx: sizes.slice(0, 10).map(([size, n]) => ({ size, share: Math.round(100 * n / chars) + '%' })),
    smallest: gs.filter(g => g.size < 14).sort((a, b) => a.size - b.size).slice(0, 8).map(g => ({ size: g.size, chars: g.chars, sample: g.sample })),
    families: tally('family').slice(0, 8).map(([family, n]) => ({ family, share: Math.round(100 * n / chars) + '%' })),
    weights: tally('weight').map(([weight]) => weight),
    underlinedButNoLink: underlined,
  };
  const contrast = {
    find: 'contrast',
    note: 'WCAG 2 contrast ratio of text on the colour behind it, cut to two decimals (never rounded up) and worked out from the colour as the screen draws it (8 bits a channel); "large" is 24 px or more, or 18.66 px bold. overPicture: a background picture lies behind the text, so the ratio is against the colour under the picture and must be judged by eye.',
    lowest: gs.filter(g => !g.overPicture).sort((a, b) => a.contrast - b.contrast).slice(0, 12).map(g => ({ ratio: g.contrast, colour: g.colour, on: g.background, size: g.size, weight: g.weight, large: large(g), chars: g.chars, sample: g.sample })),
    overPicture: gs.filter(g => g.overPicture).sort((a, b) => b.chars - a.chars).slice(0, 6).map(g => ({ colour: g.colour, size: g.size, chars: g.chars, sample: g.sample })),
  };

  // ---- lines: characters a line and leading, on blocks of three lines or more
  const blocks = [];
  for (const el of all('p, li, dd, blockquote, figcaption, td, div')) {
    if (blocks.length >= 400) break;
    if (ownText(el).length < 60 || !shown(el)) continue;
    const range = document.createRange(); range.selectNodeContents(el);
    const tops = [...new Set([...range.getClientRects()].filter(r => r.width > 1).map(r => Math.round(r.top)))].sort((a, b) => a - b);
    const lines = tops.filter((t, i) => i === 0 || t - tops[i - 1] > 3);
    if (lines.length < 3) continue;
    const cs = style(el), size = parseFloat(cs.fontSize), length = el.textContent.replace(/\s+/g, ' ').trim().length;
    blocks.push({ perLine: Math.round(length / (lines.length - 0.5)), lines: lines.length, leading: r1((lines[lines.length - 1] - lines[0]) / (lines.length - 1) / size), size: r1(size), widthPx: Math.round(el.getBoundingClientRect().width), align: cs.textAlign, sample: cut(el.textContent, 40) });
  }
  const byLength = [...blocks].sort((a, b) => a.perLine - b.perLine);
  const lines = {
    find: 'characters line, leading, line height, justified',
    note: 'perLine is characters (spaces included) a full line, on blocks of 3 lines or more; leading is the distance between lines divided by the text size.',
    blocks: blocks.length,
    charactersPerLine: blocks.length ? { shortest: byLength[0].perLine, median: median(blocks.map(b => b.perLine)), longest: byLength[byLength.length - 1].perLine } : null,
    leading: blocks.length ? { lowest: Math.min(...blocks.map(b => b.leading)), median: median(blocks.map(b => b.leading)), highest: Math.max(...blocks.map(b => b.leading)) } : null,
    longestBlocks: byLength.slice(-3).reverse(), shortestBlocks: byLength.slice(0, 3),
    justified: blocks.filter(b => b.align === 'justify').length,
  };

  // ---- targets: what a finger or a pointer has to hit
  const targets = all('a[href], button, input:not([type=hidden]), select, textarea, summary, [role=button], [role=link], [role=tab], [role=checkbox], [role=switch], label[for]').filter(shown).map(el => {
    const r = el.getBoundingClientRect(), inText = inSentence(el);
    return { what: el.tagName.toLowerCase() + (el.type ? '[' + el.type + ']' : '') + ' ' + cut(el.textContent || el.getAttribute('aria-label') || el.value || el.name || '', 30), w: Math.round(r.width), h: Math.round(r.height), inText, labelled: !!(el.labels && el.labels.length) };
  });
  const alone = targets.filter(t => !t.inText);
  const tap = {
    find: 'finger, fingertip, touch',
    note: 'Sizes in CSS pixels. inText: a link inside a sentence, counted apart because its height follows the line of text. A small checkbox or radio with labelled: true is also hit through its label.',
    total: targets.length,
    under24: alone.filter(t => Math.min(t.w, t.h) < 24).length,
    under44: alone.filter(t => Math.min(t.w, t.h) < 44).length,
    inTextLinks: targets.length - alone.length,
    smallest: [...alone].sort((a, b) => Math.min(a.w, a.h) - Math.min(b.w, b.h)).slice(0, 12),
  };

  // ---- headings
  const hs = all('h1, h2, h3, h4, h5, h6, [role=heading]').filter(shown).map(el => ({ level: +(el.getAttribute('aria-level') || el.tagName[1]), text: cut(el.textContent, 50), size: r1(parseFloat(style(el).fontSize)) }));
  const headings = {
    find: 'heading, outline',
    count: hs.length, h1: hs.filter(h => h.level === 1).length, empty: hs.filter(h => !h.text).length,
    skips: hs.map((h, i) => i && h.level > hs[i - 1].level + 1 ? `h${hs[i - 1].level} to h${h.level} at "${h.text}"` : null).filter(Boolean).slice(0, 8),
    outline: hs.slice(0, 40),
  };

  // ---- images
  const resources = performance.getEntriesByType('resource');
  const bytesOf = url => { const e = resources.find(x => x.name === url); return e ? (e.encodedBodySize || e.transferSize || 0) : 0; };
  const imgs = all('img').filter(shown).map(el => {
    const r = el.getBoundingClientRect(), src = el.currentSrc || el.src;
    return { src: tail(src), alt: el.getAttribute('alt'), shownW: Math.round(r.width), shownH: Math.round(r.height), fileW: el.naturalWidth, fileH: el.naturalHeight, kb: kb(bytesOf(src)), sized: el.hasAttribute('width') && el.hasAttribute('height'), lazy: el.loading === 'lazy', vector: /\.svg(\?|$)/i.test(src) || src.startsWith('data:image/svg'), linked: !!el.closest('a') };
  });
  const raster = imgs.filter(i => !i.vector && i.fileW > 0);
  const images = {
    find: 'alt, alternative text, image file, larger than, lossy, format',
    note: 'kb is the file as sent (0: not reported, for example a cached or cross-origin file). stretched: shown wider than the file has pixels. oversized: the file holds more than twice the pixels the screen can show at this width and pixel ratio. notLoaded: pictures whose file had not arrived when the script ran (lazy ones not yet scrolled to, or a broken address); stretched, oversized and heaviest speak only for the loaded ones, so bring the others into view and run again.',
    count: imgs.length, pixelRatio: devicePixelRatio,
    altMissing: imgs.filter(i => i.alt === null).map(i => i.src).slice(0, 10),
    altEmpty: imgs.filter(i => i.alt === '').length,
    altEmptyButLinked: imgs.filter(i => i.alt === '' && i.linked).map(i => i.src).slice(0, 6),
    altTexts: imgs.filter(i => i.alt).slice(0, 12).map(i => cut(i.alt, 70)),
    stretched: raster.filter(i => i.shownW > i.fileW * 1.05).slice(0, 8).map(i => ({ src: i.src, shownW: i.shownW, fileW: i.fileW })),
    oversized: raster.filter(i => i.fileW > i.shownW * devicePixelRatio * 2).slice(0, 8).map(i => ({ src: i.src, shownW: i.shownW, fileW: i.fileW, kb: i.kb })),
    heaviest: [...imgs].sort((a, b) => b.kb - a.kb).slice(0, 8).filter(i => i.kb > 0).map(i => ({ src: i.src, kb: i.kb, shown: i.shownW + 'x' + i.shownH, file: i.fileW + 'x' + i.fileH })),
    notLoaded: imgs.filter(i => !i.vector && !i.fileW).map(i => i.src).slice(0, 12),
    withoutWidthAndHeight: imgs.filter(i => !i.sized).length, lazy: imgs.filter(i => i.lazy).length,
    backgroundPictures: all('*').slice(0, 4000).filter(el => /url\(/.test(style(el).backgroundImage)).length,
  };

  // ---- forms
  // A label that wraps its control: its words are the label's text without the control's own, and its place is
  // where those words stand, not the box that holds both.
  const CONTROL = 'input, select, textarea, button';
  const labelWords = label => { const copy = label.cloneNode(true); copy.querySelectorAll(CONTROL).forEach(c => c.remove()); return copy.textContent; };
  const labelBox = (label, el) => {
    if (!label.contains(el)) return label.getBoundingClientRect();
    const rects = [], walk = document.createTreeWalker(label, NodeFilter.SHOW_TEXT);
    for (let n = walk.nextNode(); n; n = walk.nextNode()) {
      if (!n.nodeValue.trim() || n.parentElement.closest(CONTROL)) continue;
      const range = document.createRange(); range.selectNodeContents(n); rects.push(...range.getClientRects());
    }
    return rects.length ? { top: Math.min(...rects.map(x => x.top)), bottom: Math.max(...rects.map(x => x.bottom)), left: Math.min(...rects.map(x => x.left)), right: Math.max(...rects.map(x => x.right)) } : null;
  };
  const controls = all('input:not([type=hidden]):not([type=submit]):not([type=button]):not([type=image]):not([type=reset]), select, textarea').filter(shown).map(el => {
    const label = el.labels && el.labels[0], r = el.getBoundingClientRect(), lr = label && shown(label) ? labelBox(label, el) : null;
    const named = el.getAttribute('aria-label') || (el.getAttribute('aria-labelledby') || '').split(' ').map(id => (document.getElementById(id) || {}).textContent || '').join(' ').trim();
    const where = !lr ? null : lr.bottom <= r.top + 4 ? 'above' : lr.right <= r.left + 4 ? 'left' : lr.left >= r.right - 4 ? 'right' : lr.top >= r.bottom - 4 ? 'below' : 'around or inside';
    return { control: el.tagName.toLowerCase() + (el.type ? '[' + el.type + ']' : ''), label: label ? cut(labelWords(label), 40) : null, labelIs: where, labelWraps: !!label && label.contains(el), ariaName: named ? cut(named, 40) : null, placeholder: el.placeholder ? cut(el.placeholder, 40) : null, autocomplete: el.getAttribute('autocomplete'), inputmode: el.getAttribute('inputmode'), required: el.required, h: Math.round(r.height), textPx: r1(parseFloat(style(el).fontSize)) };
  });
  const forms = {
    find: 'label, field, placeholder, required, error',
    controls: controls.length,
    noLabel: controls.filter(c => !c.label && !c.ariaName).length,
    placeholderOnly: controls.filter(c => !c.label && !c.ariaName && c.placeholder).length,
    hiddenLabelOnly: controls.filter(c => (c.label && !c.labelIs) || (!c.label && c.ariaName)).length,
    autofocus: all('[autofocus]').length,
    list: controls.slice(0, 25),
  };

  // ---- links
  const as = all('a[href]').filter(shown);
  const name = a => (a.textContent || '').trim() || a.getAttribute('aria-label') || (a.querySelector('img[alt]') || { alt: '' }).alt || a.title || '';
  const plain = as.filter(a => { const cs = style(a), p = a.parentElement; return inSentence(a) && !cs.textDecorationLine.includes('underline') && cs.color === style(p).color && cs.fontWeight === style(p).fontWeight; });
  const links = {
    find: 'link, underline, visited, new window, click here',
    count: as.length,
    noName: as.filter(a => !name(a)).map(a => tail(a.href)).slice(0, 8),
    vagueWords: as.filter(a => /^(click here|here|more|read more|learn more|details|link|this)$/i.test(name(a).trim())).map(a => cut(name(a), 20)).slice(0, 8),
    lookLikeTheTextAround: plain.map(a => cut(a.textContent, 30)).slice(0, 8),
    openNewWindow: as.filter(a => a.target === '_blank').length,
    goNowhere: as.filter(a => /^(#|javascript:)/i.test(a.getAttribute('href') || '')).length,
    rawAddressesAsText: as.filter(a => /^https?:\/\//i.test(name(a))).length,
  };

  // ---- page and speed
  const viewport = (document.querySelector('meta[name=viewport]') || {}).content || null;
  // The whole page, also when one part is measured: a fixed bar elsewhere still covers the part on screen.
  const fixed = [...document.querySelectorAll('*')].slice(0, 4000).filter(el => /^(fixed|sticky)$/.test(style(el).position) && shown(el));
  const page = {
    find: 'viewport, zoom, language, encoding, sideways scrolling',
    url: location.origin + location.pathname, title: document.title, lang: document.documentElement.lang || null, dir: document.documentElement.dir || null,
    charset: document.characterSet, viewportMeta: viewport, zoomBlocked: !!viewport && /user-scalable\s*=\s*(no|0)|maximum-scale\s*=\s*1(\.0*)?(\D|$)/i.test(viewport),
    windowPx: innerWidth + 'x' + innerHeight, pixelRatio: devicePixelRatio,
    sidewaysOverflowPx: Math.max(0, document.documentElement.scrollWidth - innerWidth),
    screensTall: r1(document.documentElement.scrollHeight / innerHeight),
    fixedOrSticky: fixed.slice(0, 5).map(el => ({ what: el.tagName.toLowerCase() + (el.id ? '#' + el.id : ''), h: Math.round(el.getBoundingClientRect().height), shareOfScreen: Math.round(100 * el.getBoundingClientRect().height / innerHeight) + '%' })),
    script: '2026-11-21b', measuredPart: window.WEB_CHECK_ROOT || 'the whole page', textRunsRead: seen,
  };
  const observed = (type, ms = 250) => new Promise(done => {
    const got = [];
    try { const po = new PerformanceObserver(list => got.push(...list.getEntries())); po.observe({ type, buffered: true }); setTimeout(() => { po.disconnect(); done(got); }, ms); } catch (e) { done(got); }
  });
  const [lcp, shifts] = await Promise.all([observed('largest-contentful-paint'), observed('layout-shift')]);
  const nav = performance.getEntriesByType('navigation')[0] || {};
  const kind = e => { const p = e.name.split('?')[0]; return /\.(woff2?|ttf|otf|eot)$/i.test(p) ? 'font' : /\.(png|jpe?g|gif|webp|avif|svg|ico)$/i.test(p) || e.initiatorType === 'img' ? 'image' : /\.css$/i.test(p) ? 'css' : /\.m?js$/i.test(p) || e.initiatorType === 'script' ? 'script' : 'other'; };
  const byKind = {}; let unknown = 0;
  for (const e of resources) { const b = e.encodedBodySize || e.transferSize || 0; if (!b) unknown++; const k = kind(e); byKind[k] = byKind[k] || { files: 0, kb: 0 }; byKind[k].files++; byKind[k].kb = r1(byKind[k].kb + b / 1024); }
  const speed = {
    find: 'seconds, response time, page weight, requests, font files',
    note: 'Times in ms from the start of the navigation, on this machine and connection: a local server says nothing about a real line. largestPaintMs null: the browser reported none (it reports none for a page loaded in a hidden pane). Sizes are files as sent; sizeUnknown counts files the browser reports no size for.',
    serverAnswerMs: Math.round(nav.responseStart || 0), domReadyMs: Math.round(nav.domContentLoadedEventEnd || 0), loadedMs: Math.round(nav.loadEventEnd || 0),
    largestPaintMs: lcp.length ? Math.round(lcp[lcp.length - 1].startTime) : null,
    layoutShift: Math.round(1000 * shifts.filter(s => !s.hadRecentInput).reduce((s, e) => s + e.value, 0)) / 1000,
    htmlKb: kb(nav.encodedBodySize || 0), requests: resources.length + 1, sizeUnknown: unknown,
    totalKb: r1(Object.values(byKind).reduce((s, k) => s + k.kb, 0) + (nav.encodedBodySize || 0) / 1024), byKind,
    largestFiles: [...resources].sort((a, b) => (b.encodedBodySize || 0) - (a.encodedBodySize || 0)).slice(0, 6).filter(e => e.encodedBodySize).map(e => ({ file: tail(e.name), kb: kb(e.encodedBodySize) })),
    domNodes: document.getElementsByTagName('*').length,
  };

  return {
    page, text, contrast, lines, tap, headings, images, forms, links, speed,
    notMeasured: [
      'the colour of visited links (browsers hide it from scripts)',
      'focus and hover styles, and anything that appears only after a click or a tap',
      'the page with its text enlarged to 200% or zoomed',
      'the page on a slow connection or with images off',
      'text inside pictures, and whether a picture suits its place',
      'the space between parts (margins, gaps, a spacing scale) and the drawn size of a logo: read them from the code',
      'whether the words are right: clarity, tone, what the page says first',
    ],
  };
};
  try { sessionStorage.setItem('webCheckMeasure', '(' + measure + ')()'); } catch (e) { /* storage blocked: pass the file again */ }
  return measure();
})()
