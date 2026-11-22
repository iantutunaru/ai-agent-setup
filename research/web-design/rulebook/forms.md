# Web design rulebook: forms

97 entries: 3 rule, 94 practice. Built by a script from the owner's reading notes, which are not published; not edited by hand. How to read an entry: [README.md](README.md).

### forms-001 · Ask only for what the task needs
- **Statement:** Ask only for the information the task needs and leave out every question that does not serve it. Extra questions slow people down, and people are sceptical of requests for more: they wonder why they are being asked and grow wary or annoyed.
- **Kind:** practice
- **Use:** look, check
- **Sources:** KRUG-153 (page s116), ROBBINS-158 (page 271)
- **Also in (not read):** ROBBINS-325
- **Read:** 2026-11-20, page; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate forms E01

### forms-002 · Do not ask for what is already known or can be worked out
- **Statement:** Do not ask for information that can be obtained another way, and fill in what is already known. The card type can be worked out from the first four digits of the card number; a tax return completed in advance, which the person only signs and sends, is estimated to save up to 225 million hours of preparation a year. In Norway a change to the pre-filled return can be sent by text message.
- **Kind:** practice
- **Use:** look, check
- **Sources:** THALER-216 (page 196-197), ROBBINS-159 (page 271)
- **Read:** 2026-11-20, page; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate forms E02

### forms-003 · Give the information first and ask for details afterwards
- **Statement:** Let visitors reach useful content before asking them to fill in a form. Visitors who could read content straight away and were asked for details later were twice as likely to complete the form as visitors who met the form first. Fear of losing privacy stops people filling in forms, and asked for personal details unexpectedly they may give false data (a made-up birthday); giving useful information first reduces that fear.
- **Kind:** rule
- **Use:** look, check
- **Sources:** NEURO-025 (page 52), NEURO-082 (page 123)
- **Study (as the book reports it):** NEURO-025: Gamberini et al., 2007, information site on media file formats, form before access versus form after access.
- **Current source:** confirmed by https://link.springer.com/chapter/10.1007/978-3-540-77006-0_24 (read 2026-11-20)
- **Conflict:** the study's own abstract (Springer) adds that social proof features, such as a visits counter, seemed counterproductive when the form came after access, and helped when it came before
- **Read:** 2026-11-20, page; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate forms E03

### forms-004 · Do not put registration in front of the pages others link to
- **Statement:** Requiring a subscription or even registration drives away new users who arrive by links and cuts the number of sites linking to you. If it is needed, keep some freely accessible pages with fixed addresses that bypass the login, describe the service and are easy for others to link to.
- **Kind:** practice
- **Use:** look, check
- **Sources:** NIELSEN-098 (page 96)
- **Read:** 2026-11-20, page; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate forms E04

### forms-005 · Split a long form into stages and let people save it unfinished
- **Statement:** Split a long form into stages and let visitors save an unfinished submission and come back to it. The checks for the whole form must not block the save; the full checks run only at the final submit.
- **Kind:** practice
- **Use:** look, check
- **Sources:** LAWSON-052 (page 103-104)
- **Read:** 2026-11-20, page; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate forms E08

### forms-006 · Order the options the way the person thinks through the task
- **Statement:** Order the options of a configurator or form the way the user thinks through the task: the main choices first at the top, finer details further down. In the example the main choices are written as one sentence across the top, each choice an inline value, and the results below are shown as large figures with small labels, not as further form fields.
- **Kind:** practice
- **Use:** look
- **Sources:** GENTRY-078 (page 101), GENTRY-150 (page 101)
- **Read:** 2026-11-20, image; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate forms E11

### forms-007 · Ask one easy question first, then show only what fits the answer
- **Statement:** Instead of showing every option and detail at once, ask one easy first question (log in, or see subscription options) and then show only the questions and information relevant to that answer.
- **Kind:** practice
- **Use:** look
- **Sources:** KRUG-045 (page s35)
- **Also in (not read):** KRUG-204
- **Read:** 2026-11-20, passage; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate forms E13

