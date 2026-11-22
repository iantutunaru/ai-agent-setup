# Web design rulebook: accessibility

55 entries: 3 rule, 52 practice. Built by a script from the owner's reading notes, which are not published; not edited by hand. How to read an entry: [README.md](README.md).

### accessibility-001 · What serves disabled users also serves people who cannot look at the screen
- **Statement:** A page that works in graphic, text and speech form is not a favour to a tiny minority. It also serves people who have pages read aloud to them (news while driving), people on portable devices with very limited, often black-and-white screens, people in poor viewing conditions, and search robots, which read a page like a text-only user. Accessible design takes extra effort.
- **Kind:** practice
- **Use:** look, check
- **Sources:** KIRSANOV-013 (page 13), ROBBINS-017 (page 69)
- **Also in (not read):** NIELSEN-494, KIRSANOV-359
- **Conflict:** KRUG-165 (in accessibility-021) says the argument from benefits for everyone tends to make young developers sceptical; NIELSEN-483 (in accessibility-002) calls the work fairly easy.
- **Read:** 2026-11-21, page, Opus agent, each part checked by Claude; candidate accessibility E02

### accessibility-002 · The group is large, loyal and grows as people age
- **Statement:** Beyond law and courtesy there is a business case for accessibility: users with disabilities often stay loyal to suppliers who serve them well, the work is fairly easy, and the group grows as the population ages. Nielsen gives over 30 million people in the USA with trouble using standard input and output devices, and an estimate of about 14% of people under 65 with some functional impairment against about 50% of those over 65, though many such impairments are minor or do not affect web use. WHO now gives about 1.3 billion people, 16% of the world's population, with a significant disability, a number growing as people live longer; disabling hearing loss affects over 25% of people over 60.
- **Kind:** practice
- **Use:** look
- **Sources:** NIELSEN-483 (page 375), NIELSEN-487 (page 376)
- **Needs source:** the share of people whose impairment affects web use, by age (WHO counts significant disability in general)
- **Current source:** confirmed by https://www.who.int/news-room/fact-sheets/detail/disability-and-health (read 2026-11-21)
- **Current source:** confirmed by https://www.who.int/news-room/fact-sheets/detail/deafness-and-hearing-loss (read 2026-11-21)
- **Conflict:** KRUG-165 (in accessibility-021) says arguments from disability percentages tend to make young developers sceptical; ROBBINS-017 (in accessibility-001) says accessible design takes extra effort.
- **Read:** 2026-11-21, page, Opus agent, each part checked by Claude; candidate accessibility E04

### accessibility-003 · Choose a template that was built to be accessible
- **Statement:** When a site is built on a template or theme (such as a WordPress theme), choose one designed to be accessible.
- **Kind:** practice
- **Use:** look
- **Sources:** KRUG-176 (page s126)
- **Read:** 2026-11-21, passage, Opus agent, each part checked by Claude; candidate accessibility E07

### accessibility-004 · Mark stress as emphasis, and only where it is meant
- **Statement:** Mark stress with the emphasis element, which a speech browser can render as intonation, not with an italic tag: the book calls it a visual tag a speech browser will likely ignore, and current HTML gives the i element a meaning of its own instead (an alternate voice, such as a technical term or a foreign phrase). Use emphasis where the stress changes the meaning of a sentence, not merely to set text in italics, and strong for words that are truly important, serious or urgent, such as a key instruction; the book adds that screen readers may change their tone of voice for them.
- **Kind:** practice
- **Use:** text, check
- **Sources:** KIRSANOV-014 (page 13-14, the notes cite 13), ROBBINS-042 (page 125-126)
- **Also in (not read):** LUPTON-103
- **Needs source:** whether current screen readers change their voice for em and strong (no standard, MDN or WAI page read says so)
- **Current source:** confirmed by https://html.spec.whatwg.org/multipage/text-level-semantics.html (read 2026-11-21)
- **Read:** 2026-11-21, page, Opus agent, each part checked by Claude; candidate accessibility E13

### accessibility-005 · Most screen reader users move through a page by its headings
- **Statement:** Most screen reader users find their way through a page by its headings: 76 percent of the screen reader users in a WebAIM survey said they move through pages by headings always or often, using them as a mental map of the page and as jump points. In WebAIM's 2026 survey (1,780 responses) moving through the headings is still the main way to find information on a long page (67.8%), and 88.3% find heading levels useful. Long pages are hard for blind users to search, so mark the structure with real heading elements, which a screen reader user can hear and use to skip unwanted sections.
- **Kind:** rule
- **Use:** look, check
- **Sources:** LAWSON-007 (page 53), NIELSEN-491 (page 380)
- **Also in (not read):** NIELSEN-633
- **Study (as the book reports it):** WebAIM screen reader user survey 2 (webaim.org/projects/screenreadersurvey2), called recent in a book of 2010; number of users not given on the page
- **Asked of the source:** the share of screen reader users who navigate by headings in the latest WebAIM survey.
- **Current source:** confirmed by https://webaim.org/projects/screenreadersurvey11/ (read 2026-11-21)
- **Current source:** confirmed by https://webaim.org/projects/screenreadersurvey/ (read 2026-11-21)
- **Read:** 2026-11-21, passage, Opus agent, each part checked by Claude; candidate accessibility E16

### accessibility-006 · Crawlers move through a site by its links and text
- **Statement:** Search engines are in some ways blind users: for people to find the site, crawlers must be able to move through it by real links and index its text. The book adds that they do so without looking at the images; Google today reads images with computer vision as well as their alt text and the page's text.
- **Kind:** practice
- **Use:** check
- **Sources:** NIELSEN-495 (page 381)
- **Asked of the source:** that search engine crawlers still index a site from its text and links, not from what its images show.
- **Current source:** confirmed by https://developers.google.com/search/docs/crawling-indexing/links-crawlable (read 2026-11-21)
- **Current source:** overturned by https://developers.google.com/search/docs/appearance/google-images (read 2026-11-21)
- **Read:** 2026-11-21, passage, Opus agent, each part checked by Claude; candidate search-and-filters E39

