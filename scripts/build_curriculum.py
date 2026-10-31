"""Build the learning catalog and readable notes from original editorial content."""
import csv
import io
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GITHUB = 'https://github.com/Sohila-Khaled-Abbas/'
VIDEO = 'https://www.youtube.com/watch?v=4M87qBgpafk'

def resource(id, title, url, language='English', kind='Documentation', role='Reference', note='', origin='Official documentation', verified='Official page checked 2026-10-31'):
    return dict(id=id, title=title, url=url, language=language, kind=kind, role=role, note=note, origin=origin, verification=verified)

resources = [
    resource('boot', 'Boot.dev · Python for Beginners', VIDEO, kind='Video course', role='Primary course', note='7:08:28; taught by TrashPuppy. Twelve verified chapter starts. Notes here are original companion material.', origin='User-selected YouTube course', verified='Title, channel, duration and chapters checked in the video description on 2026-10-31'),
    resource('iti', 'كورس Python منحة ITI', 'https://www.youtube.com/playlist?list=PLNFDrRZdysFzSkNWqHZof7NxFHtGNC6bf', 'Arabic', 'Video playlist', 'Arabic companion', 'Use the relevant lesson when a concept needs another explanation. Playlist-level mapping only; no invented lesson timestamps.', 'User-selected ITI playlist', 'User-provided link; also present as V007 in the existing DE resource catalog'),
    resource('cs50', 'Harvard CS50P · lectures & problem sets', 'https://cs50.harvard.edu/python/', kind='Course + exercises', role='Practice spine', note='Use lectures selectively and solve problem sets yourself. No CS50 solutions are reproduced here.', origin='User-selected HarvardX CS50P course'),
    resource('edx', 'Your HarvardX CS50P course on edX', 'https://learning.edx.org/course/course-v1:HarvardX+CS50P+Python/home', kind='Enrolled course', role='Your course', note='Continue in your enrolled course. Sign-in and access depend on your account; no completion is assumed.', origin='User-provided edX course tab', verified='Course identity from user-provided HarvardX+CS50P+Python URL'),
    resource('python', 'Python language tutorial', 'https://docs.python.org/3/tutorial/'),
    resource('packaging', 'PyPA · environments & packages', 'https://packaging.python.org/en/latest/tutorials/installing-packages/'),
    resource('pytest', 'pytest · getting started', 'https://docs.pytest.org/en/stable/getting-started.html'),
    resource('pandas', 'pandas · getting started tutorials', 'https://pandas.pydata.org/docs/getting_started/intro_tutorials/'),
    resource('numpy', 'NumPy · quickstart', 'https://numpy.org/doc/stable/user/quickstart.html'),
    resource('sklearn', 'scikit-learn · getting started', 'https://scikit-learn.org/stable/getting_started.html', role='Optional ML bridge', note='Do after Python and pandas; keep preprocessing inside a train-only fitted pipeline.'),
    resource('roadmapsh', 'roadmap.sh · Python Developer', 'https://roadmap.sh/python', kind='Roadmap', role='Broad reference', note='Visual inspiration. This project has an original layout and curriculum and is not affiliated with roadmap.sh.', origin='Official roadmap.sh page'),
]

phases = [
    dict(id='workspace', number='00', title='Make Python yours', weeks='Week 1', subtitle='A light setup. A clear starting point.', color='blue'),
    dict(id='foundations', number='01', title='Think in Python', weeks='Weeks 1–3', subtitle='Course chapters 1–6 · small functions, clear reasoning.', color='yellow'),
    dict(id='collections', number='02', title='Work with real shapes of data', weeks='Weeks 3–5', subtitle='Course chapters 7–12 · logic, collections, failure.', color='yellow'),
    dict(id='engineering', number='03', title='From scripts to reliable tools', weeks='Weeks 6–7', subtitle='Files, modules, tests, and command lines.', color='blue'),
    dict(id='data', number='04', title='Build on your SQL & BI skills', weeks='Weeks 8–9', subtitle='Tabular data, quality, joins, and precise metrics.', color='purple'),
    dict(id='delivery', number='05', title='Connect it. Test it. Ship it.', weeks='Weeks 10–12', subtitle='APIs, databases, orchestration, and portfolio evidence.', color='green'),
]

