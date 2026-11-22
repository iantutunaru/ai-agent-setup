# Web design rulebook: taste and unconfirmed

An author's preference where another designer could fairly differ, or a claim that did not hold. Never stated as proven. Built by a script from the owner's reading notes, which are not published.

## From the reading

Decided by Claude on the page.

- GOLDSTEIN-063, LAWSON-023, LAWSON-045: doubling a native element with its matching ARIA role while support is young; overturned by https://www.w3.org/TR/html-aria/ (read 2026-11-21) (accessibility E23, read 2026-11-21)
- GILLENWATER-026: a solid fallback colour for a semitransparent one; overturned by https://developer.mozilla.org/en-US/docs/Web/CSS/color_value/rgb (read 2026-11-20) (colour E81, read 2026-11-20)
- NIELSEN-383: keeping page summaries to 150 to 200 characters because search engines show only that much; overturned by https://developers.google.com/search/docs/appearance/snippet (read 2026-11-20) (content E32, read 2026-11-20)
- GOLDSTEIN-026: date and time asked in two fields because the combined field was expected to lose support; overturned by https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/datetime-local (read 2026-11-20) (forms E53, read 2026-11-20)
- GOLDSTEIN-025: a placeholder with an example date for browsers that show no calendar; overturned by https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/date (read 2026-11-20) (forms E54, read 2026-11-20)
- NIELSEN-245, NIELSEN-248: offering a separate better download because streamed video was poor; overturned by https://web.dev/articles/media-streaming-basics (read 2026-11-20) (images E116, read 2026-11-20)
- GOLDSTEIN-060: a default layout or a script for browsers that cannot read media queries (old Internet Explorer); overturned by https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media (read 2026-11-20) (phone E18, read 2026-11-20)
- ROBBINS-227: avoiding percentage margins and padding on flex items because the specification advised against them; overturned by https://www.w3.org/TR/css-flexbox-1/ (read 2026-11-20) (spacing E26, read 2026-11-20)
- KIRSANOV-308: a splash page before the site, forwarding after a delay or offering the language; overturned by https://www.nngroup.com/articles/113-design-guidelines-homepage-usability/ (read 2026-11-20) (navigation E45, read 2026-11-20)
- THALER-040, THALER-231: a loss frame persuading more than a gain frame; overturned by https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TITLE%3A%22messages%20for%20encouraging%20disease%20prevention%20behaviors%22&resultType=core&format=xml (read 2026-11-21) (content E141, read 2026-11-21)
- GILLENWATER-092: capping the maximum zoom at 1.0 to fix the iPhone's landscape scaling; overturned by https://web.dev/articles/responsive-web-design-basics (read 2026-11-20) (phone E22, read 2026-11-20)
- GOLDSTEIN-059, ROBBINS-315: a heading sized in viewport width alone (7 percent); overturned by https://www.w3.org/WAI/WCAG22/Techniques/failures/F94 (read 2026-11-20) (type E91, read 2026-11-20)
- NIELSEN-393: search by a whole question held rarely usable; overturned for AI search by https://www.nngroup.com/articles/ai-information-seeking-keyword-foraging/ (read 2026-11-20) (search-and-filters E13, read 2026-11-20)
- KIRSANOV-281, KIRSANOV-297: a page of about 100 KB with 20 to 30 KB of HTML, budgets set for the connections of 1999; overturned by https://developer.chrome.com/docs/lighthouse/performance/total-byte-weight (read 2026-11-21) (speed E21, read 2026-11-21)
- GILLENWATER-017, GILLENWATER-008, ROBBINS-068: counting a page's requests above its size and combining images into one sprite, workarounds of HTTP/1.x; overturned by https://web.dev/articles/performance-http2 (read 2026-11-21) (speed E29, read 2026-11-21)
- CEDERHOLM-057: a couple of text-size steps as enough headroom; overturned by https://www.w3.org/WAI/WCAG22/Understanding/resize-text.html (read 2026-11-21) (testing E113, read 2026-11-21)
- GILLENWATER-047, ROBBINS-176, BEAIRD-172: serving a web font in EOT, TTF or OTF, SVG and WOFF, with WOFF as the format going forward; overturned by https://web.dev/articles/font-best-practices (read 2026-11-20) (type E215, read 2026-11-20)

## From the merge: type

From the notes, not read on the page; the list read by Claude.

