# Web design rulebook: search and filters

58 entries: 6 rule, 52 practice. Built by a script from the owner's reading notes, which are not published; not edited by hand. How to read an entry: [README.md](README.md).

### search-and-filters-001 · Over half of users go straight to search
- **Statement:** Users fall into three groups: over half are search-dominant and go straight to search, about one fifth are link-dominant and use search only when they give up on the links, and the rest mix both depending on what looks most promising.
- **Kind:** rule
- **Use:** look
- **Sources:** NIELSEN-364 (page 272)
- **Study (as the book reports it):** Nielsen's own research ("Мои исследования показали"), shares given, method and sample not reported
- **Current source:** confirmed by https://www.nngroup.com/articles/search-and-you-may-find/ (read 2026-11-20)
- **Read:** 2026-11-20, page; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate search-and-filters E01

### search-and-filters-002 · People browse or search, and switch between the two
- **Statement:** Some users head for the search box the moment they arrive on a site; others browse first and search only when they run out of likely links or are frustrated enough; for everyone else the choice depends on their frame of mind, their hurry and whether the site seems to offer navigation good enough to browse. A browser who is frustrated but almost there turns to the search box; a searcher whose results do not look credible devises a better query and types it again, and one who does not find the item keeps trying until they have had enough and leave unhappy.
- **Kind:** practice
- **Use:** look, check
- **Sources:** KRUG-051 (page s44), KRUG-206 (page s44)
- **Read:** 2026-11-20, image; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate search-and-filters E02

### search-and-filters-003 · Offer several views of the same information
- **Statement:** Offer search and several different views of the same information. People have different preferences, and there is no need to limit them to one way.
- **Kind:** practice
- **Use:** look
- **Sources:** NIELSEN-620 (page 480)
- **Read:** 2026-11-20, passage; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate search-and-filters E03

### search-and-filters-004 · Put search on every page, in the form people scan for
- **Statement:** Unless the site is very small and well organised, every page has a search box, or at least a link to search, in the form users scan for: a box, a button, and the word "Search" or a magnifying-glass icon. Searchers use it at once, and link users who get lost must not have to hunt for it, since one cannot predict where they will give up on navigation.
- **Kind:** practice
- **Use:** look, check
- **Sources:** KRUG-063 (page s54), NIELSEN-366 (page 272-273)
- **Also in (not read):** NIELSEN-443
- **Read:** 2026-11-20, page; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate search-and-filters E04

### search-and-filters-005 · Search does not replace structure and navigation
- **Statement:** Even where search dominates, a site needs a clear structure and navigation: some users rely on links, and searchers must see how a found page relates to the rest of the site and move to nearby related pages, since one page rarely answers everything.
- **Kind:** practice
- **Use:** look
- **Sources:** NIELSEN-365 (page 272)
- **Read:** 2026-11-20, passage; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate navigation E16

### search-and-filters-006 · Give the home page search
- **Statement:** The home page needs search, since many users do not want to click through links. Where search is the main way in, put the search box at the top of the home page; on other sites a simple but visible link to a search page can be enough.
- **Kind:** practice
- **Use:** look, check
- **Sources:** NIELSEN-282 (page 209)
- **Read:** 2026-11-20, passage; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate search-and-filters E05

### search-and-filters-008 · Label search "Search" and add no instructions
- **Statement:** Label search "Search", not Find, Quick Find or Keyword Search, and add no instructions such as "Type a keyword". State the scope of the search only when it could be unclear.
- **Kind:** practice
- **Use:** check, text
- **Sources:** KRUG-064 (page s54)
- **Conflict:** NIELSEN-203 (in search-and-filters-009) advises a hint with realistic examples right under the search box.
- **Read:** 2026-11-20, page; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate search-and-filters E07

### search-and-filters-009 · Put search help right under the search box
- **Statement:** Help that fits the context, placed right under the search box, gets noticed by those who need it, because it sits where their attention already is. Use realistic examples, and put the link to fuller help right after the hint rather than in a distant Help button.
- **Kind:** practice
- **Use:** look, text
- **Sources:** NIELSEN-203 (page 161)
- **Conflict:** KRUG-064 (in search-and-filters-008) says to add no instructions to the search box; NIELSEN-372 (in search-and-filters-028) reports tests in which search tips worked best below the results list.
- **Read:** 2026-11-20, page; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate search-and-filters E08