topics = []
def topic(id, phase, title, hours, summary, bridge, learn, exercise, gate, requires, resource_ids, chapter=None, cs50=None, code=None, pitfalls=None):
    t = dict(id=id, phase=phase, title=title, hours=hours, summary=summary, bridge=bridge, learn=learn, exercise=exercise, gate=gate, requires=requires, resources=resource_ids, chapter=chapter, cs50=cs50, code=code or '', pitfalls=pitfalls or [], note_path=f'docs/notes/{id}.md')
    topics.append(t)

topic('environment','workspace','Interpreter & virtual environments',2,
      'Keep each project isolated and make the interpreter explicit.',
      'Use your existing Windows setup. Docker and WSL are optional for this roadmap.',
      ['Inspect the installed interpreter before changing anything.', 'Create a project .venv and run Python through its explicit path.', 'Keep .venv, secrets and generated files out of Git.'],
      'Follow docs/setup-windows.md and print sys.executable from the project interpreter.',
      'A fresh terminal runs the tests with the same interpreter, without changing PowerShell policy.',[],['packaging','python'])
topic('baseline','workspace','A diagnostic, not a restart',2,
      'Use existing Python exposure as an advantage and verify it with a small task.',
      'Your SQL, Power Query, API and analytics experience gives you useful mental models.',
      ['Read a traceback and explain a function input/output.', 'Group four EGP transactions with a dict.', 'Record which topics need practice; all progress begins unmarked.'],
      'Try exercises/foundations.py tasks 02, 03, 07 and 10 before watching the matching chapters.',
      'Explain your solution and edge cases without copying a reference answer.',['environment'],['boot','iti','cs50'])

