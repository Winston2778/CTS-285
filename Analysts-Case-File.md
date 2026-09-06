## Analyst's Case File

**CTS 285 · Systems Analysis and Design · Module 1**

| Item | Information |
|---|---|
| **System analyzed** | DataMan (Texas Instruments, 1977) |
| **Feature assigned** | Number Guesser |
| **Source document** | *The Story of DataMan* — manual transcript |
| **Your name** | Latoya Winston |
| **Date** | September 6, 2026 |

---

## How to Fill This Out

Every finding needs evidence. Evidence is an exact quoted phrase from the manual plus the section heading it came from. Cite sections by name — “Number Guesser (Story)” or “Electro Flash · Number Guesser · Wipe Out (Operating Notes).” Do not cite page numbers; the manual carries two numbering systems that do not agree.

Read both registers before you write anything. Part I describes the feature to a child. Part II describes it to an adult. Each contains information the other omits.

If you cannot find evidence for something, do not guess. Put it in Section 8. An unknown you can name is a finding. An assumption you record as fact is an error.

Rows are a format, not a quota. Add rows as your evidence requires.

---

# 1. Purpose

**Why does this feature exist? What problem does it solve for the user?**

| Finding | Evidence (exact quote) | Section |
|---|---|---|
| Number Guesser is an educational game involving number strategy. | “Number Guesser is an educational game of number strategy the whole family will enjoy.” | **Electro Flash · Number Guesser · Wipe Out (Operating Notes)** |
| The feature is intended to make working with numbers enjoyable while helping users sharpen math skills. | “As you play Number Guesser with your family or friends (or just by yourself), you'll be sharpening your math skills.” | **Number Guesser (Story)** |

---

# 2. Users and Roles

**Who interacts with this feature? Where more than one person is involved, name what each one does.**

| Role | What this role does | Evidence (exact quote) | Section |
|---|---|---|---|
| **Player / guesser** | Enters guesses and tries to find the secret number. | “You enter your guess.” | **Number Guesser (Story)** |
| **Family member or friend / competing player** | Takes turns with other players and competes to find the number in the fewest guesses. | “Children can take turns seeing who can find a secret number in the least guesses!” | **Electro Flash · Number Guesser · Wipe Out (Operating Notes)** |
| **DataMan** | Selects the secret number and provides hints about its location. | “DataMan provides a hint by displaying two numbers that the secret number is between.” | **Electro Flash · Number Guesser · Wipe Out (Operating Notes)** |

---

# 3. Inputs

**What information or action enters the system? Include keystrokes, choices, and anything the system refuses to accept.**

| Input | Supplied by | Evidence (exact quote) | Section |
|---|---|---|---|
| **ON key** | Player | “first turn DataMan on with the ON key” | **Electro Flash · Number Guesser · Wipe Out (Operating Notes)** |
| **Number Guesser key** | Player | “then press the [NUMBER GUESSER] key” | **Electro Flash · Number Guesser · Wipe Out (Operating Notes)** |
| **Numeric guess** | Player | “You enter your guess.” | **Number Guesser (Story)** |
| **Number Guesser key again** | Player | “I'll pick a new secret number each time you press [???]” | **Number Guesser (Story)** |

---

# 4. Processing

**What does the system do with the input? Include any rule, limit, or constraint you can support.**

| Rule or behavior | Evidence (exact quote) | Section |
|---|---|---|
| DataMan selects a secret number somewhere between 9 and 100. | “I'll pick a secret number for you to guess. It will be somewhere between 9 and 100.” | **Number Guesser (Story)** |
| After each guess, DataMan provides a two-number hint showing the range containing the secret number. | “As you enter each guess, DataMan provides a hint by displaying two numbers that the secret number is between.” | **Electro Flash · Number Guesser · Wipe Out (Operating Notes)** |
| When the secret number is found, DataMan displays the total number of guesses and provides a light show. | “When the secret number is found, DataMan rewards you with a spectacular 'light show' and displays the total number of guesses that were taken.” | **Electro Flash · Number Guesser · Wipe Out (Operating Notes)** |
| Pressing the Number Guesser key causes DataMan to select a new secret number. | “I'll pick a new secret number each time you press [???]” | **Number Guesser (Story)** |

---

# 5. Outputs

**What information does the system return to the user?**