### search-and-filters-010 · Two search buttons on one page confuse
- **Statement:** Two search buttons on one page are somewhat confusing; most users take an icon and its text label as the same thing, so an icon with its text copy counts as one.
- **Kind:** practice
- **Use:** check
- **Sources:** NIELSEN-314 (page 232)
- **Read:** 2026-11-20, passage; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate search-and-filters E09

### search-and-filters-012 · A wider search box gets longer queries
- **Statement:** Make the search field wide enough to encourage users to type more words. Students typed 2.8 words per query in a small field and 3.4 in a much wider one: users do not like typing what they cannot see, and the size of the box sets their expectation of how long a query should be.
- **Kind:** rule
- **Use:** look, check
- **Sources:** NIELSEN-385 (page 282), NIELSEN-370 (page 274)
- **Study (as the book reports it):** Jussi Karlgren and Kristofer Franzén, Stockholm University: a small experiment, students used the same site with two search box widths; mean words per query reported, sample size not given
- **Current source:** confirmed by https://searchuserinterfaces.com/book/sui_ch4_query_specification.html (read 2026-11-20)
- **Read:** 2026-11-20, page; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate search-and-filters E11

### search-and-filters-013 · Most queries are one or two words
- **Statement:** Over three quarters of queries have one or two words. Web queries are still longer than in older systems: in traditional online documentation 81% of queries were one word, but in 1997 logs from WebCrawler (2,261 queries) and sun.com (24,743 queries) only 43% and 46% were one word.
- **Kind:** rule
- **Use:** look
- **Sources:** NIELSEN-384 (page 282, 286, the notes cite 282)
- **Study (as the book reports it):** NIELSEN-384: Meghan Ede and Nielsen, traditional documentation queries; Nielsen, 1997 analysis of 2,261 WebCrawler and 24,743 sun.com queries.
- **Needs source:** how long the queries typed into a site's own search box are today (NN/g's mean of 2.0 words is from 2001)
- **Current source:** confirmed by https://www.nngroup.com/articles/search-visible-and-simple/ (read 2026-11-20)
- **Current source:** overturned by https://blog.google/products-and-platforms/products/search/ai-mode-us-insights/ (read 2026-11-20)
- **Read:** 2026-11-20, page; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate search-and-filters E12

### search-and-filters-015 · Search the whole site by default
- **Statement:** Search covers the whole site by default, and a search limited to one part of the site is usually avoided. Users often do not understand the site's structure, think the answer lies in a part the limited search does not cover, or do not realise what scope they are searching.
- **Kind:** rule
- **Use:** look, check
- **Sources:** NIELSEN-368 (page 273)
- **Study (as the book reports it):** NIELSEN-368: Nielsen's observations of users; no details given.
- **Current source:** confirmed by https://www.nngroup.com/articles/search-and-you-may-find/ (read 2026-11-20)
- **Read:** 2026-11-20, passage; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate search-and-filters E14

### search-and-filters-016 · A section's own search states its scope and links to the whole site
- **Statement:** Where a search of one section is truly needed, both the query page and the results page state the scope at the top and link to the search of the whole site. On the results page the link reads "Didn't find it? Search the whole site" and reruns the same query across the whole site.
- **Kind:** practice
- **Use:** look, check, text
- **Sources:** NIELSEN-369 (page 273)
- **Also in (not read):** NIELSEN-459
- **Read:** 2026-11-20, page; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate search-and-filters E15

### search-and-filters-017 · No choice between this site and the whole web
- **Statement:** Do not offer a choice between searching this site and searching the whole web: everyone knows where to find web search engines, and the option only clutters the interface.
- **Kind:** practice
- **Use:** check
- **Sources:** NIELSEN-363 (page 271)
- **Read:** 2026-11-20, passage; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate search-and-filters E16