### forms-009 · Show a follow-up field only when the answer calls for it
- **Statement:** When an answer makes a new field necessary (the details box when "Other" is picked, a parent's consent when the date of birth shows the person is under 13), show it at once and move the cursor to it. When a changed answer makes it unnecessary again, hide it and clear what was in it, so it is empty if it is shown again. Such a field is checked only while it is shown.
- **Kind:** practice
- **Use:** look, check
- **Sources:** DUCKETT-071 (page 624), DUCKETT-047 (page 588), DUCKETT-069 (page 623)
- **Read:** 2026-11-20, page; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate forms E15

### forms-010 · Disable the parts of a form an earlier answer rules out
- **Statement:** Disabling fields is a way to restrict parts of a form depending on what the user entered earlier; browsers show disabled controls greyed out by default.
- **Kind:** practice
- **Use:** look, check
- **Sources:** ROBBINS-129 (page 246)
- **Asked of the source:** that browsers still show a disabled control greyed out and keep it out of use
- **Current source:** confirmed by https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/disabled (read 2026-11-20)
- **Read:** 2026-11-20, passage; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate forms E16

### forms-011 · A drop-down that depends on another offers only what fits
- **Statement:** When one drop-down depends on another (type, then model), fill the second with only the options that fit the first choice, and until the first is made, let the second say plainly that the first must be chosen.
- **Kind:** practice
- **Use:** look, check
- **Sources:** DUCKETT-050 (page 592)
- **Read:** 2026-11-20, passage; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate forms E17

### forms-012 · An "any" box ticks and clears a whole group of tick boxes
- **Statement:** In a group of tick boxes, offer one "any" box that ticks or clears all the options at once. When the person then clears a single option, the "any" box clears itself, since not everything is chosen any more.
- **Kind:** practice
- **Use:** look, check
- **Sources:** DUCKETT-046 (page 586)
- **Read:** 2026-11-20, passage; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate forms E18

### forms-013 · Put labels above their fields
- **Statement:** Where labels sit relative to fields affects how long a form takes to fill in. Labels placed above their fields form one alignment line that lets users scan and complete the form faster, especially for familiar information such as name and address, and they can be of any length, which suits narrow screens; the cost is a longer form. The author says research shows forms are easier and faster to use when labels and fields are laid out properly, but names no study.
- **Kind:** practice
- **Use:** look, check
- **Sources:** ROBBINS-161 (page 271), ROBBINS-213 (page 653)
- **Read:** 2026-11-20, passage; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate forms E19

### forms-014 · Labels above their fields on a narrow screen
- **Statement:** Make forms responsive: on wide screens labels and fields sit side by side, the labels at one fixed width and the fields growing to fill the free space; on a narrow screen, where both do not fit side by side, the labels sit above their fields.
- **Kind:** practice
- **Use:** look, check
- **Sources:** ROBBINS-221 (page 656-657, the notes cite 656)
- **Read:** 2026-11-20, page; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate phone E40

### forms-015 · Put labels to the left when height is short or people should slow down
- **Statement:** Put labels to the left of their fields when vertical space is short. Left-aligned labels slow completion down, which can be useful when users should slow down, read and consider what information is wanted.
- **Kind:** practice
- **Use:** look
- **Sources:** ROBBINS-162 (page 271-272)
- **Read:** 2026-11-20, page; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate forms E20

### forms-016 · No labels inside fields, with one narrow exception
- **Statement:** Do not put labels inside form fields unless all of these hold: the form is very simple, the label disappears on typing and returns if the field is emptied, it cannot be mistaken for an answer or sent with the input, and it is fully accessible.
- **Kind:** practice
- **Use:** look, check
- **Sources:** KRUG-185 (page s132)
- **Read:** 2026-11-20, passage; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate forms E21

### forms-017 · Every field says what it expects
- **Statement:** Every field tells the user what kind of data it expects, through its label and, where needed, a short line of help text, such as the password rule (at least 6 characters, no spaces) under the password field's label.
- **Kind:** practice
- **Use:** check, text
- **Sources:** GOLDSTEIN-002 (page 91-92, the notes cite 92)
- **Read:** 2026-11-20, page; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate forms E22

### forms-018 · A field looks typeable and a button looks pressable
- **Statement:** Affordances must be visible: a border around a text field is what shows it can be typed in, and a raised look shows a button can be pressed. They need not be loud, but users must be able to notice the ones their tasks need. A row of four "Report" buttons shows the scale from strong to weak: a rounded orange button with a gradient and a glow, a flat orange rounded button with a thin outline, a white box with a black border, and the bare word with no box at all.
- **Kind:** practice
- **Use:** look, check
- **Sources:** KRUG-137 (page s101), KRUG-224 (page s101)
- **Read:** 2026-11-20, image; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate forms E26

### forms-019 · The main action dominates and secondary actions look lesser
- **Statement:** The primary action at the end of a form (Buy, Register) dominates visually and is easy to find, ideally aligned with the form's main axis. Secondary actions, which usually take a step back (clearing or resetting the form), are styled differently and look less important; also consider offering a way to undo.
- **Kind:** practice
- **Use:** look, check
- **Sources:** ROBBINS-165 (page 272), ROBBINS-167 (page 272)
- **Also in (not read):** ROBBINS-135
- **Read:** 2026-11-20, passage; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate forms E27

### forms-020 · Leave out the reset button unless people will want it
- **Statement:** Before putting a reset button on a form, ask whether users will ever want to throw away everything they have entered; include one only if they will. Reset buttons are used much less than before, because feedback while typing and well-designed forms leave few users needing one; a reset returns fields to their initial values and does not empty them.
- **Kind:** practice
- **Use:** look, check
- **Sources:** GOLDSTEIN-008 (page 101), ROBBINS-136 (page 250)
- **Read:** 2026-11-20, page; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate forms E28

### forms-021 · A short form sits on one line
- **Statement:** For a short form (a search box, a newsletter sign-up), put the label, the text field and the button on one line, also on phone screens with enough width, and let the text field take whatever width is left between label and button, so it fits any box width and any user text size. Even when the button wraps in portrait, the form uses the space better.
- **Kind:** practice
- **Use:** look, check
- **Sources:** GILLENWATER-087 (page 250-251, the notes cite 251), GILLENWATER-099 (page 289)
- **Read:** 2026-11-20, page; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate forms E29

### forms-022 · Style the form to fit the site
- **Statement:** Default form rendering looks far below professional forms, so style it: even simple alignment and making the form consistent with the rest of the site greatly improve the impression on users.
- **Kind:** practice
- **Use:** look, check
- **Sources:** ROBBINS-168 (page 272)
- **Conflict:** LAWSON-049 (in forms-023) says to keep form controls as close to the browser's default look as possible, even against branding wishes.
- **Read:** 2026-11-20, passage; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate forms E33

### forms-023 · Keep form controls close to the browser's default look
- **Statement:** Keep form controls as close to the browser's default look as possible, even against branding wishes: a date picker or slider that looks and behaves the same on every site is easier for people to understand, and native controls are more likely to work with assistive technology than ones faked with a script. Radio buttons and checkboxes are best left unstyled apart from a colour tint (the accent-color property keeps their native look), and the options inside a select menu are probably best left to the browser and the operating system.
- **Kind:** practice
- **Use:** look, check
- **Sources:** LAWSON-049 (page 100), ROBBINS-216 (page 655), ROBBINS-217 (page 655)
- **Asked of the source:** whether radio buttons, checkboxes and select options can now be styled without harm, and whether native controls still work better with assistive technology than ones faked with a script
- **Current source:** confirmed by https://www.w3.org/TR/using-aria/ (read 2026-11-20)
- **Current source:** confirmed by https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Advanced_form_styling (read 2026-11-20)
- **Conflict:** ROBBINS-168 (in forms-022) says default form rendering looks far below professional forms and should be styled.
- **Read:** 2026-11-20, page; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate forms E34

### forms-025 · Test a styled form in different browsers
- **Statement:** Form controls are drawn by the browser following the operating system's conventions, though their size, spacing, fonts, colours, borders and backgrounds can be styled; test the styled form in different browsers to avoid unpleasant surprises. Restyled fieldsets and legends need thorough testing: browsers treat fieldset backgrounds differently and legend text does not wrap.
- **Kind:** practice
- **Use:** check
- **Sources:** ROBBINS-169 (page 272-273), ROBBINS-153 (page 268)
- **Needs source:** whether fieldset backgrounds and the wrapping of legend text still differ between current browsers (MDN says legend placement is tricky and nothing of either)
- **Current source:** confirmed by https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Styling_web_forms (read 2026-11-20)
- **Read:** 2026-11-20, passage; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate testing E108

### forms-026 · Use the control made for the purpose
- **Statement:** Always use the form control made for the purpose; turning ordinary page elements into editable areas is a fallback for needs no control meets, such as inline rich-text editing. Custom form widgets make it very easy to create an interaction that is awkward even for sighted users, so build them with care or use a ready-made widget from an established library.
- **Kind:** practice
- **Use:** look, check
- **Sources:** GOLDSTEIN-029 (page 122-123), ROBBINS-156 (page 270)
- **Read:** 2026-11-20, passage; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate forms E36

### forms-027 · Radio buttons for one choice, tick boxes for any number
- **Statement:** Use radio buttons when only one option of a group may be chosen because the choices exclude each other (yes or no, pick-up or delivery), and checkboxes when the user may pick any number of options, from one to all. A single checkbox on its own can serve as an opt-in, for example to receive news and promotions by email.
- **Kind:** practice
- **Use:** look, check
- **Sources:** ROBBINS-138 (page 254-255, the notes cite 254), ROBBINS-139 (page 256)
- **Read:** 2026-11-20, page; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate forms E38

### forms-028 · A menu takes less room than a group of buttons or boxes
- **Statement:** A drop-down or scrolling menu is usually more compact than a group of radio buttons or checkboxes for presenting a list of options; a drop-down allows only one choice.
- **Kind:** practice
- **Use:** look
- **Sources:** ROBBINS-140 (page 257)
- **Read:** 2026-11-20, page; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate forms E39

### forms-029 · Choose each control with care and test the choice with users
- **Statement:** Choose each input type with care (for example a drop-down menu or a set of checkboxes for a list of options), weigh the pros and cons of each control, and test the choice with users.
- **Kind:** practice
- **Use:** look, check
- **Sources:** ROBBINS-163 (page 272)
- **Read:** 2026-11-20, passage; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate testing E109

### forms-030 · Divide a menu's options into headed groups
- **Statement:** A menu's options can be divided into conceptual groups, each with its own heading.
- **Kind:** practice
- **Use:** look, check
- **Sources:** ROBBINS-141 (page 258)
- **Read:** 2026-11-20, passage; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate forms E40

### forms-031 · Drop-down lists with several picks are seldom used
- **Statement:** Drop-down lists that allow several picks at once are seldom used, because they give a poor experience.
- **Kind:** practice
- **Use:** look, check
- **Sources:** DUCKETT-049 (page 590)
- **Read:** 2026-11-20, passage; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate forms E41

### forms-032 · A text field with suggestions that also takes the user's own value
- **Statement:** A text field with a list of suggested options, unlike a closed drop-down list, lets users pick one of the suggestions or type a value of their own. The suggestions can also be refreshed as the user types, in the manner of search suggestions.
- **Kind:** practice
- **Use:** look, check
- **Sources:** GOLDSTEIN-013 (page 106), LAWSON-034 (page 91)
- **Also in (not read):** ROBBINS-134
- **Needs source:** whether Safari and the phone browsers show a datalist's suggestions and let a long list scroll (MDN marks datalist not Baseline, and its options do not zoom)
- **Current source:** confirmed by https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/datalist (read 2026-11-20)
- **Read:** 2026-11-20, page; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate forms E42

### forms-033 · A field accepts loose typing and offers matching choices
- **Statement:** A field that accepts what the user types and offers sensible matching choices (a flight search that suggests airports) removes guesswork and errors, compared with one that demands an exact format and then reports a puzzling error. In the better of two flight search forms the suggestion list opens from the first letters, each line gives the code, the full name and the city with the typed letters in bold, the loose "ny" is accepted, and after a pick the field keeps both the code and the name.
- **Kind:** practice
- **Use:** look, check
- **Sources:** KRUG-009 (page s19), KRUG-194 (page s19)
- **Read:** 2026-11-20, image; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate forms E43

### forms-034 · Give each field the input type that fits what it asks for
- **Statement:** Give each field the type that matches what it asks for (number, e-mail, web address, phone), so the browser itself checks the entry where the type has a format and warns the person when it does not fit; a phone field is not checked, since phone formats vary. A browser that does not know a type shows an ordinary text field, so nothing breaks.
- **Kind:** practice
- **Use:** check
- **Sources:** DUCKETT-053 (page 596), LAWSON-026 (page 85-87, the notes cite 85-86)
- **Also in (not read):** GOLDSTEIN-015, ROBBINS-133
- **Asked of the source:** which of these field types current browsers support and check, and that an unknown type still falls back to a text field.
- **Current source:** confirmed by https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/HTML5_input_types (read 2026-11-20)
- **Current source:** confirmed by https://html.spec.whatwg.org/multipage/input.html (read 2026-11-20)
- **Read:** 2026-11-20, page; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate forms E45

### forms-035 · Give each field its type so the phone shows the fitting keyboard
- **Statement:** Mark a field with its specific type (email, phone number, web address, search): the phone then shows the keyboard best suited to the entry, such as one with the @ sign and period for an email address, a Search key or a ".com" key, often with a clear-field button, and the browser warns when, for example, an email address is not in the expected format. A site's search box marked as a search field may also look like the search boxes people know from their system, which shows them where to go to search.
- **Kind:** practice
- **Use:** check
- **Sources:** ROBBINS-131 (page 247-248, the notes cite 248), GOLDSTEIN-017 (page 111), GOLDSTEIN-016 (page 110)
- **Also in (not read):** DUCKETT-055, LAWSON-048
- **Asked of the source:** that current phone browsers show a fitting keyboard for email, telephone, number, web address and search fields and check the format of an email address.
- **Current source:** confirmed by https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/HTML5_input_types (read 2026-11-20)
- **Current source:** confirmed by https://html.spec.whatwg.org/multipage/input.html (read 2026-11-20)
- **Current source:** confirmed by https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/enterkeyhint (read 2026-11-20)
- **Read:** 2026-11-20, page; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate phone E37, joined by search-and-filters E10

### forms-036 · A number field only for plain quantities
- **Statement:** Do not use a number field (with up and down arrows) for a required field whose values have a wide range or may contain letters or symbols, such as street numbers like 36B or account numbers with dashes; where the pattern of the number is known, give the field that pattern. For an optional field a number field may still do, or a telephone field to bring up the number keypad on touch screens.
- **Kind:** practice
- **Use:** check
- **Sources:** GOLDSTEIN-022 (page 114)
- **Asked of the source:** that a telephone field brings up the number keypad on current phones, and what current guidance says on when a number field fits.
- **Current source:** confirmed by https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/number (read 2026-11-20)
- **Conflict:** the GOV.UK design system (government, from its research) advises against the number type unless research shows a need, and uses a text field with inputmode numeric for whole numbers
- **Read:** 2026-11-20, passage; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate forms E46

### forms-037 · Use the telephone keypad for phone numbers
- **Statement:** Use the telephone field type for phone numbers, so that touch devices usually show the phone keypad.
- **Kind:** practice
- **Use:** check
- **Sources:** GOLDSTEIN-021 (page 113)
- **Asked of the source:** that current guidance still recommends the telephone field type for number codes other than phone numbers.
- **Current source:** confirmed by https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/HTML5_input_types (read 2026-11-20)
- **Current source:** overturned by https://web.dev/articles/sms-otp-form (read 2026-11-20)
- **Conflict:** for other number codes MDN's guide still suggests the telephone type wherever a number keypad helps, while web.dev calls it a semantically incorrect hack now that inputmode numeric is widely supported; the GOV.UK design system uses inputmode numeric
- **Read:** 2026-11-20, passage; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate phone E38

### forms-038 · A number with known limits carries its lowest, its highest and its step
- **Statement:** For a number with known limits, set the minimum, the maximum and the step, so the control cannot go beyond the range and moves in sensible increments, while the user can still type a value. Only evenly stepped values are then possible, not an arbitrary list of allowed values; the mobile browsers of the book's time (iOS Safari, Android, Chrome for Android) did not honour the limits.
- **Kind:** practice
- **Use:** check
- **Sources:** LAWSON-031 (page 89), ROBBINS-145 (page 263-264)
- **Needs source:** whether current phone browsers honour a number field's minimum, maximum and step (MDN's page text does not say)
- **Current source:** confirmed by https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/number (read 2026-11-20)
- **Read:** 2026-11-20, page; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate forms E47

