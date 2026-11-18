"""Tests the business rules with NO text interface. Run: python test_logic.py
(also works with pytest)."""
from dataman import logic
from dataman.store import InMemoryStore


def raises(fn, *args):
    try:
        fn(*args)
    except logic.RuleError:
        return True
    return False


def new(problem):
    s = InMemoryStore()
    return s, logic.start_problem(s, problem)["problem_id"]


def test_us01_right_and_wrong_for_all_four_operations():
    for text, good, bad in [("12 + 5", "17", "18"), ("9 - 4", "5", "6"),
                            ("6 x 7", "42", "41"), ("20 / 4", "5", "4")]:
        s, pid = new(text)
        assert logic.submit_answer(s, pid, good)["verdict"] == "right"
        s, pid = new(text)
        assert logic.submit_answer(s, pid, bad)["verdict"] == "wrong"


def test_us02_wrong_first_offers_second_try_without_revealing():
    s, pid = new("6 x 7")
    r = logic.submit_answer(s, pid, "40")
    assert r["verdict"] == "wrong" and r["tries_left"] == 1
    assert not r["finished"] and r["correct_result"] is None


def test_us02_right_on_second_try():
    s, pid = new("6 x 7")
    logic.submit_answer(s, pid, "40")
    r = logic.submit_answer(s, pid, "42")
    assert r["verdict"] == "right" and r["finished"]


def test_us02_two_wrong_reveals_and_closes():
    s, pid = new("6 x 7")
    logic.submit_answer(s, pid, "40")
    r = logic.submit_answer(s, pid, "41")
    assert r["verdict"] == "wrong" and r["finished"] and r["correct_result"] == 42
    assert raises(logic.submit_answer, s, pid, "42")  # no third try


def test_invalid_input_does_not_use_a_try():
    s, pid = new("6 x 7")
    assert raises(logic.submit_answer, s, pid, "abc")
    assert logic.submit_answer(s, pid, "40")["tries_left"] == 1


def test_unsupported_problems_rejected():
    s = InMemoryStore()
    assert raises(logic.start_problem, s, "7 / 2")   # remainder: US-03 unresolved
    assert raises(logic.start_problem, s, "7 / 0")
    assert raises(logic.start_problem, s, "seven plus two")


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_"):
            fn()
            print("ok", name)
