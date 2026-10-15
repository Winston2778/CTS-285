# DataMan Product Backlog

## Sources

This backlog uses these files from my repository:

- `docs/requirements.md`
- `docs/decisions/m3-backlog-triage-record.md`
- `docs/decisions/m3-product-owner-decision-record.md`

This backlog uses the current version of `docs/requirements.md`, which includes evidence E-05 to E-07, FR-05, and open questions Q-03 to Q-06.

## Priority Order

1. US-01
2. US-02
3. US-03
4. US-04
5. US-05
6. US-06
7. US-07
8. US-08

## Stories

### US-01 — Immediate right/wrong feedback in the browser

**Requirement ID:** FR-01, NFR-02 (NFR-02 applies as a constraint on this story and every story after it)

**User Story:** As a student, I want to enter an arithmetic problem and my answer and be told right away whether it is right or wrong so that I learn from each attempt.

**Acceptance Criteria:**

- Given I have opened DataMan in a standard web browser, when I start, then I can use it without installing any software.
- Given I am on the answer-checking screen, when I enter an addition, subtraction, multiplication, or division problem and an answer and submit, then the system shows whether the answer is right or wrong without any further action from me.
- Given the system has checked my answer, when it shows the result, then a right result and a wrong result look clearly different.

**Relative Effort:** S — This is the smallest complete flow in the backlog, and every other story builds on it.

**Dependency / Constraint:** None. It is the core capability (evidence E-02). The supported browsers and devices are an open question (Q-05), and Q-02 and Q-03 (digit limits and negative answers) may affect which problems are accepted (see Open Questions Carried Forward).

**Priority:** 1

**Readiness:** Move Forward

**Priority Rationale:** Highest value and lowest uncertainty: it is the core capability of the product, and the instructor stakeholder requires immediate answer feedback in the first usable release. Small effort and no dependencies make it the foundation for the rest of the backlog. Triage item S1 was Move Forward in both rounds.

---

### US-02 — Second try after a wrong answer

**Requirement ID:** FR-01 (the second-try rule comes from evidence E-02 and is not yet written into FR-01)

**User Story:** As a student, I want a second try after a wrong answer, and to be shown the correct result if my second try is also wrong, so that I can correct my mistake and still learn the answer.

**Acceptance Criteria:**

- Given I answered a problem wrong, when the system shows the wrong result, then it offers me a second try on the same problem.
- Given I am on my second try, when I submit a right answer, then the system shows the answer as right.
- Given I am on my second try, when I submit a wrong answer, then the system shows me the correct result.
- Given I have used my second try, when the result is shown, then no further tries are offered on that problem.

**Relative Effort:** S — It adds one repeat step to the flow in US-01 and needs no new screens or data.

**Dependency / Constraint:** Depends on US-01. The second-try rule needs to be written into FR-01 or its own requirement (see Open Questions Carried Forward).

**Priority:** 2

**Readiness:** Move Forward

**Priority Rationale:** High value, small effort, and low risk. It extends the feedback loop from US-01 so a mistake becomes a learning step, and it can only follow US-01. Triage item S5 was Move Forward in both rounds.

---

### US-03 — Division answers with remainders

**Requirement ID:** FR-02

**User Story:** As a student, I want to enter a division answer as a whole number and see the remainder so that I can practice division problems that do not divide evenly.

**Acceptance Criteria:**

- Given a division problem has a remainder, when I enter the whole-number part as my answer, then the system accepts the answer and indicates that a remainder exists.
- Given a division problem has a remainder, when the system shows the result, then it displays the remainder.
- Given a division problem has no remainder, when the system shows the result, then no remainder is displayed.

**Relative Effort:** M — It is larger than US-01 and US-02 because the rules for judging a division answer with a remainder are not settled.

**Dependency / Constraint:** Depends on US-01. FR-02 does not say whether the student must also enter the remainder to be marked right.

**Priority:** 3

**Readiness:** Refine

**Priority Rationale:** It completes division, one of the four operations in FR-01, and the current product handles it explicitly (E-03), so the value is solid. It ranks below US-01 and US-02 because it is not needed for the first feedback loop and its correctness rule is unresolved. The rule should be settled before the story is committed. The triage record has no decision for this requirement.

---

### US-04 — Score after 10 problems

**Requirement ID:** FR-03

**User Story:** As a student, I want to see how many answers I got right out of how many problems I tried after a set of 10 problems so that I know how I did.

**Acceptance Criteria:**

- Given I have completed a set of 10 problems, when the set ends, then the system displays the number of right answers.
- Given I have completed a set of 10 problems, when the set ends, then the system also displays the number of problems tried.
- Given the system displays my score, when I compare it to the results shown during the set, then the number of right answers equals the number of answers the system marked right.

