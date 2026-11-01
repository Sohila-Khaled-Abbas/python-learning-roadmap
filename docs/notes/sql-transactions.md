# Database transactions & connection lifetimes

Control the unit of work and distinguish a transaction from a connection.

Extension beyond the Boot.dev video

## Connect to your work

Apply this to your Python data tools, PixelFed quality work, n8n integrations or BI delivery when the project needs it.

## Learn by doing

- Bind values as SQL parameters and keep identifiers controlled.
- Demonstrate commit and rollback on a multi-row operation.
- Close resources and define conflict handling before introducing concurrency.

## Original practice

Port a fixture load to a chosen SQLAlchemy driver; fail the second write and prove the intended transaction boundary.

## Exit check

The rollback behavior matches the documented unit of work, duplicate delivery policy remains stable, and credentials stay outside source.

## Understand the idea

A connection is a communication resource; a transaction groups changes under a commit or rollback boundary. A context manager can make that boundary visible, but you must understand which context manages only the connection and which also manages the transaction.

Parameter binding protects values from being interpreted as SQL syntax. It does not turn an arbitrary user-provided table name into a safe identifier. Use a controlled identifier mapping and explicit database constraints for keys and uniqueness.

## Resources

- [SQLAlchemy 2.0 · transactions and bound parameters](https://docs.sqlalchemy.org/en/20/tutorial/dbapi_transactions.html)
- [Python SQLite Tutorial: Build a Python project with a SQLite database](https://www.youtube.com/watch?v=iXYeb2artTE)

[Back to the roadmap](../roadmap.md) · [Source and attribution policy](../sources.md)