# Published chapter starts read from the source video description, not guessed transcript offsets.
chapters = [
 (1,'introduction','Run a program',221,'03:41',2,'A program is an ordered set of instructions with observable output.',
  'A query returns rows; a script can coordinate several steps around those rows.',
  ['Run a .py file and use print for visible output.', 'Distinguish source code from the interpreter that executes it.', 'Predict the output before running the program.'],
  'Task 01: format a short pipeline completion message.', 'pipeline_message("landing", 4) returns "landing: 4 rows".',
  'def pipeline_message(stage, rows):\n    return f"{stage}: {rows} rows"\n\nprint(pipeline_message("landing", 4))', ['Returning a value and printing a value have different effects.'], '0'),
 (2,'variables','Variables, types & missing values',902,'15:02',3,'A name refers to an object; type determines the operations that object supports.',
  'Compare Python None with SQL NULL, and distinguish missingness from zero and an empty string.',
  ['Use str, int, float, bool and None deliberately.', 'Convert text at input boundaries and inspect types.', 'Use integer minor units for these EGP exercises: 100 piastres = 1 EGP.'],
  'Task 02: convert a decimal EGP string to integer piastres; reject fractions below one piastre.', '"12.50" becomes 1250; "0.001" and "NaN" raise ValueError.',
  'from decimal import Decimal\namount = Decimal("12.50")\npiastres = int(amount * 100)\nprint(piastres)  # 1250; validate precision before int in real input code', ['bool("False") is True because the string is nonempty.', 'Binary floats are unsuitable for exact currency equality.'], '0'),
 (3,'functions','Functions & explicit contracts',2586,'43:06',3,'A function turns named inputs into a useful result with a clear contract.',
  'Think of a reusable Power Query function, but make data dependencies explicit.',
  ['Separate input/output from transformation logic.', 'Use return values, parameters and small docstrings.', 'Specify valid inputs and the result unit.'],
  'Task 03: calculate net revenue from gross and discount piastres.', 'net_revenue(10000, 1500) is 8500; a discount larger than gross is rejected.',
  'def net_revenue(gross, discount):\n    if not 0 <= discount <= gross:\n        raise ValueError("discount outside gross amount")\n    return gross - discount', ['A missing return produces None.', 'A function that mutates input may surprise its callers.'], '0'),
 (4,'scope','Scope & side effects',4572,'01:16:12',2,'Local names help a function behave predictably across calls.',
  'Avoid notebook state that makes a cell work only after an undocumented execution order.',
  ['Trace local versus module names.', 'Pass configuration as a parameter.', 'Return a new value rather than modifying a shared dict accidentally.'],
  'Task 04: add a category to a copied record without changing the original.', 'The original dict stays identical after classify_copy(record, "Food").',
  'def classify_copy(record, category):\n    result = dict(record)\n    result["category"] = category\n    return result', ['A shallow copy does not clone nested mutable values.', 'Mutable default arguments persist between calls.'], None),
 (5,'debugging','Testing & debugging',5335,'01:28:55',2,'A failing example is evidence you can narrow to a specific cause.',
  'Apply your troubleshooting habit: reproduce, inspect, change one thing, verify.',
  ['Read a traceback from the final exception back to your call.', 'Write a normal, empty and boundary example.', 'Keep assertions in tests; use explicit validation in application code.'],
  'Task 05: fix mean_or_none so empty data is meaningful and zero is retained.', 'mean_or_none([]) is None; mean_or_none([0, 10]) is 5.',
  'def mean_or_none(values):\n    return sum(values) / len(values) if values else None\n\nassert mean_or_none([0, 10]) == 5', ['Do not use bare except to hide a failure.', 'assert can be disabled; it is not a production input-validation boundary.'], '5'),
 (6,'computing','Operators & computation',6898,'01:54:58',2,'Operators encode arithmetic, precedence and discrete decisions.',
  'ETL batching and reconciliation depend on clear units and correct integer arithmetic.',
  ['Explain /, //, %, ** and parentheses.', 'Calculate batches without losing a partial batch.', 'Define the behavior of zero and invalid batch sizes.'],
  'Task 06: compute the number of API pages from row count and page size.', 'page_count(101, 50) is 3; zero rows is 0; size zero is rejected.',
  'def page_count(rows, size):\n    if rows < 0 or size <= 0:\n        raise ValueError("invalid pagination inputs")\n    return (rows + size - 1) // size', ['Integer division discards the remainder.', 'Do not confuse percent change with a percent of the new value.'], None),
 (7,'comparisons','Comparisons & branching',8863,'02:27:43',3,'Branch on explicit conditions and keep unknown values distinct.',
  'Translate a Power Query conditional column or SQL CASE into readable Python.',
  ['Combine conditions with and, or and not.', 'Use is None for an absent value.', 'Write complete boundary rules before coding.'],
  'Task 07: label missing, negative, zero and positive amounts.', 'None → missing; -1 → invalid; 0 → zero; 1 → valid.',
  'def amount_status(value):\n    if value is None:\n        return "missing"\n    if value < 0:\n        return "invalid"\n    return "zero" if value == 0 else "valid"', ['= assigns; == compares.', 'if not value merges zero with missingness.'], '1'),
 (8,'loops','Loops & accumulation',12286,'03:24:46',3,'Iteration applies a rule repeatedly while preserving an invariant.',
  'A row loop is useful for learning. Later compare it with SQL and pandas operations.',
  ['Use for, range, enumerate, break and continue.', 'Accumulate a total with a clear initial value.', 'Trace a loop on an empty input and a single record.'],
  'Task 08: sum only nonmissing, nonnegative integer amounts.', 'valid_total([None, 0, -2, 10]) is 10.',
  'total = 0\nfor amount in [None, 0, -2, 10]:\n    if amount is not None and amount >= 0:\n        total += amount\nprint(total)', ['Changing a list while iterating over it can skip entries.', 'A while loop needs a path toward termination.'], '2'),
 (9,'lists','Lists, slices & comprehensions',13454,'03:44:14',4,'Sequences preserve order, including repeated values.',
  'A list can hold landing records, but it has no enforced table schema.',
  ['Use indexes, slices, append and list comprehensions.', 'Understand aliasing, copying and in-place methods.', 'Preserve input order when filtering and deduplicating.'],
  'Task 09: return the last n records without changing the input list.', 'latest([1, 2, 3], 2) is [2, 3]; n=0 returns []; negative n is invalid.',
  'records = ["a", "b", "c"]\nlast_two = records[-2:]\nprint(last_two)\nprint(records)  # still intact', ['sort() changes the list and returns None.', 'items[-0:] returns the full list, not an empty list.'], '2'),
 (10,'dictionaries','Dictionaries & grouping',20688,'05:44:48',3,'Mappings connect unique keys to values and support lookup and grouping.',
  'Implement a small GROUP BY yourself before using pandas groupby.',
  ['Use items, keys, values and get deliberately.', 'Aggregate amounts by category.', 'Explain why repeated assignment to a key replaces its previous value.'],
  'Task 10: group transaction piastres by category.', 'Two Food rows with 300 and 200 produce {"Food": 500}.',
  'totals = {}\nfor row in [{"category": "Food", "amount": 300}, {"category": "Food", "amount": 200}]:\n    key = row["category"]\n    totals[key] = totals.get(key, 0) + row["amount"]\nprint(totals)', ['dict.get(key) may return None if the key is absent.', 'A dictionary is not a substitute for a validated database primary key.'], '2'),
 (11,'sets','Sets & reconciliation',22791,'06:19:51',2,'Sets answer membership and difference questions without keeping duplicates.',
  'Use set differences to find missing foreign keys before a warehouse load.',
  ['Use intersection, union and difference.', 'Compare observed keys with a reference set.', 'Sort results for deterministic reports.'],
  'Task 11: report profile IDs absent from the reference set.', 'missing_ids([1, 2, 2, 4], [1, 4]) is [2].',
  'observed = {1, 2, 2, 4}\nreference = {1, 4}\nprint(sorted(observed - reference))', ['set iteration order is not a reporting contract.', '{} creates an empty dict; set() creates an empty set.'], '2'),
 (12,'errors','Exceptions & honest failures',23847,'06:37:27',3,'Expected input problems need useful error messages and a visible policy.',
  'Route invalid landing records to quarantine, as you would in a documented ETL contract.',
  ['Distinguish syntax errors, exceptions and incorrect results.', 'Catch narrow exceptions near the input boundary.', 'Preserve a rejected record and its reason; never silently invent a value.'],
  'Task 12: parse a nonnegative integer count; reject blanks, decimals, negatives and booleans.', '"12" → 12; "12.5", "", -1 and True raise ValueError.',
  'try:\n    count = int("invalid")\nexcept ValueError as exc:\n    print(f"Rejected count: {exc}")', ['An exception is not evidence that the data should be filled with zero.', 'Do not expose API keys or complete sensitive payloads in logs.'], '3'),
]

