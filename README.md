# Release Readiness Dashboard

A lightweight release-governance application that turns engineering quality signals into a repeatable Go/No-Go decision package.

## Inputs
- test pass rate
- open defects by severity
- requirements coverage
- rollback readiness
- deployment validation
- risk register

## Decision model
The application does not hide risk behind a single score. It presents gate status, evidence, blockers, owners, and explicit decision criteria.

## Run
```bash
pip install -r requirements.txt
python -m release.dashboard
```

## Portfolio artifacts
See `docs/RACI.md`, `docs/GO_NO_GO.md`, and `docs/ROLLBACK.md`.
