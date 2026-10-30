# Data Quality Audit — Python

A small, reproducible project inspired by the challenges of checking and reconciling records in graduate analytics coursework.

## Business question
Before combining two datasets, how can we detect duplicate identifiers, missing keys, and unmatched records?

## Deliverable
[Run the audit](audit.py) using `python audit.py`. It uses only the Python standard library and fictional records.

## What it checks
- Missing and duplicate IDs in the left dataset
- Missing and duplicate IDs in the right dataset
- IDs that occur on only one side
- Count of unique matched IDs

## Why it matters
Record matching requires more than counting rows. A join can multiply rows when keys are duplicated, and missing identifiers can hide mismatches.

## Attribution
This is a new, independent coding example, not a copy of the RAFT group's school records or final verification output.