### search-and-filters-018 · Keep scope and field options out of the search box on every page
- **Statement:** Think very carefully before putting options for scope (this section only) or field (by title or by author) into the search box that sits on every page: their payoff is seldom worth making people work out what they are and whether they need them. Offer the scope option on the results page, when a search of the whole site has given the user far more results than they can use.
- **Kind:** practice
- **Use:** look, check
- **Sources:** KRUG-065 (page s54)
- **Conflict:** NIELSEN-371 (in search-and-filters-019) puts the advanced options, scope among them, on a separate advanced search page.
- **Read:** 2026-11-20, page; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate search-and-filters E17

### search-and-filters-019 · No Boolean operators in the main search
- **Statement:** Do not use Boolean operators in the main search. In the author's tests with many user groups, asked to find information about their cats and dogs, almost all users typed "cats AND dogs"; the test held no page on both animals, so they usually got nothing, and most concluded there was no information. Even experienced programmers did it, though on seeing no results they said they should have typed OR. Most users cannot reformulate a query. Advanced options (scope, Boolean, search by parameters) belong on a separate advanced search page.
- **Kind:** rule
- **Use:** look, check
- **Sources:** NIELSEN-371 (page 275)
- **Study (as the book reports it):** Nielsen's tests with many groups of users on a cats-and-dogs search task; group count and sizes not given
- **Current source:** confirmed by https://www.nngroup.com/articles/search-and-you-may-find/ (read 2026-11-20)
- **Conflict:** KRUG-065 (in search-and-filters-018) offers the scope and field options on the results page.
- **Read:** 2026-11-20, page; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate search-and-filters E18

### search-and-filters-020 · Give the advanced search page a forbidding name
- **Statement:** Give the advanced search page an intimidating name such as "Advanced", so that beginners stay away from options they will not understand.
- **Kind:** practice
- **Use:** text
- **Sources:** NIELSEN-373 (page 276)
- **Read:** 2026-11-20, passage; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate search-and-filters E19

### search-and-filters-021 · Match the site's own search to the default search engine
- **Statement:** On an organisation's own network, keep one search engine as the default in its browsers and, where possible, match the internal search to it. Non-technical users do not know that each engine has its own query commands and reuse whatever they remember, with poor results.
- **Kind:** practice
- **Use:** look
- **Sources:** NIELSEN-467 (page 347)
- **Needs source:** that search engines still differ in their query commands and that people carry the commands of one engine over to another.
- **Current source:** none found (searched 2026-11-20)
- **Read:** 2026-11-20, passage; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate search-and-filters E20

### search-and-filters-023 · Live search narrows the list with every letter
- **Statement:** A live search narrows the shown items with every letter the person types, keeping only the items whose text contains what was typed, and it ignores the difference between capital and small letters.
- **Kind:** practice
- **Use:** look, check
- **Sources:** DUCKETT-033 (page 556)
- **Asked of the source:** that narrowing a list in the page with every letter typed is still a current pattern; the finding describes a jQuery technique of 2014.
- **Current source:** confirmed by https://developer.apple.com/design/human-interface-guidelines/search-fields (read 2026-11-20)
- **Read:** 2026-11-20, passage; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate search-and-filters E22

### search-and-filters-024 · A live filter or search must not rebuild the list on every change
- **Statement:** For a filter that reacts live, build all the rows once and only show or hide them on each change: rebuilding the whole table every time the control moves can make the page slow. For live search, prepare the searchable text of every item once and search that on each keystroke, instead of going through and converting all the page's items every time.
- **Kind:** practice
- **Use:** check
- **Sources:** DUCKETT-029 (page 544), DUCKETT-034 (page 556)
- **Asked of the source:** how fast a live filter or search must answer and how its speed is measured in current browsers (web.dev); the finding rests on browser performance of 2014.
- **Current source:** confirmed by https://web.dev/articles/inp (read 2026-11-20)
- **Current source:** confirmed by https://web.dev/articles/dom-size-and-interactivity (read 2026-11-20)
- **Read:** 2026-11-20, passage; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate speed E70

