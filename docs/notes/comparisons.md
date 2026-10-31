# Comparisons & branching

Branch on explicit conditions and keep unknown values distinct.

[Chapter 7 · 02:27:43](https://www.youtube.com/watch?v=4M87qBgpafk&t=8863s)

## Connect to your work

Translate a Power Query conditional column or SQL CASE into readable Python.

## Learn by doing

- Combine conditions with and, or and not.
- Use is None for an absent value.
- Write complete boundary rules before coding.

## Original practice

Task 07: label missing, negative, zero and positive amounts.

## Exit check

None → missing; -1 → invalid; 0 → zero; 1 → valid.

## Small original example

```python
def amount_status(value):
    if value is None:
        return "missing"
    if value < 0:
        return "invalid"
    return "zero" if value == 0 else "valid"
```

## Watch for

- = assigns; == compares.
- if not value merges zero with missingness.

## Resources

- [Boot.dev · Python for Beginners](https://www.youtube.com/watch?v=4M87qBgpafk)
- [كورس Python منحة ITI](https://www.youtube.com/playlist?list=PLNFDrRZdysFzSkNWqHZof7NxFHtGNC6bf)
- [Harvard CS50P · lectures & problem sets](https://cs50.harvard.edu/python/)
- [Python language tutorial](https://docs.python.org/3/tutorial/)
- [CS50P Week 1: lecture and problem set](https://cs50.harvard.edu/python/weeks/1/). Solve independently; this repo contains no CS50 problem-set answers.

[Back to the roadmap](../roadmap.md) · [Source and attribution policy](../sources.md)
