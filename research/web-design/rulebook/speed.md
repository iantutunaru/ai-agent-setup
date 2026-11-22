# Web design rulebook: speed

42 entries: 6 rule, 36 practice. Built by a script from the owner's reading notes, which are not published; not edited by hand. How to read an entry: [README.md](README.md).

### speed-001 · Make fast loading the first criterion of a page's design
- **Statement:** Treat download speed as the main criterion when building a page: keep graphics to a minimum and use multimedia only where it really helps users understand. After every lecture the author gave from 1994 on, users asked for faster pages; on a nearly graphic-free medical lab site, 45 of 201 free-form feedback comments praised the fast loading while one complained of unimaginative design. Restraint need not mean a dull site: coloured table cells, restrained use of fonts and above all style sheets give design without slow downloads.
- **Kind:** practice
- **Use:** look
- **Sources:** NIELSEN-054 (page 63), NIELSEN-041 (page 54), NIELSEN-051 (page 62)
- **Read:** 2026-11-21, passage, Opus agent, each part checked by Claude; candidate speed E02

### speed-002 · Three limits of response time: 0.1, 1 and 10 seconds
- **Statement:** A response within 0.1 second feels instant and needs no feedback; direct manipulation of objects on screen (rotating a shape, hover hints) must answer within 0.1 second of the key press or mouse move to feel direct. Up to 1 second the delay is noticed but the flow of thought is unbroken. 10 seconds is the limit of keeping attention on the task, after which people turn to other things; users still keep following links if pages arrive within 20 seconds.
- **Kind:** rule
- **Use:** look, check
- **Sources:** NIELSEN-043 (page 58), NIELSEN-212 (page 163)
- **Study (as the book reports it):** NIELSEN-043: Robert B. Miller, paper at the Fall Joint Computer Conference, 1968.
- **Needs source:** whether users still keep following a site's links when pages arrive within 20 seconds; the figure is the book's, of 1999
- **Current source:** confirmed by https://www.nngroup.com/articles/response-times-3-important-limits/ (read 2026-11-21)
- **Read:** 2026-11-21, page, Opus agent, each part checked by Claude; candidate speed E05

### speed-003 · No page should take more than ten seconds
- **Statement:** As a minimum, users should never wait more than 10 seconds for a page, the limit of how long a person holds attention while waiting; past it they become annoyed, and good navigation needs even less. On one newspaper site, page thumbnails of about 60 kB that took about 20 seconds each over a 28.8 kbit/s modem made navigation very slow.
- **Kind:** practice
- **Use:** check
- **Sources:** NIELSEN-044 (page 58), NIELSEN-329 (page 243)
- **Conflict:** ROBBINS-023 (in speed-004) says users expect a site to load in under 2 seconds and almost a third leave if it does not.
- **Read:** 2026-11-21, passage, Opus agent, each part checked by Claude; candidate speed E07

### speed-004 · Users expect a site to load in under two seconds
- **Statement:** Users expect a site to load in under 2 seconds, and almost a third leave for another site if it does not and rarely come back, according to studies the book cites without naming them; Google also uses speed in search ranking. Current sources carry the direction and the ranking: the BBC lost a further 10% of users for every extra second its site took to load (web.dev), and Google asks for the main content to appear within 2.5 seconds of the page starting to load (Largest Contentful Paint) and says page experience aligns with what its ranking systems reward.
- **Kind:** rule
- **Use:** check
- **Sources:** ROBBINS-023 (page 71-72, the notes cite 72)
- **Study (as the book reports it):** "other studies", not named or described (Robbins, page 71)
- **Needs source:** a current study of how fast users expect a page to load and what share leave; the 2 seconds and the one third are from studies the book does not name
- **Current source:** confirmed by https://web.dev/learn/performance/why-speed-matters (read 2026-11-21)
- **Current source:** confirmed by https://developers.google.com/search/docs/appearance/core-web-vitals (read 2026-11-21)
- **Conflict:** NIELSEN-044, NIELSEN-329 (in speed-003) give 10 seconds as the longest acceptable wait for a page.
- **Read:** 2026-11-21, passage, Opus agent, each part checked by Claude; candidate speed E08

### speed-005 · Show progress, and a way to cancel, for anything over ten seconds
- **Statement:** Any operation that takes more than 10 seconds needs a progress indicator showing its actual state (for a file upload, for example, the percentage complete) and the estimated time to finish, in the user's terms and not the system's. A program in the page that calls the server (the book: an applet) should also offer a cancel button to stop an operation that runs too slowly; the chance to cancel matters most for calls to the server, which often meet delays from the internet.
- **Kind:** practice
- **Use:** look, check
- **Sources:** NIELSEN-418 (page 311), ROBBINS-146 (page 265)
- **Read:** 2026-11-21, page, Opus agent, each part checked by Claude; candidate speed E10, joined by forms E92