### forms-039 · A slider where the exact number does not matter
- **Statement:** A slider suits a value where the exact number does not matter, such as a customer satisfaction rating; where the exact number matters, use a number field.
- **Kind:** practice
- **Use:** look, check
- **Sources:** GOLDSTEIN-023 (page 114-115)
- **Read:** 2026-11-20, page; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate forms E48

### forms-040 · A slider shows its range and its current value
- **Statement:** Show the user the allowed range of a slider (its minimum and maximum) and echo its current value next to it as it moves.
- **Kind:** practice
- **Use:** look, check
- **Sources:** LAWSON-044 (page 97)
- **Read:** 2026-11-20, page; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate forms E49

### forms-041 · Use the browser's own date field
- **Statement:** Typed dates are error-prone because people cannot tell which order the site expects (day-month-year or month-day-year), and home-made script date pickers vary widely in looks, usability and accessibility from site to site; a native date field lets the browser show its own calendar. A home-made list of twelve fixed English month names does not adapt to the visitor's language, whereas a native month field lets the browser offer month names in the user's own language.
- **Kind:** practice
- **Use:** look, check
- **Sources:** LAWSON-029 (page 87), LAWSON-030 (page 88)
- **Also in (not read):** ROBBINS-144
- **Asked of the source:** that current browsers show a calendar for a date field and month names in the user's language.
- **Current source:** confirmed by https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/date (read 2026-11-20)
- **Conflict:** MDN's page on the month field says many major browsers do not yet support it
- **Read:** 2026-11-20, passage; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate forms E50

