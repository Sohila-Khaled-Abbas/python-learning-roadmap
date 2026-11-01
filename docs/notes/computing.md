# Operators & computation

Operators encode arithmetic, precedence and discrete decisions.

[Chapter 6 · 01:54:58](https://www.youtube.com/watch?v=4M87qBgpafk&t=6898s)

## Connect to your work

ETL batching and reconciliation depend on clear units and correct integer arithmetic.

## Learn by doing

- Explain /, //, %, ** and parentheses.
- Calculate batches without losing a partial batch.
- Define the behavior of zero and invalid batch sizes.

## Original practice

Task 06: compute the number of API pages from row count and page size.

## Exit check

page_count(101, 50) is 3; zero rows is 0; size zero is rejected.

## Small original example

```python
def page_count(rows, size):
    if rows < 0 or size <= 0:
        raise ValueError("invalid pagination inputs")
    return (rows + size - 1) // size
```

## Watch for

- Integer division discards the remainder.
- Do not confuse percent change with a percent of the new value.

## Understand the idea

Operators encode arithmetic, precedence and discrete decisions. ETL batching and reconciliation depend on clear units and correct integer arithmetic.

Work through the practice with a tiny fixture, predict the result before running it, and record one boundary case. Use the exit check as evidence before moving on.

## Resources

- [Boot.dev · Python for Beginners](https://www.youtube.com/watch?v=4M87qBgpafk)
- [كورس Python منحة ITI](https://www.youtube.com/playlist?list=PLNFDrRZdysFzSkNWqHZof7NxFHtGNC6bf)
- [Harvard CS50P · lectures & problem sets](https://cs50.harvard.edu/python/)
- [Python language tutorial](https://docs.python.org/3/tutorial/)

[Back to the roadmap](../roadmap.md) · [Source and attribution policy](../sources.md)