### search-and-filters-025 · Search tolerates misspellings and the names people use
- **Statement:** Search must not demand exact spelling, which defeats poor spellers and foreigners, or a name people do not use. At least check the spelling; one way is to check the words that found nothing and offer a list of similar words to search again. The Medicare plan finder returned nothing for a misspelled drug name, unlike Google, and assumed a generic drug, while most people look generics up by the original brand's name.
- **Kind:** practice
- **Use:** check
- **Sources:** NIELSEN-514 (page 391), THALER-178 (page 153)
- **Also in (not read):** NIELSEN-379
- **Read:** 2026-11-20, page; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate search-and-filters E23

### search-and-filters-026 · Search checks spelling and looks for synonyms itself
- **Statement:** A site search checks spelling, both in the queries and in the documents, and searches for synonyms: computers are good at scanning long lists and finding synonyms, and users are not.
- **Kind:** practice
- **Use:** check
- **Sources:** NIELSEN-374 (page 276)
- **Read:** 2026-11-20, passage; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate search-and-filters E24

### search-and-filters-027 · Offer a few related terms next to the query
- **Statement:** Offer a few related terms for reformulating the query, each one a click that reruns the search, placed close to the current query rather than separated from it by ads and clutter. People are poor at thinking of synonyms and type as little as possible, so the search system must suggest ways to widen the search. A huge table of options overwhelms most users and belongs behind an "Expert search" link.
- **Kind:** practice
- **Use:** look, check
- **Sources:** NIELSEN-387 (page 288, 290, the notes cite 288), NIELSEN-390 (page 287)
- **Read:** 2026-11-20, page; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate search-and-filters E25

### search-and-filters-028 · Put tips for a better search below the results
- **Statement:** Tips for improving a search work best below the results list, where users who reached the end have a reason to want better results. Without them many users would never notice that they could widen the scope of the search.
- **Kind:** rule
- **Use:** look, check
- **Sources:** NIELSEN-372 (page 275)
- **Study (as the book reports it):** tips placed in different spots of the Sun AnswerBook2 results page, below the results judged best; method and users not reported
- **Current source:** none found (searched 2026-11-20)
- **Conflict:** NIELSEN-203 (in search-and-filters-009) places search help right under the search box.
- **Read:** 2026-11-20, passage; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate search-and-filters E26

### search-and-filters-029 · Read the site's own search log
- **Statement:** Study your own site's search log: terms that recur often show what many users want to find on the site but have trouble finding.
- **Kind:** practice
- **Use:** check
- **Sources:** NIELSEN-389 (page 286)
- **Read:** 2026-11-20, passage; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate testing E78

### search-and-filters-030 · Let people find an item by what they see or remember
- **Statement:** Let people identify an item by what they can see or remember, not only by its exact name. A drug reference app finds a pill by its colour, size and shape, and works with partial names.
- **Kind:** practice
- **Use:** look
- **Sources:** THALER-179 (page 153-154)
- **Asked of the source:** that search by an item's visible attributes and by part of its name is still advised; the finding rests on a phone app of 2008.
- **Current source:** confirmed by https://www.nngroup.com/articles/keyword-foraging/ (read 2026-11-20)
- **Read:** 2026-11-20, page; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate search-and-filters E27

### search-and-filters-031 · Let people find a product by its full name
- **Statement:** Let people find a product by its full name, not only by its model number: numbers suit computers, not people.
- **Kind:** practice
- **Use:** look, check
- **Sources:** NIELSEN-198 (page 156)
- **Read:** 2026-11-20, passage; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate forms E44

### search-and-filters-032 · Search results come in the user's language
- **Statement:** If every document exists in every language, search returns results only in the user's preferred language. Where not everything is translated, the search itself searches across languages, since users forget to enter translated terms even when they know several languages.
- **Kind:** practice
- **Use:** check
- **Sources:** NIELSEN-549 (page 416)
- **Read:** 2026-11-20, passage; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate search-and-filters E28

### search-and-filters-033 · Best result first, without relevance scores
- **Statement:** Sort search results by relevance with the best first, and do not show relevance scores, which users do not understand.
- **Kind:** practice
- **Use:** check
- **Sources:** NIELSEN-376 (page 278)
- **Read:** 2026-11-20, passage; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate search-and-filters E29