### speed-006 · State the format and size of a download beside its link
- **Statement:** State a file's format and size beside its link, so users can decide whether to download it and predict the wait. Current sources ask this for every link to a file (NN/g for PDFs; the U.S. Web Design System, in the form [file type, size]); the book (1999) asked it from a ten-second download on the audience's usual connection. If the audience's connection speed is unknown, the book advises finding it out by survey, since it affects many design choices.
- **Kind:** practice
- **Use:** look, check, text
- **Sources:** NIELSEN-216 (page 165), NIELSEN-048 (page 60)
- **Asked of the source:** that stating a large file's format and size beside its link is still advised, and which file size takes more than ten seconds on today's usual connections; NIELSEN-048's 50 KB threshold is for the analogue modems of 1999
- **Current source:** confirmed by https://www.nngroup.com/articles/avoid-pdf-for-on-screen-reading/ (read 2026-11-21)
- **Current source:** confirmed by https://designsystem.digital.gov/components/link/ (read 2026-11-21)
- **Read:** 2026-11-21, page, Opus agent, each part checked by Claude; candidate speed E12

### speed-007 · File sizes from which the size is stated, and the playing time of media
- **Statement:** Give the size of a downloadable file beside its link, the playing time of media, and the format if it is not a standard one. Current sources ask for the size on every file link (NN/g) and for a video's length on the page before it plays, so users can decide whether to play it (NN/g); the book's thresholds, any file from 50 kB with most home users on 56 kbit/s modems and from 200 kB for corporate users on faster lines, were set for the connections of 1999.
- **Kind:** practice
- **Use:** check, text
- **Sources:** NIELSEN-217 (page 165-166)
- **Asked of the source:** what file size takes ten seconds on today's usual connections, and that stating size, format and playing time beside a download or media link is still advised (Nielsen Norman Group).
- **Current source:** confirmed by https://www.nngroup.com/articles/avoid-pdf-for-on-screen-reading/ (read 2026-11-21)
- **Current source:** confirmed by https://www.nngroup.com/articles/instructional-video-guidelines/ (read 2026-11-21)
- **Read:** 2026-11-21, page, Opus agent, each part checked by Claude; candidate speed E13

### speed-009 · Give every image its width and height
- **Statement:** State every image's width and height (or reserve its space with CSS aspect-ratio) so the browser reserves its space in the layout while it loads and need not rebuild the page as each image arrives, which makes the page display faster and keeps the layout from shifting. Modern browsers turn the two attributes into an aspect ratio, so this holds for images that scale with the layout and for responsive images (srcset, picture) of one aspect ratio too (web.dev). Kirsanov (1999) required the sizes for every image in a layout built of tables, which the browser cannot draw until it knows every cell's size, and advised leaving them out in his plain "academic" style; Robbins found the attributes of less use in modern design and only for images of one fixed size, a view web.dev no longer holds.
- **Kind:** practice
- **Use:** check
- **Sources:** KIRSANOV-393 (page 114), ROBBINS-080 (page 186-187, the notes cite 186)
- **Also in (not read):** NIELSEN-062
- **Asked of the source:** that current browsers reserve an image's space from its width and height, also for images that scale with the layout, and that this prevents layout shift (web.dev, MDN).
- **Current source:** confirmed by https://web.dev/articles/optimize-cls (read 2026-11-21)
- **Read:** 2026-11-21, page, Opus agent, each part checked by Claude; candidate speed E16

### speed-010 · A photo viewer that fetches the large picture on demand and keeps it
- **Statement:** Duckett's example photo viewer fetches the large picture only when its thumbnail is clicked and shows it only once it has fully loaded, and only if it is still the most recently requested one: when a person clicks two thumbnails quickly, the slower first picture can finish loading last and replace the one they actually chose. While a picture loads an animated loading sign shows, and it is removed when the picture has arrived. The viewer keeps every picture element it has made in a cache, since a picture opened again is best shown from the same element rather than made anew.
- **Kind:** practice
- **Use:** look, check
- **Sources:** DUCKETT-016 (page 514), DUCKETT-018 (page 515), DUCKETT-019 (page 515)
- **Needs source:** that loading large images on demand, a visible loading state and reuse of images already fetched are current practice (web.dev, MDN), confirmed below; open: that the loading race between two quick clicks still occurs with current browsers and gallery code
- **Current source:** confirmed by https://developer.mozilla.org/en-US/docs/Web/API/HTMLImageElement/decode (read 2026-11-21)
- **Current source:** none found (searched 2026-11-20)
- **Read:** 2026-11-21, page, Opus agent, each part checked by Claude; candidate speed E18, joined by images E101

### speed-011 · Heavier pages lose more visitors
- **Statement:** Page size directly loses visitors. On one small-business site 7 to 10% of users abandoned pages of more than 32 to 33 KB and 25 to 30% abandoned pages near 40 KB; cutting only the file size of the graphics on the largest pages brought abandonment down to 7 to 10%, and traffic rose about 25%.
- **Kind:** practice
- **Use:** check
- **Sources:** NIELSEN-058 (page 65-66, the notes cite 66)
- **Asked of the source:** a current measurement of how many visitors abandon a page as its weight or loading time grows; these page sizes were measured on modems.
- **Current source:** confirmed by https://developer.chrome.com/docs/lighthouse/performance/total-byte-weight (read 2026-11-21)
- **Current source:** confirmed by https://web.dev/learn/performance/why-speed-matters (read 2026-11-21)
- **Read:** 2026-11-21, page, Opus agent, each part checked by Claude; candidate speed E19

