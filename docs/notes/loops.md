# Loops & accumulation

Iteration applies a rule repeatedly while preserving an invariant.

[Chapter 8 · 03:24:46](https://www.youtube.com/watch?v=4M87qBgpafk&t=12286s)

## Connect to your work

A row loop is useful for learning. Later compare it with SQL and pandas operations.

## Learn by doing

- Use for, range, enumerate, break and continue.
- Accumulate a total with a clear initial value.
- Trace a loop on an empty input and a single record.

## Original practice

Task 08: sum only nonmissing, nonnegative integer amounts.

## Exit check

valid_total([None, 0, -2, 10]) is 10.

## Small original example

```python
total = 0
for amount in [None, 0, -2, 10]:
    if amount is not None and amount >= 0:
        total += amount
print(total)
```

## Watch for

- Changing a list while iterating over it can skip entries.
- A while loop needs a path toward termination.

## Understand the idea

Iteration applies a rule repeatedly while preserving an invariant. A row loop is useful for learning. Later compare it with SQL and pandas operations.

Work through the practice with a tiny fixture, predict the result before running it, and record one boundary case. Use the exit check as evidence before moving on.

## Resources

- [Boot.dev · Python for Beginners](https://www.youtube.com/watch?v=4M87qBgpafk)
- [كورس Python منحة ITI](https://www.youtube.com/playlist?list=PLNFDrRZdysFzSkNWqHZof7NxFHtGNC6bf)
- [Harvard CS50P · lectures & problem sets](https://cs50.harvard.edu/python/)
- [Python language tutorial](https://docs.python.org/3/tutorial/)
- [Python - The Basics - Part 1 | جحر السوعبان](https://www.youtube.com/watch?v=XKQaCF_Om8o)
- [CS50P Week 2: lecture and problem set](https://cs50.harvard.edu/python/weeks/2/). Solve independently; this repo contains no CS50 problem-set answers.

[Back to the roadmap](../roadmap.md) · [Source and attribution policy](../sources.md)
