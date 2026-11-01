# Profiling, memory & measured optimization

Measure a bottleneck before changing a correct implementation.

Extension beyond the Boot.dev video

## Connect to your work

Apply this to your Python data tools, PixelFed quality work, n8n integrations or BI delivery when the project needs it.

## Learn by doing

- Separate benchmarking from profiling.
- Use cProfile and tracemalloc with a stated interpreter and workload.
- Verify outputs and memory behavior after optimization.

## Original practice

Profile the fixture pipeline and a scaled synthetic input; compare an eager reader with a bounded streaming design.

## Exit check

The report states input size, environment, elapsed time and peak allocation; outputs remain identical.

## Small original example

```python
import tracemalloc

tracemalloc.start()
values = list(range(1000))
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()
print({"current_bytes": current, "peak_bytes": peak})
```

## Understand the idea

A profiler attributes execution cost to functions; a benchmark compares elapsed behavior under controlled conditions. Profiling adds overhead, so a profiler report is not automatically a fair benchmark between Python and native library code.

Measure the whole pipeline, including parsing, joins, serialization and database work. A faster line of code is not valuable if the dominant cost lies elsewhere. Keep the input and expected outputs fixed while changing one design choice.

## Resources

- [Python 3.12 · profiling with cProfile](https://docs.python.org/3.12/library/profile.html)
- [Python · memory allocation tracing](https://docs.python.org/3/library/tracemalloc.html)

[Back to the roadmap](../roadmap.md) · [Source and attribution policy](../sources.md)