### speed-012 · Budget a page's weight from the response time aimed at and the connection
- **Statement:** Budget a page's weight from the response time aimed at and the connection; a page's size is the sum of its HTML file and every embedded object, such as each image. The book's figures (1999, assuming 0.5 s of latency) were 2 KB by modem for a 1-second response and 34 KB for 10 seconds, 8 KB and 150 KB by ISDN, 100 KB and 2 MB by T1, and even on a fast intranet under 100 KB a page, since users rarely get the full bandwidth. Budgets set the same way today are far larger: about 170 KB of critical-path resources (compressed) for a 5-second load, and 1,600 KiB in total for 10 seconds, on a baseline phone over 3G (web.dev, Lighthouse).
- **Kind:** practice
- **Use:** check
- **Sources:** NIELSEN-057 (page 65), NIELSEN-059 (page 65)
- **Asked of the source:** a current page-weight or loading-time budget for today's mobile and fixed connections (web.dev); these figures are for the connections of 1999.
- **Current source:** confirmed by https://web.dev/articles/performance-budgets-101 (read 2026-11-21)
- **Current source:** overturned by https://developer.chrome.com/docs/lighthouse/performance/total-byte-weight (read 2026-11-21)
- **Read:** 2026-11-21, page, Opus agent, each part checked by Claude; candidate speed E20

### speed-013 · Keep a large background image light
- **Statement:** Keep a large background image as light as it can be. The book (1999) set 20 to 30 kB for a full-page background image, even one hundreds or thousands of pixels high, reached by heavy lossy compression of soft dark images or by cutting flat images to 2 to 4 colours, and advised a middle ground between room for content of any length and download weight. Current guidance gives no kilobyte figure but asks for the right size, a modern format and compression for the largest image on screen, and finds a large image drawn as a CSS background late to load, since the browser discovers it only after the style sheet (web.dev).
- **Kind:** practice
- **Use:** check
- **Sources:** KIRSANOV-434 (page 131), CEDERHOLM-039 (page 142)
- **Asked of the source:** a current weight budget for a large background or hero image (web.dev); the 20 to 30 kB is a budget of 1999.
- **Current source:** confirmed by https://web.dev/articles/optimize-lcp (read 2026-11-21)
- **Read:** 2026-11-21, passage, Opus agent, each part checked by Claude; candidate speed E22

### speed-014 · An advert's file size decides how many people see it
- **Statement:** The heavier an advert's graphic, the more readers leave before it appears and are lost to the advertiser for good, so file size is one of the main factors in how often a banner is clicked. Budgets given for a 468x60 banner: 15 kB on Western sites, 10 kB on ad-funded content sites, 7 to 8 kB for the slower Russian connections of the time.
- **Kind:** practice
- **Use:** check
- **Sources:** KIRSANOV-479 (page 144), KIRSANOV-480 (page 144)
- **Needs source:** a current weight limit for a banner or other advert; the budgets are for the connection speeds of 1999.
- **Current source:** none found (searched 2026-11-21)
- **Read:** 2026-11-21, passage, Opus agent, each part checked by Claude; candidate speed E23