previous = 'baseline'
for n,id,title,start,label,hours,summary,bridge,learn,exercise,gate,code,pitfalls,cs50 in chapters:
    topic(id, 'foundations' if n <= 6 else 'collections', title, hours, summary, bridge, learn, exercise, gate, [previous], ['boot','iti','cs50','python'], dict(number=n,start=start,label=label,url=f'{VIDEO}&t={start}s'), cs50, code, pitfalls)
    previous = id

topic('modules','engineering','Modules, typing & data classes',3,'Turn a growing script into small importable parts.','Bring schema discipline from SQL into Python interfaces.', ['Create modules with no work on import.', 'Use type hints and a dataclass for a validated record.', 'Keep configuration separate from transformations.'], 'Split the ledger into parsing, validation and reporting modules.', 'Importing a module performs no file writes or network calls.',['errors'],['python','cs50'],cs50='8')
topic('files','engineering','Files, CSV, JSON & paths',3,'Read and write data with explicit formats and encodings.','Treat landing files as immutable inputs and publish new outputs.', ['Use pathlib and with to manage files.', 'Distinguish CSV strings from typed values.', 'Record UTF-8, delimiters, field names and date formats.'], 'Run the supplied pipeline on data/fixtures/orders.csv and inspect rejects.csv.', 'Missing columns fail clearly; Arabic text round-trips; original input is untouched.',['modules'],['python','cs50'],cs50='6')
topic('tests','engineering','Tests that catch a broken contract',3,'Use examples and failure cases to protect meaningful behavior.','Reconciliation checks become executable tests.', ['Run the stdlib unit tests before adding a dependency.', 'Use pytest later for fixtures and parametrization.', 'Test malformed input, duplicates, empty data and reruns.'], 'Add a regression test for a defect you introduce in a working copy.', 'The test fails with the defect and passes after a targeted repair.',['debugging','files'],['pytest','cs50'],cs50='5')
topic('cli','engineering','Command lines, config & logging',2,'Make a script runnable by you, CI, or an orchestrator.','n8n can call a deliberate CLI contract with visible exit status.', ['Parse arguments with argparse.', 'Send summary output to stdout and diagnostic logs to stderr.', 'Use environment variables for credentials; never commit secrets.'], 'Explain every argument of python -m projects.pipeline --help.', 'A new terminal can run the tool and distinguish input failure from a valid empty result.',['files'],['python'])
topic('ledger','engineering','Build 01 · EGP expense ledger',3,'Apply the twelve foundations in one small useful program.','Connect to your Telegram/Notion EGP finance-tracker domain using offline fixtures.', ['Group by category and month.', 'Use integer piastres or validated Decimal values.', 'Write your own README with known assumptions.'], 'Build the specification in projects/01-egp-ledger.md before reading reference solutions.', 'Reconcile the output to a hand calculation and demonstrate a rejected input.',['dictionaries','sets','errors','tests','cli'],['iti','cs50'])
topic('pandas','data','DataFrames through a SQL lens',3,'Use labeled tabular operations with explicit data types.','Map WHERE → filtering, GROUP BY → groupby and SELECT → column projection.', ['Inspect schema and null patterns before cleaning.', 'Use vectorized transformations and groupby.', 'Retain raw values when coercing dates or numbers.'], 'Reproduce ledger category totals with pandas and compare them with your pure-Python result.', 'Both outputs agree; explain how missing groups and numeric conversion are handled.',['ledger'],['pandas'])
topic('joins','data','Joins, nulls & grain',3,'A join is a cardinality decision, not just a merge call.','Use your star/galaxy modeling knowledge to prevent multiplied facts.', ['Declare one row per entity before joining.', 'Use pandas merge(validate=...) and inspect unmatched keys.', 'Separate None, NaN, empty text and business-unknown values.'], 'Join a fact fixture to a duplicate dimension and make the validation fail.', 'No total changes silently; unmatched keys and duplicated keys have separate reports.',['pandas'],['pandas','iti'])
topic('quality','data','Build 02 · PixelFed quality CLI',3,'Profile landing data and publish a quality report without rewriting source files.','Extend your PixelFed contracts; social posts and profiles are not sales transactions.', ['Inspect actual PixelFed filenames and grain before choosing checks.', 'Report missing IDs, invalid timestamps, duplicates and orphans.', 'Write a small JSON report and a quarantine file.'], 'Follow projects/02-pixelfed-quality.md using a copied sample, never the only landing copy.', 'Every rule has a test and an example; no indiscriminate fillna(0).',['joins','tests','cli'],['pandas','python'])
topic('numpy','data','NumPy & time-aware analysis',2,'Understand array shape, masks and units before optimizing.','Use NumPy for numeric work; preserve exact currency separately.', ['Explain axes, broadcasting and boolean masks.', 'Parse timestamps as aware UTC values and display Africa/Cairo when needed.', 'Measure a transformation before replacing clear code.'], 'Compare a list comprehension and an array operation on the same small numeric input.', 'Results agree, units are documented and a timezone assumption is explicit.',['pandas'],['numpy'])
topic('ml','data','Optional · a clean ML bridge',3,'Carry reliable Python into model preparation and evaluation.','Build on your ML direction after data contracts and reproducibility are solid.', ['Split data before fitting preprocessing.', 'Keep transformations inside a pipeline.', 'Choose an honest baseline and a metric aligned to the task.'], 'Write a leakage checklist and a small baseline experiment on an appropriately licensed dataset.', 'The held-out set never fits the imputer, encoder or scaler.',['quality','numpy'],['sklearn'])
topic('http','delivery','APIs, JSON & failure policies',3,'Treat external data as an input that can be late, incomplete or unavailable.','Use your networking and n8n experience to reason about timeouts and rate limits.', ['Set an explicit timeout and validate response status and schema.', 'Use bounded retries only when appropriate; respect Retry-After.', 'Persist provider timestamp, fetch timestamp and provenance.'], 'Design an offline EUR/EGP quote fixture with provider_as_of and fetched_at; label it fixture data.', 'A stale or malformed quote is visible; a cached value is never labeled live.',['errors','files','tests'],['python'])
topic('sql','delivery','SQL loading & idempotency',3,'Loading twice should have a documented, stable outcome.','Start with SQLite, then transfer the pattern to PostgreSQL or SQL Server.', ['Parameterize SQL and use transactions.', 'Choose a business key and an explicit conflict policy.', 'Reconcile accepted inputs with stored rows.'], 'Run python -m projects.pipeline twice on the same fixture database.', 'Stored row count and total stay stable; conflicting duplicate records are rejected.',['http','quality'],['python'])
topic('pipeline','delivery','Build 03 · a rerunnable data pipeline',4,'Connect extraction, validation, quarantine and loading into one traceable run.','Use your ETL/ELT background to explain what each stage promises.', ['Run the supplied offline reference pipeline and inspect every artifact.', 'Add an HTTP adapter as a separate extension, keeping fixture tests offline.', 'Export a flat, typed Power BI-ready table and document grain.'], 'Complete projects/03-api-to-sql.md and compare against projects/pipeline.py.', 'A malformed source header fails before loading; reruns are stable; reject reasons survive.',['sql'],['pandas','python'])
topic('orchestration','delivery','n8n, CI & operational handover',3,'Wrap a tested tool with the smallest useful scheduler.','Reuse your n8n queue setup; scheduling does not repair a broken data contract.', ['Pass configuration through the execution environment.', 'Run checks on pull requests and deploy only validated site files.', 'Document failure notification, rerun policy and ownership.'], 'Design a manual/scheduled n8n call to a lab copy of your CLI and record the exit-code policy.', 'Two simultaneous or repeated deliveries have an explicit deduplication strategy.',['pipeline','cli'],['python'])
topic('algorithms','delivery','Useful problem-solving patterns',3,'Choose structures by the operation you need to perform.','Use LeetCode as targeted practice for mapping, grouping and lookup.', ['Compare list scans with set/dict membership.', 'Practice frequency counts and two-pointer reasoning.', 'Explain time and memory growth using a small example.'], 'Solve two fresh dictionary/set problems and explain your complexity aloud.', 'You can explain the tradeoff and test empty, repeated and large inputs.',['sets','loops'],['python','cs50'])
topic('publish','delivery','Publish evidence & choose your next step',4,'Finish with a reproducible artifact and a clear account of what you learned.','Link the result to your portfolio, DE roadmap and FDE roadmap.', ['Show setup, data contract, architecture, tests and one failure case.', 'Label synthetic data and distinguish built features from proposed extensions.', 'Choose the next DE, FDE or ML branch after reviewing your gaps.'], 'Use templates/weekly-review.md and templates/project-readme.md for a final review.', 'A reviewer can run the project from the README and trace a total back to input records.',['pipeline','orchestration','algorithms'],['roadmapsh','cs50'])

