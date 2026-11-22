"""Readability audit for English prose others will read (SU-Q27).

usage: python -I audit_text.py [--skip-class NAME ...] <file> [<file> ...]
Measures what the plain-language and business-writing skills check:
sentences over 25 words, average sentence length (target 15-20), passive
voice share (target <= 10%), Flesch Reading Ease (target >= 60), filler
phrases, buzzwords and curly quotes. Table cells, headings and figure boxes
are skipped; only running prose is measured. In .html files, <div> elements with one of the SKIP classes (labels,
figure boxes, the signature and legal footer from class "sign" on) are not prose; --skip-class adds a project's own.
Advisory: always exits 0.
"""
import argparse, html, re, sys

SKIP = ["label", "value", "sub", "kicker", "addressee", "meta", "page-head", r"lbl[^\"]*"]

FILLER = ["in order to", "due to the fact that", "at this point in time", "in the event that",
          "with regard to", "pursuant to", "aforementioned", "henceforth", "utilize", "leverage",
          "facilitate", "commence", "additionally", "furthermore", "moreover", "it is worth noting",
          "going forward", "robust", "seamless", "deep dive", "bandwidth", "best-in-class"]
PASSIVE = re.compile(r"\b(is|are|was|were|be|been|being)\s+(\w+ly\s+)?(\w+ed|built|done|made|given|shown|seen|known|taken|issued|sold|held|kept|left|set|paid)\b", re.I)

def prose(path, skip=SKIP):
    s = open(path, encoding="utf-8").read()
    if path.endswith(".html"):
        s = re.sub(r"(?s)<(style|table|head|h1|h2|h3)\b.*?</\1>", " ", s)
        s = re.sub(r'(?s)<div class="sign">.*', " ", s)  # signature and legal footer (legal register is exempt)
        s = re.sub(r'(?s)<div class="(' + "|".join(skip) + r')"[^>]*>.*?</div>', " ", s)
        s = re.sub(r"<(br|li|p|div)[^>]*>", "\n", s)
        s = html.unescape(re.sub(r"<[^>]+>", " ", s))
    else:
        s = "\n".join(l for l in s.splitlines() if not l.lstrip().startswith(("|", "#", "**")))
    return s

def sentences(text):
    out = []
    for block in text.split("\n"):
        block = " ".join(block.split())
        out += [x for x in re.split(r"(?<=[.!?])\s+(?=[A-Z€\d])", block) if len(x.split()) >= 3]
    return out

def syllables(word):
    w = re.sub(r"[^a-z]", "", word.lower())
    if not w: return 1
    n = len(re.findall(r"[aeiouy]+", w))
    if w.endswith("e") and not w.endswith(("le", "ee")) and n > 1: n -= 1
    return max(n, 1)

def main(argv=None):
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--skip-class", action="append", default=[], metavar="NAME", help="another non-prose div class")
    ap.add_argument("files", nargs="+")
    args = ap.parse_args(argv)
    skip = SKIP + [re.escape(c) for c in args.skip_class]
    for p in args.files:
        text = prose(p, skip); sents = sentences(text)
        words = [w for s in sents for w in s.split()]
        if not sents: continue
        avg = len(words) / len(sents)
        passive = [s for s in sents if PASSIVE.search(s)]
        fre = 206.835 - 1.015 * avg - 84.6 * sum(syllables(w) for w in words) / len(words)
        print(f"\n== {p}\n{len(sents)} sentences · avg {avg:.1f} words (target 15-20) · "
              f"passive {100*len(passive)/len(sents):.0f}% (target <=10) · Flesch {fre:.0f} (target >=60)")
        for s in sents:
            if len(s.split()) > 25: print(f"  LONG {len(s.split())}w: {s[:140]}")
        for s in passive: print(f"  PASSIVE: {s[:140]}")
        low = text.lower()
        for f in FILLER:
            if re.search(r"\b" + re.escape(f) + r"\b", low): print(f"  FILLER: '{f}'")
        if re.search("[“”‘’]", text): print("  CURLY QUOTES present")

if __name__ == "__main__":
    main()