### accessibility-007 · Headings form a logical outline in level order
- **Statement:** Headings build the outline that screen readers use to present and move through a page: start with a top-level heading (h1) and use the levels in numerical order. Heading structure and meaningful link words (never "click here") let blind users and people with dyslexia find the section they want in a long page.
- **Kind:** practice
- **Use:** check
- **Sources:** ROBBINS-029 (page 105), NIELSEN-513 (page 391)
- **Asked of the source:** that screen readers navigate by heading levels and link text, and what WCAG asks of heading order and link wording today.
- **Current source:** confirmed by https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements (read 2026-11-21)
- **Current source:** confirmed by https://www.w3.org/WAI/WCAG22/Understanding/link-purpose-in-context.html (read 2026-11-21)
- **Read:** 2026-11-21, passage, Opus agent, each part checked by Claude; candidate content E23

### accessibility-008 · A heading's level follows the structure, not its look
- **Statement:** Use the heading levels in their logical order (h1 for the page title or main heading, h2 for major sections, h3 for subheadings) and apply them by structure even where two levels look alike; the looks are set in the style sheet, so the tag follows structure while the look may differ: a section name can be the h1 and still be set smaller and paler than the headlines below it. A page should generally have one h1 that describes its content. The book's reason, that search engines weigh the h1 most, finds no support today: Google says heading order does not matter to its search and no number of headings is ideal.
- **Kind:** practice
- **Use:** look, check
- **Sources:** KRUG-171 (page s126), LUPTON-104 (page 135), LUPTON-194 (page 145)
- **Asked of the source:** that one h1 to a page is still advised, and whether search engines still weigh it most.
- **Current source:** confirmed by https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements (read 2026-11-21)
- **Current source:** overturned by https://developers.google.com/search/docs/fundamentals/seo-starter-guide (read 2026-11-21)
- **Conflict:** BEAIRD-052 (in accessibility-009) says the heading levels in the markup should match the visual emphasis of the headings.
- **Read:** 2026-11-21, image, Opus agent, each part checked by Claude; candidate accessibility E17

### accessibility-009 · Heading levels and visual emphasis tell the same story
- **Statement:** Match the heading levels h1 to h6 in the markup to the visual emphasis of the headings, so that search engines and visitors with impaired vision get the same picture of what matters as sighted visitors.
- **Kind:** practice
- **Use:** look, check
- **Sources:** BEAIRD-052 (page 42)
- **Conflict:** LUPTON-104, LUPTON-194 (in accessibility-008) say the level follows structure while the visual weight may differ: their example sets the h1 smaller and paler than the h3 headlines.
- **Read:** 2026-11-21, passage, Opus agent, each part checked by Claude; candidate accessibility E18

### accessibility-010 · Rank headings by their number, not by the section they sit in
- **Statement:** Give each heading the rank of its real nesting level (h1, then h2, then h3) rather than h1 everywhere with sectioning elements to set the level. Browsers do not pass the computed outline to screen readers, so a page of h1 headings loses its navigability.
- **Kind:** practice
- **Use:** check
- **Sources:** LAWSON-008 (page 53), ROBBINS-041 (page 123)
- **Asked of the source:** that browsers still do not implement the HTML5 outline algorithm, and that hierarchical heading levels are the current advice.
- **Current source:** confirmed by https://html.spec.whatwg.org/multipage/sections.html (read 2026-11-21)
- **Current source:** confirmed by https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements (read 2026-11-21)
- **Read:** 2026-11-21, passage, Opus agent, each part checked by Claude; candidate accessibility E19

### accessibility-011 · Imperfect headings beat flat headings, flat headings beat none
- **Statement:** For screen reader users, imperfectly nested headings are better than headings all at the same level, and headings all at the same level are still better than none.
- **Kind:** practice
- **Use:** check
- **Sources:** LAWSON-009 (page 54)
- **Study (as the book reports it):** LAWSON-009: informal Twitter poll of screen reader users, about 2010, described by the authors as completely unscientific; size not given.
- **Read:** 2026-11-21, passage, Opus agent, each part checked by Claude; candidate accessibility E20

### accessibility-012 · Mark the page's regions as landmarks
- **Statement:** Many screen reader users navigate by landmarks: in WebAIM's January 2014 survey about 28 percent seldom or never did, against more than half in 2010 who did not use them or did not know of them. The rise did not last: frequent use fell from 43.8% in 2014 to 28.3% in WebAIM's 2026 survey, where 39.0% seldom or never use landmarks. Mark the page's regions (navigation, banner, main, complementary, contentinfo) so the users who rely on them can find their way; the HTML elements nav, header, main, aside and footer give the same landmarks with shorter, clearer code (header and footer only when they belong to the whole page, not to a section).
- **Kind:** rule
- **Use:** check
- **Sources:** GOLDSTEIN-064 (page 388), ROBBINS-058 (page 145-146, the notes cite 145)
- **Study (as the book reports it):** WebAIM's fifth screen reader user survey, January 2014, set beside a similar survey of 2010; participant counts not given on the page
- **Asked of the source:** the share of screen reader users who navigate by landmarks in the latest WebAIM survey, and that current browsers and screen readers expose nav, header, main, aside and footer as landmarks.
- **Current source:** overturned by https://webaim.org/projects/screenreadersurvey11/ (read 2026-11-21)
- **Current source:** confirmed by https://www.w3.org/WAI/ARIA/apg/practices/landmark-regions/ (read 2026-11-21)
- **Read:** 2026-11-21, page, Opus agent, each part checked by Claude; candidate accessibility E21

