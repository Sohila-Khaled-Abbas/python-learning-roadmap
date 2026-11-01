# Testing & debugging

A failing example is evidence you can narrow to a specific cause.

[Chapter 5 · 01:28:55](https://www.youtube.com/watch?v=4M87qBgpafk&t=5335s)

## Connect to your work

Apply your troubleshooting habit: reproduce, inspect, change one thing, verify.

## Learn by doing

- Read a traceback from the final exception back to your call.
- Write a normal, empty and boundary example.
- Keep assertions in tests; use explicit validation in application code.

## Original practice

Task 05: fix mean_or_none so empty data is meaningful and zero is retained.

## Exit check

mean_or_none([]) is None; mean_or_none([0, 10]) is 5.

## Small original example

```python
def mean_or_none(values):
    return sum(values) / len(values) if values else None

assert mean_or_none([0, 10]) == 5
```

## Watch for

- Do not use bare except to hide a failure.
- assert can be disabled; it is not a production input-validation boundary.

## Understand the idea

A failing example is evidence you can narrow to a specific cause. Apply your troubleshooting habit: reproduce, inspect, change one thing, verify.

Work through the practice with a tiny fixture, predict the result before running it, and record one boundary case. Use the exit check as evidence before moving on.

## Resources

- [Boot.dev · Python for Beginners](https://www.youtube.com/watch?v=4M87qBgpafk)
- [كورس Python منحة ITI](https://www.youtube.com/playlist?list=PLNFDrRZdysFzSkNWqHZof7NxFHtGNC6bf)
- [Harvard CS50P · lectures & problem sets](https://cs50.harvard.edu/python/)
- [Python language tutorial](https://docs.python.org/3/tutorial/)
- [CS50P Week 5: lecture and problem set](https://cs50.harvard.edu/python/weeks/5/). Solve independently; this repo contains no CS50 problem-set answers.

[Back to the roadmap](../roadmap.md) · [Source and attribution policy](../sources.md)
