# OOP, composition & data classes

Use objects to express a useful boundary, with functions for transformation logic.

Extension beyond the Boot.dev video

## Connect to your work

Apply this to your Python data tools, PixelFed quality work, n8n integrations or BI delivery when the project needs it.

## Learn by doing

- Model a validated record with a dataclass and explicit units.
- Pass an extractor into a pipeline instead of hard-coding its source.
- Compare composition with inheritance using one concrete change request.

## Original practice

Create an Order dataclass and a report service that accepts a fixture reader.

## Exit check

A second reader can be substituted without rewriting the aggregation; invalid input is rejected before creating the domain record.

## Small original example

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Order:
    order_id: str
    total_piastres: int

order = Order("O001", 12550)
print(order.total_piastres)
```

## Watch for

- frozen=True is not deep immutability for nested mutable objects.
- Type annotations alone do not enforce a runtime schema.

## Understand the idea

A class is useful when related state and behavior form a stable concept. A dataclass reduces repetitive initialization and representation code, but it does not validate every input automatically. Keep boundary parsing separate from the trusted object.

Composition means a service receives the collaborator it needs: for example, a reader or a clock. This makes fixture tests possible without making HTTP calls. Inheritance is appropriate for a genuine substitutable relationship, not simply for sharing two helper methods.

## Resources

- [Python · dataclasses](https://docs.python.org/3/library/dataclasses.html)
- [Python Object Oriented Programming - شرح للبرمجة كائنية التوجه في بايثون](https://www.youtube.com/watch?v=A9kSngn7254)

[Back to the roadmap](../roadmap.md) · [Source and attribution policy](../sources.md)