### accessibility-013 · One banner, one footer landmark, one main, holding only this page's content
- **Statement:** Only the page-wide header (logo, site identity, site search) carries the banner landmark and only the page-wide footer (copyright, privacy links) the contentinfo landmark, not every header or footer inside the page. Mark the main content once, so screen readers and other assistive tools know where it starts; it holds only content unique to that page, never headers, sidebars or other parts repeated across the site. The book reports that the main element replaces the older "skip to main content" links; today the main element is the usual target of such a link, and skip links still help sighted keyboard users.
- **Kind:** practice
- **Use:** check
- **Sources:** LAWSON-024 (page 67), ROBBINS-035 (page 117)
- **Asked of the source:** that current screen readers let users jump to the main element, and whether a skip link is still needed beside it.
- **Current source:** confirmed by https://www.w3.org/WAI/ARIA/apg/practices/landmark-regions/ (read 2026-11-21)
- **Current source:** confirmed by https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/main (read 2026-11-21)
- **Conflict:** KRUG-173, LUPTON-108 (in navigation-040) ask for a "skip to content" link at the start of every page.
- **Read:** 2026-11-21, page, Opus agent, each part checked by Claude; candidate accessibility E22

### accessibility-014 · Mark the main navigation as a landmark assistive programs can jump to
- **Statement:** The main navigation is marked up as a list of links inside a navigation landmark, which gives assistive programs a place to jump to. Not every list of links gets this mark: reserve it for the primary navigation of the site or of a large section or article.
- **Kind:** practice
- **Use:** check
- **Sources:** CEDERHOLM-024 (page 46-47), ROBBINS-039 (page 122)
- **Also in (not read):** ROBBINS-211
- **Asked of the source:** how a navigation landmark is declared today and which link lists should carry it; the explicit role the book adds is said to be redundant in current HTML.
- **Current source:** confirmed by https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/nav (read 2026-11-21)
- **Current source:** confirmed by https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/navigation_role (read 2026-11-21)
- **Read:** 2026-11-21, page, Opus agent, each part checked by Claude; candidate navigation E84

### accessibility-015 · Lead the source code with the key content
- **Statement:** Write the page in the order that makes sense without any styling (header, content, sidebar, footer), lead the markup with the content that matters most and position it on screen with CSS: screen reader and text browser users meet content in source order, and a layout that starts with a left column makes them wade through less important material to reach the main text; key content early in the markup also helps devices without CSS and search engines. The source order may differ from the visual order for this: in the example the name and tagline come first in the code, so the top of the page is not clogged with navigation, though the menu sits right under the logo on screen.
- **Kind:** practice
- **Use:** look, check
- **Sources:** CEDERHOLM-063 (page 223), LUPTON-110 (page 137), CEDERHOLM-066 (page 225), GILLENWATER-095 (page 277)
- **Also in (not read):** LUPTON-189, CEDERHOLM-054, ROBBINS-266
- **Asked of the source:** that the reading and focus order must follow a meaningful sequence when the visual order differs from the source order (WCAG, meaningful sequence)
- **Current source:** confirmed by https://www.w3.org/WAI/WCAG22/Understanding/meaningful-sequence.html (read 2026-11-21)
- **Current source:** confirmed by https://www.w3.org/WAI/WCAG22/Understanding/focus-order.html (read 2026-11-21)
- **Conflict:** LUPTON-111, ROBBINS-243 (in accessibility-028) say to keep visual order and source order close and to reorder visually only with care.
- **Read:** 2026-11-21, page, Opus agent, each part checked by Claude; candidate accessibility E26, joined by layout E156

### accessibility-016 · A control is a real link when it goes somewhere and a real button when it acts
- **Statement:** Any control a person interacts with is a real link when it goes somewhere and a real button when it acts like a button: both take keyboard focus with Tab, and while a tabindex can give any element focus, only links and a few other elements fire their action on Enter. An ARIA button role does not make Enter work either.
- **Kind:** practice
- **Use:** check
- **Sources:** DUCKETT-004 (page 497)
- **Asked of the source:** that in current browsers an element given a tabindex or a button role still does not act on Enter by itself.
- **Current source:** confirmed by https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/button_role (read 2026-11-21)
- **Read:** 2026-11-21, passage, Opus agent, each part checked by Claude; candidate accessibility E30

### accessibility-017 · A home-made control declares its role, state and value
- **Statement:** A control built from scripts, images or plain elements (a slider, a tab bar, a list item that sorts content, a drop-down built from a list) is invisible to screen readers, or cannot be told for what it is, unless its role, state and value are declared, which is what ARIA attributes do: properties that stay stable (which label belongs to a form control, that a control opens a pop-up menu) and states that change as the user acts (which item is selected). Elements that already say what they are, such as headings and navigation, mostly need no extra ARIA, and an element whose role is implicit gets none.
- **Kind:** practice
- **Use:** check
- **Sources:** LAWSON-020 (page 65), GOLDSTEIN-062 (page 387), ROBBINS-057 (page 144-145), ROBBINS-155 (page 270), ROBBINS-059 (page 146)
- **Also in (not read):** GOLDSTEIN-061, ROBBINS-019
- **Asked of the source:** the current ARIA guidance on roles, states, properties and values for custom controls and widgets, and on leaving ARIA off elements whose role is implicit
- **Current source:** confirmed by https://www.w3.org/WAI/WCAG22/Understanding/name-role-value.html (read 2026-11-21)
- **Current source:** confirmed by https://www.w3.org/TR/html-aria/ (read 2026-11-21)
- **Read:** 2026-11-21, page, Opus agent, each part checked by Claude; candidate accessibility E31, joined by forms E37

### accessibility-018 · Plan for the four groups of impairment
- **Statement:** Disability on the web is about whether a person has trouble using the usual input and output devices in the way they were meant to be used, not about wheelchairs. Plan for four broad groups: visual (screen readers, Braille displays, magnifiers, browser text zoom), motor (modified mice and keyboards, pedals, voice, joysticks), hearing (transcripts of audio, captions for video) and cognitive (simple, clear sites, which help every user).
- **Kind:** practice
- **Use:** look, check
- **Sources:** ROBBINS-018 (page 69), NIELSEN-484 (page 375)
- **Also in (not read):** ROBBINS-016, KISSANE-051
- **Read:** 2026-11-21, page, Opus agent, each part checked by Claude; candidate accessibility E01

