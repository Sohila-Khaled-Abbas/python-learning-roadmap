# Python in action: the browser coding lab

[Open the coding lab](https://sohila-khaled-abbas.github.io/python-learning-roadmap/lab/).

The practice loop is **read → change → run → check → vary → explain**. Every roadmap topic and full lesson links to the lab. Matching topics open a relevant challenge; other lessons open the playground, with the lesson example prefilled when available and no playground draft already exists.

## Practice path

| Challenge | What you build |
| --- | --- |
| 01 · First useful script | A formatted PixelFed quality message |
| 02 · EGP invoice | A reusable total with final rounding |
| 03 · Delivery policy | Branching, normalization and threshold behavior |
| 04 · Customer names | A new cleaned list without changing the source |
| 05 · Expense ledger | Grouped totals and reconciliation |
| 06 · Source/target IDs | Sorted missing and unexpected keys |
| 07 · Amount validation | Explicit failures for invalid and non-finite values |
| 08 · CSV orders | File handling, dictionary rows and type conversion |
| 09 · API response | Validation of a synthetic EUR/EGP-shaped payload |
| 10 · PixelFed quality | Unique orphan foreign keys, separate from null keys |
| 11 · SQLite summary | Bound parameters, grouping and connection cleanup |
| 12 · Streaming batches | A generator that consumes only the next batch |
| 13 · pandas summary | Numeric coercion, valid-row filtering and grouping |

The free playground also supports standard-library experiments. The editable `orders.csv` contains synthetic teaching records, not production data or a live financial quote. Fixture files and execution globals are recreated on every run. `input()` reads the separate input-lines field, one line at a time. A header-only/empty result, invalid data, boundaries, repeated keys and one-pass iteration appear in the exercise cases where relevant.

## Feedback and progress

Run code inspects output; **Check my work** tests the function's behavior on the supplied cases. Incomplete starters fail at least one case. Hints appear one at a time, reference solutions are separate, and the learner can try a variation after passing. Revealing a reference is recorded locally. These visible practice checks are self-assessment aids; a green result is not certification or proof that every lesson exit check has been met.

Drafts and the last successful checked version per challenge use `sohila-python-lab-v1`. Topic statuses retain the existing `sohila-python-roadmap-v1` format. Checking code never changes topic completion automatically. Lab backups export/import drafts and practice history separately; the CSV and input fields are temporary session experiments. Download `.py` preserves the current script for local work.

## Runtime and recovery

The lab uses [Pyodide 314.0.7](https://pyodide.org/en/stable/usage/webworker.html), a pinned CPython/WebAssembly release, loaded from the documented jsDelivr distribution on the first run. An ES module Web Worker keeps Python execution off the page's UI thread. The optional pandas exercise loads its compatible distribution package on demand. The site needs no Python application server, account or API key.

Stop terminates the worker, including an unbounded loop or a pending runtime/package download. Each execution has a 12-second limit after loading; each loading phase has a two-minute limit and a retry message. A later run starts a new worker after cancellation/failure. Output is bounded to 16,000 characters per stream; input/code/backup sizes are also bounded. Python exceptions and failed cases are displayed as plain text. The worker client ignores responses from terminated workers.

This is a browser learning environment, not a hardened service for hosting third-party code. Python can access browser APIs through Pyodide's JavaScript bridge. Packages, sockets, subprocesses and OS integration differ from desktop Python; imported modules can remain loaded in the reusable worker until Stop or navigation. WebAssembly memory is browser-managed; the timeout does not impose a separate hard memory quota. First-run downloads require internet/CDN access. A clear failure message leaves the draft intact; the repo exercises remain available for local Python.

## Source and validation

- `web/lab-curriculum.mjs`: original briefs, starters, hints, reference solutions and behavior checks.
- `web/lab-runner.py`: fresh execution globals, temporary CSV fixtures, input and bounded output.
- `web/lab-worker.mjs`: lazy runtime/package initialization and worker messaging.
- `web/lab-core.mjs`: draft validation, worker cancellation and deadlines.
- `web/lab.mjs`, `web/lab.css`, `scripts/lab-page.html`: accessible editor, console, mobile challenge selector and feedback.

`npm test` covers catalog/lesson integrity, draft validation, cancellation, stale responses and deadlines. Python tests exercise reference solutions, incomplete starters, namespace/fixture isolation, input, Unicode, syntax errors and bounded output. The standard-library CI skips the optional pandas contract when pandas is absent; browser QA checks the actual WebAssembly pandas and SQLite flows. The lab is also included in canonical metadata, structured data, sitemap coverage and internal-link checks.

Primary implementation references: [Pyodide worker guide](https://pyodide.org/en/stable/usage/webworker.html), [getting started](https://pyodide.org/en/stable/usage/quickstart.html), [package loading](https://pyodide.org/en/stable/usage/loading-packages.html), and [JavaScript API](https://pyodide.org/en/stable/usage/api/js-api.html).
