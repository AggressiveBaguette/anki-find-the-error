"""Find-the-error method: draw error counts and build Anki .apkg files.

Usage (Python 3, `pip install genanki`):
    from anki_cards import draw_counts, build_apkg
    counts = draw_counts(20, seed=123)        # number of errors per card, 20/40/20/10/10
    build_apkg(cards, "batch.apkg")           # cards: list of dicts, see build_apkg

Set LABELS below to "fr" or "en" (language of the card labels). The "fr" note type is
identical to the one used by the shared deck "Chasse au -s (francophones)", so both can
live in the same collection without duplicates.
"""
import hashlib, random
import genanki

LABELS = "en"   # "fr" or "en"

L = {
 "fr": dict(id=1794208575990, name="Trouve l'erreur",
            fields=["Paragraphe", "Corrections", "Phrase corrigée", "Règles", "Consigne"], deck="Trouve l'erreur",
            instr="Trouve les erreurs.", corr="Corrections :", rules="Règles :", none="Aucune erreur"),
 "en": dict(id=1794208575991, name="Find the error",
            fields=["Paragraph", "Corrections", "Corrected text", "Rules", "Instruction"], deck="Find the error",
            instr="Find the errors.", corr="Corrections:", rules="Rules:", none="No errors"),
}

CSS = """.card{font-family:sans-serif;font-size:20px;text-align:left;color:#222;background:#fff}
.night_mode .card,.nightMode .card{color:#eee;background:#1e1e1e}
.consigne{font-style:italic;color:#888;font-size:.8em}
.corr b{color:#2e7d32}.night_mode .corr b,.nightMode .corr b{color:#81c784}
.phrase{margin-top:1.2em}
.regles{margin-top:2em;color:#999;font-size:.8em}
.ok{font-size:1.1em}"""

def _templates(l):
    P, C, F, R, I = l["fields"]
    qf = ("{{%s}}<div class=consigne><br>{{#%s}}{{%s}}{{/%s}}{{^%s}}%s{{/%s}}</div>"
          % (P, I, I, I, I, l["instr"], I))
    af = ("{{FrontSide}}<hr id=answer>\n{{#%s}}\n"
          "<div class=corr><b>%s</b><br><span id=c>{{%s}}</span></div>\n"
          "<div class=phrase id=p>{{%s}}</div>\n"
          "<div class=regles><b>%s</b><br>{{%s}}</div>\n{{/%s}}\n"
          "{{^%s}}<div class=ok>✓ <b>%s</b></div>{{/%s}}\n"
          % (C, l["corr"], C, F, l["rules"], R, C, C, l["none"], C)) + r"""<script>
(function(){var c=document.getElementById('c'),p=document.getElementById('p');if(!c)return;var t=[];
c.innerHTML=c.innerHTML.replace(/→\s*([^<]+)/g,function(m,x){x=x.trim();t.push(x);return '→ <b>'+x+'</b>';});
if(!p)return;t.sort(function(a,b){return b.length-a.length;});var h=p.innerHTML;
t.forEach(function(x){var i=h.indexOf(x);if(i>=0&&h.lastIndexOf('<b>',i)<=h.lastIndexOf('</b>',i))h=h.slice(0,i)+'<b>'+x+'</b>'+h.slice(i+x.length);});
p.innerHTML=h;})();
</script>"""
    return qf, af

def model(lang=None):
    l = L[lang or LABELS]
    qf, af = _templates(l)
    return genanki.Model(l["id"], l["name"], fields=[{"name": f} for f in l["fields"]],
                         templates=[{"name": "Carte" if (lang or LABELS) == "fr" else "Card", "qfmt": qf, "afmt": af}], css=CSS)

def draw_counts(n, seed):
    """Number of errors per card: 20% 0, 40% 1, 20% 2, 10% 3, 10% 4 (exact when n is a multiple of 10)."""
    base = [0, 0, 1, 1, 1, 1, 2, 2, 3, 4]
    counts = base * (n // 10) + random.Random(seed).sample(base, n % 10)
    random.Random(seed).shuffle(counts)
    return counts

def corrected(paragraph, corrections):
    out = paragraph
    for c in corrections:
        out = out.replace(c["original"], c["correction"], 1)
    return out

def validate(cards):
    """Returns a list of problems: each `original` must appear exactly once in its paragraph."""
    probs = []
    for i, card in enumerate(cards):
        for c in card.get("corrections", []):
            k = card["paragraph"].count(c["original"])
            if k != 1:
                probs.append(f"card {i+1}: '{c['original']}' found {k} times")
            if c["original"] == c["correction"]:
                probs.append(f"card {i+1}: correction identical to original")
    return probs

def build_apkg(cards, path, deck=None, tags=("error",), instruction="", lang=None):
    """cards: [{"paragraph": str, "corrections": [{"original", "correction", "rule"}], "instruction": optional}].
    Stable GUIDs (derived from the paragraph), so re-importing never duplicates notes."""
    probs = validate(cards)
    if probs:
        raise ValueError("\n".join(probs))
    m = model(lang)
    deck = deck or L[lang or LABELS]["deck"]
    d = genanki.Deck(int(hashlib.sha1(deck.encode()).hexdigest()[:8], 16), deck)
    for card in cards:
        cs = card.get("corrections", [])
        rules = []
        for c in cs:
            if c["rule"] not in rules:
                rules.append(c["rule"])
        d.add_note(genanki.Note(model=m, tags=list(tags),
            guid=hashlib.sha1(("fte:" + card["paragraph"]).encode()).hexdigest()[:10],
            fields=[card["paragraph"],
                    "<br>".join(f"• {c['original']} → {c['correction']}" for c in cs),
                    corrected(card["paragraph"], cs) if cs else "",
                    "<br>".join(f"• {r}" for r in rules),
                    card.get("instruction", instruction)]))
    genanki.Package(d).write_to_file(path)
    return len(d.notes)

if __name__ == "__main__":
    # python anki_cards.py --print [fr|en] : prints the note type for a manual setup in Anki
    import sys
    if len(sys.argv) >= 2 and sys.argv[1] == "--print":
        lang = sys.argv[2] if len(sys.argv) > 2 else LABELS
        l = L[lang]; qf, af = _templates(l)
        print(f"Note type: {l['name']}\nFields, in order: {', '.join(l['fields'])}\n\n--- Front template ---\n{qf}\n\n--- Back template ---\n{af}\n\n--- Styling ---\n{CSS}")