### forms-043 · Tie every field to its label
- **Statement:** Tie each field's descriptive text to its field as a label, so the form works with screen readers: a label that sits next to the field on screen may be far from it in the code, and the tie gives users of speech browsers the context they need. Each label belongs to exactly one control, so radio buttons and checkboxes are labelled one by one.
- **Kind:** practice
- **Use:** check
- **Sources:** KRUG-172 (page s126), ROBBINS-148 (page 266), ROBBINS-150 (page 267)
- **Read:** 2026-11-20, page; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate accessibility E38

### forms-044 · A date field offers only dates that make sense
- **Statement:** Give a date field a minimum and a maximum date, set on the server where they depend on today, so users can pick only dates that make sense for the form: from tomorrow to about three months ahead for a subscription start, a minimum of today for a flight booking so only future dates can be chosen, a maximum of today for a date of birth.
- **Kind:** practice
- **Use:** check
- **Sources:** GOLDSTEIN-024 (page 119-120), LAWSON-042 (page 95)
- **Read:** 2026-11-20, page; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate forms E52

### forms-047 · Do not make users format data the site's way
- **Statement:** Never make users format data the site's way (dashes in an identity number, spaces in a card number, brackets in a phone number); write the little code it takes to accept what they type. Spaces in card numbers in fact make them easier to type correctly. Phone numbers have no single standard format: valid numbers differ in length and punctuation around the world and some use letters; a wanted format can be encouraged with a placeholder showing it or an example after the field.
- **Kind:** practice
- **Use:** check
- **Sources:** KRUG-152 (page s116), GOLDSTEIN-020 (page 113)
- **Also in (not read):** LAWSON-033
- **Conflict:** GOLDSTEIN-009, LAWSON-039 (in forms-048) accept fields that take only a set format, provided the format is stated.
- **Read:** 2026-11-20, passage; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate forms E55

### forms-048 · When only one format is accepted, state it in plain words
- **Statement:** When a field accepts only a set format (a part number, a specific kind of web address), always tell the user what that format is, in a full readable sentence shown as visible text near the field, not only in its title text; a short example of a valid value can be added as a hint.
- **Kind:** practice
- **Use:** check, text
- **Sources:** GOLDSTEIN-009 (page 102), LAWSON-039 (page 93), GOLDSTEIN-019 (page 112-113)
- **Asked of the source:** whether the field's title text, which both books use to carry that sentence, is shown by current browsers with their error message and reaches all users.
- **Current source:** confirmed by https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/pattern (read 2026-11-20)
- **Conflict:** KRUG-152 (in forms-047) says never to make users format data the site's way.
- **Read:** 2026-11-20, page; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate forms E56

### forms-049 · Nothing depends on upper or lower case
- **Statement:** Nothing in a user interface should depend on upper or lower case where it can be avoided: the upper and lower forms of a letter are nearly the same, so users confuse them and case-sensitivity causes many errors.
- **Kind:** practice
- **Use:** check
- **Sources:** NIELSEN-403 (page 299)
- **Read:** 2026-11-20, passage; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate forms E58

### forms-050 · Placeholder text is a short hint and never the only instruction
- **Statement:** Placeholder text inside a field is for a short hint only, such as an example web address. It must not be the only place the field's requirements are stated, because it disappears once the user types; longer advice belongs in the label or beside the field.
- **Kind:** practice
- **Use:** check, text
- **Sources:** GOLDSTEIN-005 (page 98), LAWSON-036 (page 92)
- **Also in (not read):** DUCKETT-059
- **Read:** 2026-11-20, page; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate forms E59

### forms-051 · Placeholder text can include "e.g."
- **Statement:** Some developers suggest adding "e.g." to placeholder text so it is clearly an example and not a value already filled in for the user.
- **Kind:** practice
- **Use:** check, text
- **Sources:** GOLDSTEIN-006 (page 98)
- **Read:** 2026-11-20, passage; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate forms E60

### forms-052 · A hint goes in the placeholder, not in the field's value
- **Statement:** Text pre-filled into a field or a multi-line box as its value is sent with the form unless the user changes it; placeholder text is only a hint about what to type and is never sent. Developers often leave a multi-line box empty and give a placeholder hint such as "50 words or less" instead.
- **Kind:** practice
- **Use:** check
- **Sources:** ROBBINS-125 (page 245), ROBBINS-127 (page 245-246)
- **Read:** 2026-11-20, page; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate forms E61