- BEAIRD-189: old-style serifs feel historic and handcrafted, transitional serifs more modern and mechanical.
- BEAIRD-192: a typeface's conventional associations can be gone against on purpose.
- BEAIRD-195: neutral sans serifs such as Arial and Verdana suit body copy; headlines need more character.
- BOULTON-056: neutral sans serifs read as safe and corporate, rounded faces as youthful and playful.
- BRINGHURST-015: the ideal is a creative restraint that lets the letters live.
- BRINGHURST-120: logos push type towards pictures; good text type is plain and made to be used.
- BRINGHURST-178: use punctuation marks more sparingly than typists do.
- BRINGHURST-183: use the best ampersand available in headings, an italic one even in a roman line.
- BRINGHURST-184: borrow a better hyphen (sloped, tapered or shorter) from another face.
- BRINGHURST-187, BRINGHURST-486: prefers an en dash with a word space on each side to the em dash in text.
- BRINGHURST-227: Baskerville, Helvetica, Palatino and Times Roman do not combine with each other.
- BRINGHURST-274: a typeface can echo the architecture around a text.
- BRINGHURST-290, BRINGHURST-291: the proportions of the text face should relate to those of the text block and the page.
- BRINGHURST-352: slightly differing forms of one letter give a page liveliness.
- BRINGHURST-392: in some faces the bold weights matter little; judge a text face by roman, italic, small capitals and old-style figures first.
- BRINGHURST-416: grotesques such as Helvetica and Franklin Gothic are dark, coarse and closed.
- BRINGHURST-425: blackletter can serve for emphasis or contrast within roman type.
- BRINGHURST-457: holds pictogram dingbats in contempt.
- BRINGHURST-469: against faces built to one formula of a uniformly large x-height.
- CABARGA-007: nested rounded boxes in one mark should share their corner radii.
- CABARGA-017: grunge and distressed fonts communicate well when the context suits.
- CABARGA-029: a literal logo with no concept is justified by a strong illustration.
- CABARGA-032: a well-designed abstract logo conveys continuity and stability.
- CABARGA-035: a retro look pushed too far turns into parody, which suits only a playful client.
- CABARGA-037: modest type with a hopeful graphic carries a subtle message.
- CABARGA-040: a letter of a logo can echo a local landmark.
- CABARGA-065: decoration in a logo is welcome when it carries the concept.
- CABARGA-115: typographic rules may be broken, and legibility, fineness and taste are all subjective.
- GILLENWATER-051: where no installed font resembles the web font, fall back to a clean plain one.
- KIRSANOV-088: a heading may be demoted to a side or footer caption.
- KIRSANOV-100: a heading styled as a sketch with faint construction lines.
- KIRSANOV-164: old-style serifs such as Garamond suit an unusually wide range of moods.
- KIRSANOV-165: transitional serifs feel the most transparent and natural.
- KIRSANOV-166: high-contrast modern serifs now look dry, mannered and old-fashioned.
- KIRSANOV-167: Clarendon-type slab serifs look strict and solid yet fairly modern.
- KIRSANOV-169: Helvetica is the neutral all-purpose sans serif.
- KIRSANOV-184: monospaced faces can look stylish against textures and distortion effects.
- KIRSANOV-196: Title Case makes a heading sound newspapery, salesy and dated.
- KIRSANOV-199: all lowercase keeps a certain detachment; avoid it on strict business pages.
- KIRSANOV-204: negative letter spacing with overlapping letters in headings, best in bold sans serifs.
- KIRSANOV-216: bent baselines and "dancing letters" give a playful character.
- KIRSANOV-367: the few common screen fonts have become tired to the eye.
- KIRSANOV-449: in logos all lowercase looks more modern, all capitals a good middle way.
- LUPTON-025: sets words entirely in small capitals, not mixed with full capitals.
- LUPTON-205: quotations printed in a second colour inside the running text, not set apart as blocks.
- ROBBINS-192: treats ligatures, true small capitals and special numerals as optional extras.
- ROBBINS-203: a text shadow should be blurred, not sharp.

## From the merge: layout

From the notes, not read on the page; the list read by Claude.

