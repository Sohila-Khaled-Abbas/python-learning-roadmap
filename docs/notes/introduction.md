# Run a program

A program is an ordered set of instructions with observable output.

[Chapter 1 · 03:41](https://www.youtube.com/watch?v=4M87qBgpafk&t=221s)

## Connect to your work

A query returns rows; a script can coordinate several steps around those rows.

## Learn by doing

- Run a .py file and use print for visible output.
- Distinguish source code from the interpreter that executes it.
- Predict the output before running the program.

## Original practice

Task 01: format a short pipeline completion message.

## Exit check

pipeline_message("landing", 4) returns "landing: 4 rows".

## Small original example

```python
def pipeline_message(stage, rows):
    return f"{stage}: {rows} rows"

print(pipeline_message("landing", 4))
```

## Watch for

- Returning a value and printing a value have different effects.

## Resources

- [Boot.dev · Python for Beginners](https://www.youtube.com/watch?v=4M87qBgpafk)
- [كورس Python منحة ITI](https://www.youtube.com/playlist?list=PLNFDrRZdysFzSkNWqHZof7NxFHtGNC6bf)
- [Harvard CS50P · lectures & problem sets](https://cs50.harvard.edu/python/)
- [Python language tutorial](https://docs.python.org/3/tutorial/)
- [CS50P Week 0: lecture and problem set](https://cs50.harvard.edu/python/weeks/0/). Solve independently; this repo contains no CS50 problem-set answers.

[Back to the roadmap](../roadmap.md) · [Source and attribution policy](../sources.md)
