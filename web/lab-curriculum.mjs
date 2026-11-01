// Original exercises. Checks are visible learning aids, not certification or grading.
export const ORDERS_CSV = `order_id,category,amount_egp,status
EG-101,Books,180.50,completed
EG-102,Transport,45.00,completed
EG-103,Books,80.00,pending
EG-104,Books,120.25,completed
EG-105,Transport,-5.00,completed
`;
export const challenges = [
  {id:'first-script',title:'01 · Your first useful script',level:'Start here',minutes:5,topics:['introduction','variables','environment','baseline'],brief:'Build a short status message for a data-quality report. Define project and valid_rows, then use an f-string to create message.',contract:'message must be "PixelFed: 42 valid rows". Print it so you can inspect the result.',starter:`project = "PixelFed"
valid_rows = 42

# Replace this with an f-string using both variables.
message = "Your report goes here"
print(message)
`,solution:`project = "PixelFed"
valid_rows = 42
message = f"{project}: {valid_rows} valid rows"
print(message)
`,hints:['An f-string starts with f before the opening quote.','Put expressions inside braces: f"{project}: ...".'],stretch:'Change valid_rows to 0. Predict the new message before running it.',checks:[{name:'Uses the report values',code:'assert message == f"{project}: {valid_rows} valid rows", "Build the message from project and valid_rows."'},{name:'Expected report text',code:'assert message == "PixelFed: 42 valid rows", f"Expected PixelFed: 42 valid rows; got {message!r}."'}]},
  {id:'invoice-total',title:'02 · Reconcile an EGP invoice',level:'Foundations',minutes:10,topics:['functions','computing','scope'],brief:'Write invoice_total(prices). Return the sum rounded to two decimal places. An empty invoice totals 0. Do not round each line before adding it.',contract:'Return a number, rather than printing inside the function. The checks call it with several invoices.',starter:`def invoice_total(prices):
    # Return the total rounded to two decimal places.
    return 0

print(invoice_total([180.50, 45.00, 120.25]))
`,solution:`def invoice_total(prices):
    return round(sum(prices), 2)

print(invoice_total([180.50, 45.00, 120.25]))
`,hints:['sum(prices) adds a sequence of numbers.','Return round(sum(prices), 2). For production money, explore Decimal in the time/money lesson.'],stretch:'Try two values with three decimal places. How does rounding the final total differ from rounding each line?',checks:[{name:'Reconciles a multi-line invoice',code:'assert invoice_total([180.50, 45, 120.25]) == 345.75, "The invoice should total 345.75 EGP."'},{name:'Handles an empty invoice',code:'assert invoice_total([]) == 0, "An empty invoice should total 0."'},{name:'Rounds the final total',code:'assert invoice_total([1.123, 2.234]) == 3.36, "Round the final sum to two decimal places."'}]},
  {id:'delivery-policy',title:'03 · Encode a delivery policy',level:'Foundations',minutes:10,topics:['comparisons'],brief:'Implement delivery_fee(subtotal, city). An invoice of at least 500 EGP has free delivery. Below 500, Cairo costs 35 EGP and every other city costs 60 EGP. Treat city names case-insensitively and ignore surrounding spaces.',contract:'Check the free-delivery threshold first. Return an integer fee.',starter:`def delivery_fee(subtotal, city):
    return 0

print(delivery_fee(200, " Cairo "))
`,solution:`def delivery_fee(subtotal, city):
    if subtotal >= 500:
        return 0
    if city.strip().casefold() == "cairo":
        return 35
    return 60

print(delivery_fee(200, " Cairo "))
`,hints:['The threshold includes exactly 500: use >=.','Use city.strip().casefold() before comparing with "cairo".'],stretch:'Try 499.99, 500, and 500.01. These boundary cases often reveal policy bugs.',checks:[{name:'Cairo normalization',code:'assert delivery_fee(200, " CAIRO ") == 35, "Normalize spaces and case for Cairo."'},{name:'Other cities',code:'assert delivery_fee(200, "Damietta") == 60, "Other cities cost 60 EGP below the threshold."'},{name:'Threshold and precedence',code:'assert delivery_fee(500, "Cairo") == 0 and delivery_fee(700, "Damietta") == 0, "Delivery is free at 500 EGP and above, in any city."'}]},
  {id:'clean-names',title:'04 · Clean a customer-name column',level:'Collections',minutes:10,topics:['lists','loops','text-unicode'],brief:'Write clean_names(values). Remove surrounding whitespace, use casefold for consistent case, and skip values that are empty after stripping. Preserve the remaining order and do not mutate the input list.',contract:'Return a new list. The inputs in this exercise are strings.',starter:`def clean_names(values):
    return values

print(clean_names(["  Sohila ", "", "   ", " Mona"]))
`,solution:`def clean_names(values):
    return [value.strip().casefold() for value in values if value.strip()]

print(clean_names(["  Sohila ", "", "   ", " Mona"]))
`,hints:['Build a new list with a loop or comprehension.','Test value.strip() before adding value.strip().casefold() to the result.'],stretch:'Try Arabic names. Case folding does not remove Arabic diacritics; decide explicitly whether your project needs that normalization.',checks:[{name:'Normalizes and removes blanks',code:'assert clean_names(["  Sohila ", "", "   ", " Mona"]) == ["sohila", "mona"], "Strip spaces, normalize case, and skip blanks."'},{name:'Handles empty input',code:'assert clean_names([]) == [], "An empty input should produce an empty list."'},{name:'Preserves the source',code:'source = [" SOHILA "]; clean_names(source); assert source == [" SOHILA "], "Do not change the input list."'}]},
  {id:'expense-groups',title:'05 · Group an EGP expense ledger',level:'Collections',minutes:15,topics:['dictionaries','ledger'],brief:'Write expense_totals(rows). Each row has category and amount_egp. Aggregate amounts by category, preserving all categories. Return a dictionary; return {} for no rows.',contract:'The fixture for this exercise already contains valid numeric amounts. Validation is a separate exercise.',starter:`def expense_totals(rows):
    return {}

rows = [{"category": "Food", "amount_egp": 75},
        {"category": "Food", "amount_egp": 25},
        {"category": "Transport", "amount_egp": 30}]
print(expense_totals(rows))
`,solution:`def expense_totals(rows):
    totals = {}
    for row in rows:
        category = row["category"]
        totals[category] = totals.get(category, 0) + row["amount_egp"]
    return totals

print(expense_totals([{"category": "Food", "amount_egp": 75},
                     {"category": "Food", "amount_egp": 25}]))
`,hints:['Use a dictionary with category names as keys.','totals.get(category, 0) provides a starting value for the first row.'],stretch:'Reconcile sum(totals.values()) with the sum of source amounts. This is the same idea as a SQL GROUP BY reconciliation.',checks:[{name:'Accumulates repeated categories',code:'assert expense_totals([{"category":"Food","amount_egp":75},{"category":"Food","amount_egp":25},{"category":"Transport","amount_egp":30}]) == {"Food":100,"Transport":30}, "Accumulate repeated keys rather than overwriting the previous amount."'},{name:'Handles no expenses',code:'assert expense_totals([]) == {}, "No rows should produce an empty dictionary."'}]},
  {id:'reconcile-ids',title:'06 · Reconcile source and target IDs',level:'Collections',minutes:10,topics:['sets','algorithms'],brief:'Write reconcile_ids(expected, actual). Return a dictionary with missing and unexpected, each a sorted list of unique IDs. Duplicate IDs do not change the reconciliation.',contract:'missing = expected IDs absent from actual. unexpected = actual IDs absent from expected.',starter:`def reconcile_ids(expected, actual):
    return {"missing": [], "unexpected": []}

print(reconcile_ids([101, 102, 103], [101, 103, 104]))
`,solution:`def reconcile_ids(expected, actual):
    source, target = set(expected), set(actual)
    return {"missing": sorted(source - target),
            "unexpected": sorted(target - source)}

print(reconcile_ids([101, 102, 103], [101, 103, 104]))
`,hints:['Convert the inputs to sets.','Set difference is directional: source - target and target - source answer different questions.'],stretch:'What extra check would you add if duplicate business keys were an error rather than something to ignore?',checks:[{name:'Finds both mismatch directions',code:'assert reconcile_ids([101,102,103], [101,103,104]) == {"missing":[102],"unexpected":[104]}, "Keep missing and unexpected directions separate."'},{name:'Sorts and deduplicates',code:'assert reconcile_ids([3,1,3], [4,4]) == {"missing":[1,3],"unexpected":[4]}, "Return sorted unique mismatches."'},{name:'Empty reconciliation',code:'assert reconcile_ids([], []) == {"missing":[],"unexpected":[]}, "Both empty lists reconcile."'}]},
  {id:'validate-amount',title:'07 · Reject a bad amount honestly',level:'Reliable tools',minutes:15,topics:['errors','debugging','tests','time-money'],brief:'Write parse_amount(text). Convert a numeric string to float and require a positive, finite value. Invalid text, zero, negatives, NaN and infinity must raise ValueError.',contract:'Return a float for valid input. Do not return 0 to hide invalid data.',starter:`import math

def parse_amount(text):
    return 0.0

print(parse_amount("180.50"))
`,solution:`import math

def parse_amount(text):
    value = float(text)
    if not math.isfinite(value) or value <= 0:
        raise ValueError("Amount must be positive and finite")
    return value

print(parse_amount("180.50"))
`,hints:['float(text) already raises ValueError for invalid numeric strings.','Use math.isfinite(value) and value > 0 to define the valid case.'],stretch:'Try "nan". Why does checking only value <= 0 fail to reject it?',checks:[{name:'Parses a valid amount',code:'assert parse_amount("180.50") == 180.5 and isinstance(parse_amount("1"), float), "Return a float for valid numeric text."'},{name:'Rejects invalid, zero and negative amounts',code:'for text in ("bad", "", "0", "-5"):\n    try:\n        parse_amount(text)\n    except ValueError:\n        pass\n    else:\n        raise AssertionError(f"{text!r} must raise ValueError")'},{name:'Rejects non-finite values',code:'for text in ("nan", "inf", "-inf"):\n    try:\n        parse_amount(text)\n    except ValueError:\n        pass\n    else:\n        raise AssertionError(f"{text!r} must raise ValueError")'}]},
  {id:'csv-orders',title:'08 · Read a real-shaped CSV file',level:'Data work',minutes:15,topics:['files','cli','packaging-projects'],brief:'Write load_orders(path). Read a UTF-8 CSV using csv.DictReader, and return a list of dictionaries with order_id as a string and amount_egp as float. Keep the other columns and row order.',contract:'A synthetic orders.csv file is available in the working directory. Checks create their own small CSVs to verify the function.',starter:`import csv

def load_orders(path):
    return []

orders = load_orders("orders.csv")
print(orders[:2])
`,solution:`import csv

def load_orders(path):
    with open(path, encoding="utf-8", newline="") as handle:
        return [{**row, "amount_egp": float(row["amount_egp"])}
                for row in csv.DictReader(handle)]

print(load_orders("orders.csv")[:2])
`,hints:['Use with open(path, encoding="utf-8", newline="") as handle.','Each DictReader row is a dictionary. Replace only amount_egp with float(row["amount_egp"]).'],stretch:'Edit the dataset below and rerun. Add a quarantine path for malformed amounts before using this pattern in a pipeline.',checks:[{name:'Reads and converts CSV amounts',code:'from pathlib import Path\nPath("check.csv").write_text("order_id,category,amount_egp,status\\nT-1,Books,12.50,completed\\n", encoding="utf-8")\nassert load_orders("check.csv") == [{"order_id":"T-1","category":"Books","amount_egp":12.5,"status":"completed"}], "Read the supplied path and convert amount_egp to float."'},{name:'Handles a header-only file',code:'Path("empty.csv").write_text("order_id,category,amount_egp,status\\n", encoding="utf-8")\nassert load_orders("empty.csv") == [], "A header-only CSV has no data rows."'}]},
  {id:'api-rate',title:'09 · Validate an API response',level:'Reliable tools',minutes:15,topics:['http','orchestration','publish'],brief:'Implement extract_rate(payload). The documented fixture shape is {"data": {"EGP": {"value": 50.25}}}. Return its value as float if positive and finite; raise ValueError for a missing, malformed or invalid rate. This is a synthetic fixture, not a live quote.',contract:'No API key or network request is needed. Avoid accepting booleans as rates.',starter:`import math

def extract_rate(payload):
    return 0.0

print(extract_rate({"data": {"EGP": {"value": 50.25}}}))
`,solution:`import math

def extract_rate(payload):
    try:
        raw = payload["data"]["EGP"]["value"]
        if isinstance(raw, bool):
            raise ValueError("Boolean rate")
        rate = float(raw)
    except (KeyError, TypeError, ValueError) as exc:
        raise ValueError("Missing or invalid rate") from exc
    if not math.isfinite(rate) or rate <= 0:
        raise ValueError("Rate must be positive and finite")
    return rate

print(extract_rate({"data": {"EGP": {"value": 50.25}}}))
`,hints:['Read the nested keys inside try and convert the value with float.','Catch KeyError, TypeError and ValueError; then check finiteness and positivity.'],stretch:'Add a timestamp freshness policy. A valid number alone cannot prove a quote is current.',checks:[{name:'Extracts a valid fixture rate',code:'assert extract_rate({"data":{"EGP":{"value":50.25}}}) == 50.25, "Read data → EGP → value."'},{name:'Rejects malformed responses',code:'for payload in ({}, {"data":None}, {"data":{"EGP":{"value":"bad"}}}):\n    try:\n        extract_rate(payload)\n    except ValueError:\n        pass\n    else:\n        raise AssertionError("Malformed responses must raise ValueError")'},{name:'Rejects invalid numeric rates',code:'for value in (0, -1, "nan", "inf", True):\n    try:\n        extract_rate({"data":{"EGP":{"value":value}}})\n    except ValueError:\n        pass\n    else:\n        raise AssertionError(f"Invalid rate {value!r} must raise ValueError")'}]},
  {id:'pixelfed-quality',title:'10 · Find PixelFed orphan keys',level:'Data work',minutes:15,topics:['quality','joins','modules'],brief:'Write orphan_profiles(profiles, events). profiles contains dictionaries with profile_id; events contains dictionaries with the same foreign key. Return sorted unique event IDs that have no matching profile. Ignore null event IDs.',contract:'Input records are synthetic. Known profile IDs are unique; repeated orphan events should appear once in the result.',starter:`def orphan_profiles(profiles, events):
    return []

profiles = [{"profile_id": 1}, {"profile_id": 2}]
events = [{"profile_id": 2}, {"profile_id": 9}, {"profile_id": None}]
print(orphan_profiles(profiles, events))
`,solution:`def orphan_profiles(profiles, events):
    known = {row["profile_id"] for row in profiles}
    return sorted({row["profile_id"] for row in events
                   if row["profile_id"] is not None
                   and row["profile_id"] not in known})

print(orphan_profiles([{"profile_id": 1}], [{"profile_id": 9}]))
`,hints:['Build a set of dimension/profile keys first.','Use a set for unknown event keys, filter out None, and sort at the end.'],stretch:'Treat null foreign keys and orphan foreign keys as separate quality rules. How would you report the rejected row counts?',checks:[{name:'Finds unique orphan keys',code:'assert orphan_profiles([{"profile_id":1},{"profile_id":2}], [{"profile_id":2},{"profile_id":9},{"profile_id":9},{"profile_id":7}]) == [7,9], "Return sorted unique keys absent from profiles."'},{name:'Ignores null event keys',code:'assert orphan_profiles([], [{"profile_id":None},{"profile_id":3}]) == [3], "Null keys are handled separately from orphan keys."'},{name:'Handles no events',code:'assert orphan_profiles([{"profile_id":1}], []) == [], "No events means no orphan event keys."'}]},
  {id:'sqlite-totals',title:'11 · Query a SQLite summary',level:'Data work',minutes:20,topics:['sql','sql-transactions','pipeline'],brief:'Write category_totals(rows) using an in-memory sqlite3 database. Create an expenses table, insert category/amount pairs with bound parameters, then GROUP BY category and ORDER BY category.',contract:'Return a list of (category, total) tuples. Each call starts with an empty database. All amounts are already valid.',starter:`import sqlite3

def category_totals(rows):
    return []

print(category_totals([("Books", 180.5), ("Transport", 45), ("Books", 120.25)]))
`,solution:`import sqlite3

def category_totals(rows):
    connection = sqlite3.connect(":memory:")
    try:
        connection.execute("CREATE TABLE expenses (category TEXT, amount REAL)")
        connection.executemany("INSERT INTO expenses VALUES (?, ?)", rows)
        return connection.execute(
            "SELECT category, SUM(amount) FROM expenses GROUP BY category ORDER BY category"
        ).fetchall()
    finally:
        connection.close()

print(category_totals([("Books", 180.5), ("Books", 120.25)]))
`,hints:['sqlite3.connect(":memory:") creates a temporary database.','Use executemany with (?, ?) placeholders; fetchall returns the query rows.'],stretch:'Try a category containing an apostrophe. Bound parameters handle it without string-concatenating SQL.',checks:[{name:'Aggregates and sorts categories',code:'assert category_totals([("Transport",45),("Books",180.5),("Books",120.25)]) == [("Books",300.75),("Transport",45.0)], "Return grouped totals ordered by category."'},{name:'Handles quoted text and fresh calls',code:'assert category_totals([("Reader\'s books",5)]) == [("Reader\'s books",5.0)] and category_totals([]) == [], "Use bound parameters and a new database for each call."'}]},
  {id:'stream-batches',title:'12 · Stream records in batches',level:'Optional depth',minutes:20,topics:['generators','contexts-decorators','profiling','columnar-data'],brief:'Write batches(records, size) as a generator. Yield lists containing at most size records, including a final partial batch. Accept one-pass iterators and raise ValueError when size is less than 1.',contract:'Do not materialize all input records before yielding. The first batch should consume only size records.',starter:`def batches(records, size):
    # yield a batch when it reaches size; keep a final partial batch.
    yield []

print(list(batches(range(7), 3)))
`,solution:`def batches(records, size):
    if size < 1:
        raise ValueError("size must be positive")
    batch = []
    for record in records:
        batch.append(record)
        if len(batch) == size:
            yield batch
            batch = []
    if batch:
        yield batch

print(list(batches(range(7), 3)))
`,hints:['Keep one current list and yield it when len(batch) == size.','After yielding, replace batch with a new list. Yield a non-empty remainder after the loop.'],stretch:'Change size and compare peak memory with list(records). The consumer and aggregation state also affect memory use.',checks:[{name:'Includes the final partial batch',code:'assert list(batches(iter(range(7)), 3)) == [[0,1,2],[3,4,5],[6]], "Keep the final partial batch."'},{name:'Streams without exhausting the input',code:'seen=[]\ndef source():\n    for value in range(100):\n        seen.append(value)\n        yield value\niterator=iter(batches(source(), 3))\nassert next(iterator) == [0,1,2] and len(seen) == 3, "The first batch must consume only three records."'},{name:'Empty input and invalid sizes',code:'assert list(batches([], 2)) == [], "Empty input yields no batches."\ntry:\n    list(batches([1], 0))\nexcept ValueError:\n    pass\nelse:\n    raise AssertionError("size=0 must raise ValueError")'}]},
  {id:'pandas-summary',title:'13 · Summarize orders with pandas',level:'Optional package',minutes:20,topics:['pandas','numpy','ml','data-apps'],packages:['pandas'],brief:'Write summarize_orders(path). Read a CSV with pandas. Keep completed orders whose amount_egp converts to a positive number. Group by category and return a dictionary of totals rounded to two decimal places.',contract:'Invalid numeric text is treated as missing and excluded. The optional pandas download happens on your first run of this exercise.',starter:`import pandas as pd

def summarize_orders(path):
    return {}

print(summarize_orders("orders.csv"))
`,solution:`import pandas as pd

def summarize_orders(path):
    frame = pd.read_csv(path)
    frame["amount_egp"] = pd.to_numeric(frame["amount_egp"], errors="coerce")
    valid = frame[(frame["status"] == "completed") & (frame["amount_egp"] > 0)]
    return valid.groupby("category")["amount_egp"].sum().round(2).to_dict()

print(summarize_orders("orders.csv"))
`,hints:['Use pd.to_numeric(..., errors="coerce") before comparing amounts.','Filter on both status and positive amount; groupby("category")["amount_egp"].sum() performs the aggregation.'],stretch:'Compare the totals to a SQL query at the same grain. Add a reject report so filtering is visible to the person using the data.',checks:[{name:'Filters and groups a fixture',code:'from pathlib import Path\nPath("pandas-check.csv").write_text("order_id,category,amount_egp,status\\nT1,Books,10.25,completed\\nT2,Books,5.50,completed\\nT3,Books,90,pending\\nT4,Food,-2,completed\\nT5,Food,bad,completed\\nT6,Transport,20,completed\\n", encoding="utf-8")\nassert summarize_orders("pandas-check.csv") == {"Books":15.75,"Transport":20.0}, "Exclude pending, negative and malformed amounts before grouping."'},{name:'Handles no valid rows',code:'Path("pandas-empty.csv").write_text("order_id,category,amount_egp,status\\nT1,Food,2,pending\\n", encoding="utf-8")\nassert summarize_orders("pandas-empty.csv") == {}, "No valid rows should produce an empty dictionary."'}]},
  {id:'playground',title:'Free playground',level:'Explore',minutes:null,topics:[],brief:'Try your own standard-library Python, read the synthetic orders.csv, or use input() with the input lines below. This space has no scored checks.',contract:'Use print() to show results. Each run uses fresh variables and recreates orders.csv. Stop cancels a running script; the time limit is 12 seconds.',starter:`import csv

with open("orders.csv", encoding="utf-8", newline="") as handle:
    orders = list(csv.DictReader(handle))

print(f"Loaded {len(orders)} synthetic orders")
print("Your next idea goes here.")
`,hints:['The standard library includes csv, json, sqlite3, math, datetime, statistics and more.','Use the optional pandas challenge when you need DataFrames. Native packages must be supported by the browser runtime.'],stretch:'Use this space to build a small end-to-end quality report: read, validate, group, reconcile, explain.',checks:[]}
];
export const guidedChallenges = challenges.filter(c=>c.checks.length);
export function challengeForTopic(topic){return challenges.find(c=>c.topics.includes(topic)) || challenges.at(-1);}
