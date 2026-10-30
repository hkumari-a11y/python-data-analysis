# School Finance KPI Validation with Python

**Status:** Reproducible educational example using a tiny fictional dataset.

## Connection to my portfolio
My [School Finance Analytics Dashboard](https://github.com/hkumari-a11y/business-analytics-capstone) reports revenue, expenditure, enrollment, and revenue per student for a cleaned sample of school district records. This small Python exercise shows how to validate the same types of KPI calculations without publishing the underlying workbook.

## What the script does
- Validates required columns.
- Excludes records with invalid negative financial values or nonpositive enrollment.
- Calculates aggregate revenue, expenditure, enrollment, and revenue per student.
- Prints summary statistics and a state-level comparison.

## Run
`python school_finance_kpis.py`

The script uses only Python's standard library and includes a small, fictional example. Its output must **not** be confused with results from the real dashboard workbook.