connections = [
 dict(repo='data-engineering-learning-roadmap', title='Data Engineering Roadmap', role='The parent learning path', use='This repo expands Phase 2 (Python) and supports data quality, orchestration and engineering phases.', url=GITHUB+'data-engineering-learning-roadmap', site='https://sohila-khaled-abbas.github.io/data-engineering-learning-roadmap/'),
 dict(repo='forward-deployed-engineer-roadmap', title='Forward Deployed Engineer Roadmap', role='The application & delivery branch', use='Use functions, API contracts, SQL and tests before the FastAPI/customer-delivery work.', url=GITHUB+'forward-deployed-engineer-roadmap', site='https://sohila-khaled-abbas.github.io/forward-deployed-engineer-roadmap/'),
 dict(repo='pixelfed-analytics-engineering', title='PixelFed Analytics Engineering', role='Apply quality checks', use='Add a Python validation CLI around documented landing grain and reference keys.', url=GITHUB+'pixelfed-analytics-engineering'),
 dict(repo='n8n-production-queue-setup', title='n8n Production Queue Setup', role='Orchestrate a tested tool', use='Keep Python logic testable outside n8n, then define schedule, retry and failure routing.', url=GITHUB+'n8n-production-queue-setup'),
 dict(repo='kickstarter-analytics-engineering', title='Kickstarter Analytics Engineering', role='Reconcile transformations', use='Compare Python cleaning and aggregates with your Power Query pipeline at the same grain.', url=GITHUB+'kickstarter-analytics-engineering'),
 dict(repo='udemy-networking-fundamentals', title='Networking Fundamentals', role='Understand HTTP failures', use='Connect API behavior to TCP, TLS, timeouts and response status.', url=GITHUB+'udemy-networking-fundamentals'),
 dict(repo='fundamentals-of-operating-systems-labs', title='Operating Systems Labs', role='Explain runtime behavior', use='Relate Python processes, files and memory use to the operating-system labs.', url=GITHUB+'fundamentals-of-operating-systems-labs'),
 dict(repo='egyptian-cosmetics-market', title='Egyptian Cosmetics Market', role='A domain for an extension', use='Design a separately labeled synthetic inventory/order scenario; do not claim market measurements.', url=GITHUB+'egyptian-cosmetics-market'),
]

