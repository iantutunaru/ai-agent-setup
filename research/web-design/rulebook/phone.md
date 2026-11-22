# Web design rulebook: phone

40 entries: 1 rule, 39 practice. Built by a script from the owner's reading notes, which are not published; not edited by hand. How to read an entry: [README.md](README.md).

### phone-002 · On small screens the device's own fonts can serve better than downloaded ones
- **Statement:** Small-screen devices may be on a mobile connection, so fonts already on the device can perform better than downloaded web fonts; where possible, use web fonts only on large screens.
- **Kind:** practice
- **Use:** look, check
- **Sources:** ROBBINS-309 (page 604)
- **Needs source:** whether web fonts are still best kept to large screens (web.dev gives its font advice for every screen and does not treat phones apart)
- **Current source:** confirmed by https://web.dev/articles/font-best-practices (read 2026-11-20)
- **Read:** 2026-11-20, passage; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate speed E68

### phone-004 · Most web use is on phones, and for some the phone is the only way online
- **Statement:** Mobile web use overtook desktop use in 2016, and for about 10% of Americans a smartphone or tablet is the only way to get online; younger users tend to choose mobile devices, and most people use several platforms in a day. So the choice of a site's design and functions for phones is very important.
- **Kind:** rule
- **Use:** look
- **Sources:** ROBBINS-272 (page 585), ROBBINS-003 (page 62)
- **Study (as the book reports it):** ROBBINS-272: Pew Research Center, "Smartphone Use in 2015", for the 10%; the book names no source for the 2016 overtaking.
- **Needs source:** today's shares of mobile and desktop web use (only StatCounter, an analytics vendor, gives them)
- **Current source:** confirmed by https://www.pewresearch.org/internet/2015/04/01/us-smartphone-use-in-2015/ (read 2026-11-20)
- **Current source:** confirmed by https://www.pewresearch.org/internet/fact-sheet/mobile/ (read 2026-11-20)
- **Read:** 2026-11-20, page; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate phone E02

### phone-005 · The same usability principles hold on phones
- **Statement:** The usability principles that hold on a large screen hold on a phone, and if anything people move faster and read even less on small screens.
- **Kind:** practice
- **Use:** look, text
- **Sources:** KRUG-128 (page s97)
- **Read:** 2026-11-20, passage; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate phone E03

### phone-006 · On a small screen, crop the picture instead of only shrinking it
- **Statement:** Scaling is sometimes not enough: fine details of a large scene cannot be made out on a phone. For small screens offer a tighter version that keeps the important details (minor details cropped away, a portrait crop instead of a wide one, text inside it changed or removed) instead of a scaled-down one that loses them.
- **Kind:** practice
- **Use:** look, check
- **Sources:** ROBBINS-107 (page 207), ROBBINS-323 (page 607)
- **Also in (not read):** ROBBINS-410
- **Read:** 2026-11-20, passage; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate images E31

### phone-008 · Design web access on a television for the television
- **Statement:** Television and computer use differ in screen resolution, input device (remote against mouse and keyboard), viewing distance (metres against tens of centimetres), posture, room, number of viewers and passive against active use. Web access on a television should be more interactive and personal than broadcast television, but move in directions that suit the television as a device; following link after link, as on a computer, suits it poorly.
- **Kind:** practice
- **Use:** look
- **Sources:** NIELSEN-597 (page 462-463)
- **Asked of the source:** that current guidance for television and other screens away from the desk still sets them apart by input device, viewing distance and posture.
- **Current source:** confirmed by https://developer.android.com/design/ui/tv/guides/foundations/design-for-tv (read 2026-11-20)
- **Read:** 2026-11-20, page; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate phone E04