### accessibility-019 · A quick check of how the page reads without its looks
- **Statement:** As a quick accessibility check, visit the site with a text-only browser. The book holds that if the site works and reads well there, most disabled users can probably use it; W3C warns that a page can pass quick checks and still have significant barriers, and that knowledgeable human evaluation is needed. Test how pages linearise for screen readers with software made for that purpose. Also have a colour-blind person look at the site, or view it in black and white yourself.
- **Kind:** practice
- **Use:** check
- **Sources:** NIELSEN-518 (page 392), LUPTON-109 (page 136)
- **Asked of the source:** which tools check a page's linear reading order and its use by screen readers today, and whether a text-only view is still a fair stand-in (WCAG, W3C's guidance on evaluating accessibility); the book names Lynx.
- **Current source:** overturned by https://www.w3.org/WAI/test-evaluate/easy-checks/ (read 2026-11-21)
- **Current source:** confirmed by https://www.w3.org/WAI/test-evaluate/ (read 2026-11-21)
- **Read:** 2026-11-21, passage, Opus agent, each part checked by Claude; candidate testing E116

### accessibility-020 · Keep content and structure apart from presentation
- **Statement:** Separating form from content lets the same content be reformatted for different devices and users and outlive its storage format. Layouts built from nested tables mix content with decoration, need far more code, are hard for screen readers, text browsers and small screens, and make a redesign so laborious that rebuilding the page can be easier.
- **Kind:** practice
- **Use:** check
- **Sources:** LUPTON-055 (page 98-99), CEDERHOLM-064 (page 222-223, the notes cite 223)
- **Also in (not read):** NIELSEN-040, ROBBINS-210, LUPTON-117, LUPTON-102, KIRSANOV-036
- **Asked of the source:** that tables used for layout still harm screen reader and small-screen use (WCAG, MDN).
- **Current source:** confirmed by https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content/HTML_table_basics (read 2026-11-21)
- **Read:** 2026-11-21, page, Opus agent, each part checked by Claude; candidate process E83

### accessibility-021 · The reason that holds is the change in some people's lives
- **Statement:** The reason to make a site accessible that matters is that it greatly improves some people's lives: blind people can read almost any paper or magazine on their own. Legal requirements will also come.
- **Kind:** practice
- **Use:** look
- **Sources:** KRUG-165 (page s119)
- **Conflict:** NIELSEN-483, NIELSEN-487 (in accessibility-002) argue from the share of people with an impairment, and KIRSANOV-013, ROBBINS-017 (in accessibility-001) from the benefit to everyone; KRUG-165 says both arguments tend to make young developers sceptical.
- **Read:** 2026-11-21, page, Opus agent, each part checked by Claude; candidate accessibility E03

### accessibility-022 · Serve each audience in full, without taking from the other
- **Statement:** Accessibility at its best serves each audience fully without diminishing the other, like a sign with Braille embossed on a clear overlay, so that both the print and the Braille stay full size.
- **Kind:** practice
- **Use:** look
- **Sources:** KRUG-166 (page s120)
- **Read:** 2026-11-21, passage, Opus agent, each part checked by Claude; candidate accessibility E05

### accessibility-023 · Imperfect beats careless: start with the pages most used
- **Statement:** Perfect accessibility is not always reached, but an imperfect design differs greatly from a careless one: apply the rules wherever possible, since many are simple and cheap. On a large site, phase the W3C accessibility guidelines in: first bring the home page, the most visited pages and every page on the path to a purchase or other key transaction up to the most important requirements; make every new page fully compliant; then gradually bring the medium-traffic pages up to the priority rules, with the most visited pages meeting every requirement as the long-term aim. Old, little-used pages may stay unless they are of particular interest to disabled users.
- **Kind:** practice
- **Use:** check
- **Sources:** NIELSEN-486 (page 376-377), NIELSEN-517 (page 392)
- **Read:** 2026-11-21, page, Opus agent, each part checked by Claude; candidate accessibility E06

### accessibility-024 · Section 508 baseline, part one: what the content must offer
- **Statement:** A baseline checklist from US Section 508, useful for any site: give text equivalents for non-text elements; synchronise alternatives with multimedia; never carry information by colour alone; keep documents readable without the style sheet; mark row and column headers in data tables and link cells to headers in multi-level tables. The first, third and fourth points have entries of their own (E42, E69, E67).
- **Kind:** practice
- **Use:** check
- **Sources:** ROBBINS-020 (page 70-71, the notes cite 70)
- **Asked of the source:** that the current Section 508 standard, or WCAG, still holds each of these points, the data table headers and the synchronised alternatives above all.
- **Current source:** confirmed by https://www.access-board.gov/ict/ (read 2026-11-21)
- **Current source:** confirmed by https://www.access-board.gov/ict/wcag2ict.html (read 2026-11-21)
- **Read:** 2026-11-21, page, Opus agent, each part checked by Claude; candidate accessibility E10

### accessibility-025 · Section 508 baseline, part two: what the page must let people do
- **Statement:** More checks from US Section 508, now carried by WCAG: nothing flashes more than three times in any one second unless the flash is below the general and red flash thresholds (WCAG 2.3.1, which replaced the old 2 Hz to 55 Hz flicker range); content generated by scripts must be readable by assistive technology; online forms must let users of assistive technology reach all fields, instructions and the submit function; give a way to skip repeated navigation links (E24); warn users of timed responses and let them ask for more time.
- **Kind:** practice
- **Use:** check
- **Sources:** ROBBINS-021 (page 71)
- **Asked of the source:** that the current Section 508 standard, or WCAG, still holds each of these points, and the flicker range it now gives.
- **Current source:** confirmed by https://www.access-board.gov/ict/wcag2ict.html (read 2026-11-21)
- **Current source:** overturned by https://www.w3.org/WAI/WCAG22/Understanding/three-flashes-or-below-threshold.html (read 2026-11-21)
- **Read:** 2026-11-21, page, Opus agent, each part checked by Claude; candidate accessibility E11

