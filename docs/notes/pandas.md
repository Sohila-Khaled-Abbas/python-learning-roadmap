# DataFrames through a SQL lens

Use labeled tabular operations with explicit data types.

Extension beyond the Boot.dev video

## Connect to your work

Map WHERE → filtering, GROUP BY → groupby and SELECT → column projection.

## Learn by doing

- Inspect schema and null patterns before cleaning.
- Use vectorized transformations and groupby.
- Retain raw values when coercing dates or numbers.

## Original practice

Reproduce ledger category totals with pandas and compare them with your pure-Python result.

## Exit check

Both outputs agree; explain how missing groups and numeric conversion are handled.

## Understand the idea

Inspect a sample, shape, dtypes and missingness before choosing a transformation. Keep a raw copy and a small typed contract so coercion failures remain visible.

When comparing pandas with SQL or Power Query, use identical row grain, null rules and grouping keys. Reconciliation is more useful than a screenshot of a successful notebook cell.

## Resources

- [pandas · getting started tutorials](https://pandas.pydata.org/docs/getting_started/intro_tutorials/)
- [تحليل البيانات في بايثون (الدورة المصغرة) | Python for Data Analysis (Crash Course)](https://www.youtube.com/playlist?list=PLWd4nYaF_Vx7Db9uFWf_Df-UrP8ArF4L_)
- [Python for Data Analysis](https://www.youtube.com/playlist?list=PLiEts138s9P0w-WX4Rmml-_zhnBkXLWtc)
- [Data Exploration and Preparation](https://www.youtube.com/playlist?list=PLQ1FVkQVumFIEH7dYP_2L6vi_LyjlVsGm)

[Back to the roadmap](../roadmap.md) · [Source and attribution policy](../sources.md)
