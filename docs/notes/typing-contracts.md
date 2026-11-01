# Type hints, protocols & validation

Use static contracts to improve maintainability while validating external data at runtime.

Extension beyond the Boot.dev video

## Connect to your work

Apply this to your Python data tools, PixelFed quality work, n8n integrations or BI delivery when the project needs it.

## Learn by doing

- Annotate collection element types and optional results.
- Use Protocol to describe a small reader interface.
- Distinguish a type checker from runtime parsing and validation.

## Original practice

Type a reader returning Iterable[Order], then inject a fake reader in tests. Add a malformed JSON input test.

## Exit check

The fake satisfies the interface and the malformed payload is rejected independently of its annotations.

## Small original example

```python
from typing import Protocol, Iterable

class Reader(Protocol):
    def read(self) -> Iterable[dict[str, str]]: ...
```

## Watch for

- Use syntax supported by the selected interpreter; this repo baseline remains Python 3.11+.

## Understand the idea

Type hints describe expected values to editors and static tools. Python does not automatically reject a string passed into an int-annotated parameter. Validate untrusted CSV, JSON and environment values when they enter the application.

A protocol describes the operations a collaborator must support without requiring a shared implementation. Keep the interface narrow: one read method is easier to fake and reason about than a provider object exposing dozens of unrelated calls.

## Resources

- [Python · type hints and protocols](https://docs.python.org/3/library/typing.html)
- [pytest · mock modules and environments](https://docs.pytest.org/en/stable/how-to/monkeypatch.html)

[Back to the roadmap](../roadmap.md) · [Source and attribution policy](../sources.md)
