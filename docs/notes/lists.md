# Lists, slices & comprehensions

Sequences preserve order, including repeated values.

[Chapter 9 · 03:44:14](https://www.youtube.com/watch?v=4M87qBgpafk&t=13454s)

## Connect to your work

A list can hold landing records, but it has no enforced table schema.

## Learn by doing

- Use indexes, slices, append and list comprehensions.
- Understand aliasing, copying and in-place methods.
- Preserve input order when filtering and deduplicating.

## Original practice

Task 09: return the last n records without changing the input list.

## Exit check

latest([1, 2, 3], 2) is [2, 3]; n=0 returns []; negative n is invalid.

## Small original example

```python
records = ["a", "b", "c"]
last_two = records[-2:]
print(last_two)
print(records)  # still intact
```

## Watch for

- sort() changes the list and returns None.
- items[-0:] returns the full list, not an empty list.

## Understand the idea

Sequences preserve order, including repeated values. A list can hold landing records, but it has no enforced table schema.

Work through the practice with a tiny fixture, predict the result before running it, and record one boundary case. Use the exit check as evidence before moving on.

## Resources

- [Boot.dev · Python for Beginners](https://www.youtube.com/watch?v=4M87qBgpafk)
- [كورس Python منحة ITI](https://www.youtube.com/playlist?list=PLNFDrRZdysFzSkNWqHZof7NxFHtGNC6bf)
- [Harvard CS50P · lectures & problem sets](https://cs50.harvard.edu/python/)
- [Python language tutorial](https://docs.python.org/3/tutorial/)
- [Python Full Course for Beginners (13 Hours) – From Zero to Hero](https://www.youtube.com/watch?v=Rq5gJVxz55Q)
- [CS50P Week 2: lecture and problem set](https://cs50.harvard.edu/python/weeks/2/). Solve independently; this repo contains no CS50 problem-set answers.

[Back to the roadmap](../roadmap.md) · [Source and attribution policy](../sources.md)
