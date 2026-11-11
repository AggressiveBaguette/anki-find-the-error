# {{TARGET_LANGUAGE}} learning — overview (read first)

Last updated: {{DATE}}.

## 1. Profile
- Native language: {{NATIVE_LANGUAGE}}. Target: {{TARGET_LANGUAGE}} ({{TARGET_VARIETY}}). Level: {{LEVEL}}. Hardest: {{HARDEST}}.
- Anki on: {{DEVICES}}. Existing decks: {{EXISTING_DECKS}}.
- Writing practice: {{TOPICS}}; format: {{WRITING_FORMAT}}.
- Signature error measured: {{SIGNATURE_ERROR}}.
- Card labels and rules in: {{CARD_LANGUAGE}}.

## 2. How the method works
- **Goal: transfer.** What is practised in Anki must come out correctly and spontaneously in real writing and speech. Anki success rates are not a measure of progress; only new texts, back-translations and transfer tests are.
- **Why find-the-error cards.** Cloze cards are good for new vocabulary, but for rules the learner already knows and still breaks, they plateau: you learn the card, not the reflex. Those mistakes are attention failures, so the training is *spotting* them in context: a short coherent paragraph containing 0 to 4 real mistakes taken from the learner's own writing, mixed together. Read it, correct it aloud or in your head, then flip the card.
- **Random number of errors**: 20% of cards have none, 40% one, 20% two, 10% three, 10% four (mean 1.5). After each error found, there is always a 50% chance another remains, so finding one error says nothing about the rest.
- **Calques** (word-for-word translations from the native language) get translation cards: translate a native-language sentence and check whether you fell into the trap.
- **The loop**: write → active correction in 3 rounds → mistakes sorted into card types → cards generated → two independent reviews → learner's review → import → write again. A few days after each text: back-translation. Every 2–3 weeks: transfer test.

## 3. Decks
| Deck | Content | Note type | Status |
|---|---|---|---|
| {{DECK}} | mixed paragraphs, 0–4 real errors, tag `error` | {{NOTE_TYPE}} | {{STATUS}} |
| Translations | calque cards (native sentence → target), tag `calque` | Basic | {{STATUS}} |
| (vocabulary deck) | cloze cards for unknown words and expressions | Cloze | {{STATUS}} |

## 4. Anki setup (manual alternative to the starter .apkg)
Run `python anki_cards.py --print {{CARD_LANGUAGE_CODE}}`: it prints the note type name, the fields and the three templates. In Anki: Tools → Manage Note Types → Add: Basic → name it "{{NOTE_TYPE}}" → Fields: {{FIELDS}} (in this order) → Cards: paste Front, Back and Styling.
Reviewing a card: read the paragraph and say or type the corrected version *before* flipping. Press "Again" (its label depends on Anki's interface language) if you missed an error or flagged something correct.

## 5. Current state
- Texts written: 0. Cards: none yet.
- Next step: first text ("topic").
- Next transfer test due: 2–3 weeks after the first batch of translation cards.
