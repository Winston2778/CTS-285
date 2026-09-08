
Analyst's Case File
CTS 285 · Systems Analysis and Design · Module 1
System analyzed	DataMan (Texas Instruments, 1977)

Feature assigned	Number Guesser

Source document	The Story of DataMan — manual transcript

Your name	Latoya Winston

Date	9/08/26
How to fill this out
Every finding needs evidence. Evidence is an exact quoted phrase from the manual plus the section heading it came from. Cite sections by name — “Number Guesser (Story)” or “Electro Flash · Number Guesser · Wipe Out (Operating Notes).” Do not cite page numbers; the manual carries two numbering systems that do not agree.
Read both registers before you write anything. Part I describes the feature to a child. Part II describes it to an adult. Each contains information the other omits.
If you cannot find evidence for something, do not guess. Put it in Section 8. An unknown you can name is a finding. An assumption you record as fact is an error.
Rows are a format, not a quota. Add rows as your evidence requires.

1. Purpose
Why does this feature exist? What problem does it solve for the user?
Finding	Evidence (exact quote)	Section
Number Guesser is an educational game designed to give players practice with number strategy and mathematics.	"Number Guesser is an educational game of number strategy the whole family will enjoy."	Electro Flash · Number Guesser · Wipe Out (Operating Notes)
The game also provides practice in mathematical reasoning and strategy while making numbers enjoyable.	As you play Number Guesser with your family or friends (or just by yourself), you'll be sharpening your math skills."	Number Guesser (Story)
		
2. Users and Roles
Who interacts with this feature? Where more than one person is involved, name what each one does — the person who sets something up and the person who responds to it are different roles even when they are the same human being.
Role	What this role does	Evidence (exact quote)	Section
Player / guesser	Enters guesses and attempts to find the secret number.	"You enter your guess."	Number Guesser (Story)
Family member or friend / competing player	Takes turns with other players and competes to find the secret number in the fewest guesses.	"Children can take turns seeing who can find a secret number in the least guesses!"	Electro Flash · Number Guesser · Wipe Out (Operating Notes)
DataMan	Selects the secret number and provides hints showing the range in which the secret number is located.	"As you enter each guess, DataMan provides a hint by displaying two numbers that the secret number is between."	Electro Flash · Number Guesser · Wipe Out (Operating Notes)
			
3. Inputs
What information or action enters the system? Include keystrokes, choices, and anything the system refuses to accept.
Input	Supplied by	Evidence (exact quote)	Section
ON key	player	"first turn DataMan on with the ON key"	DataMan on with the ON key"
Electro Flash · Number Guesser · Wipe Out (Operating Notes)
Number
Guesser Key
	player	"then press the [NUMBER GUESSER] key"	Electro Flash · Number Guesser · Wipe Out (Operating Notes)
Numeric guess	player	"You enter your guess."	Number Guesser (Story)
Number Guesser key to begin another round	player	"I'll pick a new secret number each time you press [???]"	Number Guesser (Story)
4. Processing
What does the system do with the input? Include any rule, limit, or constraint you can support.
Rule or behavior	Evidence (exact quote)	Section
DataMan selects a secret number within the stated range.	"I'll pick a secret number for you to guess. It will be somewhere between 9 and 100."	Number Guesser (Story)
After each guess, DataMan displays two numbers that identify a range containing the secret number.	"As you enter each guess, DataMan provides a hint by displaying two numbers that the secret number is between."	Electro Flash · Number Guesser · Wipe Out (Operating Notes)
The game continues until the player finds the secret number, and DataMan counts the guesses.	"When the secret number is found, DataMan rewards you with a spectacular 'light show' and displays the total number of guesses that were taken."	Electro Flash · Number Guesser · Wipe Out (Operating Notes)
A new round uses a new secret number when the Number Guesser key is pressed again.	"I'll pick a new secret number each time you press [???]"	Number Guesser (Story)
5. Outputs
What information does the system return to the user?
Output	When it appears	Evidence (exact quote)	Section
Two-number hint	After the player enters a guess.	"I'll flash and show you two numbers in my face mask. The secret number is always somewhere between the two numbers I show you."	Number Guesser (Story)
Total number of guesses	When the secret number is found.	"displays the total number of guesses that were taken."	Electro Flash · Number Guesser · Wipe Out (Operating Notes)
Light show	When the secret number is found.	"DataMan rewards you with a spectacular 'light show'"	Electro Flash · Number Guesser · Wipe Out (Operating Notes)
6. Feedback
How does the system respond to the user's actions? Feedback tells the user how they are doing. An output returns information; feedback comments on it. If you think one behavior is both, record it once and say why.
Feedback behavior	What it tells the user	Evidence (exact quote)	Section
Two-number hint	Tells the player the range containing the secret number and helps guide the next guess.	"DataMan provides a hint by displaying two numbers that the secret number is between."	Electro Flash · Number Guesser · Wipe Out (Operating Notes)
Light show	Signals that the player successfully found the secret number and provides a reward for completing the game.	"When the secret number is found, DataMan rewards you with a spectacular 'light show'"	Electro Flash · Number Guesser · Wipe Out (Operating Notes)
			
