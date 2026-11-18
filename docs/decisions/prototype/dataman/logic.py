"""Business logic layer: US-01 (immediate right/wrong feedback) and
US-02 (second try after a wrong answer, then show the correct result).

No print(), no input(), no knowledge of the interface. Every function takes the
store as a parameter so the rules run (and are tested) without the text
interface, and can be reused unchanged by Flask.

STATE DECISION: the second try means the system must remember something between
two submissions. That memory is the problem record: its `attempts` list and its
`outcome`. Tries left are DERIVED (MAX_TRIES - attempts used), not stored.

    outcome None        -> still open (0 or 1 attempts used)
    outcome "right"     -> student answered correctly (on try 1 or try 2)
    outcome "revealed"  -> two wrong answers; correct result was shown; closed
"""
import re

MAX_TRIES = 2
RIGHT = "right"
WRONG = "wrong"
REVEALED = "revealed"

_PROBLEM = re.compile(r"^\s*(-?\d+)\s*([+\-*/x\u00d7\u00f7])\s*(-?\d+)\s*$", re.I)
_OPS = {"+": "+", "-": "-", "*": "*", "x": "*", "\u00d7": "*", "/": "/", "\u00f7": "/"}


class RuleError(ValueError):
    """A business rule was broken. The message is safe to show a student."""


def parse_problem(text):
    match = _PROBLEM.match(text or "")
    if not match:
        raise RuleError("Enter a problem like 12 + 5, 9 - 4, 6 x 7 or 20 / 4.")
    left, op, right = int(match.group(1)), _OPS[match.group(2).lower()], int(match.group(3))
    correct_result(left, op, right)  # reject unsupported problems up front
    return left, op, right


def correct_result(left, op, right):
    if op == "+":
        return left + right
    if op == "-":
        return left - right
    if op == "*":
        return left * right
    if right == 0:
        raise RuleError("You cannot divide by zero.")
    quotient, remainder = divmod(left, right)
    if remainder:
        # FR-02 / US-03 (Refine) and Q-02 are unresolved, so this slice does
        # not judge remainder answers.
        raise RuleError("Division with a remainder is not supported yet (US-03).")
    return quotient


def parse_answer(text):
    try:
        return int((text or "").strip())
    except ValueError:
        raise RuleError("Enter your answer as a whole number.")


def _tries_left(record):
    if record["outcome"] is not None:
        return 0
    return MAX_TRIES - len(record["attempts"])


def start_problem(store, problem_text):
    left, op, right = parse_problem(problem_text)
    record = store.add(
        {"left": left, "op": op, "right": right, "attempts": [], "outcome": None}
    )
    return {"problem_id": record["id"], "tries_left": _tries_left(record)}


def submit_answer(store, problem_id, answer_text):
    """Check one answer. Returns what the interface may show.

    `correct_result` is included ONLY when the problem is revealed (two wrong
    answers), so an interface cannot leak it after the first wrong answer.
    """
    record = store.get(problem_id)
    if record is None:
        raise RuleError(f"No problem with id {problem_id}.")
    if record["outcome"] is not None:
        raise RuleError("This problem is finished. No further tries are offered.")
    answer = parse_answer(answer_text)  # bad input does NOT use up a try

    record["attempts"].append(answer)
    correct = correct_result(record["left"], record["op"], record["right"])
    if answer == correct:
        record["outcome"] = RIGHT
    elif len(record["attempts"]) >= MAX_TRIES:
        record["outcome"] = REVEALED
    store.save(record)

    return {
        "problem_id": record["id"],
        "verdict": RIGHT if answer == correct else WRONG,
        "tries_left": _tries_left(record),
        "finished": record["outcome"] is not None,
        "correct_result": correct if record["outcome"] == REVEALED else None,
    }
