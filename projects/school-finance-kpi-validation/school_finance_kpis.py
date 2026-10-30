"""School finance KPI example using fictional records only."""
from collections import defaultdict

ROWS = [
    {"district": "Demo North", "state": "CA", "revenue": 1_500_000, "expenditure": 1_400_000, "enrollment": 100},
    {"district": "Demo South", "state": "CA", "revenue": 900_000, "expenditure": 850_000, "enrollment": 60},
    {"district": "Demo East", "state": "NY", "revenue": 1_100_000, "expenditure": 1_050_000, "enrollment": 80},
    {"district": "Invalid Demo", "state": "NY", "revenue": -10, "expenditure": 100, "enrollment": 10},
]

REQUIRED = {"district", "state", "revenue", "expenditure", "enrollment"}


def valid(row):
    if not REQUIRED.issubset(row):
        return False
    return (
        isinstance(row["revenue"], (int, float))
        and isinstance(row["expenditure"], (int, float))
        and isinstance(row["enrollment"], (int, float))
        and row["revenue"] >= 0
        and row["expenditure"] >= 0
        and row["enrollment"] > 0
    )


def summarize(rows):
    clean = [r for r in rows if valid(r)]
    revenue = sum(r["revenue"] for r in clean)
    expenditure = sum(r["expenditure"] for r in clean)
    enrollment = sum(r["enrollment"] for r in clean)
    return {
        "districts": len(clean),
        "revenue": revenue,
        "expenditure": expenditure,
        "enrollment": enrollment,
        "revenue_per_student": revenue / enrollment if enrollment else None,
    }


if __name__ == "__main__":
    clean_rows = [row for row in ROWS if valid(row)]
    print("All valid fictional districts:", summarize(clean_rows))
    by_state = defaultdict(list)
    for row in clean_rows:
        by_state[row["state"]].append(row)
    for state, rows in sorted(by_state.items()):
        print(state, summarize(rows))
    assert summarize(ROWS)["districts"] == 3
    assert summarize(ROWS)["revenue"] == 3_500_000
