# CSV, Parquet & schema evolution

Choose a storage format using types, access pattern and downstream compatibility.

Extension beyond the Boot.dev video

## Connect to your work

Apply this to your Python data tools, PixelFed quality work, n8n integrations or BI delivery when the project needs it.

## Learn by doing

- Compare text CSV with typed columnar Parquet.
- Read selected columns and inspect schema metadata.
- Define compatible column changes, nullability and precision.

## Original practice

Export a copied synthetic fixture to Parquet, reload selected columns and compare values, nulls and timestamp interpretation.

## Exit check

The round-trip report identifies every type conversion and the consumer can reproduce the expected row count and totals.

## Understand the idea

CSV is convenient for inspection and interchange, but it does not carry a universal typed schema. Parquet stores typed columnar data and can support reading only the columns needed by an analysis. Performance depends on the actual file layout and workload.

Schema evolution is a compatibility decision. Adding an optional field differs from changing a business key or reducing decimal precision. Keep a written schema contract and test an older consumer against the changed dataset before promoting it.

## Resources

- [Apache Arrow · Parquet in Python](https://arrow.apache.org/docs/python/parquet/)
- [pandas · getting started tutorials](https://pandas.pydata.org/docs/getting_started/intro_tutorials/)

[Back to the roadmap](../roadmap.md) · [Source and attribution policy](../sources.md)
