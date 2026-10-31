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

## Resources

- [Python language tutorial](https://docs.python.org/3/tutorial/)

[Back to the roadmap](../roadmap.md) · [Source and attribution policy](../sources.md)
