# Find the error — an Anki method for the mistakes you *know* but keep making

After months of cloze cards, my English mistakes didn't go away: I knew the rules, I passed the cards, and I still wrote "he work" and "several option" in real emails. Cloze cards trained me to answer the card, not to *notice* the error in context.

So I switched to **"find the error" cards**: short, coherent paragraphs that contain **0 to 4 real mistakes taken from my own writing**, mixed together. I read the paragraph, correct it aloud, then flip the card.

In my case, the rate of correct -s in obligatory contexts (third-person verbs, plural nouns, possessives) in my own texts went from **60% (18/30)** to **83–100%** within about three weeks. One learner, no control group: take it as a data point, not a study.

## What's in this repo

| Folder | What it is | For whom |
|---|---|---|
| [`prompt/`](prompt/) | A prompt to paste into **any AI** (ChatGPT, Claude, Gemini, Mistral…). It explains the method, asks you a few questions and guides you step by step. | Everyone |
| [`claude-skill/`](claude-skill/) | A **Claude skill** that sets up a Claude Project running the whole method (your error list, measurements and back-translations stay in the Project, so nothing to copy-paste between chats). | Claude users |
| [`decks/`](decks/) | **Chasse au -s (francophones)**: ready-made cards on the -s (missing or extra), for French speakers learning English. Two levels: **easy** (200 short cards) and **standard** (200 longer paragraphs). | French speakers |

## The method in short

1. **Write** something real (default: 10 minutes, no rereading).
2. **Active correction in 3 rounds**: the AI only marks the passages and the category of error; you fix them. Then a hint and "why is it wrong?". Only then the answers and an annotated version.
3. **Sort the mistakes**:
   - fixed alone or with a hint → **find-the-error** cards (you know the rule; you need to *spot* it);
   - unknown word → cloze card;
   - calque (word-for-word translation from your language) you couldn't fix → **translation** card.
4. **Random number of errors per card**: 20% of cards have none, 40% one, 20% two, 10% three, 10% four. After each error you find, there is always a 50% chance that another one remains, so you can never stop looking early.
5. **Back-translation** a few days later: you translate your own text back from your native language, to check that the natural phrasings stuck.
6. **Measure on new texts only**: the rate of your "signature error" and calques per 100 words. Anki success rates don't count.

## How to use

### Any AI: the prompt
Open [`prompt/find-the-error-coach-prompt.md`](prompt/find-the-error-coach-prompt.md), copy everything from "PROMPT — copy from here", paste it as the first message of a new chat, and follow the AI. It gives you a **STATE block** at the end of each session: save it and paste it next time with the prompt (AIs don't remember between chats).

### Claude: the skill
1. In Claude, make sure **Code execution and file creation** is on.
2. **Customize → Skills → + → Create skill → Upload a skill**, and choose [`claude-skill/find-the-error-setup.zip`](claude-skill/find-the-error-setup.zip) (don't unzip it).
3. Create a **Project**, open a chat in it and write: *"Set up the find-the-error method"*.
4. Follow the checklist at the end: paste the Project instructions, add the generated documents to the Project, import the starter deck into Anki.
5. Start a new chat in the Project and type **"topic"**, or paste something you wrote.

### The -s decks (French speakers)
Two levels, same error types. **Start with easy**; move to standard when easy feels too simple.

| Deck | Cards | Download | Browse the cards |
|---|---|---|---|
| **Easy**: 1–3 short sentences, simple English | 200 | [`Chasse-au-s-francophones-easy.apkg`](decks/Chasse-au-s-francophones-easy.apkg) | [preview](decks/Chasse-au-s-easy-apercu.md) |
| **Standard**: 3–5 sentence paragraphs, richer English | 200 | [`Chasse-au-s-francophones.apkg`](decks/Chasse-au-s-francophones.apkg) | [preview](decks/Chasse-au-s-apercu.md) |

Open the `.apkg` with Anki (desktop, AnkiDroid or AnkiMobile).
- Each deck: 300 errors, distribution 40/80/40/20/20 (0 to 4 errors per card), British English.
- Error types taken from my own mistakes: missing third-person -s (including after *each / every / nobody / one of*, -ing subjects, long subjects, relative clauses, *if / when*), extra -s (plural subjects, after modals, *does / did*, *to*, *let / make*), missing plurals after numbers and quantifiers, extra -s on uncountables and adjectives (*informations*, *differents*, *a two-years contract*), *has / have*, *is / are*, *don't / doesn't*, possessives.
- Tags `erreurs::N` (number of errors) and `type::…` if you want to filter.
- Review: read the paragraph and say the corrected version **before** flipping. Press "Again" if you missed an error or corrected something that was right.

Found a wrong card? Open an issue with the card's first words.

## License
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/): you can share and adapt everything here, including commercially, as long as you give credit.