**Relative Effort:** S — It adds one summary display at the end of a set using results that already exist.

**Dependency / Constraint:** Depends on US-01. How a second-try answer from US-02 is counted follows whatever the system marks right, so the story does not need a separate scoring rule.

**Priority:** 4

**Readiness:** Move Forward

**Priority Rationale:** Score reporting is a core feedback feature (E-02) with small effort and low risk. It adds value once answers can be checked, but the first release does not depend on it, so it follows the feedback stories. The triage record has no decision for this requirement.

---

### US-05 — Understand each activity from on-screen content

**Requirement ID:** NFR-03

**User Story:** As a student practicing alone, I want to understand how to use each activity from on-screen content so that I do not need a printed manual or an adult to explain it.

**Acceptance Criteria:**

- Given a first-time student opens an activity, when they use it with no printed manual and no adult explanation, then they can start the activity.
- Given the pass threshold for NFR-03 is defined, when students are observed using each activity, then the observed results meet that threshold.

**Relative Effort:** M — The work touches every activity and can only be checked by watching students use them.

**Dependency / Constraint:** Depends on US-01 to US-04 existing. The pass threshold is an open question (Q-06; see Open Questions Carried Forward).

**Priority:** 5

**Readiness:** Refine

**Priority Rationale:** Students often practice on their own (E-07), and the 1977 product relied on a printed manual (E-01), so this matters for the intended users. It ranks after the activity stories because it can only be checked once those activities exist, and its second criterion cannot be tested until the threshold is defined. The triage record has no decision for this requirement.

---

### US-06 — Complete a practice session without adult help

**Requirement ID:** NFR-01

**User Story:** As a student, I want to start and complete a practice session without help from an adult so that I can practice on my own.

**Acceptance Criteria:**

- Given a student has opened DataMan, when they start a practice session with no adult assistance, then the session starts.
- Given a student has started a session, when they continue with no adult assistance, then they can complete the session.
- Given the pass threshold for NFR-01 is defined, when students are observed using the system with no adult assistance, then the observed results meet that threshold.

**Relative Effort:** M — It spans the whole session, from start to finish, and is checked by observation.

**Dependency / Constraint:** Depends on US-01, US-04, and US-05. The pass threshold is an open question (Q-06; see Open Questions Carried Forward).

**Priority:** 6

**Readiness:** Refine

**Priority Rationale:** Independent practice is a stated need for the intended users (E-01, E-07), but it depends on the activities and on-screen guidance being in place and cannot be fully tested until its threshold exists. The triage record has no decision for this requirement.

---

### US-07 — Save practice progress between sessions

**Requirement ID:** FR-05

**User Story:** As a student, I want my practice progress saved so that I can leave a practice session and return later without losing what I already did.

**Acceptance Criteria:**

- Given I have recorded progress in a practice session, when I leave the session and return later, then my previously recorded progress is still available.
- Given I return to a practice session, when I look at my progress, then none of the progress I recorded before leaving is missing.

**Relative Effort:** L — It adds saved data that lasts beyond a single session, and it depends on how the system recognizes a returning student, which is not decided.

**Dependency / Constraint:** The account/session approach is not ready (triage record), and it is blocking (Q-04). It needs a decision on how a returning student is recognized before criteria about whose progress is shown can be written. It would also need to be split before commitment.

**Priority:** 7

**Readiness:** Defer

**Priority Rationale:** High value, because students want to keep their work (E-05) and the project context names saving work as a need. It is large, and it depends on an identity/session approach that is not ready, so the risk of rework is high if it is committed now. Triage item S2 was Refine in Round 1 and moved to Defer after the session approach proved not ready. It should return for refinement once that decision is made.

---

### US-08 — Parent or teacher stores problems for a child

**Requirement ID:** FR-04

**User Story:** As a parent or teacher, I want to store up to 10 problems and have them presented one at a time to a child so that I can set practice for the child to work through.

**Acceptance Criteria:**

- Given I am an adult setting up practice, when I enter problems, then the system lets me store up to 10 problems.
- Given problems are stored, when the child starts the practice, then the system presents the stored problems one at a time.
- Given a stored problem is presented, when the child submits an answer, then the system shows whether it is right or wrong, as in US-01.

**Relative Effort:** L — It adds a second kind of user, storing problems, and a new way of running a session, so it is among the largest stories in the backlog.

**Dependency / Constraint:** Depends on US-01 and US-04. It is unresolved whether stored problems must last between sessions, which would tie it to US-07 and the unresolved session approach (Q-04). Splitting it into "store problems" and "present problems" should be considered. Evidence E-04 says an elapsed-time display applies to this mode, but no requirement covers the timer yet.

