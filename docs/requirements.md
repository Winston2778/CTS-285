# DataMan Requirements Register

> Replace all bracketed prompts with your own project evidence and requirements. Delete the prompts before submitting.

## Project Context

[In 2–4 sentences, identify the DataMan modernization goal, the primary users, and the problem the project is trying to solve.]

## Evidence Notes

Use at least four concise evidence statements. Label the source of each.

- **E-01 — Source:** The system must let a user enter an arithmetic problem and an answer using addition, subtraction, multiplication, or division, and then indicate whether the answer is right or wrong.[]  
  **Evidence:** [E-02. Answer Checker is the default mode and the core capability of the product.]

- **E-02 — Source:** [accept a division answer as a whole number and, when the quotient has a remainder, indicate this and display the remainder.]  
  **Evidence:** [E-03. Division with remainders is explicitly handled in the current product.]

- **E-03 — Source:** [DataMan manual, pp. 3, 20  ]  
  **Evidence:** [Division answers are entered as the whole-number part, and DataMan shows an "r" and then the remainder.
]

- **E-04 — Source:** [DataMan manual, pp. 4, 21]  
  **Evidence:** [let a user enter an arithmetic problem and an answer using addition, subtraction, multiplication, or division, and then indicate whether the answer is right or wrong]

[Add additional evidence notes if needed.]

## Functional Requirements

Write at least four functional requirements. Each requirement should describe a capability or behavior the system must provide.

### FR-01
**Requirement:** The system must [let a user enter an arithmetic problem and an answer using addition, subtraction, multiplication, or division, and then indicate whether the answer is right or wrong].  
**Source/Rationale:** [E-02. Answer Checker is the default mode and the core capability of the product.
]

### FR-02
**Requirement:** The system must [accept a division answer as a whole number and, when the quotient has a remainder, indicate this and display the remainder.].  
**Source/Rationale:** [E-03. Division with remainders is explicitly handled in the current product]

### FR-03
**Requirement:** The system must [display the number of right answers and the number of problems tried after a set of 10 problems].  
**Source/Rationale:** [E-02. Score reporting is a core feedback feature.]

### FR-04
**Requirement:** The system must [The system must let an adult or peer store up to 10 problems and then present them one at a time for the child to answer].  
**Source/Rationale:** [DataMan manual, pp. 4, 21 (Memory Bank). It supports teacher/parent-set practice and several games, and the elapsed-time display in E-04 applies to it.]

[Add additional functional requirements if needed.]

## Non-Functional Requirements

Write at least three non-functional requirements. Each requirement should describe a measurable quality, constraint, or condition the system must satisfy.

### NFR-01
**Requirement:** The system must [turn itself off after 5 minutes without user input].  
**Source/Rationale:** [DataMan manual, pp. 3, 19 (power saver). The manual says "about 5 minutes," so the exact tolerance is listed in Q-04.]

### NFR-02
**Requirement:** The system must [accept operands of one or two digits only and must support answers of up to three digits.].  
**Source/Rationale:** [DataMan manual, p. 20. This is a stated constraint of the current product. Whether to keep it is listed in Q-02.]

### NFR-03
**Requirement:** The system must [ reject subtraction input that would produce a negative result].  
**Source/Rationale:** [DataMan manual, p. 20. This is a stated constraint of the current product. Whether to keep it is listed in Q-02.]

[Add additional non-functional requirements if needed.]

## Open Questions / Assumptions

Do not turn an unsupported idea into a confirmed requirement. Record unresolved items here until evidence supports a decision.

- **Q-01:** [What platform does the modernized DataMan target?]
- **Q-02:** [What is the acceptable tolerance for the auto-off delay in NFR-01?]

[Add or remove items as appropriate.]

## Final Quality Check

Before submitting, confirm that each requirement is:

- [ x] Clear enough for another team member to interpret consistently.
- [ x] Supported by evidence, a stakeholder need, or a confirmed project constraint.
- [x ] Testable or verifiable later.
- [x ] Solution-neutral enough for this stage of the project.
- [x ] Focused on one main capability or quality.
- [ x] Classified correctly as functional or non-functional.

Also confirm:

- [ x] At least four functional requirements are included.
- [ x] At least three non-functional requirements are included.
- [ x] Every confirmed requirement has a source/rationale.
- [x ] Open questions and assumptions are separated from confirmed requirements.
- [ ] The simulation decision record is saved at `docs/decisions/m2-elicitation-decision-record.md`.
- [ ] This file is saved as `docs/requirements.md`, committed, and synced to GitHub.
