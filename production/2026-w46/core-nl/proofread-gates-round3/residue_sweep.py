"""Round 3 independent residue sweep (proofreader's own method).
Pass 1: targeted tokens + broad English wordlist over NON-EN editions' full SVG text.
Pass 2: edition-only strings (multiset diff vs core, per page) scanned against
  distinctive function-word lists of every OTHER language -> cross-language leaks
  in the explanation layer specifically.
Pass 3: script-leak scan (Cyrillic/kana/Hangul/CJK outside their editions).
Pass 4 handled separately by reading ABSTRACT.txt files in full.
All hits printed with full string for adjudication; nothing auto-cleared silently.
"""
import pathlib, re, collections, xml.etree.ElementTree as ET
F = pathlib.Path.home()/"workspace/goals/lucernaread-social-media-operations/files"
OUT = pathlib.Path.home()/"workspace/goals/lucernaread-social-media-operations/hidden_files/w46/nl-proofread-gates-round3"
NS = "{http://www.w3.org/2000/svg}"
PAGES = ["p1-voorpagina.svg","p2-leven.svg","p3-cultuur.svg","p4-sport.svg",
         "p5-jongeren.svg","p6-verdieping.svg","p7-taal.svg","p8-toets.svg"]
EDS = ["core","de","en","es","fr","it","ja","ko","pt","ru","zh-tw"]
def texts(ed, pg):
    return ["".join(el.itertext()) for el in ET.parse(F/f"weekly-report-w46-nl-{ed}/svg"/pg).iter(f"{NS}text")]
def alltexts(ed):
    return [(pg, t) for pg in PAGES for t in texts(ed, pg)]

log = open(OUT/"residue-sweep.log","w",encoding="utf-8")
def say(s=""):
    print(s); log.write(s+"\n")

# ---- Pass 1 ----
EN_WORDS = set("""the and with from this that have will your about every news festival sharing arrive arrival
compared compare write read answer answers question questions page pages article articles
watch watching look looks day days week weeks year years old new first last when where what
which their there here very much more most only also into over under between through during
before after above below up down out off again further then once am is are was were be been
being do does did doing would should could ought i'm you're he's she's it's we're they're
i you he she it we they my his her its our their me him us them this that these those
who whom whose why how all any both each few more most other some such no nor not only
own same so than too very can just don should now""".split())
say("=== PASS 1: English wordlist over non-EN editions (full SVG text) ===")
hits = collections.Counter()
for ed in EDS:
    if ed == "en": continue
    for pg, t in alltexts(ed):
        toks = re.findall(r"[A-Za-zÀ-ÿ]+(?:'[A-Za-z]+)?", t)
        for tok in toks:
            low = tok.lower().strip("'")
            if low in EN_WORDS:
                hits[(ed, pg, low)] += 1
                say(f"P1 {ed} {pg} [{low}] :: {t}")
say(f"Pass 1 total hits: {sum(hits.values())} distinct (ed,page,word): {len(hits)}")

# ---- Pass 2 ----
say("\n=== PASS 2: edition-only strings vs other-language function words ===")
FUNC = {
 "en": set("the and with from this that have will your".split()),
 "de": set("der die das und ist ein eine den dem von zu im für mit sich".split()),
 "fr": set("les des une est sont pour dans avec plus".split()),  # le/la/de/que omitted: too homographic; covered by targeted lists below
 "es": set("los las una son para pero".split()),
 "it": set("che sono nella degli delle".split()),
 "pt": set("para pela pelo estão".split()),
}
# targeted distinctive tokens per language (low homograph risk)
TARGET = {
 "en": ["the "," and "," with "," festival"," sharing"," arrival"],
 "de": [" und "," ist "," ein "," eine "," der "," die "," das "],
 "fr": [" les "," des "," une "," est "," pour "," avec "," nous "," vous "],
 "es": [" los "," las "," para "," pero "," son "," está "," también "],
 "it": [" che "," sono "," nella "," degli "," delle "," anche "],
 "pt": [" para "," pelo "," pela "," estão "," também "," você "],
}
for ed in EDS:
    if ed == "core": continue
    added = []
    for pg in PAGES:
        c = collections.Counter(texts("core", pg)); e = collections.Counter(texts(ed, pg))
        for s, n in (e - c).items(): added.extend([(pg, s)]*n)
    for lang, toks in TARGET.items():
        if lang == ed: continue
        for pg, s in added:
            low = " " + s.lower() + " "
            for tok in toks:
                if tok in low:
                    say(f"P2 {ed} {pg} [{lang}:{tok.strip()}] :: {s}")
                    break
say("Pass 2 done (added-string counts per edition printed in sweep summary below)")
for ed in EDS:
    if ed == "core": continue
    n = 0
    for pg in PAGES:
        c = collections.Counter(texts("core", pg)); e = collections.Counter(texts(ed, pg))
        n += sum((e-c).values())
    say(f"  added strings {ed}: {n}")

# ---- Pass 3 ----
say("\n=== PASS 3: script leaks ===")
def script_of(ch):
    o = ord(ch)
    if 0x0400 <= o <= 0x04FF: return "cyrillic"
    if 0x3040 <= o <= 0x30FF: return "kana"
    if 0xAC00 <= o <= 0xD7A3: return "hangul"
    if 0x4E00 <= o <= 0x9FFF or 0x3400 <= o <= 0x4DBF: return "cjk"
    return None
ALLOWED = {"ru": {"cyrillic"}, "ja": {"kana","cjk"}, "ko": {"hangul","cjk"},
           "core": {"cjk"}, "zh-tw": {"cjk"}}
for ed in EDS:
    allow = ALLOWED.get(ed, set())
    bad = collections.Counter()
    for pg, t in alltexts(ed):
        for ch in t:
            s = script_of(ch)
            if s and s not in allow: bad[s] += 1
    say(f"{ed}: out-of-script chars {dict(bad)}")
log.close()
print("SWEEP DONE")
