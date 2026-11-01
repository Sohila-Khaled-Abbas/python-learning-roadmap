# Iterators, generators & streaming

Process a sequence without requiring every record to be resident in memory.

Extension beyond the Boot.dev video

## Connect to your work

Apply this to your Python data tools, PixelFed quality work, n8n integrations or BI delivery when the project needs it.

## Learn by doing

- Explain iterable versus iterator and one-pass consumption.
- Yield parsed rows while the file context is open.
- Use bounded batches and measure peak memory.

## Original practice

Replace a fixture reader that returns list(reader) with a generator and compare peak memory on a larger synthetic file.

## Exit check

Both versions produce identical aggregates; the streaming version keeps peak memory bounded by the chosen batch and aggregation state.

## Small original example

```python
import csv

def rows(path):
    with open(path, encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            yield row
```

## Watch for

- An iterator may be exhausted after the first pass.
- list(generator) materializes the records again.

## Understand the idea

A generator defers execution until the consumer asks for a value. That can reduce the input retained in memory, but an unbounded grouping dictionary can still grow with the number of distinct keys. Streaming describes the whole design, not merely the presence of yield.

Keep file ownership clear. Opening a file outside a generator and returning an iterator after closing that file creates a reader that cannot be used. Test early termination as well as complete consumption.

## Resources

- [Python · iterators and generators](https://docs.python.org/3/howto/functional.html)

[Back to the roadmap](../roadmap.md) · [Source and attribution policy](../sources.md)