### phone-009 · One responsive site, not separate versions for different screens
- **Statement:** Build one site whose layout adapts to every screen size instead of keeping separate versions: separate versions at least double the work (content planning, design templates, production and upkeep) and drift out of sync. A separate mobile site can be the best choice when mobile visitors are known to use the service in clearly different patterns from desktop visitors; a mostly text site needs only a little layout tuning. One responsive design is itself much work and hard to do well.
- **Kind:** practice
- **Use:** look
- **Sources:** KRUG-133 (page s100), ROBBINS-013 (page 67-68, the notes cite 67)
- **Also in (not read):** BEAIRD-070, CEDERHOLM-089
- **Read:** 2026-11-20, page; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate phone E05

### phone-010 · Search ranking favours one responsive site over a separate mobile one
- **Statement:** Google pushed sites with a separate mobile address to move to responsive design before its mobile-first index (2018) and favours responsive sites with a single address over separate mobile versions; a site that struggles in search rankings may improve them by switching to responsive design.
- **Kind:** practice
- **Use:** look, check
- **Sources:** ROBBINS-015 (page 68), ROBBINS-273 (page 586)
- **Asked of the source:** what Google says today about responsive design, separate mobile addresses and mobile-first indexing.
- **Current source:** confirmed by https://developers.google.com/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing (read 2026-11-20)
- **Conflict:** Google Search Central today recommends responsive design because it is the easiest to build and maintain, and still documents separate mobile addresses as a supported setup; it names no ranking advantage for responsive sites
- **Read:** 2026-11-20, passage; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate phone E06

### phone-011 · Layout changes alone may not be enough on a large site
- **Statement:** Changing the layout by screen width is not a whole mobile strategy. A small brochure site can manage with layout changes alone, but a large, complex site may need different content, navigation and functions on phones, with the device detected and the content chosen on the server.
- **Kind:** practice
- **Use:** look
- **Sources:** GILLENWATER-081 (page 245), ROBBINS-012 (page 67)
- **Conflict:** KRUG-131, ROBBINS-002, GOLDSTEIN-050 (in content-219) say to send every device the same content and not to cut the phone site down.
- **Read:** 2026-11-20, passage; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate phone E10

### phone-012 · A few links can simply sit in a row or two at the top of a small screen
- **Statement:** The real difficulty of navigation is reorganising it for small screens. A site with only a few navigation links (Nielsen Norman Group: four or fewer on phones) can set them in one or two rows at the top of the screen; a bar that also holds a logo and a search box may need different arrangements at several breakpoints.
- **Kind:** practice
- **Use:** look, check
- **Sources:** ROBBINS-316 (page 606), ROBBINS-333 (page 612)
- **Asked of the source:** current guidance on how many links a phone screen can show in rows at the top.
- **Current source:** confirmed by https://www.nngroup.com/articles/hamburger-menus/ (read 2026-11-20)
- **Current source:** confirmed by https://www.nngroup.com/articles/mobile-navigation-patterns/ (read 2026-11-20)
- **Read:** 2026-11-20, page; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate navigation E86

### phone-013 · Content hidden on a narrow screen is still downloaded
- **Statement:** Avoid hiding or swapping content for narrow screens with style rules alone where possible: the hidden content may still be downloaded to the device, so hiding it is not a real saving.
- **Kind:** practice
- **Use:** check
- **Sources:** CEDERHOLM-088 (page 298), GILLENWATER-082 (page 245-246)
- **Needs source:** whether images loaded at once, and background images, hidden by a style rule for narrow screens are still downloaded
- **Current source:** confirmed by https://web.dev/articles/browser-level-image-lazy-loading (read 2026-11-20)
- **Conflict:** web.dev: Chrome, Safari and Firefox do not load a lazy-loaded image hidden with display: none (on the image or a parent); one hidden with opacity: 0 still loads
- **Read:** 2026-11-20, passage; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate speed E45

