# Joins, nulls & grain

A join is a cardinality decision, not just a merge call.

Extension beyond the Boot.dev video

## Connect to your work

Use your star/galaxy modeling knowledge to prevent multiplied facts.

## Learn by doing

- Declare one row per entity before joining.
- Use pandas merge(validate=...) and inspect unmatched keys.
- Separate None, NaN, empty text and business-unknown values.

## Original practice

Join a fact fixture to a duplicate dimension and make the validation fail.

## Exit check

No total changes silently; unmatched keys and duplicated keys have separate reports.

## Resources

- [pandas · getting started tutorials](https://pandas.pydata.org/docs/getting_started/intro_tutorials/)
- [كورس Python منحة ITI](https://www.youtube.com/playlist?list=PLNFDrRZdysFzSkNWqHZof7NxFHtGNC6bf)

[Back to the roadmap](../roadmap.md) · [Source and attribution policy](../sources.md)