### accessibility-026 · Mark up what the content is, not how it looks
- **Statement:** Choose each element by what the content is (this is a heading of level 2), not by its look (bold 12 point), and set the look in the style sheet. Every kind of reader can then render the page its own way: a graphic browser in large bold type, a text browser with blank lines, a speech browser with a pause and a change of tone or by reading out the headings for the user to choose from, a search robot by giving the heading more weight; small screens and TVs can adapt the page too.
- **Kind:** practice
- **Use:** check
- **Sources:** KIRSANOV-003 (page 7), NIELSEN-039 (page 52-53, the notes cite 53)
- **Also in (not read):** ROBBINS-027, NIELSEN-485, ROBBINS-007, CEDERHOLM-003, LUPTON-106
- **Read:** 2026-11-21, page, Opus agent, each part checked by Claude; candidate accessibility E12

### accessibility-027 · Read in source order, the page must still make sense
- **Statement:** Screen readers read a page as one linear stream and keyboard tabbing follows the same order: changing the visual order with CSS does not change it. So the source order must itself make sense, and things that belong together sit together in it: never a heading in one table cell with its text in the cell below, where a row by row reading puts other cells' content between them.
- **Kind:** practice
- **Use:** check
- **Sources:** GOLDSTEIN-052 (page 280), KIRSANOV-016 (page 14)
- **Also in (not read):** LUPTON-128, LUPTON-107
- **Asked of the source:** that current screen readers and keyboard focus still follow the source order when CSS reorders the items on screen (KIRSANOV-016 and LUPTON-128 speak of layout tables).
- **Current source:** confirmed by https://www.w3.org/TR/css-display-4/ (read 2026-11-21)
- **Current source:** confirmed by https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/reading-flow (read 2026-11-21)
- **Read:** 2026-11-21, passage, Opus agent, each part checked by Claude; candidate accessibility E25

### accessibility-028 · Keep the visual order and the source order close
- **Statement:** Keep the differences between visual order and source order small: not every screen reader user is blind, and people who navigate by source order while seeing the layout get confused when the two diverge much. Change the source order when there is a logical reason, and reorder visually only when both the logical and the visual order call for it, never because it is convenient.
- **Kind:** practice
- **Use:** look, check
- **Sources:** LUPTON-111 (page 137), ROBBINS-243 (page 536)
- **Asked of the source:** how current screen readers and keyboard focus treat items that CSS has reordered on screen.
- **Current source:** confirmed by https://www.w3.org/TR/css-display-4/ (read 2026-11-21)
- **Current source:** confirmed by https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/order (read 2026-11-21)
- **Conflict:** CEDERHOLM-063, LUPTON-110 (in accessibility-015) advise putting the main content first in the source and placing it elsewhere on screen with CSS.
- **Read:** 2026-11-21, page, Opus agent, each part checked by Claude; candidate accessibility E27

### accessibility-029 · Use the native element wherever one exists
- **Statement:** Use the native HTML element wherever one exists (a real h2 rather than styled text with a heading role, the native range slider rather than one faked with scripts and images) and keep ARIA for meanings HTML cannot express. Native elements carry their meaning built in and work from the keyboard with less code; added ARIA attributes are easy to forget, and the fakes need extra care and code to work from the keyboard.
- **Kind:** practice
- **Use:** check
- **Sources:** LAWSON-021 (page 65), LAWSON-032 (page 90)
- **Asked of the source:** that the native range slider works from the keyboard in current browsers.
- **Current source:** confirmed by https://www.w3.org/TR/using-aria/ (read 2026-11-21)
- **Current source:** confirmed by https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/slider_role (read 2026-11-21)
- **Read:** 2026-11-21, passage, Opus agent, each part checked by Claude; candidate accessibility E29

### accessibility-030 · Where accessibility and valid markup pull apart, accessibility wins
- **Statement:** Where accessibility and formal validity conflict, accessibility wins: ARIA attributes that make an older page fail validation are acceptable as long as the rest of the markup is sound.
- **Kind:** practice
- **Use:** check
- **Sources:** LAWSON-022 (page 65)
- **Read:** 2026-11-21, passage, Opus agent, each part checked by Claude; candidate accessibility E32

### accessibility-031 · Everything can be reached and worked by keyboard
- **Statement:** Make all content reachable by keyboard, since not everyone can use a mouse; any applet or embedded component whose interactive elements go beyond standard HTML must also work without a mouse.
- **Kind:** practice
- **Use:** check
- **Sources:** KRUG-174 (page s126), NIELSEN-509 (page 389)
- **Asked of the source:** what WCAG now requires for keyboard operation (NIELSEN-509 names Java applets and ActiveX).
- **Current source:** confirmed by https://www.w3.org/WAI/WCAG22/Understanding/keyboard.html (read 2026-11-21)
- **Read:** 2026-11-21, passage, Opus agent, each part checked by Claude; candidate accessibility E33

### accessibility-032 · Do not ask for precise pointing at small targets
- **Statement:** Many people struggle with precise mouse movement or with pressing several keys at once. That is mostly for browser makers to solve, but a site should not require precise pointing on clickable image maps, where the targets are small.
- **Kind:** practice
- **Use:** look, check
- **Sources:** NIELSEN-508 (page 389)
- **Read:** 2026-11-21, passage, Opus agent, each part checked by Claude; candidate accessibility E35

### accessibility-033 · Text meant only for screen reader users is hidden from view, not left out
- **Statement:** Some developers hide a fieldset legend that is not wanted on screen visually (shrunk to 1 px with overflow hidden) so that screen readers still announce it; W3C's technique C7 gives this 1-pixel box as the current way to keep text for screen readers only, since display:none and visibility:hidden hide it from them too. Information meant only for users who cannot see the images can likewise be offered separately, for example as a linked spoken description or, in the book's older technique, in the alt text of an invisible image.
- **Kind:** practice
- **Use:** check
- **Sources:** ROBBINS-219 (page 655), NIELSEN-505 (page 387)
- **Asked of the source:** the current way to give text to screen readers only (NIELSEN-505 uses a transparent spacer image, ROBBINS-219 a legend shrunk to 1 px with overflow hidden).
- **Current source:** confirmed by https://www.w3.org/WAI/WCAG22/Techniques/css/C7 (read 2026-11-21)
- **Read:** 2026-11-21, passage, Opus agent, each part checked by Claude; candidate accessibility E41