### search-and-filters-034 · Rank results by quality and by the weight of their source
- **Statement:** Rank search results by quality as well as relevance: an FAQ on the searched term tops the list even if other pages score higher. Ratings from users who are asked whether a result page satisfied them can be stored and used to rank future results. On an intranet, results are weighed by the importance of their source, for example with a special icon on official pages in the result list.
- **Kind:** practice
- **Use:** look, check
- **Sources:** NIELSEN-378 (page 278-279), NIELSEN-445 (page 336)
- **Read:** 2026-11-20, page; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate search-and-filters E30

### search-and-filters-035 · Never list the same page twice in the results
- **Statement:** Never list the same page twice in search results, for example under slightly different addresses (with and without a trailing slash or index.html). Merge them into one entry, since duplicates confuse users.
- **Kind:** practice
- **Use:** check
- **Sources:** NIELSEN-377 (page 278)
- **Read:** 2026-11-20, passage; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate search-and-filters E31

### search-and-filters-036 · Show which part of the site each result comes from
- **Statement:** In a structured information space, show with each search result the section it comes from. Users then see which area is most promising and which hits fit (birds as animals or birds as pets) without opening and reading the wrong pages; this holds for children too.
- **Kind:** practice
- **Use:** look, check
- **Sources:** NIELSEN-375 (page 277), NIELSEN-381 (page 281)
- **Read:** 2026-11-20, passage; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate search-and-filters E32

### search-and-filters-037 · Group the results by the site's structure
- **Statement:** Group search results by the site's structure: many hits from one part of the site become one entry, results within a site are grouped by section or category, and the key site areas related to the query are linked. Users then see how the hits relate, the forest rather than only the trees.
- **Kind:** practice
- **Use:** look, check
- **Sources:** NIELSEN-380 (page 281), NIELSEN-386 (page 283-284)
- **Read:** 2026-11-20, page; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate search-and-filters E33

### search-and-filters-038 · Offer "More like this" on a result
- **Statement:** Put a "More like this" link on each search result, and ideally on the destination page too. A user who has found one good item can then find more without inventing new search terms.
- **Kind:** practice
- **Use:** look
- **Sources:** NIELSEN-392 (page 291), NIELSEN-515 (page 391)
- **Read:** 2026-11-20, passage; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate search-and-filters E34

### search-and-filters-039 · Highlight the searched words on the page reached
- **Statement:** A page reached from search results highlights all the query terms, so users can scan to the relevant parts and judge quickly why the page was offered and whether the terms are used in their sense; on long pages this makes the sections of interest easier to find. A light background like a highlighter's makes the terms easy to find.
- **Kind:** practice
- **Use:** look, check
- **Sources:** NIELSEN-391 (page 288), ROBBINS-048 (page 131), NIELSEN-394 (page 295)
- **Read:** 2026-11-20, page; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate search-and-filters E35, joined by search-and-filters E36

### search-and-filters-041 · A list of search results can be bookmarked
- **Statement:** Send a search form with the GET method so that its result, a list of search results, can be bookmarked: the form's contents then travel openly in the page's address. For that reason a form with personal or financial information must not be sent with GET.
- **Kind:** practice
- **Use:** check
- **Sources:** ROBBINS-121 (page 240-241)
- **Asked of the source:** that a form sent with the GET method still puts its contents in the address, so that the result can be bookmarked and the contents can be seen.
- **Current source:** confirmed by https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Sending_and_retrieving_form_data (read 2026-11-20)
- **Read:** 2026-11-20, page; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate search-and-filters E37

### search-and-filters-042 · A long list gets sorting, filters and search
- **Statement:** On a page that holds a lot of data, help people find what they need in three ways: filtering narrows the set to the items that meet chosen criteria, search shows the items that match the words typed, and sorting puts the items in an order such as alphabetical. Stepping through items one at a time is often a sign of poor organisation: for a long list such as 753 films, offer sorting (by rating) and filters, and if an alphabetical list must be used, jump by letter, not by item number.
- **Kind:** practice
- **Use:** look, check
- **Sources:** NIELSEN-328 (page 242), DUCKETT-027 (page 534)
- **Asked of the source:** that filtering, searching and sorting a list inside the page is still a current pattern; DUCKETT-027 describes a client-side technique of 2014.
- **Current source:** confirmed by https://www.nngroup.com/articles/data-tables/ (read 2026-11-20)
- **Read:** 2026-11-20, page; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate search-and-filters E41

