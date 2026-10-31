# Build 02 · PixelFed quality CLI

Add a Python validation layer to [PixelFed Analytics Engineering](https://github.com/Sohila-Khaled-Abbas/pixelfed-analytics-engineering). Begin by reading its current data contracts and inspecting an actual copied sample. Do not assume filenames, column names or entity grain from this brief.

## Deliverables

- A CLI taking an explicit copied landing directory and a separate output directory.
- A contract mapping actual entity keys, required fields and timestamp formats.
- Counts for rows, missing required values, duplicate business keys, invalid timestamps and orphan foreign keys.
- A JSON quality report, rejected-record file and readable log summary.
- Tests with small, hand-authored fixtures covering each rule.

## Grain and null policy

PixelFed is a social-platform analytics scenario, not an order/revenue dataset. Validate profiles, posts and their relationships at the grain declared by the existing repo. A missing profile identifier may justify quarantine; an optional profile attribute may remain unknown. A count of zero differs from an unavailable count. Never apply global `fillna(0)` or turn synthetic activity into financial transactions.

## Acceptance checks

An orphan-key fixture fails the matching rule. A duplicate dimension key is visible before a join. A timezone-naive timestamp has an explicit policy. Valid Arabic text survives UTF-8 reading/writing. The tool never edits the source directory. Report checks, assumptions and unresolved anomalies instead of making silent repairs.

## Where this connects

Reconcile the Python quality counts to Power Query at the same grain. Put the final tool in a separate feature branch of PixelFed when you are ready, and use its current PR rules. This roadmap adds the practice path and links; it does not alter PixelFed’s existing generator or datasets.
