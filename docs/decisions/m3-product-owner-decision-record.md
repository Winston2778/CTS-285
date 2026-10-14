# M3 Product Owner Decision Record

## Scenario
StudyTrack release planning under constrained capacity.

## Round 1 — Capacity 13
- ST-01: Create a study task (3 pts)
- ST-02: Mark a study task complete (2 pts)
- ST-03: Recover a missed task (3 pts)
- ST-04: Keyboard-accessible task entry (2 pts)

**Why this release slice was defensible:**
the goal here is to find a way to plan study work and a way to recover their work.

**One intentional deferral and why:**
I deferred ST-05 because it depends on ST-01 and ST-02, and also it can only build after them.it becomes the natural first candidate for the next release, and it unblocks ST-08 (the parent dashboard) later, once that story’s scope and privacy questions are refined.

## Complication
Capacity dropped from 13 to 10 points. Keyboard accessibility testing revealed that task entry cannot reliably be completed with keyboard navigation, so ST-04 became release-critical.

## Revised Release Slice — Capacity 10
- ST-01: Create a study task (3 pts)
- ST-03: Recover a missed task (3 pts)
- ST-04: Keyboard-accessible task entry (2 pts)

### Removed after complication
- ST-02: Mark a study task complete

### Added after complication
- None

**What changed and why:**
Two things changed at once. Capacity fell from 13 to 10 points, and accessibility testing.The second fact changes the status of ST-04. In Round 1 it was a high-value story I chose to include. Now it is a pre-release fix, so it is mandatory and the plan has to be built around it

**Tradeoff accepted:**
I accepted that students can create tasks and recover missed ones in this release, but cannot mark a task complete (ST-02). I gave up part of the planning loop to protect recovery (ST-03), the required accessibility fix (ST-04), and a 2-point buffer. ST-02 is the first story I would bring back

## Transfer to DataMan
Before finalizing your DataMan backlog, review whether any item is high value but not ready, depends on unresolved work, consumes disproportionate effort, or should move because it reduces risk or unlocks other work.
