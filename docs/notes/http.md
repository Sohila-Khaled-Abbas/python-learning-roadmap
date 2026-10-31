# APIs, JSON & failure policies

Treat external data as an input that can be late, incomplete or unavailable.

Extension beyond the Boot.dev video

## Connect to your work

Use your networking and n8n experience to reason about timeouts and rate limits.

## Learn by doing

- Set an explicit timeout and validate response status and schema.
- Use bounded retries only when appropriate; respect Retry-After.
- Persist provider timestamp, fetch timestamp and provenance.

## Original practice

Design an offline EUR/EGP quote fixture with provider_as_of and fetched_at; label it fixture data.

## Exit check

A stale or malformed quote is visible; a cached value is never labeled live.

## Resources

- [Python language tutorial](https://docs.python.org/3/tutorial/)

[Back to the roadmap](../roadmap.md) · [Source and attribution policy](../sources.md)
