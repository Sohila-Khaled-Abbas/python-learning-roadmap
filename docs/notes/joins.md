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

## Understand the idea

Declare the expected relationship before merging: one-to-one, many-to-one or many-to-many. Validate reference-key uniqueness before a join; counting rows only after multiplication can hide the reason a KPI changed.

Check unmatched keys in both directions and decide what an unknown dimension means. An inner join may discard legitimate facts, while filling every missing value with zero invents measurements.

## Resources

- [pandas · getting started tutorials](https://pandas.pydata.org/docs/getting_started/intro_tutorials/)
- [كورس Python منحة ITI](https://www.youtube.com/playlist?list=PLNFDrRZdysFzSkNWqHZof7NxFHtGNC6bf)
- [تحليل البيانات في بايثون (الدورة المصغرة) | Python for Data Analysis (Crash Course)](https://www.youtube.com/playlist?list=PLWd4nYaF_Vx7Db9uFWf_Df-UrP8ArF4L_)
- [Python for Data Analysis](https://www.youtube.com/playlist?list=PLiEts138s9P0w-WX4Rmml-_zhnBkXLWtc)
- [Data Exploration and Preparation](https://www.youtube.com/playlist?list=PLQ1FVkQVumFIEH7dYP_2L6vi_LyjlVsGm)

[Back to the roadmap](../roadmap.md) · [Source and attribution policy](../sources.md)
