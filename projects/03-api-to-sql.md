# Build 03 · API-to-SQL learning pipeline

Create a traceable path from external input to an analytical output. Start with the **working offline reference**, then implement the HTTP adapter as a separate step.

## Run the reference

```powershell
.\.venv\Scripts\python.exe -m projects.pipeline --input data/fixtures/orders.csv --database output/orders.sqlite --output output
.\.venv\Scripts\python.exe -m projects.pipeline --input data/fixtures/orders.csv --database output/orders.sqlite --output output
```

The fixture is synthetic. Seven input rows yield four accepted deliveries, three rejects, three distinct stored orders and 361.75 EGP total. The identical duplicate is an accepted replay, not another order. A rerun inserts zero rows. Conflicting duplicate IDs are rejected; updates require a separate, explicit change policy.

The reference validates the header before loading, preserves input, uses parameterized SQL, writes a reject file and exports a stable orders table. It loads the full input into memory and expects a single writer. It has no HTTP request or production scheduler.

## Add the API adapter

1. Choose an appropriately licensed source and document its endpoint, access plan, quotas and data contract.
2. Build a `fetch → raw snapshot` adapter with a timeout and a bounded, justified retry policy. Keep HTTP tests mocked or fixture-backed.
3. Store source identity, provider timestamp, retrieval timestamp in UTC and an ingestion/run identifier. Apply an explicit freshness policy.
4. Validate schema before normalization; keep raw data immutable. Missing fields or malformed data must not masquerade as a valid empty response.
5. Preserve a business key and change policy before loading SQL. Test the same delivery twice and a changed record with the same key.

A possible extension is your EUR/EGP monitor. A forex quote needs a **separate quote schema**, not the orders table: base currency, quote currency, provider rate, provider timestamp and fetched timestamp. Do not put a made-up quote into the fixture and label it live. Verify provider base-currency support, rate precision, freshness and plan limitations before implementing it.

## Connect your stack

- **PostgreSQL/SQL Server:** port the key, transaction and conflict policy; use the selected driver’s parameter API. Keep credentials outside source control.
- **Power BI:** load the exported table and reconcile integer `total_piastres / 100` to the source. Preserve date and row-grain definitions.
- **n8n:** use a lab workflow to call the CLI or API adapter, capture exit code and summary, and route failures. Retries must obey the same replay policy.
- **FDE path:** expose a read-only status endpoint or small UI only after the ingestion contract is proven.

## Completion evidence

Publish the architecture, source/access notes, sample raw response, contract tests, two-run evidence, rejection report, reconciliation and failure/recovery instructions. Label what was simulated. Do not claim HTTP retrieval, orchestration or production deployment until you have built and verified them.
