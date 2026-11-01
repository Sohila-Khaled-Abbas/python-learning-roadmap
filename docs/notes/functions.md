# Functions & explicit contracts

A function turns named inputs into a useful result with a clear contract.

[Chapter 3 · 43:06](https://www.youtube.com/watch?v=4M87qBgpafk&t=2586s)

## Connect to your work

Think of a reusable Power Query function, but make data dependencies explicit.

## Learn by doing

- Separate input/output from transformation logic.
- Use return values, parameters and small docstrings.
- Specify valid inputs and the result unit.

## Original practice

Task 03: calculate net revenue from gross and discount piastres.

## Exit check

net_revenue(10000, 1500) is 8500; a discount larger than gross is rejected.

## Small original example

```python
def net_revenue(gross, discount):
    if not 0 <= discount <= gross:
        raise ValueError("discount outside gross amount")
    return gross - discount
```

## Watch for

- A missing return produces None.
- A function that mutates input may surprise its callers.

## Understand the idea

A function turns named inputs into a useful result with a clear contract. Think of a reusable Power Query function, but make data dependencies explicit.

Work through the practice with a tiny fixture, predict the result before running it, and record one boundary case. Use the exit check as evidence before moving on.

## Resources

- [Boot.dev · Python for Beginners](https://www.youtube.com/watch?v=4M87qBgpafk)
- [كورس Python منحة ITI](https://www.youtube.com/playlist?list=PLNFDrRZdysFzSkNWqHZof7NxFHtGNC6bf)
- [Harvard CS50P · lectures & problem sets](https://cs50.harvard.edu/python/)
- [Python language tutorial](https://docs.python.org/3/tutorial/)
- [Python - The Basics - Part 1 | جحر السوعبان](https://www.youtube.com/watch?v=XKQaCF_Om8o)
- [Python Full Course for Beginners (13 Hours) – From Zero to Hero](https://www.youtube.com/watch?v=Rq5gJVxz55Q)
- [03 تعليم الآلة , القسم الثالث : بايثون Machine learning , Python](https://www.youtube.com/playlist?list=PL6-3IRz2XF5UM-FWfQeF1_YhMMa12Eg3s)
- [CS50P Week 0: lecture and problem set](https://cs50.harvard.edu/python/weeks/0/). Solve independently; this repo contains no CS50 problem-set answers.

[Back to the roadmap](../roadmap.md) · [Source and attribution policy](../sources.md)
