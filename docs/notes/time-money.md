# Time zones, money & measurement units

Make temporal and numeric meaning explicit before aggregation.

Extension beyond the Boot.dev video

## Connect to your work

Apply this to your Python data tools, PixelFed quality work, n8n integrations or BI delivery when the project needs it.

## Learn by doing

- Store event and ingestion timestamps separately as aware UTC instants.
- Convert to Africa/Cairo for display or a documented business date.
- Use validated Decimal values or integer minor units with a rounding policy.

## Original practice

Design a quote fixture contract with provider_as_of, fetched_at, rate precision, base and quote currency. Test an invalid date and stale quote.

## Exit check

A stale observation is not described as live; time conversion preserves the instant; amounts reconcile at the documented precision.

## Small original example

```python
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

instant = datetime(2026, 11, 1, 12, tzinfo=timezone.utc)
local = instant.astimezone(ZoneInfo("Africa/Cairo"))
print(instant.isoformat(), local.isoformat())
```

## Understand the idea

A timestamp without a time zone is ambiguous until a source contract supplies its meaning. The event time and the time your process fetched the event answer different questions. Keep both when freshness affects a downstream decision.

A currency amount and an exchange rate need different precision policies. EGP minor units work well for many expense amounts, but a forex rate may require more than two decimal places. Do not truncate a rate using the ledger’s amount parser. On Windows, install the first-party tzdata package in the project environment if IANA zone data is unavailable.

## Resources

- [Python · IANA time zones](https://docs.python.org/3/library/zoneinfo.html)
- [Python language tutorial](https://docs.python.org/3/tutorial/)

[Back to the roadmap](../roadmap.md) · [Source and attribution policy](../sources.md)
