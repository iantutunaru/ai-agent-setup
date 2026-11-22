# measure.js on fixture.html: the values to expect

`measure.js` runs in a browser, so it is tried by hand. Serve this folder's parent
(`python -m http.server 8765 --bind 127.0.0.1` in `web-check/`), open
`http://127.0.0.1:8765/tests/fixture.html`, set the width, and run in the JavaScript tool:
`await eval(await (await fetch('/measure.js', {cache: 'no-store'})).text())`. Without `no-store` the pane can
serve an older copy from its cache: a later chat once got the version before a fix from this very address.

Measured on 2026-11-21 in the Claude desktop app's browser pane, at 1280 by 800:

| Field | Value | Why |
|---|---|---|
| `page.zoomBlocked` | true | the viewport line says `user-scalable=no` |
| `page.lang` | en | |
| `page.script` | the version in the file's head comment | shows which copy of the script ran |
| `images.notLoaded` | none | both pictures have arrived (tried again 2026-11-21, with the other rows) |
| `contrast.lowest[0]` | ratio 2.84, #999999 on #ffffff | the grey paragraph; the ratio is cut to two decimals, never rounded up |
| `contrast.overPicture` | 1 run, "White text over a picture" | a background picture lies behind it |
| `lines.charactersPerLine` | shortest 37, longest 110 | the 200 px and the 800 px paragraph |
| `lines.leading` | lowest 1, highest 1.5 | 12 on 12, and 16 on 24 |
| `tap.smallest` | "click here" 68 by 17, button "x" 20 by 20; `under24` 4, `under44` 5 | the two fields are 20 and 21 high |
| `tap.inTextLinks` | 1 | the plain link inside a sentence |
| `headings.skips` | h1 to h3 | |
| `images.altMissing` | 1 | the first image has no alt |
| `images.stretched` | 2 | a 1 px file shown at 100 and at 30 px |
| `forms.placeholderOnly` | 1; the name field's `labelIs` above | |
| `links.vagueWords` | "click here"; `lookLikeTheTextAround` "in this plain link"; `openNewWindow` 1 | |
| `text.underlinedButNoLink` | "Underlined but no link" | |

At the phone preset (375 by 812, pixel ratio 2): `page.sidewaysOverflowPx` 445 (the 800 px paragraph), and the
one-line rerun `eval(sessionStorage.getItem('webCheckMeasure'))` gives the result after a reload.

In a hidden browser pane the window has no size; the script then returns only an `error` saying so.
`speed.largestPaintMs` was null in this run: the browser reported no largest paint for a page loaded in a
hidden pane.

## `fixture-labels.html`: labels that wrap their control, and a fixed bar outside the measured part

Served the same way, at 1280 by 800, with `window.WEB_CHECK_ROOT = "#part"` (measured 2026-11-21).

| Field | Value | Why |
|---|---|---|
| `forms.list[0]` | textarea, label "Message", `labelIs` above, `labelWraps` true | the label's words, without the text typed into the box, and where those words stand |
| `forms.list[1]` | input[text], label "City", `labelIs` left, `labelWraps` true | |
| `forms.noLabel`, `forms.hiddenLabelOnly` | 0, 0 | |
| `page.fixedOrSticky` | one `div`, 60 px high, 8% of the screen | the bar is outside `#part` and is still reported |

Found on a real page (2026-11-21): before this the script printed a wrapping
label run together with the field's own text ("Message" and then the text, with no space) with `labelIs` "around or inside", printed a contrast of
4.47 as 4.5, and with a part set reported no fixed bar although one covered the bottom of the screen.
