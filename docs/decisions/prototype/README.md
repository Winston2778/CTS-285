# DataMan text prototype (Module 4)

## What this prototype tests
Slice: **US-01 Immediate right/wrong feedback** (FR-01) and **US-02 Second try
after a wrong answer** (FR-06), the Priority 1 and 2 stories in
`docs/product-backlog.md` (both Move Forward, effort S). One complete path:
student gives a problem -> enters an answer -> sees right/wrong -> if wrong,
gets one more try on the same problem -> if wrong again, is shown the correct
result and the problem closes.

> **Design question:**
> Can the checking and second-try rules live in business logic, with the
> per-problem attempt state held behind a data boundary, so the interface only
> displays what the logic returns? And what state does a "second try" really need?

Traceability: **FR-01** and **FR-06** (evidence **E-02**, DataMan manual pp. 3, 20),
plus constraint **NFR-02** (not testable in text). Open questions touched: Q-02,
Q-03, Q-04, Q-05.

Related records: `docs/product-backlog.md`, `docs/requirements.md`,
`docs/decisions/m3-product-owner-decision-record.md`,
`docs/decisions/m3-backlog-triage-record.md`.

## Layers and where to find them
| Layer | File | Responsibility |
|---|---|---|
| Text interface | `app.py` | Prompts, reads input, prints right/wrong. No rules. |
| Business logic | `dataman/logic.py` | Parse problem, compute correct result, judge answers, enforce 2 tries. No print/input. |
| Stubbed data | `dataman/store.py` | In-memory add/get/save/list_all of problem records. No arithmetic. |
| Tests | `test_logic.py` | Runs the rules with no interface. |

Run: `python app.py` (try `12 + 5`, answer `18`, then `17`). Tests: `python test_logic.py`.

## State represented deliberately
Stored per problem: `left`, `op`, `right`, `attempts` (list of answers), `outcome`
(`None` / `right` / `revealed`). **Derived, not stored:** tries left. The record
is what lets the system remember the problem between the first and second
submission.

## Acceptance criteria demonstrated
| Backlog criterion | Where shown |
|---|---|
| US-01: enter problem and answer, system shows right/wrong with no further action | test `us01_*`; app session |
| US-01: right and wrong look clearly different | app prints `✔ RIGHT` vs `✘ WRONG` (text stand-in) |
| US-02: wrong answer offers a second try on the same problem | test `us02_wrong_first_*` |
| US-02: right on second try shows right | test `us02_right_on_second_try` |
| US-02: wrong on second try shows the correct result | test `us02_two_wrong_*` |
| US-02: no further tries after the second | same test (third submit is rejected) |

## Intentionally stubbed / not tested
- Persistence, student identity, database-generated ids (see Q-04).
- US-01 "no install, standard browser" and Q-05 (supported browsers): meaningless in a text prototype; first testable in Module 5.
- Sets of 10 and scoring (US-04), division with remainders (US-03), digit limits (Q-02), timer (E-04), adult-entered problems (US-08).

## Sample run
Typed input follows each prompt. This session shows a wrong answer then a right
one (US-01, US-02), a second miss that reveals the result (US-02), bad input that
does not use up a try, and an unsupported division problem.

```
DataMan prototype. Practice arithmetic. Type 'quit' to leave.
Problem: 12 + 5
  Your answer (2 tries left): 18
  ✘ WRONG
  Try again on the same problem.
  Your answer (1 try left): 17
  ✔ RIGHT
Problem: 6 x 7
  Your answer (2 tries left): 40
  ✘ WRONG
  Try again on the same problem.
  Your answer (1 try left): abc
  ! Enter your answer as a whole number.
  Your answer (1 try left): 41
  ✘ WRONG
  The correct result is 42.
Problem: 7 / 2
  ! Division with a remainder is not supported yet (US-03).
Problem: quit
```

## What running it revealed (revisions and unresolved issues)
1. **The backlog's effort note for US-02 is wrong.** It says US-02 "needs no new
   screens or data." It does need new *state*: the system must remember the
   problem and attempts so far between two submissions. In a browser, each
   submission is a separate request, so Module 5 must decide where that memory
   lives (browser session, hidden form field, or saved record). That pushes on
   the unresolved identity/session question (Q-04) even though US-02 is marked
   Move Forward. **Unresolved:** update US-02's effort/dependency note.
2. **Information-leak risk found and designed out.** The correct result must not
   be shown after the first wrong answer. `submit_answer` returns
   `correct_result` only once the problem is revealed, so no interface can leak it.
3. **Requirement gap, assumption made:** FR-06 says a second try follows a wrong
   answer but not whether a non-number entry ("abc") counts as one. The prototype
   assumes it does not use up a try. Confirm and add to FR-06. FR-06 also does
   not say the second try is on the *same* problem; E-02 and the US-02 criteria do.
4. **FR-01 and FR-02 pull against each other.** FR-01 accepts division problems,
   and E-03 shows the original DataMan accepted ones like 7 / 2 (whole-number
   answer, then "r" and the remainder). FR-02 requires that, but does not say
   whether the student must also enter the remainder to be right (US-03 is
   Refine). Until that is settled, "right" has no definition for such problems,
   so this prototype rejects them at entry. That is a deliberate stub, not the
   final behavior. Resolve through FR-02/US-03.
5. **Q-02 and Q-03 not enforced.** The logic imposes no digit limits (Q-02) and
   allows negative operands and answers (Q-03). These are placeholders, not
   decisions; the 1977 limits may only reflect display hardware.
6. **Who supplies the problem?** US-01 has the student type both problem and
   answer. The logic accepts a problem from any source, so US-08 (adult-stored
   problems) can reuse it unchanged.
7. **Score groundwork (US-04):** storing `outcome` per problem means a score can
   later be derived without changing this slice; `revealed` counts as not right.

## Carries into Module 5
`dataman/logic.py` moves to Flask unchanged. `app.py` is replaced by routes and
templates; `store.py` by a database-backed class with the same four methods.
Carry forward: items 1, 3, 4 and 5 above as open implementation questions.
