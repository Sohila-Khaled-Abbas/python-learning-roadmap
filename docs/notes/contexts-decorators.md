# Context managers & decorators

Make cleanup and cross-cutting behavior explicit without obscuring a function contract.

Extension beyond the Boot.dev video

## Connect to your work

Apply this to your Python data tools, PixelFed quality work, n8n integrations or BI delivery when the project needs it.

## Learn by doing

- Use with and try/finally for deterministic cleanup.
- Write one context manager that yields exactly once.
- Preserve wrapped function metadata with functools.wraps.

## Original practice

Create a timer context and a logging decorator for a fixture transformation. Test cleanup when the transformation raises.

## Exit check

The original error remains visible, cleanup always runs, and a decorated function keeps its name and docstring.

## Small original example

```python
from contextlib import contextmanager
from time import perf_counter

@contextmanager
def elapsed():
    start = perf_counter()
    try:
        yield
    finally:
        print(f"seconds={perf_counter()-start:.6f}")
```

## Understand the idea

The with statement gives a resource an explicit lifetime. A generator-based context manager acquires the resource before yield and releases it in finally. Cleanup must not silently turn a failed operation into a successful result.

A decorator replaces a callable with another callable. Keep validation and business rules visible; a short timer or logging wrapper is easier to review than a stack of decorators that changes retry, transaction and exception behavior at once.

## Resources

- [Python · contextlib](https://docs.python.org/3/library/contextlib.html)
- [Python language tutorial](https://docs.python.org/3/tutorial/)

[Back to the roadmap](../roadmap.md) · [Source and attribution policy](../sources.md)
