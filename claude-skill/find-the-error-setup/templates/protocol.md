# Protocol — detailed rules

(Overview, profile and current state: `method-overview.md`, read first.)

General: one step at a time; short answers; never generate card files before the learner's "go"; never make a card from a sentence that was actually correct (check twice — a natural phrasing that differs from yours is not an error); check every number twice; active formats over passive ones.

## 1. Writing topics
On "topic": a topic matching the learner's preferences (overview, section 1). Default format: {{WRITING_FORMAT}}. Silently choose topics that create opportunities to use the target phrases in `progress-log.md`; never say which.

## 2. Active correction in 3 rounds
Never give the corrected text straight away.
1. **Round 1**: return the text with numbered markers [1], [2]… on passages to fix and, for each, only the category: agreement / -s, preposition, article, tense, word order, wrong word / false friend, spelling, "calque: try a more natural phrasing". No corrections. The learner rewrites the marked passages.
2. **Round 2**: for what is still wrong, ask *why* it is wrong, then give a more precise hint. The learner tries again.
3. **Round 3**: give the answer for what still resists, then the **annotated version** keeping the learner's style: `~~original~~ → **correction**` for an error, with (1)/(2)/(3) for the round in which it was fixed; `~~original~~ → *rephrasing*` for a style improvement where the original was acceptable; a count of errors and of improvements.

Then: metrics (section 3); 2–3 natural phrasings from the clean version that the learner wouldn't have produced (→ target phrases in `progress-log.md`); errors that already have cards (sign that the transfer hasn't happened); prepare the back-translation (section 8); propose cards (section 4) as a numbered list and wait for the review. Mistakes introduced when retyping in round 1 are expected: no cards unless they are real errors.

## 3. Metrics (on every first draft)
- **Signature-error rate** ({{SIGNATURE_ERROR}}). For the -s in English: correct -s / places where an -s was required (third-person singular present verbs, plural nouns, possessive 's), giving both numbers. Don't count forms of *be*. Count extra -s separately. Don't divide by the number of words. Fewer than ~12 opportunities: give the figure, don't interpret it.
- **Calques per 100 words**: word-for-word translations from {{NATIVE_LANGUAGE}} (wrong or just unnatural) / number of words × 100. Noisy: read trends over several texts only.
Record both in `progress-log.md`.

## 4. Sorting mistakes into card types
| What happened in the correction | Card type |
|---|---|
| Fixed alone in round 1 (attention slip) | Find-the-error |
| Fixed with a hint (fragile rule) | Find-the-error, priority |
| Unknown word or expression | Cloze (vocabulary deck) |
| Calque not fixed even with the hint | Translation card, only if the wrong form is really what the learner writes from {{NATIVE_LANGUAGE}} |

- Prepositions and collocations → find-the-error, never translation cards, with contrasting contexts (e.g. happy *with* a purchase vs happy *about* some news).
- A calque fixed alone or with a hint gets no translation card.
- Every real error goes into `error-reservoir.md`. An error absent from 3 texts in a row where it could have appeared → status "dormant" (no new cards). An error that comes back despite its cards → note the date, more occurrences in the next batch.
- Never modify cards that already exist in Anki; never build batches only from errors already carded.

## 5. Find-the-error cards
- One paragraph of 3–6 sentences telling **one small coherent situation**; never glue unrelated sentences. Long enough to hold 4 errors.
- Errors from the reservoir, mixed (not one type per card). A new error appears ~5 times per batch in different contexts; priority to errors that came back.
- Number of errors per card: 20/40/20/10/10 for 0/1/2/3/4. Draw it with `anki_cards.py` (`draw_counts`, note the seed). Without code, use these sequences in order: A = 1, 0, 2, 1, 4, 1, 3, 0, 2, 1 — B = 2, 1, 0, 1, 3, 1, 4, 2, 1, 0.
- Only **unambiguous** errors in {{TARGET_VARIETY}}: if a form is acceptable (even informal), replace it with a clearly wrong form or drop it. Everything else in the paragraph must be correct and natural.
- Note type {{NOTE_TYPE}}, deck {{DECK}}, tag `error`. Fields (plain text, `<br>` between lines): Paragraph; Corrections (one line `• original → correction` per error, empty if none); Corrected text (empty if no error); Rules (one line `• rule` per rule, no duplicates, in {{CARD_LANGUAGE}}); Instruction (empty).
- In `original`, use a short segment copied verbatim that appears once in the paragraph, including the word that shows why it's wrong (e.g. "Each of the children get", not "children get").

## 6. Translation cards (calques)
Front: a {{NATIVE_LANGUAGE}} sentence + an instruction in {{CARD_LANGUAGE}} meaning "Translate the whole sentence. Press Again only if you wrote a ✗ form."; the sentence must not give away the structure. Back: target sentence with the key structure in bold; "✓ also:" other correct phrasings; "✗" the calques the learner would really write; "Rule:" one line. 5 cards per phrase, varied contexts. Note type Basic, deck Translations, tag `calque`. The learner amends the ✓/✗ lines with their real answers.

## 7. Review before the learner sees any batch
1. **Blind reviewer** (sub-agent, or a new chat if sub-agents aren't available): receives the paragraphs only, lists every error it sees, and separately anything debatable. Prompt: `reviewer-prompts.md`.
2. **Answer-key reviewer**: receives the cards with corrections and the corrected text; checks each correction (is the original really wrong? is the fix right? is the rule right?), looks for remaining errors and incoherent paragraphs.
3. Decision rule: keep an intended error only if every reviewer sees it as wrong; fix every unintended error. Re-check the cards you modified.
4. Show the batch to the learner as a numbered list; they answer e.g. "ok 1-12, change 4: …, drop 7". Then build the files (`anki_cards.py`: `.apkg` with a stable GUID; or a `.txt` with `#separator:tab`, `#html:true`, `#notetype:…`, `#deck:…`, `#tags column:N`).

## 8. Back-translation (a few days after each text)
- End of round 3: write a {{NATIVE_LANGUAGE}} version of the text that keeps the meaning and tone and sounds natural (don't calque the target language back); keep the clean target version as reference, plus the "phrasings to watch" (natural phrasings missed, calques, errors that needed a hint or the answer). Store in `back-translations.md` with a due date ≥ 3 days later.
- When due: give **only** the {{NATIVE_LANGUAGE}} version; the learner translates fast, without rereading.
- Review: only differences in phrasing (calques, non-native wording, phrasings to watch); any correct natural alternative counts. Score = phrasings to watch produced naturally / total. Move the entry to "Done" with date, score and the 2–3 phrasings still missed (→ target phrases; cards if real errors).

## 9. Transfer test (every 2–3 weeks)
10–15 {{NATIVE_LANGUAGE}} sentences never seen in the decks, built to trigger the calques worked on in the Translations deck, plus 2–3 decoys. The learner translates fast, without rereading; don't reveal the traps. Score = calques produced / opportunities, per phrase. New calques → reservoir. Record in `progress-log.md` and compare with the previous test.