weeks = [
 ('Set your baseline',['environment','baseline','introduction'],'Interpreter note, diagnostic results and first script'),
 ('Functions with a contract',['variables','functions','scope'],'Three tested pure functions using EGP minor units'),
 ('Debug with evidence',['debugging','computing','comparisons'],'A boundary-case log and a corrected function'),
 ('Shape and iterate',['loops','lists'],'List transformations with empty-input checks'),
 ('Group, reconcile, reject',['dictionaries','sets','errors'],'Category totals, orphan IDs and useful error messages'),
 ('Give the code a home',['modules','files','cli'],'A modular CSV/JSON command-line tool'),
 ('Finish the EGP ledger',['tests','ledger'],'Build 01 with reconciliation and a clear README'),
 ('Translate SQL into pandas',['pandas','joins'],'A join-cardinality experiment and matching totals'),
 ('Validate PixelFed inputs',['quality','numpy','ml'],'Build 02 plus optional ML leakage checklist'),
 ('Define external contracts',['http','sql'],'API failure matrix and idempotent fixture load'),
 ('Build one complete path',['pipeline','orchestration'],'Build 03, reject report and scheduling/runbook design'),
 ('Prove and connect the work',['algorithms','publish'],'Case study, source links and a next-branch decision'),
]

def build():
    # Reuse the Python-related rows from the existing DE catalog, preserving provenance.
    inherited = ROOT / 'data/inherited-resources.csv'
    if inherited.exists():
        for row in csv.DictReader(io.StringIO(inherited.read_text(encoding='utf-8-sig'))):
            rid = 'de-'+row['Resource ID']
            resources.append(resource(rid, row['Title'], row['URL'], 'Arabic' if 'Arabic' in row['Title'] else 'English', row['Format'], 'Existing DE collection', row['How to Use It']+' '+row['Access / Cost Note'], 'Inherited from data-engineering-learning-roadmap: '+row['Source'], 'Preserved existing catalog link; current access not independently retested'))
    data = dict(schema_version=1, title='Python Learning Roadmap', owner='Sohila Khaled Abbas', updated='2026-10-31', pacing=dict(weeks=12,hours_per_week=7,note='Suggested 84-hour learning budget, not a deadline. The ML node is optional. Reallocate time using your diagnostic and exit checks.'), phases=phases, topics=topics, resources=resources, connections=connections, weeks=[dict(number=i+1,title=w[0],topics=w[1],deliverable=w[2]) for i,w in enumerate(weeks)])
    (ROOT/'data/roadmap.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    notes=ROOT/'docs/notes'; notes.mkdir(parents=True,exist_ok=True)
    rmap={r['id']:r for r in resources}
    for t in topics:
        watch=f"[Chapter {t['chapter']['number']} · {t['chapter']['label']}]({t['chapter']['url']})" if t['chapter'] else 'Extension beyond the Boot.dev video'
        text=f"# {t['title']}\n\n{t['summary']}\n\n{watch}\n\n## Connect to your work\n\n{t['bridge']}\n\n## Learn by doing\n\n"+'\n'.join('- '+s for s in t['learn'])+f"\n\n## Original practice\n\n{t['exercise']}\n\n## Exit check\n\n{t['gate']}\n"
        if t['code']: text+='\n## Small original example\n\n```python\n'+t['code']+'\n```\n'
        if t['pitfalls']: text+='\n## Watch for\n\n'+'\n'.join('- '+p for p in t['pitfalls'])+'\n'
        text+='\n## Resources\n\n'+'\n'.join(f"- [{rmap[r]['title']}]({rmap[r]['url']})" for r in t['resources'])+'\n'
        if t['cs50'] is not None: text+=f"- [CS50P Week {t['cs50']}: lecture and problem set](https://cs50.harvard.edu/python/weeks/{t['cs50']}/). Solve independently; this repo contains no CS50 problem-set answers.\n"
        text+='\n[Back to the roadmap](../roadmap.md) · [Source and attribution policy](../sources.md)\n'
        (ROOT/t['note_path']).write_text(text,encoding='utf-8')
    roadmap='# Python learning roadmap\n\nA focused expansion of the Python stage in [Sohila’s data engineering roadmap]('+GITHUB+'data-engineering-learning-roadmap). Readiness comes from the exit checks, not from watching a video.\n\n'
    for p in phases:
        roadmap+=f"## {p['number']} · {p['title']}\n\n{p['weeks']} · {p['subtitle']}\n\n| Topic | Practice | Exit evidence |\n| --- | --- | --- |\n"
        for t in topics:
            if t['phase']==p['id']: roadmap+=f"| [{t['title']}](notes/{t['id']}.md) | {t['exercise']} | {t['gate']} |\n"
        roadmap+='\n'
    (ROOT/'docs/roadmap.md').write_text(roadmap,encoding='utf-8')
    weekly='# A flexible 12-week plan\n\nPlan around seven hours per week: about two learning, four building and one reviewing. This is a planning budget; repeat or compress weeks based on exit evidence. The optional ML branch can be deferred.\n\n'
    for i,(title,ids,outcome) in enumerate(weeks,1):
        weekly+=f"## Week {i} · {title}\n\n"+'\n'.join(f"- [{next(t['title'] for t in topics if t['id']==id)}](notes/{id}.md)" for id in ids)+f"\n\n**Evidence:** {outcome}.\n\n**Review:** Explain one idea without notes, add one boundary test, and record the next smallest step.\n\n"
    (ROOT/'docs/weekly-plan.md').write_text(weekly,encoding='utf-8')
    print(f'Built {len(topics)} topics, {len(resources)} resources and {len(weeks)} weeks.')

if __name__ == '__main__':
    build()
