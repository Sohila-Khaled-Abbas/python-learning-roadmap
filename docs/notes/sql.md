# SQL loading & idempotency

Loading twice should have a documented, stable outcome.

Extension beyond the Boot.dev video

## Connect to your work

Start with SQLite, then transfer the pattern to PostgreSQL or SQL Server.

## Learn by doing

- Parameterize SQL and use transactions.
- Choose a business key and an explicit conflict policy.
- Reconcile accepted inputs with stored rows.

## Original practice

Run python -m projects.pipeline twice on the same fixture database.

## Exit check

Stored row count and total stay stable; conflicting duplicate records are rejected.

## Understand the idea

The same business key delivered twice must have an explicit policy: accept identical replay, reject a conflict, or apply a documented update rule. A random new identifier on every run prevents replay detection.

Verify database constraints and transaction behavior with deliberate failures. A successful second run should reconcile stored rows and totals, not merely exit without an exception.

## Resources

- [Python language tutorial](https://docs.python.org/3/tutorial/)
- [Python SQLite Tutorial: Build a Python project with a SQLite database](https://www.youtube.com/watch?v=iXYeb2artTE)

[Back to the roadmap](../roadmap.md) · [Source and attribution policy](../sources.md)