### search-and-filters-043 · Arrange a large range so that choosing is easy
- **Statement:** Arrange a large range so that it is easy to choose from. Paints sorted alphabetically are a very poor arrangement; paints grouped by hue on a colour wheel make the choice easier, because people see the real colours, especially when the names say nothing.
- **Kind:** practice
- **Use:** look, check
- **Sources:** THALER-119 (page 93)
- **Read:** 2026-11-20, page; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate search-and-filters E43

### search-and-filters-044 · Put all filters in one place
- **Statement:** Put all filters in one place, in the example a column on the left of a shop's results: once users learn where some filters are, they expect any other filter there too, and grouping features of similar function lowers cognitive load. The shop prototype's left column holds the filter groups Categories (a checkbox list in one column), Colours (two columns, each name with a colour dot), Sizes (checkboxes in two columns) and Price range (a slider with two handles); above the results grid sit a result count ("Showing 1-9 of 48 results") on the left and a switch between grid and list view on the right.
- **Kind:** practice
- **Use:** look, check
- **Sources:** GENTRY-104 (page 133), GENTRY-165 (page 133)
- **Read:** 2026-11-20, image; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate search-and-filters E44

### search-and-filters-045 · Build the filter buttons from the tags the items have
- **Statement:** A gallery can be filtered by tags: each picture carries one or more tags, the filter buttons are made from the tags the pictures actually have, and a click on a button shows only the pictures with that tag.
- **Kind:** practice
- **Use:** look, check
- **Sources:** DUCKETT-030 (page 550)
- **Asked of the source:** that filtering a set of items by tag buttons inside the page is still a current pattern; the finding describes a jQuery technique of 2014.
- **Current source:** confirmed by https://developer.android.com/develop/ui/compose/components/chip (read 2026-11-20)
- **Read:** 2026-11-20, passage; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate search-and-filters E45

### search-and-filters-046 · A tag filter has "show all" and marks the button last pressed
- **Statement:** A tag filter has a "show all" button that is marked active when the page opens. The button last pressed is marked active and the others lose that mark.
- **Kind:** practice
- **Use:** look, check
- **Sources:** DUCKETT-031 (page 554)
- **Asked of the source:** that a "show all" choice and a visible mark on the active filter are still advised for filter controls; the finding describes a jQuery technique of 2014.
- **Current source:** confirmed by https://www.nngroup.com/articles/data-tables/ (read 2026-11-20)
- **Current source:** confirmed by https://design-system.dwp.gov.uk/research/filters/design-notes (read 2026-11-20)
- **Read:** 2026-11-20, page; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate search-and-filters E46

### search-and-filters-047 · Each filter shows how many items it will give
- **Statement:** Each filter button shows the tag's name followed by the number of items that carry it.
- **Kind:** practice
- **Use:** look, check
- **Sources:** DUCKETT-032 (page 554)
- **Asked of the source:** that showing the number of results on each filter choice is still advised; the finding describes a jQuery technique of 2014.
- **Current source:** confirmed by https://www.nngroup.com/articles/applying-filters/ (read 2026-11-20)
- **Read:** 2026-11-20, page; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate search-and-filters E47

### search-and-filters-048 · Narrowing by attributes works without typing and without a mouse
- **Statement:** Search by parameters lets users narrow results by attributes such as a price above a level or a release date, often with sliders and without typing a word. Such sliders must also work without a mouse.
- **Kind:** practice
- **Use:** look, check
- **Sources:** NIELSEN-516 (page 391)
- **Asked of the source:** what a slider must do to be worked from the keyboard and by touch.
- **Current source:** confirmed by https://www.w3.org/WAI/ARIA/apg/patterns/slider/ (read 2026-11-20)
- **Current source:** confirmed by https://www.w3.org/WAI/WCAG22/Understanding/dragging-movements.html (read 2026-11-20)
- **Read:** 2026-11-20, passage; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate search-and-filters E48