7. Observations and Assumptions
List three statements you were tempted to write as fact but could not fully support. For each, say what evidence you would need.
Statement	Observation or assumption?	What evidence would settle it?
The secret number is selected randomly.	Assumption	Both Number Guesser sections say DataMan picks or selects a secret number, but neither explicitly says that the selection is random. Evidence needed: an explicit statement that the secret-number selection is random.
The two displayed hint numbers are always the immediate lower and upper bounds around the secret number.	Assumption	The manual only states that the secret number is between the two displayed numbers. Evidence needed: examples or a rule defining how the two hint numbers are calculated.
A player can enter any number as a guess.	Assumption	The Number Guesser sections do not specify which guess values are accepted or rejected. Evidence needed: an operating rule describing valid guess inputs or what happens when a player enters a value outside the allowed range.
8. Unknowns and Open Questions
What could not be determined from the manual? For each, state what you looked for and where you looked, so a reader knows the gap is real and not merely unsearched.
Open question	Where I looked	Why the manual does not answer it
How does DataMan choose the secret number within 9–100?	Number Guesser (Story); Electro Flash · Number Guesser · Wipe Out (Operating Notes)	Both sections state that DataMan picks or selects a number in the range, but neither explains the selection method or says whether it is random.
How exactly are the two hint numbers calculated?	Number Guesser (Story); Electro Flash · Number Guesser · Wipe Out (Operating Notes)	Both sections say the secret number is between the two displayed numbers, but neither gives the rule for generating those numbers.
What happens if a player enters a guess outside the 9–100 range?	Number Guesser (Story); Electro Flash · Number Guesser · Wipe Out (Operating Notes)	The sections specify the secret number's range but do not describe validation, rejection, or feedback for an out-of-range guess.
9. Cross-Register Note
This manual documents the same feature twice. Identify one thing your assigned feature's two sections handle differently — something one section states and the other omits, or something the two describe in ways that do not match.
What differs:
The Story gives information about playing Number Guesser with family, friends, or alone, while the Operating Notes give a more specific explanation of the educational concepts and strategy involved.
Part I says (quote):

"As you play Number Guesser with your family or friends (or just by yourself), you'll be sharpening your math skills."
Part II says (quote), or is silent:

Number Guesser helps to teach the important basic concept of number betweeness ... and number logic. The strategy involved in getting to the answer in the fewest tries will help build skills in estimation and averaging."
Why this matters to an analyst:


The Story provides player-facing information about who can play and how the game is experienced, while the Operating Notes provide a more detailed explanation of the educational purpose and strategy. Reading both sections gives a more complete system model and prevents the analyst from missing information contained in only one register.
Before you submit
☐	Every finding has a quoted phrase, not a paraphrase.
☐	Every quote names the section it came from.
☐	I cited section headings, not page numbers.
☐	I read both Part I and Part II before writing.
☐	Section 8 is not empty.
☐	Nothing in Sections 1–6 is a conclusion I could not support.
