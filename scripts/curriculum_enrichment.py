"""Original companion material and user-selected resource metadata, reviewed 2026-11-01."""
from urllib.parse import parse_qs, urlparse

DATE = '2026-11-01'

def youtube_key(url):
    u = urlparse(url)
    q = parse_qs(u.query)
    if u.hostname not in {'youtube.com', 'www.youtube.com', 'youtu.be'}:
        return None
    if q.get('list'):
        return 'playlist:' + q['list'][0]
    value = u.path.strip('/') if u.hostname == 'youtu.be' else q.get('v', [''])[0]
    return 'video:' + value if value else None


def enrich(resources, topics, phases):
    # Titles were checked against the requested YouTube pages in the connected browser.
    # These editorial mappings are learning choices, not claims of transcript analysis.
    videos = [
        ('arabigdata-basics', 'Python - The Basics - Part 1 | جحر السوعبان', 'XKQaCF_Om8o', 'Arabic', 'Foundations companion', ['environment','variables','functions','loops'], 'An Arabic foundations alternative. Use it for a concept you cannot yet explain; apply the same original exit checks.'),
        ('baraa-python', 'Python Full Course for Beginners (13 Hours) – From Zero to Hero', 'Rq5gJVxz55Q', 'English', 'Visual course alternative', ['variables','functions','lists','dictionaries','modules'], 'Use Data with Baraa’s visual explanations as an alternative foundation course. Avoid repeating thirteen hours if the diagnostic already shows mastery.'),
        ('streamlit-arabic', 'تطبيق عملي: مبادئ تصميم واجهات وتطبيقات علم البيانات | Streamlit Basics (Dashboards & Data Apps)', '6aoIQ4bz49w', 'Arabic', 'Build a data interface', ['data-apps','publish'], 'Apply the interface ideas to a synthetic quality report or EGP summary after the transformation logic has tests.'),
        ('codezilla-oop', 'Python Object Oriented Programming - شرح للبرمجة كائنية التوجه في بايثون', 'A9kSngn7254', 'Arabic', 'OOP companion', ['modules','oop-design'], 'Use for object-oriented vocabulary, then implement a small data model and compare composition with inheritance.'),
        ('venv-video', 'The Complete Guide to Python Virtual Environments!', 'KxvKCSwlUv8', 'English', 'Environment companion', ['environment','packaging-projects'], 'Pair this explanation with the Windows-first setup note. Use your existing interpreter and project environment.'),
        ('sqlite-video', 'Python SQLite Tutorial: Build a Python project with a SQLite database', 'iXYeb2artTE', 'English', 'Database project companion', ['sql','sql-transactions','pipeline'], 'Compare the project approach with the supplied fixture pipeline. Reconcile keys, transactions and repeated deliveries.'),
    ]
    playlists = [
        ('analysis-crash', 'تحليل البيانات في بايثون (الدورة المصغرة) | Python for Data Analysis (Crash Course)', 'PLWd4nYaF_Vx7Db9uFWf_Df-UrP8ArF4L_', 'Arabic', ['pandas','joins','quality'], 'An Arabic data-analysis companion. Reproduce a filtering, grouping and join task on your own fixture.'),
        ('analysis-playlist', 'Python for Data Analysis', 'PLiEts138s9P0w-WX4Rmml-_zhnBkXLWtc', 'Check source', ['pandas','joins','numpy'], 'Select lessons matching tabular processing and analysis. The title is verified; spoken language and individual lesson coverage are not inferred.'),
        ('ml-python-arabic', '03 تعليم الآلة , القسم الثالث : بايثون Machine learning , Python', 'PL6-3IRz2XF5UM-FWfQeF1_YhMMa12Eg3s', 'Arabic', ['variables','functions','numpy','ml'], 'Already present in your inherited collection; retained once and enriched with the requested playlist title and topic mappings.'),
        ('exploration-preparation', 'Data Exploration and Preparation', 'PLQ1FVkQVumFIEH7dYP_2L6vi_LyjlVsGm', 'Check source', ['pandas','joins','quality','ml'], 'Use for exploration and preparation decisions: inspect missingness, duplicates, outliers and feature assumptions before selecting a treatment.'),
        ('dash-plotly-powerbi', 'Data Visualization using Dash, Plotly, and PowerBI', 'PLQ1FVkQVumFJpSpiVrgCF0UQxTGrmVnRk', 'Check source', ['data-apps','publish'], 'Connect your Power BI experience to Python visualization and app interfaces. Choose a chart from the question, row grain and audience.'),
    ]
    mapping = {}
    for rid,title,vid,language,role,ids,note in videos:
        row = dict(id=rid,title=title,url=f'https://www.youtube.com/watch?v={vid}',language=language,kind='Video',role=role,note=note,origin='User-selected YouTube resource',verification=f'Page title verified {DATE}; no full transcript or playback entitlement is claimed.',topics=ids)
        resources.append(row)
        mapping[rid] = ids
    for rid,title,pid,language,ids,note in playlists:
        key = 'playlist:'+pid
        existing = next((r for r in resources if youtube_key(r['url']) == key), None)
        row = dict(id=existing['id'] if existing else rid,title=title,url=f'https://www.youtube.com/playlist?list={pid}',language=language,kind='Playlist',role='Topic companion',note=note,origin='User-selected YouTube playlist'+(' · also in the inherited DE catalog' if existing else ''),verification=f'Playlist title verified {DATE}; lesson order and availability are controlled by its owner.',topics=ids)
        if existing:
            inherited_origin = existing['origin']
            existing.update(row)
            existing['origin'] += ' · '+inherited_origin
        else:
            resources.append(row)
        mapping[row['id']] = ids

    official = [
        ('iterators-docs','Python · iterators and generators','https://docs.python.org/3/howto/functional.html'),
        ('context-docs','Python · contextlib','https://docs.python.org/3/library/contextlib.html'),
        ('dataclass-docs','Python · dataclasses','https://docs.python.org/3/library/dataclasses.html'),
        ('typing-docs','Python · type hints and protocols','https://docs.python.org/3/library/typing.html'),
        ('regex-docs','Python · regular expressions','https://docs.python.org/3/library/re.html'),
        ('unicode-docs','Python · Unicode normalization','https://docs.python.org/3/library/unicodedata.html'),
        ('package-projects-docs','PyPA · packaging a Python project','https://packaging.python.org/en/latest/tutorials/packaging-projects/'),
        ('zoneinfo-docs','Python · IANA time zones','https://docs.python.org/3/library/zoneinfo.html'),
        ('profile-docs','Python 3.12 · profiling with cProfile','https://docs.python.org/3.12/library/profile.html'),
        ('memory-docs','Python · memory allocation tracing','https://docs.python.org/3/library/tracemalloc.html'),
        ('async-docs','Python · asyncio','https://docs.python.org/3/library/asyncio.html'),
        ('parquet-docs','Apache Arrow · Parquet in Python','https://arrow.apache.org/docs/python/parquet/'),
        ('sqlalchemy-docs','SQLAlchemy 2.0 · transactions and bound parameters','https://docs.sqlalchemy.org/en/20/tutorial/dbapi_transactions.html'),
        ('streamlit-docs','Streamlit · app fundamentals','https://docs.streamlit.io/get-started/fundamentals/main-concepts'),
        ('plotly-docs','Plotly · Python visualization','https://plotly.com/python/'),
        ('dash-docs','Dash · official introductory tutorial','https://dash.plotly.com/tutorial'),
        ('mock-docs','pytest · mock modules and environments','https://docs.pytest.org/en/stable/how-to/monkeypatch.html'),
    ]
    for rid,title,url in official:
        resources.append(dict(id=rid,title=title,url=url,language='English',kind='Documentation',role='Concept reference',note='Read the section needed for the exercise and verify compatibility with your project interpreter.',origin='Official project documentation',verification=f'Official documentation checked {DATE}.'))

    phases.append(dict(id='depth',number='06',title='Choose your next depth',weeks='After the core · optional branches',subtitle='Twelve focused extensions for reliable data tools and applications.',color='purple'))
    def add(id,title,requires,refs,summary,learn,exercise,gate,explanation,code='',pitfalls=None):
        topics.append(dict(id=id,phase='depth',title=title,hours=3,optional=True,summary=summary,bridge='Apply this to your Python data tools, PixelFed quality work, n8n integrations or BI delivery when the project needs it.',learn=learn,exercise=exercise,gate=gate,requires=requires,resources=refs,chapter=None,cs50=None,code=code,pitfalls=pitfalls or [],explanation=explanation,note_path=f'docs/notes/{id}.md'))
    add('oop-design','OOP, composition & data classes',['modules'],['dataclass-docs','codezilla-oop'],
        'Use objects to express a useful boundary, with functions for transformation logic.',
        ['Model a validated record with a dataclass and explicit units.','Pass an extractor into a pipeline instead of hard-coding its source.','Compare composition with inheritance using one concrete change request.'],
        'Create an Order dataclass and a report service that accepts a fixture reader.',
        'A second reader can be substituted without rewriting the aggregation; invalid input is rejected before creating the domain record.',
        ['A class is useful when related state and behavior form a stable concept. A dataclass reduces repetitive initialization and representation code, but it does not validate every input automatically. Keep boundary parsing separate from the trusted object.', 'Composition means a service receives the collaborator it needs: for example, a reader or a clock. This makes fixture tests possible without making HTTP calls. Inheritance is appropriate for a genuine substitutable relationship, not simply for sharing two helper methods.'],
        'from dataclasses import dataclass\n\n@dataclass(frozen=True)\nclass Order:\n    order_id: str\n    total_piastres: int\n\norder = Order("O001", 12550)\nprint(order.total_piastres)',
        ['frozen=True is not deep immutability for nested mutable objects.','Type annotations alone do not enforce a runtime schema.'])
    add('generators','Iterators, generators & streaming',['loops','files'],['iterators-docs'],
        'Process a sequence without requiring every record to be resident in memory.',
        ['Explain iterable versus iterator and one-pass consumption.','Yield parsed rows while the file context is open.','Use bounded batches and measure peak memory.'],
        'Replace a fixture reader that returns list(reader) with a generator and compare peak memory on a larger synthetic file.',
        'Both versions produce identical aggregates; the streaming version keeps peak memory bounded by the chosen batch and aggregation state.',
        ['A generator defers execution until the consumer asks for a value. That can reduce the input retained in memory, but an unbounded grouping dictionary can still grow with the number of distinct keys. Streaming describes the whole design, not merely the presence of yield.', 'Keep file ownership clear. Opening a file outside a generator and returning an iterator after closing that file creates a reader that cannot be used. Test early termination as well as complete consumption.'],
        'import csv\n\ndef rows(path):\n    with open(path, encoding="utf-8", newline="") as handle:\n        for row in csv.DictReader(handle):\n            yield row', ['An iterator may be exhausted after the first pass.','list(generator) materializes the records again.'])
    add('contexts-decorators','Context managers & decorators',['functions','errors','files'],['context-docs','python'],
        'Make cleanup and cross-cutting behavior explicit without obscuring a function contract.',
        ['Use with and try/finally for deterministic cleanup.','Write one context manager that yields exactly once.','Preserve wrapped function metadata with functools.wraps.'],
        'Create a timer context and a logging decorator for a fixture transformation. Test cleanup when the transformation raises.',
        'The original error remains visible, cleanup always runs, and a decorated function keeps its name and docstring.',
        ['The with statement gives a resource an explicit lifetime. A generator-based context manager acquires the resource before yield and releases it in finally. Cleanup must not silently turn a failed operation into a successful result.', 'A decorator replaces a callable with another callable. Keep validation and business rules visible; a short timer or logging wrapper is easier to review than a stack of decorators that changes retry, transaction and exception behavior at once.'],
        'from contextlib import contextmanager\nfrom time import perf_counter\n\n@contextmanager\ndef elapsed():\n    start = perf_counter()\n    try:\n        yield\n    finally:\n        print(f"seconds={perf_counter()-start:.6f}")')
    add('typing-contracts','Type hints, protocols & validation',['modules','oop-design'],['typing-docs','mock-docs'],
        'Use static contracts to improve maintainability while validating external data at runtime.',
        ['Annotate collection element types and optional results.','Use Protocol to describe a small reader interface.','Distinguish a type checker from runtime parsing and validation.'],
        'Type a reader returning Iterable[Order], then inject a fake reader in tests. Add a malformed JSON input test.',
        'The fake satisfies the interface and the malformed payload is rejected independently of its annotations.',
        ['Type hints describe expected values to editors and static tools. Python does not automatically reject a string passed into an int-annotated parameter. Validate untrusted CSV, JSON and environment values when they enter the application.', 'A protocol describes the operations a collaborator must support without requiring a shared implementation. Keep the interface narrow: one read method is easier to fake and reason about than a provider object exposing dozens of unrelated calls.'],
        'from typing import Protocol, Iterable\n\nclass Reader(Protocol):\n    def read(self) -> Iterable[dict[str, str]]: ...', ['Use syntax supported by the selected interpreter; this repo baseline remains Python 3.11+.'])
    add('text-unicode','Regex, Unicode & Arabic text',['variables','files'],['regex-docs','unicode-docs'],
        'Treat encoding, normalization and business identifiers as separate decisions.',
        ['Read UTF-8 explicitly and retain original text.','Use raw-string patterns and fullmatch for full-field validation.','Explain Unicode digits versus an ASCII-only identifier contract.'],
        'Validate ASCII order IDs, preserve Arabic category labels, and compare composed/decomposed forms without overwriting the raw value.',
        'Arabic text round-trips; invalid identifiers fail; normalization is recorded and never silently merges distinct business keys.',
        ['Encoding converts bytes to text. Normalization changes the representation of some equivalent Unicode sequences. Neither operation decides whether two customer names represent the same person, and stripping Arabic characters is not a valid cleaning default.', 'Use a regular expression for a bounded structural rule, such as an order identifier. A pattern proving that text resembles an email or phone number cannot prove the person owns it. Keep that distinction clear when designing intake or data-quality rules.'],
        'import re\nimport unicodedata\n\nraw = "عناية بالبشرة"\nnormalized = unicodedata.normalize("NFC", raw)\nvalid_id = re.fullmatch(r"O[0-9]{3}", "O001") is not None\nprint(normalized, valid_id)')
    add('packaging-projects','Packages & reproducible dependencies',['environment','modules','tests'],['packaging','package-projects-docs','venv-video'],
        'Make the tool runnable from a clean environment with declared requirements.',
        ['Separate import package, distribution name and project directory.','Describe metadata and interpreter constraints in pyproject.toml.','Record a repeatable dependency set and test it in a clean environment.'],
        'Package the quality CLI with a console entry point and run it after a clean install in a new virtual environment.',
        'The command works outside the repository working directory and the setup documentation identifies the tested interpreter and dependencies.',
        ['A working notebook environment is not a reproducible installation contract. A project should declare what it imports and which interpreter it supports. Use a virtual environment so another project’s upgrades do not silently change this one.', 'Distinguish allowed dependency ranges from the exact set tested for an application release. Record the tool and versions used to reproduce that set. Build and install the package in a clean environment to catch accidental imports from the current directory.'])
    add('time-money','Time zones, money & measurement units',['variables','files','http'],['zoneinfo-docs','python'],
        'Make temporal and numeric meaning explicit before aggregation.',
        ['Store event and ingestion timestamps separately as aware UTC instants.','Convert to Africa/Cairo for display or a documented business date.','Use validated Decimal values or integer minor units with a rounding policy.'],
        'Design a quote fixture contract with provider_as_of, fetched_at, rate precision, base and quote currency. Test an invalid date and stale quote.',
        'A stale observation is not described as live; time conversion preserves the instant; amounts reconcile at the documented precision.',
        ['A timestamp without a time zone is ambiguous until a source contract supplies its meaning. The event time and the time your process fetched the event answer different questions. Keep both when freshness affects a downstream decision.', 'A currency amount and an exchange rate need different precision policies. EGP minor units work well for many expense amounts, but a forex rate may require more than two decimal places. Do not truncate a rate using the ledger’s amount parser. On Windows, install the first-party tzdata package in the project environment if IANA zone data is unavailable.'],
        'from datetime import datetime, timezone\nfrom zoneinfo import ZoneInfo\n\ninstant = datetime(2026, 11, 1, 12, tzinfo=timezone.utc)\nlocal = instant.astimezone(ZoneInfo("Africa/Cairo"))\nprint(instant.isoformat(), local.isoformat())')
    add('async-io','Async I/O & bounded concurrency',['http','tests'],['async-docs','mock-docs'],
        'Overlap waiting work while preserving deadlines and explicit failure policy.',
        ['Explain a coroutine, await, task and cancellation.','Limit concurrent requests and keep per-request timeouts.','Separate I/O waiting from CPU-bound transformation work.'],
        'Use fake delayed fetches to compare sequential and bounded concurrent retrieval. Inject one timeout and check cancellation cleanup.',
        'Concurrency never exceeds the limit; one timeout follows a documented policy; the test performs no live API calls.',
        ['Asyncio is most useful when a program spends time waiting for I/O. It does not make a CPU-heavy transformation faster merely because a function is declared async. Keep blocking work out of the event loop or choose a different execution model.', 'Bound concurrency to protect the provider and your own machine. A semaphore limits work in flight; a deadline limits how long a request may wait. Both differ from retries, which must also respect the endpoint’s replay safety and quota policy.'],
        'import asyncio\n\nasync def fake_fetch(value):\n    await asyncio.sleep(0.01)\n    return value\n\nasync def main():\n    limit = asyncio.Semaphore(2)\n    async def bounded(value):\n        async with limit:\n            return await fake_fetch(value)\n    print(await asyncio.gather(*(bounded(i) for i in range(4))))\n\nasyncio.run(main())')
    add('profiling','Profiling, memory & measured optimization',['generators','pandas'],['profile-docs','memory-docs'],
        'Measure a bottleneck before changing a correct implementation.',
        ['Separate benchmarking from profiling.','Use cProfile and tracemalloc with a stated interpreter and workload.','Verify outputs and memory behavior after optimization.'],
        'Profile the fixture pipeline and a scaled synthetic input; compare an eager reader with a bounded streaming design.',
        'The report states input size, environment, elapsed time and peak allocation; outputs remain identical.',
        ['A profiler attributes execution cost to functions; a benchmark compares elapsed behavior under controlled conditions. Profiling adds overhead, so a profiler report is not automatically a fair benchmark between Python and native library code.', 'Measure the whole pipeline, including parsing, joins, serialization and database work. A faster line of code is not valuable if the dominant cost lies elsewhere. Keep the input and expected outputs fixed while changing one design choice.'],
        'import tracemalloc\n\ntracemalloc.start()\nvalues = list(range(1000))\ncurrent, peak = tracemalloc.get_traced_memory()\ntracemalloc.stop()\nprint({"current_bytes": current, "peak_bytes": peak})')
    add('columnar-data','CSV, Parquet & schema evolution',['files','pandas','joins'],['parquet-docs','pandas'],
        'Choose a storage format using types, access pattern and downstream compatibility.',
        ['Compare text CSV with typed columnar Parquet.','Read selected columns and inspect schema metadata.','Define compatible column changes, nullability and precision.'],
        'Export a copied synthetic fixture to Parquet, reload selected columns and compare values, nulls and timestamp interpretation.',
        'The round-trip report identifies every type conversion and the consumer can reproduce the expected row count and totals.',
        ['CSV is convenient for inspection and interchange, but it does not carry a universal typed schema. Parquet stores typed columnar data and can support reading only the columns needed by an analysis. Performance depends on the actual file layout and workload.', 'Schema evolution is a compatibility decision. Adding an optional field differs from changing a business key or reducing decimal precision. Keep a written schema contract and test an older consumer against the changed dataset before promoting it.'])
    add('sql-transactions','Database transactions & connection lifetimes',['sql','contexts-decorators'],['sqlalchemy-docs','sqlite-video'],
        'Control the unit of work and distinguish a transaction from a connection.',
        ['Bind values as SQL parameters and keep identifiers controlled.','Demonstrate commit and rollback on a multi-row operation.','Close resources and define conflict handling before introducing concurrency.'],
        'Port a fixture load to a chosen SQLAlchemy driver; fail the second write and prove the intended transaction boundary.',
        'The rollback behavior matches the documented unit of work, duplicate delivery policy remains stable, and credentials stay outside source.',
        ['A connection is a communication resource; a transaction groups changes under a commit or rollback boundary. A context manager can make that boundary visible, but you must understand which context manages only the connection and which also manages the transaction.', 'Parameter binding protects values from being interpreted as SQL syntax. It does not turn an arbitrary user-provided table name into a safe identifier. Use a controlled identifier mapping and explicit database constraints for keys and uniqueness.'])
    add('data-apps','Data apps with Streamlit, Plotly & Dash',['pandas','quality','publish'],['streamlit-docs','plotly-docs','dash-docs','streamlit-arabic','dash-plotly-powerbi'],
        'Turn a tested dataset into an interface that communicates the right question.',
        ['Choose one framework and learn its state/rerun or callback model.','Keep transformations testable outside the UI.','Show empty, stale and invalid-data states with accessible labels.'],
        'Build a read-only quality dashboard from the synthetic CLI output. Show row counts, rejects, freshness and a filterable category chart.',
        'The chart reconciles to the CLI output; empty filters have a clear state; a reviewer can identify the source and limitations.',
        ['Streamlit is useful for rapidly building Python-led data interfaces. Its execution and state behavior differ from a static Power BI report. Keep expensive data loading and transformations separated from the display and learn the cache/state rules before relying on them.', 'Plotly provides figures; Dash adds an application model with layouts and callbacks. Choose one small workflow first. Your existing Power BI skills transfer through metric definitions, filter behavior, accessible color and clear data provenance—not through copying every dashboard interaction unchanged.'])

    # Add resource mappings after all topic IDs exist, preserving the original IDs and progress.
    for rid,ids in mapping.items():
        for t in topics:
            if t['id'] in ids and rid not in t['resources']:
                t['resources'].append(rid)
    deeper = {
        'pandas': ['Inspect a sample, shape, dtypes and missingness before choosing a transformation. Keep a raw copy and a small typed contract so coercion failures remain visible.', 'When comparing pandas with SQL or Power Query, use identical row grain, null rules and grouping keys. Reconciliation is more useful than a screenshot of a successful notebook cell.'],
        'joins': ['Declare the expected relationship before merging: one-to-one, many-to-one or many-to-many. Validate reference-key uniqueness before a join; counting rows only after multiplication can hide the reason a KPI changed.', 'Check unmatched keys in both directions and decide what an unknown dimension means. An inner join may discard legitimate facts, while filling every missing value with zero invents measurements.'],
        'http': ['Document timeout, schema, pagination, rate-limit and freshness behavior as separate parts of the API contract. HTTP 200 alone does not prove the payload is complete or current.', 'Retry only the failures and operations that justify it. Preserve the provider timestamp and fetch timestamp, and keep an offline fixture suite so provider outages do not break basic validation tests.'],
        'tests': ['Choose tests that would catch a meaningful defect: a multiplied join, a lost zero, a conflicting key or a missing transaction rollback. A test that merely repeats the implementation’s calculation is weak evidence.', 'Keep network and clock behavior injectable. Use a temporary directory or database for I/O tests, then add a focused end-to-end fixture check that reconciles the exported result.'],
        'quality': ['A quality rule needs a business meaning, severity and action. Profile a copied sample, then separate unacceptable identifiers from optional attributes whose unknown value may be valid.', 'Report the denominator for every percentage and preserve rejected records with reasons. Compare before/after quality using stable definitions; a smaller output is not automatically a cleaner one.'],
        'ml': ['Fit preprocessing on training data and apply the learned transformation to held-out data. Splitting after imputing or scaling leaks information about the evaluation set.', 'Document the prediction target, observation time and availability of each feature. A feature that becomes known after the business decision can make an apparently strong model unusable.'],
        'environment': ['An environment isolates project dependencies, while the interpreter still has its own version and executable path. Confirm both before installing or upgrading packages.', 'On your Windows workflow, invoking .venv\\Scripts\\python.exe directly avoids needing to change activation policy. Keep the environment reproducible rather than copying it between machines.'],
        'sql': ['The same business key delivered twice must have an explicit policy: accept identical replay, reject a conflict, or apply a documented update rule. A random new identifier on every run prevents replay detection.', 'Verify database constraints and transaction behavior with deliberate failures. A successful second run should reconcile stored rows and totals, not merely exit without an exception.'],
    }
    for t in topics:
        if t['id'] in deeper:
            t['explanation'] = deeper[t['id']]
        t.setdefault('optional',False)
        t.setdefault('explanation', [t['summary']+' '+t['bridge'], 'Work through the practice with a tiny fixture, predict the result before running it, and record one boundary case. Use the exit check as evidence before moving on.'])
    return resources,topics,phases
