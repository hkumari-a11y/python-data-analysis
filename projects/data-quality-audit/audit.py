"""Audit two fictional datasets before joining them."""
from collections import Counter

LEFT = [
    {"id": "A01", "name": "Sample One"},
    {"id": "A02", "name": "Sample Two"},
    {"id": "A02", "name": "Duplicate Two"},
    {"id": None, "name": "Missing ID"},
    {"id": "A04", "name": "Sample Four"},
]
RIGHT = [
    {"id": "A01", "name": "Match One"},
    {"id": "A02", "name": "Match Two"},
    {"id": "A03", "name": "Only Right"},
]


def audit_keys(left, right, key="id"):
    def summarize(rows):
        keys = [r.get(key) for r in rows]
        counts = Counter(k for k in keys if k is not None and k != "")
        return {
            "missing": sum(k is None or k == "" for k in keys),
            "duplicates": sorted(k for k, count in counts.items() if count > 1),
            "unique_keys": set(counts),
        }

    a, b = summarize(left), summarize(right)
    return {
        "left_missing": a["missing"],
        "right_missing": b["missing"],
        "left_duplicate_keys": a["duplicates"],
        "right_duplicate_keys": b["duplicates"],
        "matched_unique_keys": sorted(a["unique_keys"] & b["unique_keys"]),
        "left_only_keys": sorted(a["unique_keys"] - b["unique_keys"]),
        "right_only_keys": sorted(b["unique_keys"] - a["unique_keys"]),
    }


if __name__ == "__main__":
    report = audit_keys(LEFT, RIGHT)
    for metric, value in report.items():
        print(f"{metric}: {value}")
    assert report["left_missing"] == 1
    assert report["left_duplicate_keys"] == ["A02"]
    assert report["matched_unique_keys"] == ["A01", "A02"]
