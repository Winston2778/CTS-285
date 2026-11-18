"""Stubbed data layer.

An in-memory stand-in for the real database. It keeps and returns problem
records and knows NOTHING about arithmetic or the second-try rule. Logic uses
only add / get / save / list_all, so Flask + a database in Module 5 can replace
this class without touching dataman/logic.py.

Record shape the logic relies on:
    {"id", "left", "op", "right", "attempts": [ints], "outcome": None|"right"|"revealed"}

STUBBED: persistence (data is lost on exit), who owns a record (no student
identity: see Q-04), database-generated ids, transactions.
"""


class InMemoryStore:
    def __init__(self):
        self._records = {}
        self._next_id = 1

    def add(self, fields):
        record = dict(fields)
        record["attempts"] = list(record.get("attempts", []))
        record["id"] = self._next_id
        self._records[record["id"]] = record
        self._next_id += 1
        return self._copy(record)

    def get(self, record_id):
        record = self._records.get(record_id)
        return self._copy(record) if record else None

    def save(self, record):
        self._records[record["id"]] = self._copy(record)
        return self._copy(record)

    def list_all(self):
        return [self._copy(r) for r in self._records.values()]

    @staticmethod
    def _copy(record):
        copy = dict(record)
        copy["attempts"] = list(record["attempts"])
        return copy