### forms-053 · A value to see but not change is read-only and looks it
- **Statement:** For a value the user should see and send but not change (such as the article being commented on), use a read-only field and not a disabled one: a disabled field is greyed out, cannot be focused and is not sent with the form. Read-only fields must look visibly different from editable ones, otherwise users who try to change them will be confused.
- **Kind:** practice
- **Use:** look, check
- **Sources:** GOLDSTEIN-011 (page 104), ROBBINS-128 (page 246)
- **Read:** 2026-11-20, page; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate forms E62

### forms-054 · What a form hides on screen is not protected
- **Statement:** Masking a password field only hides the characters from people looking over the user's shoulder; the form encrypts nothing, so masking is not a security measure. Hidden form fields are not secret either: users can reach them and change them, and the site has to guard against that.
- **Kind:** practice
- **Use:** check
- **Sources:** ROBBINS-130 (page 247), ROBBINS-143 (page 261)
- **Asked of the source:** that a masked password field and a hidden field still give no protection of their own in current browsers.
- **Current source:** confirmed by https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/hidden (read 2026-11-20)
- **Current source:** confirmed by https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/password (read 2026-11-20)
- **Read:** 2026-11-20, passage; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate trust E37

### forms-055 · A worked-out value is shown as a result, not as a field
- **Statement:** A value the user can see but not set directly, because it is worked out from other fields (such as a cart total after shipping and taxes), is shown as an output and not as an input field.
- **Kind:** practice
- **Use:** look, check
- **Sources:** GOLDSTEIN-028 (page 122)
- **Read:** 2026-11-20, passage; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate forms E63

### forms-056 · Limit a field's length only when the processing needs it
- **Statement:** Limit the number of characters a text field accepts only when the program that processes the form requires it; by default users can type any length.
- **Kind:** practice
- **Use:** check
- **Sources:** ROBBINS-126 (page 245)
- **Read:** 2026-11-20, passage; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate forms E64

### forms-057 · Serve every form with text fields over HTTPS
- **Statement:** Any form with text fields should be served over HTTPS, so that what users type is protected on its way to the server.
- **Kind:** practice
- **Use:** check
- **Sources:** ROBBINS-123 (page 243)
- **Asked of the source:** that current guidance asks for HTTPS on every page with a form, and what browsers show the user when a form is not served over it.
- **Current source:** confirmed by https://web.dev/articles/why-https-matters (read 2026-11-20)
- **Current source:** confirmed by https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/password (read 2026-11-20)
- **Read:** 2026-11-20, page; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate trust E36

### forms-058 · A length limit shows a live count of what is left
- **Statement:** For a text box with a length limit, show a live count of the characters left while the person is typing in it, and hide the count when they leave the box within the limit. The count changes its look as the limit nears: a normal style while plenty is left, a warning style in the last 15 characters and an error style once the text runs over; an over-long text keeps its count visible after the person leaves the box.
- **Kind:** practice
- **Use:** look, check
- **Sources:** DUCKETT-051 (page 594), DUCKETT-052 (page 594)
- **Read:** 2026-11-20, page; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate forms E65

### forms-059 · The cursor starts in a field only on a page that is about that field
- **Statement:** Put the cursor into a field automatically on page load only on pages whose central purpose is that field, such as a search page, and on at most one field per page; done carelessly it hurts usability.
- **Kind:** practice
- **Use:** check
- **Sources:** LAWSON-035 (page 92)
- **Read:** 2026-11-20, passage; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate forms E66

### forms-060 · The browser's memory of earlier entries stays on, except for answers never reused
- **Statement:** Leave browser autocomplete on by default, and switch it off only for data that is never reused, such as a CAPTCHA answer, which the user must then type each time.
- **Kind:** practice
- **Use:** check
- **Sources:** GOLDSTEIN-012 (page 105), LAWSON-041 (page 95)
- **Also in (not read):** DUCKETT-054
- **Asked of the source:** what current browser and payment-form guidance says on autocomplete for card numbers and one-time codes.
- **Current source:** overturned by https://web.dev/articles/payment-and-address-form-best-practices (read 2026-11-20)
- **Current source:** overturned by https://web.dev/articles/sms-otp-form (read 2026-11-20)
- **Conflict:** web.dev today asks for autocomplete values on card fields (number, name, expiry, security code) so the browser can fill them, and autocomplete one-time-code so the system can offer the code from an SMS; the book switched autocomplete off for both
- **Read:** 2026-11-20, passage; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate forms E67

### forms-061 · A password field can offer "show password"
- **Statement:** A password field can have a "show password" checkbox under it; when it is ticked, the password is shown as plain text.
- **Kind:** practice
- **Use:** look, check
- **Sources:** DUCKETT-043 (page 582)
- **Read:** 2026-11-20, page; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate forms E68

### forms-062 · Hidden password characters hide typing slips
- **Statement:** In a study of 48 home internet households in Pittsburgh (133 people), people could not log in because Caps Lock was on and they did not notice it, since password characters are hidden while typing. Small problems like this are trivial to experts; in the study, people who reported such difficulties tended to use the internet less, a trend that was not significant.
- **Kind:** rule
- **Use:** look, check
- **Sources:** NIELSEN-578 (page 436)
- **Study (as the book reports it):** research on home users in Pittsburgh, its details given only as a link to homenet.andrew.cmu.edu; size and method not given
- **Current source:** confirmed by https://www.chi1997.chistatic.hosting.acm.org/proceedings/tech-note/sk.html (read 2026-11-20)
- **Read:** 2026-11-20, page; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate forms E69

### forms-064 · Check entries in the browser before the form is sent
- **Statement:** Check what a person typed before the form is sent and tell them when something does not pass, so they can correct mistakes before it goes off. It makes it more likely that the site gets usable information in the right format, it is faster than a round trip to the server, and it saves server load.
- **Kind:** practice
- **Use:** check
- **Sources:** DUCKETT-060 (page 604), DUCKETT-041 (page 574)
- **Read:** 2026-11-20, passage; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate forms E71

### forms-065 · The server checks every value, whatever the browser checked
- **Statement:** Form checks must always run on the server; checks in the browser are added on top to give people a smooth experience, not in place of the server checks. Every submitted value is checked again before the database is updated, because form data can be tampered with.
- **Kind:** practice
- **Use:** check
- **Sources:** LAWSON-025 (page 84), ROBBINS-132 (page 248)
- **Also in (not read):** GOLDSTEIN-010
- **Read:** 2026-11-20, passage; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate forms E72