### search-and-filters-049 · A range slider updates the list at once
- **Statement:** A price range (in the book, an hourly rate) can be chosen with a range slider that updates the table automatically as the person moves it, with no separate submit step.
- **Kind:** practice
- **Use:** look, check
- **Sources:** DUCKETT-028 (page 544-545, the notes cite 544)
- **Asked of the source:** that a slider with two handles which updates the results while it moves is still a current pattern; the finding describes a jQuery plugin technique of 2014.
- **Current source:** confirmed by https://www.w3.org/WAI/ARIA/apg/patterns/slider-multithumb/ (read 2026-11-20)
- **Conflict:** NN/g (applying-filters, 2016) accepts results that update at once only where they appear within a second, and recommends filters applied with a button on phones
- **Read:** 2026-11-20, page; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate search-and-filters E49

### search-and-filters-050 · A very large range needs search by several attributes and recommendations
- **Statement:** For very large ranges, search by several attributes (for films: actor, director, genre), together with recommendations from people with similar tastes (collaborative filtering), makes choosing easier. Do not rely on similar tastes alone, or people lose the chance of a happy find.
- **Kind:** practice
- **Use:** look
- **Sources:** THALER-121 (page 93)
- **Read:** 2026-11-20, page; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate search-and-filters E50

### search-and-filters-051 · Sort each column by what its values mean
- **Statement:** Each column of a sortable table holds one kind of data (text, a length in minutes and seconds such as 11:40, a date), and each kind needs its own comparison rule. Dates written as text are turned into real dates before sorting, so that they can be compared.
- **Kind:** practice
- **Use:** check
- **Sources:** DUCKETT-036 (page 565), DUCKETT-038 (page 566-567, the notes cite 566)
- **Asked of the source:** that sorting a table inside the page still needs a comparison rule for each kind of data; the findings describe a JavaScript technique of 2014.
- **Current source:** confirmed by https://developer.chrome.com/docs/modern-web-guidance/guides/ui-behaviors/sortable-table (read 2026-11-20)
- **Read:** 2026-11-20, page; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate search-and-filters E51

### search-and-filters-052 · Ignore a leading "The" when sorting names
- **Statement:** When names are sorted alphabetically, a leading "The" (as in band or film titles) is ignored.
- **Kind:** practice
- **Use:** check
- **Sources:** DUCKETT-039 (page 569)
- **Needs source:** that leaving out a leading article is still the advised way to sort titles alphabetically; the finding describes a technique of 2014.
- **Current source:** none found (searched 2026-11-20)
- **Read:** 2026-11-20, page; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate search-and-filters E52

### search-and-filters-053 · A click on a column heading sorts, a second click reverses
- **Statement:** In a sortable table, a click on a column heading sorts the rows by that column in rising order, and a second click on the same heading sorts it in falling order.
- **Kind:** practice
- **Use:** look, check
- **Sources:** DUCKETT-037 (page 566)
- **Asked of the source:** that sorting by a click on the column heading, with a second click to reverse, is still the expected behaviour of a sortable table; the finding describes a jQuery technique of 2014.
- **Current source:** confirmed by https://developer.chrome.com/docs/modern-web-guidance/guides/ui-behaviors/sortable-table (read 2026-11-20)
- **Read:** 2026-11-20, passage; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate search-and-filters E53

### search-and-filters-054 · A sortable table marks the sorted column's heading as rising or falling
- **Statement:** In a sortable table, the heading of the column the table is sorted by is marked as rising or falling, and that mark is taken off every other heading.
- **Kind:** practice
- **Use:** look, check
- **Sources:** DUCKETT-040 (page 570)
- **Asked of the source:** how a sortable table should show the sorted column and its direction today, to people who see the page and to people who use a screen reader.
- **Current source:** confirmed by https://www.w3.org/WAI/ARIA/apg/patterns/table/examples/sortable-table/ (read 2026-11-20)
- **Current source:** confirmed by https://developer.chrome.com/docs/modern-web-guidance/guides/ui-behaviors/sortable-table (read 2026-11-20)
- **Read:** 2026-11-20, page; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate search-and-filters E54

### search-and-filters-055 · Offer a table for comparing products
- **Statement:** Users often ask for easy ways to compare products. Because each product sits on its own page, a comparison table cuts the movement from page to page and lets users narrow down to the one or two products they care about.
- **Kind:** practice
- **Use:** look
- **Sources:** NIELSEN-349 (page 260)
- **Read:** 2026-11-20, passage; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate search-and-filters E56

