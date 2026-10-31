# Dictionaries & grouping

Mappings connect unique keys to values and support lookup and grouping.

[Chapter 10 · 05:44:48](https://www.youtube.com/watch?v=4M87qBgpafk&t=20688s)

## Connect to your work

Implement a small GROUP BY yourself before using pandas groupby.

## Learn by doing

- Use items, keys, values and get deliberately.
- Aggregate amounts by category.
- Explain why repeated assignment to a key replaces its previous value.

## Original practice

Task 10: group transaction piastres by category.

## Exit check

Two Food rows with 300 and 200 produce {"Food": 500}.

## Small original example

```python
totals = {}
for row in [{"category": "Food", "amount": 300}, {"category": "Food", "amount": 200}]:
    key = row["category"]
    totals[key] = totals.get(key, 0) + row["amount"]
print(totals)
```

## Watch for

- dict.get(key) may return None if the key is absent.
- A dictionary is not a substitute for a validated database primary key.

## Resources

- [Boot.dev · Python for Beginners](https://www.youtube.com/watch?v=4M87qBgpafk)
- [كورس Python منحة ITI](https://www.youtube.com/playlist?list=PLNFDrRZdysFzSkNWqHZof7NxFHtGNC6bf)
- [Harvard CS50P · lectures & problem sets](https://cs50.harvard.edu/python/)
- [Python language tutorial](https://docs.python.org/3/tutorial/)
- [CS50P Week 2: lecture and problem set](https://cs50.harvard.edu/python/weeks/2/). Solve independently; this repo contains no CS50 problem-set answers.

[Back to the roadmap](../roadmap.md) · [Source and attribution policy](../sources.md)