### forms-066 · Let the browser's own checks do the checking where they can
- **Statement:** Letting the browser check a form natively, and not with page scripts, gives users more consistent behaviour from site to site and lets pages load faster, because the duplicated checking script is gone. A typical comment form (name, email and comment required, website optional) can be checked entirely by the browser, provided each field has the right type, a name and the required mark where needed.
- **Kind:** practice
- **Use:** check
- **Sources:** GOLDSTEIN-001 (page 90), LAWSON-043 (page 96)
- **Also in (not read):** LAWSON-053
- **Asked of the source:** that all current browsers run the built-in form checks, and how their messages behave.
- **Current source:** confirmed by https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Form_validation (read 2026-11-20)
- **Conflict:** MDN: the browser's messages follow the browser's language, not the page's, so a page in Greek or Russian may show its errors in another language, and their look depends on the browser
- **Read:** 2026-11-20, page; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate forms E73

### forms-067 · A format check does not prove an entry is right
- **Statement:** A field set to the e-mail type checks only that the address is in a valid format, not that it exists, and an empty field still passes unless it is marked as required. Pattern checks on entries such as e-mail addresses or dates are never perfect: some wrong entries still pass them.
- **Kind:** practice
- **Use:** check
- **Sources:** LAWSON-028 (page 86), DUCKETT-067 (page 619)
- **Asked of the source:** how strict the checks of e-mail and date fields are in current browsers.
- **Current source:** confirmed by https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/email (read 2026-11-20)
- **Read:** 2026-11-20, passage; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate forms E74

### forms-068 · Two checks for every field, then the form's own
- **Statement:** Two checks fit every field of every form and come first: is a required field filled in, and does the value match the kind of field (an e-mail field holds an e-mail address). Besides these a form needs checks of its own for particular fields, such as whether the two password entries match, whether a short biography stays within its length, and whether a parent's consent is ticked when the person is under the minimum age.
- **Kind:** practice
- **Use:** check
- **Sources:** DUCKETT-061 (page 606), DUCKETT-062 (page 607)
- **Read:** 2026-11-20, passage; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate forms E75

### forms-069 · No format error on an empty optional field
- **Statement:** Do not tell a person that an empty optional field holds the wrong kind of value: with nothing entered there is nothing to judge, so the format check applies only once something has been typed.
- **Kind:** practice
- **Use:** check
- **Sources:** DUCKETT-066 (page 616)
- **Read:** 2026-11-20, passage; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate forms E76

### forms-070 · Mark required fields, and show the valid or invalid mark only on the field in use
- **Statement:** Mark required fields so the browser refuses to send the form while they are empty and shows an error message of its own, and show sighted users which fields are required (for example with an asterisk). Give feedback on valid and invalid entries, but show the valid or invalid marker only on the field that has focus, so the whole form does not look cluttered.
- **Kind:** practice
- **Use:** look, check
- **Sources:** GOLDSTEIN-004 (page 96), GOLDSTEIN-003 (page 93)
- **Conflict:** DUCKETT-072 (in forms-072) marks a field as passing or failing once the person has left it, and clears the failure mark when they go back into it.
- **Read:** 2026-11-20, page; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate forms E77

### forms-071 · A required field is announced as required
- **Statement:** Mark required fields as required, so the browser refuses to submit the form while they are empty; the required mark also tells assistive technology that the field is required.
- **Kind:** practice
- **Use:** check
- **Sources:** LAWSON-038 (page 93)
- **Asked of the source:** whether current assistive technology announces a field marked required without the added ARIA attribute.
- **Current source:** confirmed by https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-required (read 2026-11-20)
- **Current source:** overturned by https://www.w3.org/TR/html-aria/ (read 2026-11-20)
- **Read:** 2026-11-20, passage; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate accessibility E40

### forms-072 · Tell people at once whether a password passes
- **Statement:** Give feedback on a password as soon as the person leaves the field, not only on sending: mark the password field as passing or failing for length, and the repeat field by whether it matches; clear the failure mark when the person goes back into the field. A well-built system tells people both when things are going right and when they are making a mistake; quick feedback, such as a digital camera showing each shot at once, removes errors that were common without it.
- **Kind:** practice
- **Use:** look, check
- **Sources:** DUCKETT-072 (page 626), THALER-108 (page 88)
- **Conflict:** GOLDSTEIN-004 (in forms-070) shows the valid or invalid marker only on the field that has focus.
- **Read:** 2026-11-20, page; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate forms E78

### forms-073 · Show all the error messages at once
- **Statement:** Check every field before deciding whether the form can go, and show all the error messages at once. If only the first error is shown, the person has to send the form again and again, meets new errors each time, and quickly loses patience.
- **Kind:** practice
- **Use:** check
- **Sources:** DUCKETT-064 (page 609)
- **Read:** 2026-11-20, passage; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate forms E79

### forms-074 · Each error message sits right after its field
- **Statement:** Put each error message on the page right after the field it is about, as the book's example script does.
- **Kind:** practice
- **Use:** look, check
- **Sources:** DUCKETT-065 (page 615)
- **Read:** 2026-11-20, passage; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate forms E80

### forms-075 · A fixed field loses its error message
- **Statement:** When a form with several errors is sent again after the person fixed some of them, remove the messages for the fixed fields and keep the messages for the ones still wrong.
- **Kind:** practice
- **Use:** check
- **Sources:** DUCKETT-063 (page 608)
- **Read:** 2026-11-20, passage; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate forms E81

### forms-076 · The site's own wording for each kind of mistake, on top of the browser's checks
- **Statement:** A site can present its own error feedback while still using the browser's built-in checks underneath, and can find out exactly why a field failed (missing, wrong type, wrong pattern, too long, out of range, wrong step), so the message says what to fix; a message can also name the value the user entered. Check how the messages read before relying on them, since the browser may add wording of its own.
- **Kind:** practice
- **Use:** check, text
- **Sources:** LAWSON-051 (page 102-103), GOLDSTEIN-018 (page 112), LAWSON-050 (page 101)
- **Asked of the source:** how current browsers show a site's own validation messages, and whether their look can now be changed.
- **Current source:** confirmed by https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Form_validation (read 2026-11-20)
- **Read:** 2026-11-20, page; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate forms E83

### forms-077 · Error messages look the same in every browser
- **Statement:** Many designers and developers take control of the look of form controls and error messages so that the experience is the same in every browser: the browsers' built-in messages can differ a lot in look, and variety in how error messages are styled is held to confuse users. The book's long example turns the browser's own checking off and checks by script, keeping the browser's checks as the fallback for when scripts are off.
- **Kind:** practice
- **Use:** look, check
- **Sources:** DUCKETT-056 (page 598-599, the notes cite 599)
- **Asked of the source:** how much the built-in error messages of current browsers still differ in look.
- **Current source:** confirmed by https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Form_validation (read 2026-11-20)
- **Conflict:** GOLDSTEIN-001, LAWSON-053 (in forms-066) advise the browser's own checking, for behaviour that is consistent from site to site.
- **Read:** 2026-11-20, page; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate forms E84

