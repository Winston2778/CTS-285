# DataMan Requirements Register

> Replace all bracketed prompts with your own project evidence and requirements. Delete the prompts before submitting.

## Project Context

DataMan is a 1977 Texas Instruments handheld math-practice device that is being modernized into a web application. Its primary users are elementary and middle school students, and parents and teachers are secondary users who want to follow student progress. The project addresses the need for students to practice basic arithmetic with immediate feedback, save their work, and practice on their own.

## Evidence Notes

- **E-01 — Source:** DataMan manual, p. 19  
  **Evidence:** DataMan is intended for elementary and middle school students. Parents and teachers help with setup and explanation.

- **E-02 — Source:** DataMan manual, pp. 3, 20  
  **Evidence:** The student enters a problem and an answer. A right answer makes DataMan flash its display lights. A wrong answer shows "EEE" with blinking lights and allows a second try. If the second try is also wrong, DataMan shows the correct result. After 10 problems it displays the number of right answers and the number of problems tried.

- **E-03 — Source:** DataMan manual, pp. 3, 20  
  **Evidence:** Division answers are entered as the whole-number part, and DataMan shows an "r" and then the remainder.

- **E-04 — Source:** DataMan manual, pp. 4, 21  
  **Evidence:** A timer runs during the activity, and the elapsed time is shown in "ticks" of the Atom Clock with the score.



## Functional Requirements

### FR-01
**Requirement:** The system must let a user enter an arithmetic problem and an answer using addition, subtraction, multiplication, or division, and then indicate whether the answer is right or wrong.  
**Source/Rationale:** E-02. Answer Checker is the default mode and the core capability of the product.

### FR-02
**Requirement:** The system must accept a division answer as a whole number and, when the quotient has a remainder, indicate this and display the remainder.  
**Source/Rationale:** E-03. Division with remainders is explicitly handled in the current product.

### FR-03
**Requirement:** The system must display the number of right answers and the number of problems tried after a set of 10 problems.  
**Source/Rationale:** E-02. Score reporting is a core feedback feature.

### FR-04
**Requirement:** The system must let an adult or peer store up to 10 problems and then present them one at a time for the child to answer.  
**Source/Rationale:** DataMan manual, pp. 4, 21 (Memory Bank). It supports teacher/parent-set practice, and the elapsed-time display in E-04 applies to it.

## Non-Functional Requirements

Write at least three non-functional requirements. Each requirement should describe a measurable quality, constraint, or condition the system must satisfy.

### NFR-01
**Requirement:** The system must let a student start and complete a practice session without help from an adult.  
**Source/Rationale:** E-07, E-01. Students often practice on their own, and the intended users are elementary and middle school students. It can be checked by observing a student use the system with no adult assistance. The pass threshold is listed in Q-06.

### NFR-02
**Requirement:** The system must run in a standard web browser without requiring the user to install software.  
**Source/Rationale:** Project constraint: DataMan is being modernized as a web application (instructor feedback on this register). Supported browsers and devices are listed in Q-05.

### NFR-03
**Requirement:** The system must let a student understand how to use each activity from on-screen content alone, without a printed manual.  
**Source/Rationale:** E-07, E-01. A student practicing alone has no adult to explain the activity, and the 1977 product relied on a printed manual (E-01).

## Open Questions / Assumptions
- **Q-01:** Should the modern version keep the 5-minute auto power-off from the 1977 manual (pp. 3, 19)? It saved battery on the handheld, and it is unclear whether a web app needs it.
- **Q-02:** Should the modern version keep the one- or two-digit operand limit and three-digit answer limit (manual p. 20)? They may only reflect 1977 display hardware.

## Final Quality Check

- [x ] Clear enough for another team member to interpret consistently.
- [x ] Supported by evidence, a stakeholder need, or a confirmed project constraint.
- [ x] Testable or verifiable later.
- [ x] Solution-neutral enough for this stage of the project.
- [ x] Focused on one main capability or quality.
- [ x] Classified correctly as functional or non-functional.

- [x] At least four functional requirements are included.
- [x] At least three non-functional requirements are included.
- [x] Every confirmed requirement has a source/rationale.
- [x] Open questions and assumptions are separated from confirmed requirements.
- [ ] The simulation decision record is saved at `docs/decisions/m2-elicitation-decision-record.md`.
- [ ] This file is saved as `docs/requirements.md`, committed, and synced to GitHub.
