"""Creates a starter .apkg: the "find the error" note type, its deck, and two example cards.

python make_starter_apkg.py --lang fr --out find-the-error-starter.apkg
"""
import argparse, os, sys
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "templates"))
from anki_cards import build_apkg

TEXT = {
 "fr": dict(rule="nom singulier sujet → verbe en -s",
            instr1="Exemple : corrige le paragraphe à voix haute AVANT de retourner la carte. « À revoir » si tu as raté une erreur ou corrigé quelque chose de juste.",
            instr2="Exemple : il peut n'y avoir aucune erreur. Trouve les erreurs."),
 "en": dict(rule="singular subject → verb + -s",
            instr1="Example: correct the paragraph aloud BEFORE flipping the card. Mark 'Again' if you missed an error or corrected something that was right.",
            instr2="Example: there may be no error at all. Find the errors."),
}

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--lang", choices=["fr", "en"], default="en")
    ap.add_argument("--out", default="find-the-error-starter.apkg")
    a = ap.parse_args()
    t = TEXT[a.lang]
    cards = [
     {"paragraph": "My neighbour walks his dog every morning before work. On Saturdays, his two daughters come too, and the dog run ahead of them all the way to the park. Everyone in the street knows the dog's name.",
      "corrections": [{"original": "the dog run ahead", "correction": "the dog runs ahead", "rule": t["rule"]}],
      "instruction": t["instr1"]},
     {"paragraph": "Each of the shops on our street opens at nine. The baker and his wife start much earlier, and the smell of bread reaches our kitchen before the alarm goes off.",
      "corrections": [], "instruction": t["instr2"]},
    ]
    from anki_cards import L
    n = build_apkg(cards, a.out, tags=("example",), lang=a.lang)
    print(f"{a.out}: {n} example cards, deck '{L[a.lang]['deck']}', note type '{L[a.lang]['name']}'")
