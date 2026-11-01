# Regex, Unicode & Arabic text

Treat encoding, normalization and business identifiers as separate decisions.

Extension beyond the Boot.dev video

## Connect to your work

Apply this to your Python data tools, PixelFed quality work, n8n integrations or BI delivery when the project needs it.

## Learn by doing

- Read UTF-8 explicitly and retain original text.
- Use raw-string patterns and fullmatch for full-field validation.
- Explain Unicode digits versus an ASCII-only identifier contract.

## Original practice

Validate ASCII order IDs, preserve Arabic category labels, and compare composed/decomposed forms without overwriting the raw value.

## Exit check

Arabic text round-trips; invalid identifiers fail; normalization is recorded and never silently merges distinct business keys.

## Small original example

```python
import re
import unicodedata

raw = "عناية بالبشرة"
normalized = unicodedata.normalize("NFC", raw)
valid_id = re.fullmatch(r"O[0-9]{3}", "O001") is not None
print(normalized, valid_id)
```

## Understand the idea

Encoding converts bytes to text. Normalization changes the representation of some equivalent Unicode sequences. Neither operation decides whether two customer names represent the same person, and stripping Arabic characters is not a valid cleaning default.

Use a regular expression for a bounded structural rule, such as an order identifier. A pattern proving that text resembles an email or phone number cannot prove the person owns it. Keep that distinction clear when designing intake or data-quality rules.

## Resources

- [Python · regular expressions](https://docs.python.org/3/library/re.html)
- [Python · Unicode normalization](https://docs.python.org/3/library/unicodedata.html)

[Back to the roadmap](../roadmap.md) · [Source and attribution policy](../sources.md)