### accessibility-035 · Give the reader priority over how text is presented
- **Statement:** Text must be universally accessible: separate the text from its presentation and give the user priority over size, typeface and layout, so they can read comfortably given their device, lighting and preferences. A type system tied to one base size lets readers with their own style sheets change the whole page in one step. The book keeps !important for user style sheets; in current CSS a reader's !important style beats the site's !important anyway, while the site's normal styles override the reader's normal ones.
- **Kind:** practice
- **Use:** check
- **Sources:** KIRSANOV-358 (page 105), NIELSEN-113 (page 106), CEDERHOLM-012 (page 31)
- **Asked of the source:** how readers apply their own style and text settings in current browsers, and whether a site's !important still overrides them.
- **Current source:** confirmed by https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Introduction (read 2026-11-21)
- **Read:** 2026-11-21, page, Opus agent, each part checked by Claude; candidate accessibility E65

### accessibility-037 · Build the basic working page first, then layer enhancements
- **Statement:** Start with a basic experience that makes the content and core functions available even to the simplest browsers and assistive devices (plain semantic HTML that reads well without CSS and works without JavaScript), then add richer styling and scripting for browsers that can handle them, and last the nice-to-have effects such as animation that the basic use does not need.
- **Kind:** practice
- **Use:** check
- **Sources:** GILLENWATER-002 (page 30), ROBBINS-006 (page 64)
- **Also in (not read):** CEDERHOLM-041, ROBBINS-008, CEDERHOLM-083
- **Asked of the source:** that progressive enhancement is still the recommended way to build, and that browsers still skip the CSS they do not understand (MDN, web.dev).
- **Current source:** confirmed by https://developer.mozilla.org/en-US/docs/Glossary/Progressive_Enhancement (read 2026-11-21)
- **Current source:** confirmed by https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/Error_handling (read 2026-11-21)
- **Current source:** confirmed by https://www.gov.uk/service-manual/technology/using-progressive-enhancement (read 2026-11-21)
- **Read:** 2026-11-21, page, Opus agent, each part checked by Claude; candidate process E77

### accessibility-038 · Content behind tabs, accordions and sliders stays reachable when scripts do not run
- **Statement:** Accordions, tabs and sliders hide part of the content when the page loads, so a visitor without JavaScript would never reach it unless the page plans another presentation: for example a "no-js" class on the page that the script removes, so styles can serve visitors whose scripts do not run, and tabs built as links to their panels' place in the page.
- **Kind:** practice
- **Use:** check
- **Sources:** DUCKETT-003 (page 497), DUCKETT-011 (page 503)
- **Also in (not read):** DUCKETT-015
- **Asked of the source:** what current guidance (web.dev, MDN) advises for content hidden by scripts when the script does not run; the techniques are of 2014.
- **Current source:** confirmed by https://design-system.service.gov.uk/components/tabs/ (read 2026-11-21)
- **Current source:** confirmed by https://design-system.service.gov.uk/components/accordion/ (read 2026-11-21)
- **Current source:** confirmed by https://frontend.design-system.service.gov.uk/import-javascript/ (read 2026-11-21)
- **Read:** 2026-11-21, passage, Opus agent, each part checked by Claude; candidate accessibility E68

### accessibility-039 · Set text large enough for weak eyes
- **Statement:** Set text large enough for people with weak eyesight; small text also reads as a footnote and gets ignored. Experienced designers tend to set type too small: make it bigger.
- **Kind:** practice
- **Use:** look, check
- **Sources:** NIELSEN-192 (page 155), LUPTON-168 (page 218)
- **Also in (not read):** NEURO-072
- **Conflict:** KIRSANOV-186 (in type-073) holds that a little small text makes readers look closer and remember more.
- **Read:** 2026-11-21, page, Opus agent, each part checked by Claude; candidate type E78

### accessibility-040 · Never small and low in contrast at once
- **Statement:** Never use small, low-contrast type (small dark grey captions on light grey are so hard to read that people give up on them); large low-contrast or small high-contrast type is tolerable but also best avoided.
- **Kind:** practice
- **Use:** look, check
- **Sources:** KRUG-184 (page s132), KISSANE-038 (page 21)
- **Also in (not read):** NIELSEN-197
- **Read:** 2026-11-21, passage, Opus agent, each part checked by Claude; candidate type E79

### accessibility-041 · Let readers resize the text
- **Statement:** Give font sizes in relative units (a percentage of the default, em, rem), not in pixels or points, and set every size relative to the user's chosen base size (large text at 200%, headings at say 1.5 times the body text), so that people with weak sight can enlarge the text with the browser's controls and the headings grow with it: in some browsers the user cannot change text sized in pixels, which MDN calls not accessible; web.dev advises relative units such as em, rem or ch. Points, picas and inches belong only in print style sheets. The preferred size depends on screen, eyesight and whether the page is being shown to others; the worst case is tiny text that does not grow when the user asks for larger text.
- **Kind:** practice
- **Use:** check
- **Sources:** NIELSEN-492 (page 380-381), ROBBINS-179 (page 344), NIELSEN-112 (page 105-106), ROBBINS-180 (page 344)
- **Also in (not read):** BEAIRD-208
- **Asked of the source:** whether current browsers enlarge text sized in pixels, and what WCAG asks for text resizing.
- **Current source:** confirmed by https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size (read 2026-11-21)
- **Current source:** confirmed by https://www.w3.org/WAI/WCAG22/Understanding/resize-text.html (read 2026-11-21)
- **Current source:** confirmed by https://web.dev/learn/design/typography (read 2026-11-20)
- **Read:** 2026-11-21, passage, Opus agent, each part checked by Claude; candidate type E85, joined by accessibility E60

### accessibility-043 · Keep the background behind text plain
- **Statement:** Use a plain colour background or a pattern of minimal contrast: background images make text hard to recognise, busy ones slow and annoy everyone, and for people with weak sight a patterned background and pale text can make a page unreadable. If a background picture is unavoidable, it must be less prominent than the text.
- **Kind:** practice
- **Use:** look, check
- **Sources:** NIELSEN-191 (page 155, 158, the notes cite 155), NIELSEN-490 (page 380)
- **Conflict:** BEAIRD-107 (in colour-070) advises enlivening large flat colour areas with subtle background images or shapes.
- **Read:** 2026-11-21, page, Opus agent, each part checked by Claude; candidate colour E74

