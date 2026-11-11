# Reviewer prompts

Use them as sub-agent tasks, or, without sub-agents, give them to the learner to paste into a **new chat** (a fresh instance that hasn't seen the answers) with the material, then have them paste the answer back.

## 1. Blind reviewer (paragraphs only, no answers)

> You are a meticulous {{TARGET_VARIETY}} copy-editor. Here are short paragraphs written for learners; they may contain deliberate mistakes, but you are not told which. For each paragraph, list every error you find, of any kind (grammar, agreement, -s, plurals, possessives, tenses, spelling, articles, prepositions, word choice, word order, punctuation, unnatural phrasing), with the exact segment and the correction. List separately anything acceptable in standard {{TARGET_VARIETY}} but debatable (collective nouns, informal usage…). Flag any paragraph whose sentences don't follow on from each other. Do not rewrite the paragraphs.

## 2. Answer-key reviewer (cards with corrections)

> You are a meticulous {{TARGET_VARIETY}} grammar expert reviewing "find the error" cards for {{NATIVE_LANGUAGE}}-speaking learners. Each card has a paragraph with 0–4 deliberate errors, the list of corrections (original → correction, rule) and the corrected paragraph. For each card check: (1) is each original unambiguously wrong in standard {{TARGET_VARIETY}}, is the correction right, is the rule right and clear? (2) is the corrected paragraph entirely correct and natural — list any remaining error of any kind; (3) is the paragraph coherent (one small situation)? Report only cards with a problem, with a suggested fix. Be strict.