- BEAIRD-289: prefers a portfolio's facts set as bare label and value pairs under a dark title block, with no boxes or imagery.
- BOULTON-087: accepts a full-width text column, long lines and all, for pages printed on a desktop printer, to save paper and toner.
- BRINGHURST-141: prefers an opening page balanced mainly by empty space, with only a line or two at the top and bottom.
- BRINGHURST-142: against dropping big ready-made letters into the middle of an empty page.
- BRINGHURST-145: holds that neither empty space nor a full page by itself makes a page rich or poor.
- BRINGHURST-175: wants room at the start and end of a publication so the text can breathe.
- BRINGHURST-285: wants the whole surface designed with care, since a machine-made look invites only machines to read.
- BRINGHURST-292: prefers structural harmony implied, not imposed.
- BRINGHURST-297: holds the ISO page the least musical paper shape, needing a text block of another proportion.
- BRINGHURST-298: asks whether hexagon and pentagon proportions feel livelier than octagon ones, and leaves it open.
- BRINGHURST-310: reads a long line in a wide column as writing used as power, and picks proportions by their associations.
- BRINGHURST-313: reads very long narrow columns as disposable prose and prefers a somewhat wider text block.
- DUCKETT-024: the book's own slider moves on every four seconds and returns to the first slide after the last.
- GENTRY-129: one centred product photo with the name in huge faint letters behind it and a single dark button.
- GILLENWATER-079: in boxes stacked for a narrow layout, moves each illustration from above the text to its left.
- GOLDSTEIN-053: gives the items of a flexible row a common starting width, finding uneven widths ugly.
- KIRSANOV-085: keeps random scattering for elements active on their own and finds scattered background patterns irritating.
- KIRSANOV-086: finds checkerboards, circles and evenly spaced tables old-fashioned and over-ordered.
- KIRSANOV-109: likes a thick border as the main carrier of a shape, paired with a heavy sans-serif.
- KIRSANOV-431: finds vertical background stripes right for short pages and too vertical for long ones.
- KIRSANOV-564: a splash page of one treated photo, two hairlines and a name.
- KIRSANOV-574: a tightly packed, blurred wordmark against an otherwise empty black page.
- LUPTON-003: finds a centred layout static and conventional however exotic the typefaces.
- LUPTON-083: likes different alignments combined in one layout for surprise.
- LUPTON-114: likes borders and frames to draw attention and give a publication an identity.
- LUPTON-132: holds the golden section no more valid than standard paper sizes, halves and squares.
- NIELSEN-610: against a home page that imitates a complex desktop interface.

## From the merge: spacing

From the notes, not read on the page; the list read by Claude.

- BEAIRD-182, BEAIRD-293: prefers a little letter spacing on text for an open, airy feel (the pictured value, .01em, may be a misprint); E54 advises against letterspacing lowercase.
- KRUG-039, KRUG-203: prefers a little extra space between the items of a bulleted list, about half a line, with the wrapped lines of one item at normal line spacing.
- KIRSANOV-083, KIRSANOV-549: prefers items in a two-dimensional grid set clearly closer in one direction than the other, the larger gap across the items' longer side; equal gaps both ways look dull.
- KIRSANOV-091: on artistic pages likes zero and negative gaps (elements touching or overlapping) set against large spaces around the group.

## From the merge: colour

From the notes, not read on the page; the list read by Claude.

