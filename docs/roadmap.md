# Python learning roadmap

A focused expansion of the Python stage in [Sohila’s data engineering roadmap](https://github.com/Sohila-Khaled-Abbas/data-engineering-learning-roadmap). Readiness comes from the exit checks, not from watching a video.

## 00 · Make Python yours

Week 1 · A light setup. A clear starting point.

| Topic | Practice | Exit evidence |
| --- | --- | --- |
| [Interpreter & virtual environments](notes/environment.md) | Follow docs/setup-windows.md and print sys.executable from the project interpreter. | A fresh terminal runs the tests with the same interpreter, without changing PowerShell policy. |
| [A diagnostic, not a restart](notes/baseline.md) | Try exercises/foundations.py tasks 02, 03, 07 and 10 before watching the matching chapters. | Explain your solution and edge cases without copying a reference answer. |

## 01 · Think in Python

Weeks 1–3 · Course chapters 1–6 · small functions, clear reasoning.

| Topic | Practice | Exit evidence |
| --- | --- | --- |
| [Run a program](notes/introduction.md) | Task 01: format a short pipeline completion message. | pipeline_message("landing", 4) returns "landing: 4 rows". |
| [Variables, types & missing values](notes/variables.md) | Task 02: convert a decimal EGP string to integer piastres; reject fractions below one piastre. | "12.50" becomes 1250; "0.001" and "NaN" raise ValueError. |
| [Functions & explicit contracts](notes/functions.md) | Task 03: calculate net revenue from gross and discount piastres. | net_revenue(10000, 1500) is 8500; a discount larger than gross is rejected. |
| [Scope & side effects](notes/scope.md) | Task 04: add a category to a copied record without changing the original. | The original dict stays identical after classify_copy(record, "Food"). |
| [Testing & debugging](notes/debugging.md) | Task 05: fix mean_or_none so empty data is meaningful and zero is retained. | mean_or_none([]) is None; mean_or_none([0, 10]) is 5. |
| [Operators & computation](notes/computing.md) | Task 06: compute the number of API pages from row count and page size. | page_count(101, 50) is 3; zero rows is 0; size zero is rejected. |

## 02 · Work with real shapes of data

Weeks 3–5 · Course chapters 7–12 · logic, collections, failure.

| Topic | Practice | Exit evidence |
| --- | --- | --- |
| [Comparisons & branching](notes/comparisons.md) | Task 07: label missing, negative, zero and positive amounts. | None → missing; -1 → invalid; 0 → zero; 1 → valid. |
| [Loops & accumulation](notes/loops.md) | Task 08: sum only nonmissing, nonnegative integer amounts. | valid_total([None, 0, -2, 10]) is 10. |
| [Lists, slices & comprehensions](notes/lists.md) | Task 09: return the last n records without changing the input list. | latest([1, 2, 3], 2) is [2, 3]; n=0 returns []; negative n is invalid. |
| [Dictionaries & grouping](notes/dictionaries.md) | Task 10: group transaction piastres by category. | Two Food rows with 300 and 200 produce {"Food": 500}. |
| [Sets & reconciliation](notes/sets.md) | Task 11: report profile IDs absent from the reference set. | missing_ids([1, 2, 2, 4], [1, 4]) is [2]. |
| [Exceptions & honest failures](notes/errors.md) | Task 12: parse a nonnegative integer count; reject blanks, decimals, negatives and booleans. | "12" → 12; "12.5", "", -1 and True raise ValueError. |

## 03 · From scripts to reliable tools

Weeks 6–7 · Files, modules, tests, and command lines.

| Topic | Practice | Exit evidence |
| --- | --- | --- |
| [Modules, typing & data classes](notes/modules.md) | Split the ledger into parsing, validation and reporting modules. | Importing a module performs no file writes or network calls. |
| [Files, CSV, JSON & paths](notes/files.md) | Run the supplied pipeline on data/fixtures/orders.csv and inspect rejects.csv. | Missing columns fail clearly; Arabic text round-trips; original input is untouched. |
| [Tests that catch a broken contract](notes/tests.md) | Add a regression test for a defect you introduce in a working copy. | The test fails with the defect and passes after a targeted repair. |
| [Command lines, config & logging](notes/cli.md) | Explain every argument of python -m projects.pipeline --help. | A new terminal can run the tool and distinguish input failure from a valid empty result. |
| [Build 01 · EGP expense ledger](notes/ledger.md) | Build the specification in projects/01-egp-ledger.md before reading reference solutions. | Reconcile the output to a hand calculation and demonstrate a rejected input. |

## 04 · Build on your SQL & BI skills

Weeks 8–9 · Tabular data, quality, joins, and precise metrics.

| Topic | Practice | Exit evidence |
| --- | --- | --- |
| [DataFrames through a SQL lens](notes/pandas.md) | Reproduce ledger category totals with pandas and compare them with your pure-Python result. | Both outputs agree; explain how missing groups and numeric conversion are handled. |
| [Joins, nulls & grain](notes/joins.md) | Join a fact fixture to a duplicate dimension and make the validation fail. | No total changes silently; unmatched keys and duplicated keys have separate reports. |
| [Build 02 · PixelFed quality CLI](notes/quality.md) | Follow projects/02-pixelfed-quality.md using a copied sample, never the only landing copy. | Every rule has a test and an example; no indiscriminate fillna(0). |
| [NumPy & time-aware analysis](notes/numpy.md) | Compare a list comprehension and an array operation on the same small numeric input. | Results agree, units are documented and a timezone assumption is explicit. |
| [Optional · a clean ML bridge](notes/ml.md) | Write a leakage checklist and a small baseline experiment on an appropriately licensed dataset. | The held-out set never fits the imputer, encoder or scaler. |

## 05 · Connect it. Test it. Ship it.

Weeks 10–12 · APIs, databases, orchestration, and portfolio evidence.

| Topic | Practice | Exit evidence |
| --- | --- | --- |
| [APIs, JSON & failure policies](notes/http.md) | Design an offline EUR/EGP quote fixture with provider_as_of and fetched_at; label it fixture data. | A stale or malformed quote is visible; a cached value is never labeled live. |
| [SQL loading & idempotency](notes/sql.md) | Run python -m projects.pipeline twice on the same fixture database. | Stored row count and total stay stable; conflicting duplicate records are rejected. |
| [Build 03 · a rerunnable data pipeline](notes/pipeline.md) | Complete projects/03-api-to-sql.md and compare against projects/pipeline.py. | A malformed source header fails before loading; reruns are stable; reject reasons survive. |
| [n8n, CI & operational handover](notes/orchestration.md) | Design a manual/scheduled n8n call to a lab copy of your CLI and record the exit-code policy. | Two simultaneous or repeated deliveries have an explicit deduplication strategy. |
| [Useful problem-solving patterns](notes/algorithms.md) | Solve two fresh dictionary/set problems and explain your complexity aloud. | You can explain the tradeoff and test empty, repeated and large inputs. |
| [Publish evidence & choose your next step](notes/publish.md) | Use templates/weekly-review.md and templates/project-readme.md for a final review. | A reviewer can run the project from the README and trace a total back to input records. |