### search-and-filters-056 · A comparison highlights the differences and shows the facts that decide the choice
- **Statement:** A dynamic comparison table highlights the differences that matter for the decision, not the features that all the compared items share. A comparison tool's result page shows the facts that decide the choice: one tool showed the three cheapest plans but not restrictions such as prior approval or quantity limits, which were probably available only after signing up.
- **Kind:** practice
- **Use:** look, check
- **Sources:** NIELSEN-350 (page 262), THALER-181 (page 155)
- **Read:** 2026-11-20, passage; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate search-and-filters E57, joined by content E126

### search-and-filters-057 · With many options people cut by attributes, then compare the finalists
- **Statement:** Faced with thousands of homes to rent, people use "elimination by aspects" (Amos Tversky's name for it): they pick the most important attribute (commute time), set a cut-off, drop everything outside it, repeat with price, bedrooms and pets, then weigh the few finalists against each other in full. The more options and attributes there are, the more people turn to such simplifying strategies.
- **Kind:** practice
- **Use:** look, check
- **Sources:** THALER-116 (page 92)
- **Read:** 2026-11-20, page; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate search-and-filters E58

### search-and-filters-058 · A hard cut-off drops options that are excellent otherwise
- **Statement:** Hard cut-offs throw out options that are excellent in every other way: a flat 35 minutes from work is dropped under a 30-minute rule even if it has a superb view and is 200 dollars a month cheaper.
- **Kind:** practice
- **Use:** look
- **Sources:** THALER-117 (page 92)
- **Read:** 2026-11-20, passage; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate search-and-filters E59

### search-and-filters-059 · Stated must-haves are a poor guide to what people choose
- **Statement:** Home buyers' "must have" lists are a poor guide to what they will choose: an estate agent's experience is that buyers fall in love with houses that miss many of their own stated criteria.
- **Kind:** practice
- **Use:** look
- **Sources:** NEURO-037 (page 68)
- **Read:** 2026-11-20, passage; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate search-and-filters E60

### search-and-filters-060 · Find the words people will search with
- **Statement:** Build the list of search words by putting yourself in the place of the people who badly need the site, imagining as many different, even unlikely, ways of searching as possible instead of one average visitor. Padding with the most popular search terms raises traffic but brings hardly any more of the visitors who want what the site offers.
- **Kind:** practice
- **Use:** text
- **Sources:** KIRSANOV-032 (page 16), KIRSANOV-031 (page 16)
- **Also in (not read):** KIRSANOV-026
- **Read:** 2026-11-20, passage; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate content E34

### search-and-filters-061 · Pages reached only through a form stay hidden from search robots
- **Statement:** Pages produced only in answer to what a visitor types into a form, search results included, cannot be reached by search robots, which do not know what to type.
- **Kind:** practice
- **Use:** check
- **Sources:** KIRSANOV-027 (page 15)
- **Asked of the source:** whether today's search crawlers still cannot reach pages that exist only as answers to a form.
- **Current source:** confirmed by https://developers.google.com/search/docs/crawling-indexing/javascript/lazy-loading (read 2026-11-20)
- **Read:** 2026-11-20, passage; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate content E35

### search-and-filters-062 · Help can be searched
- **Statement:** Online help must be searchable, because users go to it only when stuck with a specific problem.
- **Kind:** practice
- **Use:** check
- **Sources:** NIELSEN-205 (page 162)
- **Read:** 2026-11-20, passage; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate content E156

### search-and-filters-065 · Sort numbers as numbers, not as text
- **Statement:** A plain sort puts items in dictionary order, letter by letter, so numbers come out wrong (1, 125, 14, 156, 19, 2). Any sort of prices or other numbers must compare them as numbers.
- **Kind:** practice
- **Use:** check
- **Sources:** DUCKETT-035 (page 560)
- **Asked of the source:** that the default sort in JavaScript still orders values as text (MDN, Array sort).
- **Current source:** confirmed by https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort (read 2026-11-20)
- **Read:** 2026-11-20, page; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate testing E80