### forms-078 · An obvious way to recover from a mistake
- **Statement:** Where errors cannot be prevented, give a graceful, obvious way to recover. When the site cannot give users what they want, apologise and show that it knows this is an inconvenience.
- **Kind:** practice
- **Use:** look, check, text
- **Sources:** KRUG-163 (page s117)
- **Read:** 2026-11-20, page; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate forms E85

### forms-079 · A form reacts the same however it is sent
- **Statement:** People send forms by pressing Enter as well as by clicking the button, so whatever the page does on sending (checks, messages) must happen when the form is sent, not only on a click of the button.
- **Kind:** practice
- **Use:** check
- **Sources:** DUCKETT-042 (page 580)
- **Read:** 2026-11-20, passage; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate forms E86

### forms-080 · Every form has something that sends it
- **Statement:** Every form needs something that sends it. That need not be a standard button: it can be an image, and a form with a single field can send on pressing Enter.
- **Kind:** practice
- **Use:** check
- **Sources:** KIRSANOV-009 (page 12)
- **Asked of the source:** what WCAG says today about a form that sends itself when a list item is chosen, which the notes flag as now judged an accessibility fault.
- **Current source:** overturned by https://www.w3.org/WAI/WCAG22/Understanding/on-input.html (read 2026-11-20)
- **Conflict:** WCAG 2.2 success criterion 3.2.2 On Input (level A): choosing an item in a list must not send the form unless the user was told before; automatic sending is failure F36, and a send button beside the list is a sufficient technique
- **Read:** 2026-11-20, passage; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate forms E87

