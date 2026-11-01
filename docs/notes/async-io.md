# Async I/O & bounded concurrency

Overlap waiting work while preserving deadlines and explicit failure policy.

Extension beyond the Boot.dev video

## Connect to your work

Apply this to your Python data tools, PixelFed quality work, n8n integrations or BI delivery when the project needs it.

## Learn by doing

- Explain a coroutine, await, task and cancellation.
- Limit concurrent requests and keep per-request timeouts.
- Separate I/O waiting from CPU-bound transformation work.

## Original practice

Use fake delayed fetches to compare sequential and bounded concurrent retrieval. Inject one timeout and check cancellation cleanup.

## Exit check

Concurrency never exceeds the limit; one timeout follows a documented policy; the test performs no live API calls.

## Small original example

```python
import asyncio

async def fake_fetch(value):
    await asyncio.sleep(0.01)
    return value

async def main():
    limit = asyncio.Semaphore(2)
    async def bounded(value):
        async with limit:
            return await fake_fetch(value)
    print(await asyncio.gather(*(bounded(i) for i in range(4))))

asyncio.run(main())
```

## Understand the idea

Asyncio is most useful when a program spends time waiting for I/O. It does not make a CPU-heavy transformation faster merely because a function is declared async. Keep blocking work out of the event loop or choose a different execution model.

Bound concurrency to protect the provider and your own machine. A semaphore limits work in flight; a deadline limits how long a request may wait. Both differ from retries, which must also respect the endpoint’s replay safety and quota policy.

## Resources

- [Python · asyncio](https://docs.python.org/3/library/asyncio.html)
- [pytest · mock modules and environments](https://docs.pytest.org/en/stable/how-to/monkeypatch.html)

[Back to the roadmap](../roadmap.md) · [Source and attribution policy](../sources.md)