- BEAIRD-095: white used unexpectedly (white text on a dark ground, a white block on an off-white page) makes a strong statement.
- GENTRY-040: prefers a very dark grey to pure black and avoids pure white, as too intense; E46 says otherwise.
- GENTRY-043: very basic illustrations with one strong colour are enough to set a distinct mood.
- GENTRY-139: the example screen sets its mood with a black line drawing, scattered lettering and empty space on off-white, with no strong colour.
- GENTRY-131: duotone photos in two colours (deep purple and coral red) that swap between photo and field from block to block.
- GENTRY-158: a page can lean on a complementary pair when each colour has its own full-width band, kept apart by a white band; E18 advises caution with large areas.
- KIRSANOV-108: no thin outline around a rectangle already set off by its fill colour, nor around letters.
- KIRSANOV-122: pure, fully saturated hues are worn out; keep them for minor trim and look for less obvious shades.
- KIRSANOV-123: a colour that is hard to name is a sign of a fresh choice.
- KIRSANOV-124: yellow does not survive darkening or desaturation, so it only works near full brightness and saturation.
- KIRSANOV-135: never pair hues close together on the wheel, and opposite hues rarely harmonise either; E17 says otherwise.
- KIRSANOV-136: hues about a quarter of the wheel apart contrast best, and two warm or two cool colours pair more readily than a warm with a cool.
- KIRSANOV-147: an example scheme of a light, fairly saturated background (#CCCC99), softened black text (#333333) and softened blue links (#0033FF).
- KIRSANOV-451: warm colours resist the closed nature of a logo; the traditional choice is blue and its neighbours.
- KIRSANOV-499: boosting saturation to make an element stand out gives a gaudy image that loses its photographic texture.
- KIRSANOV-508: green as colour in its purest form with the fewest side associations.

## From the merge: images

From the notes, not read on the page; the list read by Claude.

- BEAIRD-064: prefers flat design, with depth shown by sharp shadows or a darker colour instead of gradients (a 2014 trend).
- BEAIRD-154: likes a worn, weathered or grunge look in sepia for nostalgia, or as an agency's signature.
- BEAIRD-156: likes a faint noise or grain over flat colours and gradients.
- BEAIRD-157: likes a handcrafted scrapbook look for a casual, playful personality.
- GENTRY-033: few photos and much empty space for a calm, pricier mood; many full-bleed photos for a loud one.
- GENTRY-044: a collage of mixed image styles for artsy, experimental or personal sites.
- GENTRY-167: product shots floating over a full-bleed close-up of the product in use.
- GILLENWATER-086: prefers smaller icons on phones so icons and text balance.
- KIRSANOV-114: prefers curves whose curvature varies along their length to near-circular arcs.
- KIRSANOV-115: wants shapeless elements attached to objects and bounded by straight edges, never combined with arcs.
- KIRSANOV-152, KIRSANOV-550: holds fine horizontal stripes to be the one geometric texture that works well.
- KIRSANOV-158: material texture only restrained: in places, as a hint, never in repeating tiles.
- KIRSANOV-160: dislikes piled-up bevels, highlights, shadows and glows.
- KIRSANOV-427: disorder has force only when the designer put it there.
- KIRSANOV-445: an amorphous logo shape must show the artist's hand and stay one flat colour.
- KIRSANOV-494: holds that amateur filter use shows which filters were applied.
- KIRSANOV-503: finds distortion filters only comic, and filters that flatten a photo worth using.
- KIRSANOV-547: an idea too literal for a logo can make a striking photographic home-page visual.
- LUPTON-016: likes large letters cropped at the frame's edge for a sense of scale.
- LUPTON-053: holds that detailed three-dimensional icons serve brand identity more than usability.
- NIELSEN-498: wants alternative text to state what the image is for, not describe it; the author notes others prefer descriptions.
- WALTER-065: admires Mint's rich look of glows, gradients and glossy charts against flat competitors.

## From the merge: navigation

From the notes, not read on the page; the list read by Claude.

- BEAIRD-147: prefers menu buttons that look raised (slight gradient, bevelled edges, small text shadow), the active one pressed in.
- GILLENWATER-077: prefers the navigation bar aligned left when a narrow window pushes it onto its own line below the logo.
- KIRSANOV-198: prefers all-lowercase labels only in a set that gives them context, such as a navigation bar.
- KIRSANOV-376: prefers no links on italic, bold or other emphasis, and none in in-text headings unless every heading has one.
- LAWSON-016: treats a strip of headline links to stories as navigation of its own, separate from the site-wide menu.
- NIELSEN-338: finds a permanent list of all top-level categories on inner pages useful, but excessive at 20% of the page.
- NIELSEN-542: prefers no switch to the language already shown, and the language switches set clearly apart from the rest of the page.

## From the merge: search-and-filters

From the notes, not read on the page; the list read by Claude.

- THALER-122: prefers recommendations that now and then show what different people like, not only what similar users like.

## From the merge: content

From the notes, not read on the page; the list read by Claude.

- BRINGHURST-119: no special capitals or house typefaces for company and product names inside running text.
- LAWSON-002: content that needs more than about six levels of nested headings should be reorganised.
- NIELSEN-306: a memorable, unusual site name to stand out, kept to a light touch and not carried into section names.
- NIELSEN-415: holds chat to be almost always the worst way to support communication on a site.
- WALTER-007: personality built from playful copy, bright primary colours, informal sans-serif type and rounded corners.
- WALTER-032: an informal voice with contractions and lower-case form and button labels.

## From the merge: trust

From the notes, not read on the page; the list read by Claude.

- CABARGA-113: finds cheap imitations of a tool's mark, such as a fake brush script, a lapse of taste.
- GENTRY-017: describes a brand as a person to find its traits, pictures and colours.

## From the merge: persuasion

From the notes, not read on the page; the list read by Claude.

- THALER-126: prefers gains shown in vivid, concrete terms and no visible charge per use for things people do for their own good.

## From the merge: phone

From the notes, not read on the page; the list read by Claude.

- KRUG-221: a cartoon, printed without comment, mocks an app-download pop-up that covers the page, offers less than the site and cannot be refused for good.

## From the merge: process

From the notes, not read on the page; the list read by Claude.

- BRINGHURST-379: holds that typography is more art than technique and that faster tools have not made it better.
- CABARGA-049: holds that the period a design borrows from must match current fashion (in his year the 1950s to early 1970s, not the 1980s).
- CEDERHOLM-061: prefers strict HTML5 habits (a DOCTYPE, closed elements, lower-case tags, quoted attributes).
- KIRSANOV-554: sorts sites into four kinds (personal, non-commercial, corporate, content) by complexity of design and of content.