### forms-081 · A form's action is not carried out twice
- **Statement:** Disable the send button as soon as a form has been sent, so the same form cannot be sent several times in a row. A form whose sending performs an action, such as adding to or deleting from a database, must not send its data again when the person returns to it (the book's means: such forms are not sent by GET; POST is the other method).
- **Kind:** practice
- **Use:** check
- **Sources:** DUCKETT-044 (page 584), ROBBINS-120 (page 240-241)
- **Needs source:** how current browsers treat going back to or reloading the page a POST form returned, and disabling the send button after the first press
- **Current source:** confirmed by https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Methods/POST (read 2026-11-20)
- **Read:** 2026-11-20, page; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate forms E88

### forms-082 · A send button that waits for required fields is switched off by script
- **Statement:** The send button can be shown as inactive until all required information has been entered. Switch it off from the script and not in the page markup, so that a visitor whose browser runs no script can still use the form.
- **Kind:** practice
- **Use:** check
- **Sources:** ROBBINS-166 (page 272), DUCKETT-045 (page 584)
- **Read:** 2026-11-20, passage; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate forms E89

### forms-083 · The form works in full with scripts off
- **Statement:** Core functions such as sending a form must keep working when JavaScript is off; scripts only improve on that base. Fields a script would hide stay visible without it, so the form still works in full, and when the page runs its own checks in script, the browser's built-in checks stay as the fallback for visitors whose scripts are off.
- **Kind:** practice
- **Use:** check
- **Sources:** ROBBINS-009 (page 65), DUCKETT-048 (page 588), DUCKETT-057 (page 599)
- **Read:** 2026-11-20, page; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate forms E90

### forms-084 · After sending, the visitor sees that it worked
- **Statement:** After a form is sent, the visitor gets a response suited to the form's purpose: a page thanking them for signing up, the form reloaded with updated information, the next page of a multi-page form, or an error message when it was filled in wrongly. The response is how the visitor sees that the form worked.
- **Kind:** practice
- **Use:** look, check, text
- **Sources:** ROBBINS-118 (page 237)
- **Read:** 2026-11-20, passage; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate forms E91

### forms-085 · Ask for what is useful but not required after the form is sent
- **Statement:** Information that is useful but not required should be asked for later, after the form has been sent and a friendly relationship with the user is established, not in the form itself.
- **Kind:** practice
- **Use:** look, check
- **Sources:** ROBBINS-160 (page 271)
- **Read:** 2026-11-20, passage; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate persuasion E66

### forms-087 · Feedback shows where the work has been done
- **Statement:** Feedback can often be improved by showing where the work has been done while it is being done (paint that is pink while wet and white when dry); without it the gaps show only once the work is finished.
- **Kind:** practice
- **Use:** look
- **Sources:** THALER-110 (page 89)
- **Read:** 2026-11-20, page; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate forms E93

### forms-089 · A promise of compensation wins over people who distrust pre-filled data
- **Statement:** Where people distrust the party that pre-fills their data (the book's case: a tax service sending pre-filled returns), a promise to refund any error with compensation (say 100 dollars) can win them over.
- **Kind:** practice
- **Use:** look, text
- **Sources:** THALER-217 (page 197)
- **Read:** 2026-11-20, page; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate trust E34

### forms-090 · Make the wrong action impossible
- **Statement:** Making the wrong action physically impossible works: in anaesthesia, where 82% of critical incidents had been human error and not equipment failure, giving each hose its own way of fitting stopped patients getting the wrong anaesthetic through mixed-up hoses.
- **Kind:** practice
- **Use:** look
- **Sources:** THALER-105 (page 87)
- **Read:** 2026-11-20, passage; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate forms E95

### forms-091 · The step after the main task cannot be forgotten
- **Statement:** Once the main task is done, people forget the steps around it (the card left in the cash machine, the original left in the copier). Design the end of a task so the leftover step cannot be forgotten: a forcing function makes the person do the needed step before they get what they came for (take back the card before the cash comes out), which removes the error entirely.
- **Kind:** practice
- **Use:** look, check
- **Sources:** THALER-103 (page 86), THALER-104 (page 86-87)
- **Read:** 2026-11-20, passage; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate forms E96

### forms-092 · Catch a likely slip before a message is sent
- **Statement:** A system can catch a likely slip from what the user has already done: Gmail warns when a message mentions an attachment but none is attached. The authors propose the same for messages people may soon regret: a check that detects an angry email and asks "Are you sure you want to send it?", or in a stronger version holds it for 24 hours, so people can calm down.
- **Kind:** practice
- **Use:** look
- **Sources:** THALER-107 (page 88), THALER-223 (page 201)
- **Read:** 2026-11-20, page; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate forms E97

### forms-093 · Warnings are rare, or they stop working
- **Statement:** Warnings must be rare to work: when a system asks for confirmation too often, people click "yes" without thinking, and the frequency makes the warnings useless.
- **Kind:** practice
- **Use:** look, check
- **Sources:** THALER-109 (page 88-89, the notes cite 89)
- **Read:** 2026-11-20, page; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate forms E98

### forms-094 · A metaphor misleads where the interface departs from the real thing
- **Statement:** A real shopping cart implies adding five items five times, while web shops let users edit a quantity. Removing an item by setting its quantity to zero is a well-known usability problem, often done badly.
- **Kind:** practice
- **Use:** look, check
- **Sources:** NIELSEN-302 (page 222)
- **Read:** 2026-11-20, passage; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate forms E100

### forms-095 · A mail link does not open a program the person does not use
- **Statement:** On an organisation's own network, set up the browsers so that a "mailto" link opens the mail program the organisation has standardised on: a link that opens a mail program people do not know confuses them.
- **Kind:** practice
- **Use:** check
- **Sources:** NIELSEN-466 (page 346-347, the notes cite 347)
- **Asked of the source:** how current browsers and phones choose the mail program a mail link opens.
- **Current source:** confirmed by https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a (read 2026-11-20)
- **Read:** 2026-11-20, page; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate forms E102

### forms-096 · Let people pick what they mean, not handle a code
- **Statement:** Task analysis shows what users actually want: a caller wants to talk to a person, not to a number, so an interface that lets people pick a name or a photo from a directory serves the task better than one that makes them handle numbers.
- **Kind:** practice
- **Use:** look, check
- **Sources:** NIELSEN-594 (page 460)
- **Read:** 2026-11-20, passage; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate process E04

### forms-097 · For a simple yes or no with weight, require an answer and tick nothing in advance
- **Statement:** Required choice (every box left empty, the form sent only after the person ticks yes or no) suits simple yes or no questions with emotional weight, such as whether to share one's contact details, and cases where a default would be resented, so nobody agrees by accident or through inertia. In one company, requiring an explicit yes or no raised take-up by 25% compared with an opt-in form. Illinois asked about organ donation during the driving licence photo, and on a yes reminded the person that the family could not overrule it and asked again.
- **Kind:** practice
- **Use:** look, check
- **Sources:** THALER-132 (page 104), THALER-100 (page 85), THALER-191 (page 163)
- **Read:** 2026-11-20, page; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate forms E111

### forms-099 · A control's look matches the action it asks for
- **Statement:** Conflicting cues slow responses and raise errors: in the Stroop test a colour word printed in a different colour makes people answer more slowly and wrongly. When the look of a control suggests one action and it needs another, people make mistakes even after they have been told, because they follow the visual cue automatically.
- **Kind:** rule
- **Use:** look, check
- **Sources:** THALER-092 (page 81), THALER-091 (page 80)
- **Study (as the book reports it):** THALER-092: Stroop test, modern on-screen version, response time and errors measured; no sample size given.
- **Current source:** none found (searched 2026-11-20)
- **Read:** 2026-11-20, page; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate layout E52

### forms-100 · The controls used most are the largest, and a harmful one is not the same size
- **Statement:** The controls people use most should be the largest (on a remote control: power, channels and volume). A control that does harm when pressed by accident, such as the source button that makes the picture vanish, should not be the same size as the common ones.
- **Kind:** practice
- **Use:** look, check
- **Sources:** THALER-093 (page 81)
- **Read:** 2026-11-20, page; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate layout E53

### forms-101 · Controls are laid out like the things they control
- **Statement:** Lay controls out so that their position maps naturally onto what they control: with the burners set symmetrically and the knobs in one row, people confuse which knob sets the front burner and which the back one, and layouts that follow the burners are better.
- **Kind:** practice
- **Use:** look, check
- **Sources:** THALER-094 (page 81)
- **Read:** 2026-11-20, page; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate layout E54

### forms-102 · A tap on the label selects its control
- **Statement:** With a proper label, users can click or tap anywhere on the label text to select or focus the control, which touch-screen users also appreciate. Radio buttons and checkboxes get a label each, button and text together, since one label cannot cover a whole group.
- **Kind:** practice
- **Use:** check
- **Sources:** ROBBINS-149 (page 266-267, the notes cite 266)
- **Read:** 2026-11-20, page; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate phone E39

### forms-103 · No field takes the focus by itself when the page loads
- **Statement:** Do not make a field take the focus automatically when the page loads: the authors advise against it for both user experience and accessibility. Current guidance (MDN) gives the reasons: a screen reader moves its user to the field without warning, past the content before it; it can confuse people with cognitive impairments; the page may scroll and a phone may open its keyboard.
- **Kind:** practice
- **Use:** check
- **Sources:** GOLDSTEIN-014 (page 107)
- **Asked of the source:** what current guidance says about automatic focus on page load, and why.
- **Current source:** confirmed by https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/autofocus (read 2026-11-20)
- **Conflict:** LAWSON-035 (forms, "The cursor starts in a field only on a page that is about that field") allows it on a page whose central purpose is that field, such as a search page.
- **Read:** 2026-11-20, passage; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate accessibility E36

### forms-104 · Group a form's parts so their relations are explicit
- **Statement:** Group logically related form controls and name the groups (fieldset, legend, label), each group carrying its own heading (for example "Customer Information"), with groups inside groups where a section has sub-groups. This makes the relations between the parts of a form explicit for people who do not use a visual browser, and gives the style rules more hooks, which benefits all users; the group's border can be removed for a clean look while its grouping meaning and accessibility stay. Consider for every form how people without visual browsers will perceive and use it.
- **Kind:** practice
- **Use:** check
- **Sources:** ROBBINS-147 (page 265-266), ROBBINS-119 (page 238), ROBBINS-152 (page 267-269, the notes cite 267-268), ROBBINS-218 (page 655)
- **Read:** 2026-11-20, page; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate accessibility E39, joined by forms E25

### forms-105 · Test a field's format pattern with valid and invalid values
- **Statement:** A field's format pattern quickly grows complicated and is then hard to test in the field itself. Test it against valid and invalid sample values before relying on it (the book does so in the browser's console). The pattern matches case exactly, so both upper and lower case must be allowed where either is acceptable.
- **Kind:** practice
- **Use:** check
- **Sources:** LAWSON-040 (page 94-95)
- **Asked of the source:** that a field's pattern still matches case exactly in current browsers (MDN, the pattern attribute).
- **Current source:** confirmed by https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/pattern (read 2026-11-20)
- **Current source:** confirmed by https://html.spec.whatwg.org/multipage/input.html (read 2026-11-20)
- **Read:** 2026-11-20, page; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate testing E110

### forms-106 · Give a form its field sets and their headings while it is built
- **Statement:** Add fieldsets and their headings (legend) to a form right away, not as a later pass.
- **Kind:** practice
- **Use:** check
- **Sources:** ROBBINS-154 (page 269)
- **Read:** 2026-11-20, page; read again: an Opus agent, 2026-11-20; every difference settled by Claude on the page; candidate process E88
