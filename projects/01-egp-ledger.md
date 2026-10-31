# Build 01 · EGP expense ledger

Turn the finance-tracker domain you already know into a small Python program. Use [the synthetic expense fixture](../data/fixtures/expenses.csv); this is not personal financial data.

## Contract

- One row is one transaction, keyed by `transaction_id`.
- Accept an ISO date, a nonblank category and a finite positive EGP string with no more than two decimal places. Decide and document whether a zero-value expense is allowed.
- Convert once at the boundary to integer piastres; keep exact values through aggregation.
- Reject invalid records with raw values and a reason. Never fill invalid amounts with zero.
- Group by category and calendar month; export a summary plus a rejection report.
- Define what an identical duplicate does and reject a conflicting duplicate ID.

## Acceptance checks

For the supplied fixture, Food is 200.00 EGP, Transportation 30.00 EGP and Education 250.00 EGP; total is 480.00 EGP. Check an empty file, a blank amount, a zero amount, a duplicate ID and Arabic category text. Prove input is unchanged. Reconcile accepted + rejected + explicitly handled duplicate rows to the full input count.

## Suggested steps

1. Complete foundation tasks 02, 03, 07, 10 and 12.
2. Write a pure `parse_transaction` function and test boundaries.
3. Add CSV input and a deterministic category/month report.
4. Expose `--input` and `--output` arguments with argparse.
5. Write the data contract, test output and two-minute explanation in your own README.

This is an implementation brief, not a completed ledger. The foundation solutions demonstrate useful pieces; they do not contain a finished Build 01 CLI. Add Telegram or Notion integration only after the offline contract is stable.
