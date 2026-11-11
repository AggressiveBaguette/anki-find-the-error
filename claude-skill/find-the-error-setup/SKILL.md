---
name: find-the-error-setup
description: Sets up a Claude Project for the "find the error" Anki method for language learners. Use when the user wants to start or set up this method or their language-learning project.
---

# Find-the-error method — project setup

This skill installs the method **once**, inside a Claude Project. After setup, the Project runs the method on its own: its instructions say how to read the learner's messages, and its documents hold the learner's profile, error reservoir, measurements and pending back-translations. The skill is not needed again, except to start over.

Designed for French speakers learning English; works for any native/target language pair.

## Step 1 — Explain, briefly

In 6 lines maximum, explain to the user:
- the goal is **transfer** (correct, spontaneous use in real writing and speech), not Anki success rates;
- rules they *know* but keep breaking are attention failures, so they train *spotting* them: coherent paragraphs with 0–4 real mistakes from their own writing (distribution 20/40/20/10/10, so after each error found there's still a 50% chance another remains);
- the loop: write → active correction in 3 rounds → mistakes sorted into card types → cards reviewed by two independent reviewers and then by the learner → import → back-translation a few days later → transfer test every 2–3 weeks.
- it trains **writing**; speaking benefits indirectly (fewer errors to automate), but there are no speaking sessions in this setup.

Full description: `templates/method-overview.md` (section "How the method works").

## Step 2 — Ask the onboarding questions

Ask in one short message (use a multiple-choice question tool if available, otherwise a numbered list):
1. Native language, target language, target variety (e.g. British / American English).
2. Rough level, and what feels hardest.
3. Anki devices (desktop, AnkiDroid, AnkiMobile) and existing decks.
4. Writing practice: topics they want (everyday life, work, opinions…) and format. Default: 10 minutes, no rereading, any length.
5. Their "signature error" to measure, if they know one. Default for French speakers learning English: the -s in obligatory contexts (third-person verbs, plural nouns, possessive 's). Otherwise decide it together after the first text.
6. Language for the card labels and rules (default: their native language).

## Step 3 — Generate the project documents

Fill the templates in `templates/` with the answers and replace every `{{…}}` placeholder in the `.md` files:
- from the answers: `LEARNER_NAME` (first name if known, otherwise rephrase as "My …"), `NATIVE_LANGUAGE`, `TARGET_LANGUAGE`, `TARGET_VARIETY`, `LEVEL`, `HARDEST`, `DEVICES`, `EXISTING_DECKS`, `TOPICS`, `WRITING_FORMAT`, `SIGNATURE_ERROR`, `CARD_LANGUAGE`;
- from the card language (`fr` or `en`; for any other language use `en` and translate the rules on the cards): `CARD_LANGUAGE_CODE`, and `NOTE_TYPE`, `DECK`, `FIELDS` as defined in `anki_cards.py` (`L[...]`: fr = "Trouve l'erreur", deck "Trouve l'erreur", fields Paragraphe, Corrections, Phrase corrigée, Règles, Consigne; en = "Find the error", deck "Find the error", fields Paragraph, Corrections, Corrected text, Rules, Instruction);
- `STATUS`: "not started"; `DATE`: today.
The documents themselves stay in English (they are instructions for Claude) unless the user asks otherwise; only the card labels and rules follow the card language. In `anki_cards.py`, double braces are Anki field names: don't touch them, just set `LABELS`. Write the language-specific parts (e.g. calque examples, signature error) for the learner's language pair.

| Template | Project document | Content |
|---|---|---|
| `method-overview.md` | `method-overview.md` | profile, method, decks, current state; read first in every chat |
| `protocol.md` | `protocol.md` | detailed rules: correction, metrics, triage, card formats, review, back-translation, transfer test |
| `error-reservoir.md` | `error-reservoir.md` | the learner's real errors (starts empty) |
| `progress-log.md` | `progress-log.md` | metrics, target phrases, translation-card coverage, test results |
| `back-translations.md` | `back-translations.md` | pending and done back-translations |
| `anki_cards.py` | `anki_cards.py` | script to draw error counts and build `.apkg` files; copy as is, then set `LABELS` to the chosen card language |
| `reviewer-prompts.md` | `reviewer-prompts.md` | instructions for the blind reviewer and the answer-key reviewer |

**Delivery:** if a tool can write documents to the Project directly (e.g. a `project_write` method), write them there. Otherwise, save them as files and send them to the user, and tell them to add them to the Project's knowledge.

## Step 4 — Project instructions

Fill `templates/project-instructions.md` and give it to the user in a code block, to paste into the Project's custom instructions (Project → Instructions). Skills cannot set Project instructions themselves, so say so plainly.

## Step 5 — Starter deck with the note type

Run:
```
pip install genanki  # if missing (--break-system-packages may be needed)
python -B scripts/make_starter_apkg.py --lang <fr|en> --out find-the-error-starter.apkg
```
It creates the note type (for `fr`, the same one as the shared deck "Chasse au -s (francophones)"), one deck, and two example cards that explain how to review. Send the `.apkg` to the user. If code can't run here, give them the manual setup in `templates/method-overview.md` (section "Anki setup").

## Step 6 — Checklist for the user

End with this checklist, short, adapted to what you could do yourself:
1. Create a Project (if not already done) and paste the instructions.
2. Add the documents to the Project knowledge (unless already written there).
3. Import the starter `.apkg` in Anki desktop and sync.
4. Start a new chat in the Project and type "topic" (or paste a text they wrote).

Then stop. Don't start an exercise in the setup chat.

## Notes

- Never put real personal data from the user into example cards or shared material.
- The two-reviewer check uses sub-agents when available (Claude Code, or the app when sub-agents are offered). Without them, the Project instructions tell Claude to have the user paste the reviewer prompt into a new chat.
