# Sets & reconciliation

Sets answer membership and difference questions without keeping duplicates.

[Chapter 11 · 06:19:51](https://www.youtube.com/watch?v=4M87qBgpafk&t=22791s)

## Connect to your work

Use set differences to find missing foreign keys before a warehouse load.

## Learn by doing

- Use intersection, union and difference.
- Compare observed keys with a reference set.
- Sort results for deterministic reports.

## Original practice

Task 11: report profile IDs absent from the reference set.

## Exit check

missing_ids([1, 2, 2, 4], [1, 4]) is [2].

## Small original example

```python
observed = {1, 2, 2, 4}
reference = {1, 4}
print(sorted(observed - reference))
```

## Watch for

- set iteration order is not a reporting contract.
- {} creates an empty dict; set() creates an empty set.

## Resources

- [Boot.dev · Python for Beginners](https://www.youtube.com/watch?v=4M87qBgpafk)
- [كورس Python منحة ITI](https://www.youtube.com/playlist?list=PLNFDrRZdysFzSkNWqHZof7NxFHtGNC6bf)
- [Harvard CS50P · lectures & problem sets](https://cs50.harvard.edu/python/)
- [Python language tutorial](https://docs.python.org/3/tutorial/)
- [CS50P Week 2: lecture and problem set](https://cs50.harvard.edu/python/weeks/2/). Solve independently; this repo contains no CS50 problem-set answers.

[Back to the roadmap](../roadmap.md) · [Source and attribution policy](../sources.md)
