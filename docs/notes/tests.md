# Tests that catch a broken contract

Use examples and failure cases to protect meaningful behavior.

Extension beyond the Boot.dev video

## Connect to your work

Reconciliation checks become executable tests.

## Learn by doing

- Run the stdlib unit tests before adding a dependency.
- Use pytest later for fixtures and parametrization.
- Test malformed input, duplicates, empty data and reruns.

## Original practice

Add a regression test for a defect you introduce in a working copy.

## Exit check

The test fails with the defect and passes after a targeted repair.

## Understand the idea

Choose tests that would catch a meaningful defect: a multiplied join, a lost zero, a conflicting key or a missing transaction rollback. A test that merely repeats the implementation’s calculation is weak evidence.

Keep network and clock behavior injectable. Use a temporary directory or database for I/O tests, then add a focused end-to-end fixture check that reconciles the exported result.

## Resources

- [pytest · getting started](https://docs.pytest.org/en/stable/getting-started.html)
- [Harvard CS50P · lectures & problem sets](https://cs50.harvard.edu/python/)
- [CS50P Week 5: lecture and problem set](https://cs50.harvard.edu/python/weeks/5/). Solve independently; this repo contains no CS50 problem-set answers.

[Back to the roadmap](../roadmap.md) · [Source and attribution policy](../sources.md)
