"""Text interface layer. Reads typed input, calls dataman/logic.py, prints what
the logic returns. It makes no decision about right/wrong or about tries.

Run:  python app.py        (type 'quit' at the problem prompt to leave)
"""
from dataman import logic
from dataman.store import InMemoryStore


def show_result(result):
    if result["verdict"] == logic.RIGHT:
        print("  \u2714 RIGHT")
    else:
        print("  \u2718 WRONG")
        if result["correct_result"] is not None:
            print(f"  The correct result is {result['correct_result']}.")


def practice_one_problem(store, problem_text):
    started = logic.start_problem(store, problem_text)
    finished = False
    while not finished:
        tries = started["tries_left"]
        answer = input(f"  Your answer ({tries} {'try' if tries == 1 else 'tries'} left): ")
        try:
            result = logic.submit_answer(store, started["problem_id"], answer)
        except logic.RuleError as err:
            print(f"  ! {err}")
            continue
        show_result(result)
        started["tries_left"] = result["tries_left"]
        finished = result["finished"]
        if not finished:
            print("  Try again on the same problem.")


def main():
    store = InMemoryStore()
    print("DataMan prototype. Practice arithmetic. Type 'quit' to leave.")
    while True:
        try:
            text = input("Problem: ").strip()
        except EOFError:
            break
        if text.lower() in ("quit", "exit"):
            break
        if not text:
            continue
        try:
            practice_one_problem(store, text)
        except logic.RuleError as err:
            print(f"  ! {err}")
        except EOFError:
            break


if __name__ == "__main__":
    main()