### speed-015 · Design for the equipment and connection most people have, not the best
- **Statement:** A site must serve the mass of users, not the 10% with the best equipment: most people use cheap equipment two to three years behind the leaders and save on connection speed, and a site aimed only at the well-equipped rarely succeeds. Display, connection and standards vary between users, so aim at the lowest common denominator of computers, browsers and connections, not at the average.
- **Kind:** practice
- **Use:** look, check
- **Sources:** NIELSEN-589 (page 454), KIRSANOV-279 (page 85)
- **Also in (not read):** NIELSEN-590
- **Asked of the source:** what devices and connection speeds the slower part of today's audience uses (web.dev), to say what the lowest common denominator now is.
- **Current source:** confirmed by https://web.dev/articles/vitals (read 2026-11-21)
- **Conflict:** web.dev sets the targets at the 75th percentile of page loads, on baseline phones over 3G, which leaves the slowest quarter of page loads out of the target, narrower than the lowest common denominator (https://web.dev/articles/performance-budgets-101, read 2026-11-21)
- **Read:** 2026-11-21, page, Opus agent, each part checked by Claude; candidate speed E24

### speed-016 · A composition of small images and real text, not one baked image
- **Statement:** Build a complex composition from several smaller images mixed with real text and links rather than one large baked image: it is better for access to the information and for file size (Kirsanov, 1999), and under HTTP/2 several small files may indeed be lighter than one large one (MDN). His second advice, a navigation bar cut into one image file per button, is overturned: WCAG 2.2 (1.4.5) asks for real text instead of images of text wherever the technology can give the look, logotypes excepted.
- **Kind:** practice
- **Use:** check
- **Sources:** KIRSANOV-392 (page 114), KIRSANOV-354 (page 103)
- **Asked of the source:** whether slicing a picture or a navigation bar into several image files helps or hurts loading today; image-sliced navigation is a technique of 1999.
- **Current source:** overturned by https://www.w3.org/WAI/WCAG22/Understanding/images-of-text.html (read 2026-11-21)
- **Current source:** confirmed by https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Images/Implementing_image_sprites (read 2026-11-21)
- **Conflict:** CEDERHOLM-020 (in speed-037) warns that navigation drawn as images makes the page heavy and slow
- **Read:** 2026-11-21, page, Opus agent, each part checked by Claude; candidate speed E30

### speed-017 · Draw rounded corners, gradients and shadows in CSS, not as images
- **Statement:** Before making an image, ask whether CSS alone can produce the effect: rounded corners, borders, gradients, shadows and simple shapes drawn in CSS save the file and a request, often at a fraction of the bytes, stay sharp at every zoom level, have no width or height limit, and keep all their colours in the style sheet, so they can be maintained and the look changed later without an image editor or redrawing anything; all major browsers have drawn them since 2015 (web.dev, MDN). On a client site the author built in 2006 (the UNC Highway Safety Research Center), replacing nine interface images with CSS effects cut requests to 22 to 24 and loading time by a further 13 to 25 percent while the page looked almost the same in modern browsers; users of an old browser that could not show the effects (IE 6) gained the most, since their pages loaded much faster. Sites with dozens of interface images stand to gain more.
- **Kind:** practice
- **Use:** look, check
- **Sources:** GILLENWATER-018 (page 41-42, the notes cite 42), GILLENWATER-019 (page 43), ROBBINS-375 (page 778), BEAIRD-148 (page 115), CEDERHOLM-040 (page 147)
- **Asked of the source:** that CSS corners, gradients and shadows are supported in all current browsers (MDN) and still load faster than the same effects as images (web.dev).
- **Current source:** confirmed by https://web.dev/articles/choose-the-right-image-format (read 2026-11-21)
- **Current source:** confirmed by https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-radius (read 2026-11-21)
- **Current source:** confirmed by https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Images/Using_gradients (read 2026-11-20)
- **Conflict:** GILLENWATER-011, ROBBINS-205 (in speed-018) warn that generated effects and text shadows can make the browser sluggish.
- **Read:** 2026-11-21, page, Opus agent, each part checked by Claude; candidate speed E32, joined by colour E85

### speed-018 · Generated effects cost rendering time: use them sparingly and test them
- **Statement:** Rich effects such as generated gradients save image downloads but can make the browser work hard and feel sluggish, and text shadows can slow scrolling and mouse interaction, a problem on mobile devices with little processing power. Do not overuse complex effects, and test the ones used.
- **Kind:** practice
- **Use:** check
- **Sources:** GILLENWATER-011 (page 37), ROBBINS-205 (page 374)
- **Asked of the source:** which CSS effects still cost noticeable rendering time on current phones (web.dev, MDN).
- **Current source:** confirmed by https://web.dev/articles/simplify-paint-complexity-and-reduce-paint-areas (read 2026-11-21)
- **Conflict:** GILLENWATER-018, ROBBINS-375, BEAIRD-148 (in speed-017) advise CSS effects in place of images to make the page load faster.
- **Read:** 2026-11-21, passage, Opus agent, each part checked by Claude; candidate speed E33

### speed-019 · Spare the server needless round trips
- **Statement:** In a page's links, write directory addresses in full with the trailing slash: without it the server usually redirects to the full form, which adds a small but noticeable delay (in print the short form is fine). Check that the server reuses one connection for all of a page's objects, which usually halves loading time; otherwise each extra small icon costs a new connection.
- **Kind:** practice
- **Use:** check
- **Sources:** NIELSEN-401 (page 298), NIELSEN-063 (page 68-69, the notes cite 69), NIELSEN-060 (page 66)
- **Asked of the source:** that a directory link without the trailing slash still causes a redirect, and how current servers and browsers reuse connections (MDN, web.dev).
- **Current source:** confirmed by https://developer.chrome.com/docs/lighthouse/performance/redirects (read 2026-11-21)
- **Current source:** confirmed by https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Connection_management_in_HTTP_1.x (read 2026-11-21)
- **Read:** 2026-11-21, page, Opus agent, each part checked by Claude; candidate speed E38

### speed-020 · Send a stand-in script only to browsers that lack the feature
- **Statement:** A script that adds a missing feature to old browsers, loaded for everyone, costs every visitor a request and extra kilobytes. Load the stand-in only where the feature is missing, so capable browsers do not download and run code they do not need: Lawson loads an alternative validation library only after detecting that the browser lacks the feature; Gillenwater sent a media-query script only to Internet Explorer 6 to 8 through conditional comments, accepting that a few other browsers without media queries would miss out rather than make all browsers download it.
- **Kind:** practice
- **Use:** check
- **Sources:** LAWSON-046 (page 99), GILLENWATER-094 (page 260)
- **Also in (not read):** DUCKETT-058
- **Asked of the source:** that detecting a feature and loading its stand-in only where needed is still the advised way (MDN, web.dev).
- **Current source:** confirmed by https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Testing/Feature_detection (read 2026-11-21)
- **Current source:** confirmed by https://web.dev/articles/serve-modern-code-to-modern-browsers (read 2026-11-21)
- **Read:** 2026-11-21, page, Opus agent, each part checked by Claude; candidate speed E69

### speed-021 · Small font files that keep the letters translations need
- **Statement:** Make font files as small as reasonably possible, but keep enough characters that a translated version of the site is still readable.
- **Kind:** practice
- **Use:** check
- **Sources:** GOLDSTEIN-038 (page 252)
- **Asked of the source:** current practice for cutting a font file down to the characters a site uses.
- **Current source:** confirmed by https://web.dev/articles/font-best-practices (read 2026-11-21)
- **Read:** 2026-11-21, passage, Opus agent, each part checked by Claude; candidate type E219

### speed-022 · The jump when the web font arrives
- **Statement:** Loading web fonts only after the page has rendered makes the page appear faster overall, at the cost of a more visible switch from the stand-in font to the web font: the text shifts as the font swaps, which disorients the visitor. One book lists, without applying it, a script that hides the content for a couple of seconds while the fonts download. Today the CSS font-display descriptor sets how long text stays invisible and whether a late font swaps in (MDN); font-display: swap can shift the layout when the font arrives, so web.dev advises delivering the font early enough that the swap causes no shift, or font-display: optional where speed comes first, which avoids the shift by using the font only if it is there at first layout but may leave the web font unused; hiding the text alone does not stop the shift, since invisible text is still laid out in the fallback font (web.dev).
- **Kind:** practice
- **Use:** look, check
- **Sources:** GILLENWATER-062 (page 164), GOLDSTEIN-042 (page 254)
- **Asked of the source:** how current browsers and CSS control the display of text while a font loads.
- **Current source:** confirmed by https://web.dev/articles/optimize-cls (read 2026-11-21)
- **Current source:** confirmed by https://web.dev/articles/font-best-practices (read 2026-11-20)
- **Conflict:** GILLENWATER-058, GOLDSTEIN-041 (type, "Request the font as early as possible") advise requesting the font as early as possible, ahead of scripts and other files.
- **Read:** 2026-11-21, passage, Opus agent, each part checked by Claude; candidate type E220, joined by speed E66

### speed-023 · Frames of an animated GIF can take a smaller palette than a still
- **Statement:** The frames of an animated GIF can make do with a much smaller palette than a still image, often without dithering or anti-aliasing, since fast-changing pictures hide the defects and successive frames compensate for each other; the longer a frame stays on screen, the higher its quality must be.
- **Kind:** practice
- **Use:** check
- **Sources:** KIRSANOV-420 (page 125)
- **Needs source:** how current animation and video formats trade frame quality against file size.
- **Current source:** none found (searched 2026-11-21)
- **Conflict:** web.dev advises serving animation as video (MP4, WebM), far smaller than an animated GIF (https://web.dev/articles/replace-gifs-with-videos, read 2026-11-21)
- **Read:** 2026-11-21, page, Opus agent, each part checked by Claude; candidate images E112

### speed-024 · Export every image through a tool built to compress it
- **Statement:** Export web images with a tool built for strong compression rather than a plain "save as": depending on the picture and format, a plain save can give a file up to ten times larger than an export of the same image.
- **Kind:** practice
- **Use:** check
- **Sources:** ROBBINS-384 (page 791)
- **Also in (not read):** ROBBINS-391
- **Asked of the source:** current tools and targets for image compression (web.dev).
- **Current source:** confirmed by https://web.dev/learn/performance/image-performance (read 2026-11-21)
- **Read:** 2026-11-21, passage, Opus agent, each part checked by Claude; candidate images E139

### speed-025 · Load only the framework parts the page uses
- **Statement:** A responsive framework gives a ready grid and common parts so each site need not reinvent them; include only the components actually used, to keep code and file size small. Boulton found the HTML of one grid framework (Blueprint) bloated and advises keeping it trim before such a framework goes on a live site.
- **Kind:** practice
- **Use:** check
- **Sources:** BEAIRD-074 (page 58-59), BOULTON-154 (page 114)
- **Asked of the source:** that the frameworks in use today can be cut down to the parts a page uses, and what the unused parts cost in page weight (web.dev).
- **Current source:** confirmed by https://web.dev/articles/remove-unused-code (read 2026-11-21)
- **Current source:** confirmed by https://developer.chrome.com/docs/lighthouse/performance/unused-css-rules (read 2026-11-21)
- **Read:** 2026-11-21, page, Opus agent, each part checked by Claude; candidate process E84

### speed-026 · The longer people wait, the less they do and the sooner they leave
- **Statement:** Delay costs use, even delay under half a second. When Bing and Google deliberately delayed their server responses, people made fewer searches, clicked fewer results and were more likely to leave the longer they waited; Google found that delaying the results page by 100 to 400 ms cut the number of searches by 0.2 to 0.6%, and Amazon that page loads 100 ms faster raised revenue by 1%.
- **Kind:** rule
- **Use:** look, check
- **Sources:** GILLENWATER-012 (page 37), ROBBINS-022 (page 71)
- **Also in (not read):** KRUG-140, KIRSANOV-282
- **Study (as the book reports it):** GILLENWATER-012: Bing and Google server-delay experiments, reported about 2009 to 2010, numbers of users not given; ROBBINS-022: Google "Speed Matters", 2009, searches per user, and Amazon figures from Greg Linden's "Make Data Matter" presentation, Stanford, 2006.
- **Needs source:** a source of the brief's kinds for the Bing experiment and for Amazon's 100 ms and 1% figures; only reposted slides and retellings were seen
- **Current source:** confirmed by https://research.google/blog/speed-matters/ (read 2026-11-21)
- **Read:** 2026-11-21, passage, Opus agent; Claude read the line, not each part (AW-T19-Q34); candidate speed E01

### speed-027 · The most visited sites are the faster ones
- **Statement:** In a 1999 timing, the home pages of the most visited sites loaded in 8 seconds on average, against 19 seconds for the comparison group (given once as the ten biggest US companies, once as low-traffic sites); the high-traffic sites also had two thirds as many violations of the author's usability guidelines. The author reads speed and usability as a cause of the traffic, not the reverse.
- **Kind:** rule
- **Use:** look
- **Sources:** NIELSEN-052 (page 62), NIELSEN-631 (page 487)
- **Study (as the book reports it):** NIELSEN-052: the author's own timing of 20 leading home pages, 1999; NIELSEN-631: the author's 1999 count of guideline violations and home-page load times on high-traffic sites against a control group, number of sites not given.
- **Needs source:** a current measurement that relates a site's loading time to its traffic; the 8 and 19 seconds are load times of 1999.
- **Current source:** none found (searched 2026-11-21)
- **Read:** 2026-11-21, passage, Opus agent; Claude read the line, not each part (AW-T19-Q34); candidate speed E03

### speed-028 · A faster page can rank higher in search
- **Statement:** Google has used page speed as a ranking factor since March 2010, so a faster page can rank a little higher than slower competitors.
- **Kind:** practice
- **Use:** check
- **Sources:** GILLENWATER-013 (page 37)
- **Asked of the source:** that Google still counts page speed in its search ranking, and how it measures it today.
- **Current source:** confirmed by https://developers.google.com/search/docs/appearance/page-experience (read 2026-11-21)
- **Read:** 2026-11-21, passage, Opus agent; Claude read the line, not each part (AW-T19-Q34); candidate speed E04

### speed-029 · Moving from page to page should take under one second
- **Statement:** People move freely along links and work more productively when going from one page or screen to the next takes less than one second. Slower than that they feel they are waiting, use fewer features and view fewer pages, so slow response limits how deep and rich a site can be.
- **Kind:** rule
- **Use:** check
- **Sources:** NIELSEN-042 (page 54), NIELSEN-213 (page 163), NIELSEN-598 (page 466)
- **Study (as the book reports it):** NIELSEN-042: hypertext system studies, not named, and IBM studies of mainframe users, 1970s to 1980s.
- **Current source:** confirmed by https://www.nngroup.com/articles/website-response-times/ (read 2026-11-21)
- **Read:** 2026-11-21, passage, Opus agent; Claude read the line, not each part (AW-T19-Q34); candidate speed E06

### speed-030 · Keep response times predictable as well as short
- **Statement:** Satisfaction depends on expectations: an action that is sometimes fast and sometimes slow confuses users, while a delay they expect is borne calmly. Anything that steadies the response time improves usability.
- **Kind:** practice
- **Use:** check
- **Sources:** NIELSEN-047 (page 60)
- **Read:** 2026-11-21, page, Opus agent; Claude read the line, not each part (AW-T19-Q34); candidate speed E09

### speed-031 · Each video gets preview frames, a description, its running time and size; frames make the wait feel shorter
- **Statement:** People do not download things just because they exist: every multimedia object needs a preview (one or two frames of a video) and a short description of its content, and each video states its running time and its file size, so users can judge it before committing. Showing frames from each video lets users judge whether it interests them, and makes the wait feel shorter: with titles only, nearly all of the 12 to 13 year olds in an experiment rated the download speed poor; with preview frames they rated it satisfactory, at unchanged actual speed.
- **Kind:** rule
- **Use:** look, check, text
- **Sources:** NIELSEN-214 (page 164), NIELSEN-219 (page 166), NIELSEN-215 (page 164)
- **Study (as the book reports it):** NIELSEN-214: Chris Johnson, University of Glasgow, experiment with children aged 12 to 13, group size not given.
- **Current source:** confirmed by https://www.dcs.gla.ac.uk/~johnson/papers/video.html (read 2026-11-21)
- **Read:** 2026-11-21, page, Opus agent; Claude read the line, not each part (AW-T19-Q34); candidate speed E11, joined by images E113

### speed-032 · Make the top of the page usable before the rest has loaded
- **Statement:** The top of the page should make sense with no images yet: more text and fewer graphics, alternative text for every image that shows in its place while it loads, and a topmost part that renders fast. A home page defined almost entirely in one short HTML file appears nearly at once and looks good whether or not its graphics have loaded.
- **Kind:** practice
- **Use:** look, check
- **Sources:** NIELSEN-061 (page 67-68), NIELSEN-065 (page 69)
- **Also in (not read):** KIRSANOV-034
- **Asked of the source:** that current browsers show an image's alternative text in its place while the image loads (MDN)
- **Current source:** confirmed by https://html.spec.whatwg.org/multipage/rendering.html (read 2026-11-21)
- **Read:** 2026-11-21, page, Opus agent; Claude read the line, not each part (AW-T19-Q34); candidate speed E14

### speed-033 · Keep graphics few
- **Statement:** Keep graphics to a minimum because they slow loading. Designers tend to give graphics most of their attention at the expense of the text and of the structure that ties text and pictures together; a page can look fully professional with very little graphics or none. Today images are still often the heaviest resource on a page, and the current advice is to optimise them (format, compression, the right size) rather than only to keep their number down (web.dev).
- **Kind:** practice
- **Use:** look, check
- **Sources:** NIELSEN-220 (page 166), KIRSANOV-401 (page 118)
- **Asked of the source:** how much images weigh in the loading time of a page today.
- **Current source:** confirmed by https://web.dev/learn/performance/image-performance (read 2026-11-21)
- **Conflict:** BEAIRD-298 and BEAIRD-063 (in images-041) present a photograph filling the whole window.
- **Read:** 2026-11-21, page, Opus agent; Claude read the line, not each part (AW-T19-Q34); candidate images E34

### speed-034 · A public site assumes no particular browser, software or connection
- **Statement:** A public site must not demand a particular browser, since its visitors use any computer, connection speed and browser version. A client or partner area cannot assume particular software, a fast connection or users who will learn its interface either: clients use mixed equipment, reach it over the internet and deal with many other companies' portals. Only an internal site with standardised equipment may assume one browser, set fonts, a minimum screen and office software.
- **Kind:** practice
- **Use:** look, check
- **Sources:** NIELSEN-423 (page 317), NIELSEN-427 (page 319-320)
- **Asked of the source:** which range of browsers, screens and connections a public site should support today; the finding assumes the browsers and screens of about 2000.
- **Current source:** confirmed by https://www.gov.uk/service-manual/technology/designing-for-different-browsers-and-devices (read 2026-11-21)
- **Read:** 2026-11-21, page, Opus agent; Claude read the line, not each part (AW-T19-Q34); candidate speed E25

### speed-035 · Do not make content wait on software the visitor must fetch first
- **Statement:** Do not make content wait on software the visitor must fetch first. In the book's time a required download of a player or plug-in interrupted browsing and made people leave, automatic installation did not solve it (a crash while installing could lose the visitor for good), and the book advised targeting player software at least a year old and previews that work in a standard browser two versions behind the latest. Today media plays in the browser itself and no major browser supports plug-ins any more (MDN).
- **Kind:** practice
- **Use:** check
- **Sources:** NIELSEN-218 (page 165), NIELSEN-210 (page 162)
- **Also in (not read):** KIRSANOV-053
- **Asked of the source:** how far behind the latest browser version a site should still work today, and that media should play in the browser with no extra software; the findings are about plug-ins of the late 1990s.
- **Current source:** confirmed by https://developer.mozilla.org/en-US/docs/Glossary/Plugin (read 2026-11-21)
- **Read:** 2026-11-21, page, Opus agent; Claude read the line, not each part (AW-T19-Q34); candidate speed E27

### speed-036 · Speed work is two things: smaller files and fewer requests
- **Statement:** All speed work falls into two kinds: make the files smaller and make fewer requests to the server. Ways include optimising images, avoiding needless nesting in the HTML, minifying HTML and CSS, using little JavaScript, loading scripts so they do not block rendering, and not loading unneeded images, scripts or libraries.
- **Kind:** practice
- **Use:** check
- **Sources:** ROBBINS-024 (page 72)
- **Also in (not read):** ROBBINS-374
- **Read:** 2026-11-21, page, Opus agent; Claude read the line, not each part (AW-T19-Q34); candidate speed E28

### speed-037 · Keep the markup lean: no layout tables, spacer images or image navigation
- **Statement:** Layouts built from nested tables and stretched transparent spacer images, and navigation drawn as images swapped by script for hover effects, produce bulky code that makes the page heavy and slow to load, hurts accessibility and makes the site hard to extend and maintain. Lean semantic markup with CSS gives the same look.
- **Kind:** practice
- **Use:** check
- **Sources:** CEDERHOLM-005 (page 15), CEDERHOLM-020 (page 45)
- **Asked of the source:** that layout tables and images of text for navigation are still advised against (WCAG, MDN); the finding argues against the table layouts of the early 2000s.
- **Current source:** confirmed by https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content/HTML_table_basics (read 2026-11-21)
- **Current source:** confirmed by https://www.w3.org/WAI/WCAG22/Understanding/images-of-text.html (read 2026-11-21)
- **Conflict:** KIRSANOV-354 (in speed-016) advises a navigation bar cut into one image file per button.
- **Read:** 2026-11-21, page, Opus agent; Claude read the line, not each part (AW-T19-Q34); candidate speed E31

### speed-038 · Do not spread style rules over extra files
- **Statement:** Each separate style sheet is one more request. Do not move browser-specific rules into a file of their own to keep the main one valid: the extra file costs more speed than the few bytes saved, and rules kept apart are easily forgotten when something changes. Where style sheets are loaded per device condition, keep them to about one per major breakpoint and handle small adjustments inside them.
- **Kind:** practice
- **Use:** check
- **Sources:** GILLENWATER-022 (page 47), ROBBINS-289 (page 595-596)
- **Asked of the source:** whether an extra style sheet request still costs noticeable time on current connections, and how browsers load style sheets whose media condition does not match (web.dev, MDN).
- **Current source:** confirmed by https://developer.chrome.com/docs/lighthouse/performance/unused-css-rules (read 2026-11-21)
- **Current source:** confirmed by https://web.dev/articles/critical-rendering-path/render-blocking-css (read 2026-11-21)
- **Read:** 2026-11-21, page, Opus agent; Claude read the line, not each part (AW-T19-Q34); candidate speed E34

### speed-039 · Use one file for a picture that appears more than once
- **Statement:** When the same image appears several times on a page or a site, point every use at exactly the same address: the browser downloads it once and then takes it from its cache, which saves traffic and shows the image faster.
- **Kind:** practice
- **Use:** check
- **Sources:** ROBBINS-073 (page 184), ROBBINS-424 (page 813-814, the notes cite 814)
- **Also in (not read):** BEAIRD-254
- **Asked of the source:** that current browsers serve a repeated image address from their cache across the pages of one site (MDN).
- **Current source:** confirmed by https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Caching (read 2026-11-21)
- **Read:** 2026-11-21, page, Opus agent; Claude read the line, not each part (AW-T19-Q34); candidate speed E35

### speed-040 · Outside widgets and ad servers add requests and delays the site does not control
- **Statement:** Third-party widgets such as social media embeds, like buttons and ads can each send dozens of requests, and the milliseconds per request add up to real delays. Ads pulled from an outside ad server slow the page when that server is overloaded; larger sites run their own ad system to cut delays and to control every ad and its alternative text.
- **Kind:** practice
- **Use:** look, check
- **Sources:** ROBBINS-025 (page 72), KIRSANOV-456 (page 138)
- **Read:** 2026-11-21, passage, Opus agent; Claude read the line, not each part (AW-T19-Q34); candidate speed E36

### speed-041 · The server's answer time is part of the page's speed
- **Statement:** Users do not care why a server is slow: long waits erode trust and drive them to other sites, so pages built on the fly from a database need a fast server and an expert review of the system's performance. Response time is set by the slowest link in the chain (server, its connection, the internet, the user's connection, the browser's rendering) and the delays add up, so improving one link helps less than expected.
- **Kind:** practice
- **Use:** check
- **Sources:** NIELSEN-049 (page 61), NIELSEN-050 (page 61-62, the notes cite 62)
- **Asked of the source:** how server response time is measured and what target is advised today (web.dev); the finding's example is the connection types of 1999.
- **Current source:** confirmed by https://web.dev/articles/ttfb (read 2026-11-21)
- **Current source:** confirmed by https://www.nngroup.com/articles/website-response-times/ (read 2026-11-21)
- **Read:** 2026-11-21, page, Opus agent; Claude read the line, not each part (AW-T19-Q34); candidate speed E37

### speed-042 · Every web font costs download
- **Statement:** Every exact way of delivering a chosen font to the reader costs more download and some loss of compatibility; weigh the exactness of the type against that load.
- **Kind:** practice
- **Use:** look, check
- **Sources:** KIRSANOV-366 (page 107)
- **Asked of the source:** how much web fonts add to load time on current connections.
- **Current source:** confirmed by https://web.dev/articles/font-best-practices (read 2026-11-21)
- **Read:** 2026-11-21, passage, Opus agent; Claude read the line, not each part (AW-T19-Q34); candidate type E218

### speed-043 · Read the page's requests in the browser's network panel
- **Statement:** Check a page's requests with the browser's network panel: reload the page and read the waterfall chart, which lists each request, its time in milliseconds and the totals of requests and of data transferred. Speed test tools give the same and suggest fixes.
- **Kind:** practice
- **Use:** check
- **Sources:** ROBBINS-026 (page 72-73)
- **Asked of the source:** what the network panel of current browsers reports and which speed test tools are current (web.dev, the browsers' developer tools documentation); the book names WebPageTest and PageSpeed Insights as of about 2018.
- **Current source:** confirmed by https://developer.chrome.com/docs/devtools/network/reference (read 2026-11-21)
- **Current source:** confirmed by https://developers.google.com/speed/docs/insights/v5/about (read 2026-11-21)
- **Read:** 2026-11-21, page, Opus agent; Claude read the line, not each part (AW-T19-Q34); candidate testing E120