### accessibility-045 · Alternative text makes sense to someone who cannot see the image
- **Statement:** Alternative text must make sense on its own to someone who cannot see the image: "Latest news, since 19 May", not just "Since 19 May". The book allowed a little extra information where browsers showed alt text as a hover tooltip; the current HTML standard forbids browsers to present alt text the way they present a title, and it is the title attribute that is shown as a tooltip.
- **Kind:** practice
- **Use:** check, text
- **Sources:** NIELSEN-504 (page 387)
- **Asked of the source:** whether current browsers still show alternative text as a tooltip.
- **Current source:** overturned by https://html.spec.whatwg.org/multipage/embedded-content.html (read 2026-11-21)
- **Current source:** confirmed by https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img (read 2026-11-21)
- **Read:** 2026-11-21, passage, Opus agent, each part checked by Claude; candidate images E78

### accessibility-046 · The main menu needs no heading that says "Navigation"
- **Statement:** A navigation block or sidebar may go without a heading: a secondary list such as "Most popular posts" can carry one, while the main site menu does not get a redundant heading that only says "Navigation".
- **Kind:** practice
- **Use:** check
- **Sources:** LAWSON-004 (page 50)
- **Read:** 2026-11-21, passage, Opus agent, each part checked by Claude; candidate navigation E85

