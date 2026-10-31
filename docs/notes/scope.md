# Scope & side effects

Local names help a function behave predictably across calls.

[Chapter 4 · 01:16:12](https://www.youtube.com/watch?v=4M87qBgpafk&t=4572s)

## Connect to your work

Avoid notebook state that makes a cell work only after an undocumented execution order.

## Learn by doing

- Trace local versus module names.
- Pass configuration as a parameter.
- Return a new value rather than modifying a shared dict accidentally.

## Original practice

Task 04: add a category to a copied record without changing the original.

## Exit check

The original dict stays identical after classify_copy(record, "Food").

## Small original example

```python
def classify_copy(record, category):
    result = dict(record)
    result["category"] = category
    return result
```

## Watch for

- A shallow copy does not clone nested mutable values.
- Mutable default arguments persist between calls.

## Resources

- [Boot.dev · Python for Beginners](https://www.youtube.com/watch?v=4M87qBgpafk)
- [كورس Python منحة ITI](https://www.youtube.com/playlist?list=PLNFDrRZdysFzSkNWqHZof7NxFHtGNC6bf)
- [Harvard CS50P · lectures & problem sets](https://cs50.harvard.edu/python/)
- [Python language tutorial](https://docs.python.org/3/tutorial/)

[Back to the roadmap](../roadmap.md) · [Source and attribution policy](../sources.md)