**Priority:** 8

**Readiness:** Defer

**Priority Rationale:** Medium value for secondary users, but large and uncertain, and not required for the first usable release. It ranks below US-07 because the value of saved progress is higher and more directly stated by students (E-05). The unresolved session question adds risk here too, in line with the triage deferral of session-dependent work.

---

## Open Questions Carried Forward

- **Q-01:** Whether to keep the 5-minute auto power-off from the 1977 manual. No story exists for it because the question is unresolved.
- **Q-02:** Whether to keep the one- or two-digit operand limit and three-digit answer limit. No story or criterion uses a limit until this is decided; it may affect US-01 and US-03.
- **Q-03:** Whether to keep the restriction against negative answers. No criterion mentions negative answers until this is decided; it may affect US-01.
- **Q-04:** How the system recognizes a student who returns to saved progress is not decided. This one decision blocks US-07 and US-08, and it would also be needed before any adult progress summary (E-06) can be written as a requirement.
- **Q-05:** Which web browsers and devices must be supported. US-01 does not name a browser list until it is answered.
- **Q-06:** The pass threshold for observing a student who works without adult help (NFR-01, and the same kind of threshold applies to NFR-03). US-05 and US-06 are marked Refine until it is answered.
- **Second-try rule (E-02):** It is in the evidence but not in any functional requirement. US-02 traces to FR-01 until a requirement is added.
- **Timer (E-04):** No requirement covers the elapsed-time display, so it appears only as a note on US-08.
- **Remainder correctness (FR-02):** It is unclear whether the student must enter the remainder to be marked right, which is why US-03 is marked Refine.
- **Adult progress information (E-06, triage S4):** Adults want clearer and shorter information about how a student is progressing, but no functional requirement states it, so no story exists. It needs a validated requirement, and it would depend on US-07 for the progress data. Triage moved S4 from Refine to Defer for the same reason.
- **Triage items with no requirement (S3, S6):** The decorative theme selector and the advanced analytics dashboard have no matching requirement in `docs/requirements.md`, so neither became a story.

## Revisions After Triage and Release Planning

**From the triage record**

- US-01 — Kept as the top priority — Triage record: S1 (immediate answer feedback) stayed Move Forward, and the instructor stakeholder requires it for the first usable release.
- US-02 — Kept as the second priority — Triage record: S5 (retry after an incorrect response) stayed Move Forward.
- US-07 — Marked Defer — Triage record: S2 (preserve progress between sessions) moved from Refine to Defer because the account/session approach is not ready.
- US-08 — Marked Defer, ranked last — Triage record: it faces the same session uncertainty that moved S2 and S4 to Defer.
- No story for S4 — Triage record: S4 moved from Refine to Defer, and it has evidence (E-06) but no functional requirement.
- No stories for S3 or S6 — Triage record: both were deferred, and neither traces to a requirement.

**From the Product Owner decision record (StudyTrack release planning)**

- US-01 — Carries NFR-02 (browser, no install) as a constraint instead of leaving it as a separate later story — Product Owner record: the accessibility finding turned ST-04 from a nice-to-have into a pre-release requirement, so a constraint that every user depends on is built into the first slice.
- US-03, US-05, and US-06 — Marked Refine instead of Move Forward — Product Owner record: the Transfer to DataMan review asks whether an item is not ready or depends on unresolved work. The remainder rule (FR-02) and the missing pass thresholds (NFR-01, NFR-03) make these not ready to commit.
- US-07 and US-08 — Kept as Defer — Product Owner record: both are large and depend on unresolved work (the account/session approach), so they would consume disproportionate effort in a first release. US-07 is the clearest case of high value that is not ready.
- US-01 — Kept first — Product Owner record: ST-01 was protected because everything depended on it, and US-01 plays the same role here by unlocking US-02 to US-08.
- The account/session decision is recorded as an open question (Q-04) — Product Owner record: resolving work that unlocks other work reduces risk. That decision would unlock US-07, US-08, and the adult progress information in E-06.

## Before You Submit

- [x] Every story has all eight required fields: Story ID, Requirement ID, User Story, Acceptance Criteria, Relative Effort, Dependency / Constraint, Priority, Priority Rationale.
- [x] Every Requirement ID exists in `docs/requirements.md`.
- [x] Each acceptance criterion states a result another person can observe and check.
- [x] The story blocks follow the Priority Order list.
- [x] Large or uncertain stories are marked Refine or Defer, not hidden as Move Forward.
- [x] No story or criterion names a framework, database, or screen layout.
- [ x] The file path is exactly `docs/product-backlog.md`.
- x[ ] The file renders correctly on GitHub.
- [ x] The change is committed with a message that describes it.