### accessibility-048 · A page will not look the same everywhere; aim for usable everywhere
- **Statement:** A designer never knows how a page will be viewed (browser, device, window size, installed fonts, JavaScript on or off, connection speed, a screen reader speaking it), and it can never look identical in all of them. The aim is a page that is usable and accessible for everyone; cosmetic differences between browsers matter little once that holds. A page must work across the whole range of screens and connections people use, from handhelds to workstations (a 100-fold range of screen sizes and a 1000-fold range of connection speeds in the finding's year); a page that only looks right on one large monitor is wrong, and people should be able to use content in the conditions and on the devices that suit them. Do not try to make a page look identical for everyone; design it so the browser can fit the display to each device and circumstance, so the page both reads well and functions in whatever space is available.
- **Kind:** practice
- **Use:** look, check
- **Sources:** GILLENWATER-001 (page 30), ROBBINS-001 (page 60), GILLENWATER-063 (page 224), NIELSEN-025 (page 39), NIELSEN-024 (page 38), KISSANE-043 (page 22)
- **Also in (not read):** BOULTON-178, CEDERHOLM-090, ROBBINS-004
- **Asked of the source:** the range of screen sizes and connection speeds a page has to cover today
- **Current source:** confirmed by https://web.dev/articles/responsive-web-design-basics (read 2026-11-20)
- **Current source:** confirmed by https://www.w3.org/WAI/fundamentals/accessibility-intro/ (read 2026-11-20)
- **Read:** 2026-11-21, passage, Opus agent, each part checked by Claude; candidate process E76, joined by layout E146, joined by phone E01

### accessibility-049 · Relying on JavaScript for essential layout is risky
- **Statement:** Relying on JavaScript for something essential to the page's layout is risky, because a script does not work for users who have JavaScript turned off.
- **Kind:** practice
- **Use:** check
- **Sources:** GILLENWATER-102 (page 303)
- **Asked of the source:** how many visitors today have scripts off or failing, and what current guidance says about layout that depends on scripts (web.dev, MDN).
- **Current source:** confirmed by https://www.gov.uk/service-manual/technology/using-progressive-enhancement (read 2026-11-21)
- **Read:** 2026-11-21, passage, Opus agent, each part checked by Claude; candidate process E80

### accessibility-050 · A tail of older browser versions remains
- **Statement:** Browsers once spread slowly because people kept the browser they were given: in the book's data about 2% of users a week moved to a new Netscape version in 1995-1997 and only about 1% a week in 1998-1999. Today Chrome, Edge and Firefox versions reach about 95% of users in about three months, Safari, tied to operating-system updates, takes about 19 months, and most features take up to 30 months to reach about 95% of users, so a tail of older browser versions remains.
- **Kind:** rule
- **Use:** check
- **Sources:** NIELSEN-035 (page 46-48, the notes cite 46-47)
- **Study (as the book reports it):** shares of Netscape versions from www.interse.com (1995-1997) and www.starmarket.com (1998-1999), as the graph caption prints them
- **Asked of the source:** how fast new browser versions are taken up today, when browsers update themselves (current browser usage figures).
- **Current source:** overturned by https://web.dev/case-studies/rumvision (read 2026-11-21)
- **Current source:** confirmed by https://web.dev/blog/baseline-definition-update (read 2026-11-21)
- **Read:** 2026-11-21, page, Opus agent, each part checked by Claude; candidate process E81

### accessibility-051 · Wait before relying on a new web technology
- **Statement:** Never put beta web technology on a site (unless you make it or have another reason to promote it). Wait two to three years after a new web technology's stable release before relying on it, and at least a year before using a new HTML version, plug-in, data format or browser-specific feature: at about 1% of users a week, a year passes before most users can even see it and two before all can, bugs remain after the stable release, and good interaction patterns are not yet found, so early uses tend to hurt users more than help.
- **Kind:** practice
- **Use:** check
- **Sources:** NIELSEN-036 (page 47-48)
- **Asked of the source:** how long a new browser feature takes before it is safe to rely on today (web.dev Baseline, MDN compatibility data).
- **Current source:** confirmed by https://web.dev/baseline (read 2026-11-21)
- **Current source:** confirmed by https://web.dev/blog/baseline-definition-update (read 2026-11-21)
- **Current source:** confirmed by https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility (read 2026-11-21)
- **Read:** 2026-11-21, page, Opus agent, each part checked by Claude; candidate process E82

### accessibility-052 · A link keeps a visible focus style
- **Statement:** If the browser's focus outline on a link is removed or hidden (for example because an image replacement trick makes it stretch across the page), give the link a visible focus style of its own, so that keyboard users can still see where they are.
- **Kind:** practice
- **Use:** look, check
- **Sources:** BEAIRD-176 (page 143)
- **Asked of the source:** how current browsers draw the keyboard focus mark on links, and whether it still stretches across links whose text is indented off screen
- **Current source:** confirmed by https://www.w3.org/WAI/WCAG22/Techniques/failures/F78 (read 2026-11-21)
- **Current source:** confirmed by https://www.w3.org/WAI/WCAG22/Understanding/focus-visible.html (read 2026-11-21)
- **Current source:** confirmed by https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:focus-visible (read 2026-11-21)
- **Read:** 2026-11-21, passage, Opus agent; Claude read the line, not each part (AW-T19-Q34); candidate accessibility E34

### accessibility-053 · A voice interface also takes the keyboard
- **Statement:** Any interface where speech is the main input, such as a voice chat, must let people who cannot speak take part by keyboard. Voice and text channels together help everyone, for example to pass on a web address or a proper name.
- **Kind:** practice
- **Use:** look, check
- **Sources:** NIELSEN-507 (page 388-389)
- **Read:** 2026-11-21, page, Opus agent; Claude read the line, not each part (AW-T19-Q34); candidate accessibility E37

### accessibility-055 · Give text strong contrast with its background
- **Statement:** Text and background need strong contrast. Black on white reads best; white on black has the same contrast but distracts and slows reading a little; legibility drops further when text is lighter than black on a background darker than white (never, for example, light grey text on dark grey); pink on green is worst, low in contrast and unreadable for red-green colour-blind users.
- **Kind:** practice
- **Use:** look, check
- **Sources:** NIELSEN-190 (page 155), KRUG-175 (page s126)
- **Read:** 2026-11-21, passage, Opus agent; Claude read the line, not each part (AW-T19-Q34); candidate colour E72

### accessibility-056 · Have a colour-blind person check the colour pairs
- **Statement:** Common text and background colour pairs make pages nearly unreadable for colour-blind people; at least have a red-green colour-blind person, the commonest kind, check the design.
- **Kind:** practice
- **Use:** check
- **Sources:** NIELSEN-489 (page 380)
- **Read:** 2026-11-21, passage, Opus agent; Claude read the line, not each part (AW-T19-Q34); candidate colour E73

### accessibility-057 · Alternative text is short and plain, most important word first
- **Statement:** Keep alternative text plain (no markup), short and meaningful (a short phrase or sentence; the book gives at most 8 to 10 words), and put the most important word first (the company name before "logo").
- **Kind:** practice
- **Use:** check, text
- **Sources:** NIELSEN-503 (page 386), NIELSEN-499 (page 383)
- **Asked of the source:** current guidance on the length and wording of alternative text.
- **Current source:** confirmed by https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img (read 2026-11-21)
- **Current source:** confirmed by https://www.w3.org/WAI/tutorials/images/informative/ (read 2026-11-21)
- **Conflict:** W3C's images tutorial words a linked logo by where it leads ("Example.com homepage" rather than "Example.com logo")
- **Read:** 2026-11-21, passage, Opus agent; Claude read the line, not each part (AW-T19-Q34); candidate images E77

### accessibility-058 · Translate the alternative text with the page
- **Statement:** Translate alternative text with the rest of the page so it matches the user's language.
- **Kind:** practice
- **Use:** check, text
- **Sources:** NIELSEN-502 (page 385)
- **Read:** 2026-11-21, passage, Opus agent; Claude read the line, not each part (AW-T19-Q34); candidate images E80

### accessibility-059 · Content images belong to the page's content, decoration to its styling
- **Statement:** Images that are part of the content (product photos, galleries, illustrations) belong in the page's content; purely decorative images (a background behind a heading, an ornamental border) are added by the styling, which keeps the document cleaner, more accessible and easier to redesign. A background image may carry purely decorative layers, but never meaningful information, text or links: these are lost to non-visual browsers and robots, having no place in the page's linear text.
- **Kind:** practice
- **Use:** check
- **Sources:** ROBBINS-062 (page 179), KIRSANOV-395 (page 115)
- **Asked of the source:** that images placed by CSS are still left out of what a screen reader announces.
- **Current source:** confirmed by https://www.w3.org/WAI/WCAG22/Techniques/css/C9 (read 2026-11-21)
- **Current source:** confirmed by https://www.w3.org/WAI/WCAG22/Techniques/failures/F3 (read 2026-11-21)
- **Read:** 2026-11-21, page, Opus agent; Claude read the line, not each part (AW-T19-Q34); candidate images E81, joined by accessibility E53

### accessibility-061 · Test with users who have different impairments where it can be done
- **Statement:** Ideally test accessibility with several users who have different impairments. The book holds that the range of possible impairments makes this impractical unless the site is meant specifically for disabled people.
- **Kind:** practice
- **Use:** check
- **Sources:** NIELSEN-519 (page 392)
- **Read:** 2026-11-21, passage, Opus agent; Claude read the line, not each part (AW-T19-Q34); candidate testing E117

### accessibility-062 · Do not rebuild cosmetic effects for old browsers
- **Statement:** Before building a fallback for browsers that miss a cosmetic effect, ask whether it really helps users or the site's goal (sales, sign-ups); often it does not, and adding images back for old browsers can even make their pages slower. The same hours spent on accessibility work, usability testing or other real improvements help users more. The book's effects (rounded corners, box and text shadows, gradients) have worked across browsers since July 2015.
- **Kind:** practice
- **Use:** check
- **Sources:** GILLENWATER-024 (page 49-50), GILLENWATER-003 (page 31)
- **Also in (not read):** GILLENWATER-020
- **Asked of the source:** which cosmetic CSS effects still lack support in browsers in use today (MDN compatibility data, current browser usage figures).
- **Current source:** confirmed by https://developer.mozilla.org/en-US/docs/Glossary/Progressive_Enhancement (read 2026-11-21)
- **Current source:** confirmed by https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-radius (read 2026-11-21)
- **Read:** 2026-11-21, page, Opus agent; Claude read the line, not each part (AW-T19-Q34); candidate process E78