| Output | When it appears | Evidence (exact quote) | Section |
|---|---|---|---|
| **Two-number hint** | After a guess. | “I'll flash and show you two numbers in my face mask. The secret number is always somewhere between the two numbers I show you.” | **Number Guesser (Story)** |
| **Total number of guesses** | When the secret number is found. | “displays the total number of guesses that were taken.” | **Electro Flash · Number Guesser · Wipe Out (Operating Notes)** |
| **Light show** | When the secret number is found. | “DataMan rewards you with a spectacular 'light show'” | **Electro Flash · Number Guesser · Wipe Out (Operating Notes)** |

---

# 6. Feedback

**How does the system respond to the user's actions? Feedback tells the user how they are doing.**

| Feedback behavior | What it tells the user | Evidence (exact quote) | Section |
|---|---|---|---|
| **Two-number hint** | Tells the player the range in which the secret number lies and helps guide the next guess. | “DataMan provides a hint by displaying two numbers that the secret number is between.” | **Electro Flash · Number Guesser · Wipe Out (Operating Notes)** |
| **Light show** | Signals successful completion after the secret number is found. | “When the secret number is found, DataMan rewards you with a spectacular 'light show'” | **Electro Flash · Number Guesser · Wipe Out (Operating Notes)** |

---

# 7. Observations and Assumptions

**List three statements you were tempted to write as fact but could not fully support. For each, say what evidence you would need.**

| Statement | Observation or assumption? | What evidence would settle it? |
|---|---|---|
| **The secret number is selected randomly.** | Assumption | Both Number Guesser sections say DataMan picks or selects a secret number, but neither explicitly says the selection is random. Evidence needed: an explicit statement that the secret-number selection is random. |
| **The two displayed hint numbers are always the immediate lower and upper bounds around the secret number.** | Assumption | The manual only states that the secret number is between the two displayed numbers. Evidence needed: examples or a rule defining how the two hint numbers are calculated. |
| **A player can enter any number as a guess.** | Assumption | The Number Guesser sections do not specify accepted or rejected guess values. Evidence needed: an operating rule describing valid guess inputs or out-of-range behavior. |

---

# 8. Unknowns and Open Questions

**What could not be determined from the manual? For each, state what you looked for and where you looked.**

| Open question | Where I looked | Why the manual does not answer it |
|---|---|---|
| **How does DataMan choose the secret number within 9–100?** | **Number Guesser (Story); Electro Flash · Number Guesser · Wipe Out (Operating Notes)** | Both sections state that DataMan picks or selects a number in the range, but neither explains the selection method or says whether it is random. |
| **How exactly are the two hint numbers calculated?** | **Number Guesser (Story); Electro Flash · Number Guesser · Wipe Out (Operating Notes)** | Both sections say the secret number is between the two displayed numbers, but neither gives the rule for generating those numbers. |
| **What happens if a player enters a guess outside the 9–100 range?** | **Number Guesser (Story); Electro Flash · Number Guesser · Wipe Out (Operating Notes)** | The sections specify the secret number's range but do not describe validation, rejection, or feedback for an out-of-range guess. |
| **What is the actual symbol printed on the Number Guesser activity key?** | **Number Guesser (Story); Force Out (Story) keypad illustration** | The transcript marks the key as “[???]” rather than identifying its symbol, so the text provided does not establish the key label. |

---

# 9. Cross-Register Note

**This manual documents the same feature twice. Identify one thing the two sections handle differently.**

### What differs:

The Story emphasizes who can play Number Guesser, while the Operating Notes emphasize the educational skills the game is intended to develop.

### Part I says (quote):

> “As you play Number Guesser with your family or friends (or just by yourself), you'll be sharpening your math skills.”

**Section:** *Number Guesser (Story)*

### Part II says (quote), or is silent:

> “Number Guesser helps to teach the important basic concept of number betweeness ... and number logic. The strategy involved in getting to the answer in the fewest tries will help build skills in estimation and averaging.”

**Section:** *Electro Flash · Number Guesser · Wipe Out (Operating Notes)*

### Why this matters to an analyst:

The two registers provide different kinds of information about the same feature. The Story gives context about the players and how the feature can be used, while the Operating Notes give more specific information about its educational purpose. An analyst needs both sections to build a complete description of Number Guesser rather than assuming that one register contains everything.