### phone-014 · Tell the phone to lay the page out at its real width
- **Statement:** Without a viewport setting a phone browser lays the page out on a wide virtual canvas (980 points in mobile Safari; one book gives 980 pixels for the iPhone, 800 for Android's browser and 850 for Opera) and scales it down to the screen, so layout rules for small screens do not take effect. Setting the viewport width to the device width, with initial scale 1, makes the page render at the screen's real width; it is the important first step for media queries.
- **Kind:** practice
- **Use:** check
- **Sources:** ROBBINS-275 (page 587), GILLENWATER-090 (page 255-256, the notes cite 256)
- **Also in (not read):** CEDERHOLM-085
- **Asked of the source:** that phone browsers still lay a page out on a wide virtual canvas unless it sets the viewport width to the device width.
- **Current source:** confirmed by https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/viewport (read 2026-11-20)
- **Current source:** confirmed by https://web.dev/articles/responsive-web-design-basics (read 2026-11-20)
- **Conflict:** MDN (viewport) calls initial-scale=1 usually unnecessary; web.dev still sets it so the page keeps a 1:1 scale when turned to landscape
- **Read:** 2026-11-20, page; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate phone E19

### phone-015 · A desktop page shrunk to fit a phone gives a poor experience
- **Statement:** A desktop page simply shrunk to fit a phone screen gives a poor experience: the text is too small to read, the links are too small to hit with a finger, and constant zooming and scrolling distracts the user.
- **Kind:** practice
- **Use:** check
- **Sources:** ROBBINS-010 (page 65)
- **Read:** 2026-11-20, passage; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate phone E20

### phone-017 · Replace a large embedded map with a link to the phone's maps app
- **Statement:** A large embedded map that works on a desktop is of little use at postage-stamp size. Consider replacing such interactive features on a small screen, for instance with a link that opens the device's own maps app, which gives a better map there; other components, such as carousels, can be adapted.
- **Kind:** practice
- **Use:** look, check
- **Sources:** ROBBINS-327 (page 608)
- **Read:** 2026-11-20, passage; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate phone E32

### phone-018 · Use the browser's preset sizes to see where the breakpoints fall
- **Statement:** Test responsive layouts quickly with the browser's responsive design mode or preset window sizes, which show the viewport's exact pixel size, common device sizes and your own breakpoints. Resizing a desktop window does not truly emulate a phone: it misses the effect of the viewport setting, for instance.
- **Kind:** practice
- **Use:** check
- **Sources:** ROBBINS-297 (page 600), GILLENWATER-091 (page 257)
- **Asked of the source:** what the responsive design modes of current browsers show and what they do not emulate (MDN, the browsers' developer tools documentation).
- **Current source:** confirmed by https://developer.chrome.com/docs/devtools/device-mode (read 2026-11-20)
- **Read:** 2026-11-20, passage; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate testing E44

### phone-019 · A large data table shrunk to the screen cannot be read
- **Statement:** By default a large data table shrinks to the width of the screen, so the text in its cells is too small to read, and zooming in shows only a few cells at a time, so users lose track of which headings and columns they are in.
- **Kind:** practice
- **Use:** look, check
- **Sources:** ROBBINS-330 (page 609)
- **Read:** 2026-11-20, passage; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate phone E33

### phone-020 · A table on a narrow screen scrolls, stacks or hides columns
- **Statement:** A table on a narrow screen follows one of three approaches: scrolling sideways (optionally with the left column pinned); stacking each record into a narrow strip with the headings repeated, which shows all data but is long and hard to compare; or hiding some columns at first with controls to show them, which is riskier because users may never see them. Which is best depends on the kind of data and how the table will be used.
- **Kind:** practice
- **Use:** look, check
- **Sources:** ROBBINS-331 (page 609)
- **Asked of the source:** current guidance on tables on small screens (Nielsen Norman Group, MDN).
- **Current source:** confirmed by https://www.nngroup.com/articles/mobile-tables/ (read 2026-11-20)
- **Current source:** confirmed by https://developer.chrome.com/docs/modern-web-guidance/guides/ui-atoms/responsive-table (read 2026-11-20)
- **Read:** 2026-11-20, page; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate layout E124

### phone-021 · Make links large enough to hit with a finger
- **Statement:** People operate touch screens with their fingers, large tablets and convertibles included, so make links, and navigation links above all, large enough on touch screens to hit easily with a fingertip. Apple's default control size for apps, 44 by 44 points, is a good guide for web links; WCAG 2.2 asks at least 24 by 24 CSS pixels (level AA) and 44 by 44 at level AAA.
- **Kind:** practice
- **Use:** look, check
- **Sources:** GILLENWATER-068 (page 228), ROBBINS-328 (page 608)
- **Asked of the source:** the smallest touch target Apple's guidelines and WCAG give today.
- **Current source:** confirmed by https://developer.apple.com/design/human-interface-guidelines/accessibility (read 2026-11-20)
- **Current source:** confirmed by https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html (read 2026-11-20)
- **Read:** 2026-11-20, passage; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate phone E34, joined by phone E35

### phone-022 · Fields and labels fit a fingertip
- **Statement:** Forms may be filled in with fingertips and not a mouse: make fields larger, with enough padding or margins, and make labels tappable, so that touching one starts input in its field.
- **Kind:** practice
- **Use:** look, check
- **Sources:** ROBBINS-326 (page 608)
- **Asked of the source:** what size of touch target current guidelines (WCAG, Apple) ask for, and that tapping a label tied to its field starts input in it in current phone browsers.
- **Current source:** confirmed by https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/label (read 2026-11-20)
- **Current source:** confirmed by https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html (read 2026-11-20)
- **Read:** 2026-11-20, passage; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate forms E31

### phone-024 · Nothing may depend on hover or on the pointer's shape
- **Statement:** Touch screens cannot sense hover and have no pointer, so tooltips, hover changes that show what is clickable and menus that open on hover do not exist for phone users and must be replaced with something else. The pointer turning into a hand is a weak sign of what is clickable: it needs slow, deliberate pointing, and touch screens have no pointer. Where navigation or anything else on a site uses hover, test it carefully on the devices; otherwise avoid hover or find an alternative.
- **Kind:** practice
- **Use:** look, check
- **Sources:** KRUG-138 (page s102), KRUG-030 (page s32), ROBBINS-329 (page 608)
- **Asked of the source:** how current touch browsers treat hover and whether a page can now reliably tell a pointer that hovers from one that does not; the book of 2018 says a media query for hover was not yet usable.
- **Current source:** confirmed by https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/hover (read 2026-11-20)
- **Read:** 2026-11-20, page; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate phone E36, joined by navigation E70

### phone-025 · Check fancy faces on small screens
- **Statement:** When shrunk for a small screen, thin strokes become too faint and flourishes turn into dots, so check that a fancy typeface stays legible there; a decorative display font can be kept for screens wide enough for it (the example switches at 40em), with a plain serif as the default on narrower ones.
- **Kind:** practice
- **Use:** look, check
- **Sources:** ROBBINS-308 (page 604), ROBBINS-287 (page 593)
- **Needs source:** current practice for switching a font by viewport width.
- **Current source:** none found (searched 2026-11-20)
- **Read:** 2026-11-20, passage; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate type E43

### phone-027 · Spaced capital headings on narrow screens
- **Statement:** Headings in capitals with wide letter spacing take much room and may overflow a narrow column; reduce their size and letter spacing at narrow widths.
- **Kind:** practice
- **Use:** check
- **Sources:** GILLENWATER-080 (page 243)
- **Read:** 2026-11-20, passage; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate type E150

### phone-028 · From one column on a phone to more columns as space grows
- **Statement:** A single fluid layout is not enough for every screen; usually two or three layouts are designed, with small adjustments between them, starting from a single column for phones and regrouping into more columns as space grows. Most phone pages are a single column, because a small screen has no room for columns side by side: content laid out side by side on a wide screen (such as three author profiles) stacks top to bottom, each part at full width, and sidebars go under the main content. Two common patterns: "mostly fluid", a single column on small screens and a fluid layout with a maximum width on larger ones, and "column drop", which steps between one, two and three columns, dropping sidebar columns below the others when there is no room.
- **Kind:** practice
- **Use:** look, check
- **Sources:** ROBBINS-305 (page 603), ROBBINS-302 (page 602), GILLENWATER-084 (page 248), GOLDSTEIN-054 (page 284)
- **Also in (not read):** ROBBINS-105, ROBBINS-306, GILLENWATER-069, LUPTON-187, NIELSEN-587
- **Read:** 2026-11-20, passage; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate layout E152, joined by phone E24

### phone-029 · An off-canvas panel leaves a strip of the page in view
- **Statement:** In an off-canvas pattern a page component sits beside the screen and slides in on request, while a strip of the main content stays visible at the edge so users understand how the moving parts relate.
- **Kind:** practice
- **Use:** look, check
- **Sources:** ROBBINS-307 (page 604)
- **Needs source:** current guidance on off-canvas panels and drawers on phones (Nielsen Norman Group, Apple's guidelines).
- **Current source:** none found (searched 2026-11-20)
- **Read:** 2026-11-20, passage; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate layout E153

### phone-030 · Keep side margins minimal on small screens
- **Statement:** On small screens use the space fully by keeping the side margins of the main column minimal (2 to 4%). Widen them as screens grow, to control line length or add breathing room, and set the space above and below text elements in ems so it stays in proportion to the type.
- **Kind:** practice
- **Use:** look, check
- **Sources:** ROBBINS-313 (page 605)
- **Needs source:** that current guidance for phone layouts keeps the side margins of the main column to a few percent of the screen width.
- **Current source:** none found (searched 2026-11-20)
- **Read:** 2026-11-20, passage; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate spacing E22

### phone-031 · Show the most important links and put the rest behind "More"
- **Statement:** In the "priority plus" pattern the most important links show in a row at the top beside a "More" link that opens the rest. The main links stay visible and more of them can appear as the screen widens, but deciding which links matter most on a small screen is hard.
- **Kind:** practice
- **Use:** look
- **Sources:** ROBBINS-317 (page 606)
- **Asked of the source:** current guidance on this pattern for phone screens.
- **Current source:** confirmed by https://www.nngroup.com/articles/hamburger-menus/ (read 2026-11-20)
- **Read:** 2026-11-20, passage; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate navigation E87

### phone-032 · A menu behind a menu icon: push the page down, lay over it, or slide in from the side
- **Statement:** A menu hidden behind a menu icon can push the page content down when it opens, lay itself over the content, or come in as an off-canvas panel from the left or right.
- **Kind:** practice
- **Use:** look
- **Sources:** ROBBINS-321 (page 607)
- **Needs source:** current guidance on menus hidden behind an icon on phone screens and on which of the three forms to prefer.
- **Current source:** none found (searched 2026-11-20)
- **Read:** 2026-11-20, passage; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate navigation E88

### phone-033 · A "Menu" link that jumps to the footer navigation can disorient
- **Statement:** A "Menu" link at the top that jumps to the full navigation in the footer is simple, but it can disorient users who suddenly find themselves at the bottom of the page.
- **Kind:** practice
- **Use:** look, check
- **Sources:** ROBBINS-319 (page 606)
- **Needs source:** current guidance on this pattern for phone screens.
- **Current source:** none found (searched 2026-11-20)
- **Read:** 2026-11-20, passage; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate navigation E89

### phone-034 · Avoid nested submenus on a small screen, or open them as accordions
- **Statement:** Many links with nested submenus are hard on a small screen without precise mouse pointing. One answer is accordion submenus opened by a small arrow; another is to link each main item to a section landing page that lists the section's sub-navigation, which avoids nesting.
- **Kind:** practice
- **Use:** look, check
- **Sources:** ROBBINS-320 (page 607)
- **Asked of the source:** current guidance on nested menus on touch screens.
- **Current source:** confirmed by https://www.nngroup.com/articles/mobile-subnavigation/ (read 2026-11-20)
- **Read:** 2026-11-20, passage; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate navigation E90

### phone-035 · On a long page, links that jump to content further down
- **Statement:** On small phone screens, links within the page that jump to content further down can be shown; the book lists this among the uses of rules that depend on screen size. Scroll shortcuts within one long page, such as an alphabet strip that jumps to a letter in a long list, are fine, since the user stays on the same page; Nielsen says this of frames used that way.
- **Kind:** practice
- **Use:** look, check
- **Sources:** GILLENWATER-071 (page 231), NIELSEN-124 (page 112)
- **Asked of the source:** current guidance on in-page jump links on phone screens.
- **Current source:** confirmed by https://www.nngroup.com/articles/avoid-within-page-links/ (read 2026-11-20)
- **Conflict:** NIELSEN-177 (in navigation-082) says to avoid links that jump within the same page.
- **Read:** 2026-11-20, passage; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate navigation E91

### phone-036 · A form shrinks to fit a narrow screen
- **Statement:** Give a form a maximum width, so it can shrink to fit smaller viewports.
- **Kind:** practice
- **Use:** look, check
- **Sources:** ROBBINS-223 (page 656)
- **Also in (not read):** ROBBINS-241
- **Read:** 2026-11-20, passage; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate forms E30

### phone-037 · Decide the order of content for each screen size before building
- **Statement:** Plan the content before any code, with special attention to small screens: pick out what is most useful and important, split it into modules, then decide the order in which they appear at each screen size.
- **Kind:** practice
- **Use:** look
- **Sources:** ROBBINS-300 (page 601-602)
- **Also in (not read):** ROBBINS-332
- **Read:** 2026-11-20, passage; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate content E168

### phone-038 · On a television screen, short pages, short text and short summaries
- **Statement:** For sites that must work on WebTV (web access on a television set) the book advises many small, well-linked pages, each ideally fitting on one WebTV screen, and as little text as possible; the New York Times front page needed much scrolling on WebTV but stayed easy to read because its article summaries were brief.
- **Kind:** practice
- **Use:** look, text
- **Sources:** NIELSEN-586 (page 446), NIELSEN-588 (page 450)
- **Asked of the source:** whether advice set for television-sized screens of about 2000 (one screen per page, little scrolling) holds for today's phones.
- **Current source:** confirmed by https://www.nngroup.com/articles/mobile-content/ (read 2026-11-20)
- **Read:** 2026-11-20, page; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate content E169

### phone-039 · Do not switch off zooming on a phone
- **Statement:** Do not set a maximum scale of 1 in the page's viewport setting: it can stop users zooming the page, and being able to resize matters for accessibility and usability. W3C's test for WCAG 1.4.4 fails a maximum scale below 2; most current phone browsers ignore the setting or offer a way round it.
- **Kind:** practice
- **Use:** check
- **Sources:** ROBBINS-276 (page 587), KRUG-134 (page s100)
- **Asked of the source:** that the viewport setting still blocks zoom in current phone browsers, and what WCAG says on it.
- **Current source:** confirmed by https://www.w3.org/WAI/standards-guidelines/act/rules/b4f0c3/ (read 2026-11-20)
- **Current source:** confirmed by https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/viewport (read 2026-11-20)
- **Read:** 2026-11-20, passage; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate accessibility E63, joined by phone E21

### phone-041 · A test on a phone follows the same process as on a computer
- **Statement:** Testing on phones follows the same process as on computers: tasks, thinking aloud, silence, probing at the end, observers. Only the logistics differ: whose device it is, how it is held, what the observers see and how the session is recorded.
- **Kind:** practice
- **Use:** check
- **Sources:** KRUG-147 (page s109-s110)
- **Read:** 2026-11-20, page; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate testing E39

### phone-042 · In a phone test show the observers the fingers on the screen
- **Statement:** For phone tests give observers a camera view of the screen with the participant's fingers, not a mirrored screen, which hides taps and gestures. Mount the camera on the phone itself, letting the participant hold it in the usual way, and skip a face camera, because the voice shows feelings well enough.
- **Kind:** practice
- **Use:** check
- **Sources:** KRUG-148 (page s111)
- **Asked of the source:** whether today's screen recording and mirroring on phones show taps and gestures (Nielsen Norman Group on mobile usability testing); the book is based on tools of 2013.
- **Current source:** confirmed by https://www.nngroup.com/articles/mobile-usability-testing/ (read 2026-11-20)
- **Conflict:** WALTER-075 (in testing-014) says to look at users' faces at key moments.
- **Read:** 2026-11-20, page; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate testing E40

### phone-043 · Before launch test on real devices, not only in the browser's phone view
- **Statement:** The browser's responsive view is fine for the first design, but a site needs far more thorough testing before launch, above all where it uses JavaScript or server-side features. Nothing replaces testing on many real devices and systems, which shows how fast the page loads, whether links are easy to tap and whether the interactive features work at all.
- **Kind:** practice
- **Use:** check
- **Sources:** ROBBINS-335 (page 615)
- **Read:** 2026-11-20, passage; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate testing E41

### phone-044 · The smallest set of devices to test on
- **Statement:** Without a company device lab, test at least on an iPhone, an Android phone, an iPad, a 7-inch tablet and macOS and Windows computers; used devices on Wi-Fi, a public device lab or phones borrowed from friends and colleagues will do. A synchronisation tool on the computer can push the same page to all the devices at once.
- **Kind:** practice
- **Use:** check
- **Sources:** ROBBINS-336 (page 615-616, the notes cite 616), ROBBINS-337 (page 616)
- **Asked of the source:** which devices and screen sizes a minimum test set should hold today, and which tools load one page on several devices at once (web.dev, MDN on cross-browser testing).
- **Current source:** confirmed by https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Testing/Testing_strategies (read 2026-11-20)
- **Read:** 2026-11-20, page; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate testing E42

### phone-045 · Where a device is missing, an emulator or an online service beats not testing
- **Statement:** Where a device is not available, an emulator of its hardware and system shows how the site will behave on it, and online testing services give access to simulators of over a thousand devices, some free. Emulators use much memory and can have bugs, and the services do not give the insight of real devices, but both are better than not testing that device; the services' screenshots show how differently one page can render.
- **Kind:** practice
- **Use:** check
- **Sources:** ROBBINS-338 (page 616-617, the notes cite 617), ROBBINS-339 (page 617)
- **Asked of the source:** which emulators and online device testing services exist today and what they cannot show (MDN on cross-browser testing).
- **Current source:** confirmed by https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Testing/Testing_strategies (read 2026-11-20)
- **Read:** 2026-11-20, page; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate testing E43

### phone-046 · Header elements overlap sooner when the text is enlarged
- **Statement:** On small screens header elements such as a search form and the logo can overlap, and sooner when the user has set a larger text size. The book's remedy is to make the search field narrower and, on screens up to 400 pixels wide, to set its label on a line above the field.
- **Kind:** practice
- **Use:** look, check
- **Sources:** GILLENWATER-088 (page 251-252, the notes cite 251)
- **Read:** 2026-11-20, page; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate testing E45

### phone-047 · Go through six areas when a page must fit many screen sizes
- **Statement:** When a site is optimised for many viewport sizes, go through six areas: content hierarchy, layout, typography, navigation, images, and special content such as tables, forms and interactive features.
- **Kind:** practice
- **Use:** check
- **Sources:** ROBBINS-299 (page 601)
- **Read:** 2026-11-20, passage; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate process E87
