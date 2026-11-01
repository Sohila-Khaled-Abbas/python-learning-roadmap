# Variables, types & missing values

A name refers to an object; type determines the operations that object supports.

[Chapter 2 · 15:02](https://www.youtube.com/watch?v=4M87qBgpafk&t=902s)

## Connect to your work

Compare Python None with SQL NULL, and distinguish missingness from zero and an empty string.

## Learn by doing

- Use str, int, float, bool and None deliberately.
- Convert text at input boundaries and inspect types.
- Use integer minor units for these EGP exercises: 100 piastres = 1 EGP.

## Original practice

Task 02: convert a decimal EGP string to integer piastres; reject fractions below one piastre.

## Exit check

"12.50" becomes 1250; "0.001" and "NaN" raise ValueError.

## Small original example

```python
from decimal import Decimal
amount = Decimal("12.50")
piastres = int(amount * 100)
print(piastres)  # 1250; validate precision before int in real input code
```

## Watch for

- bool("False") is True because the string is nonempty.
- Binary floats are unsuitable for exact currency equality.

## Understand the idea

A name refers to an object; type determines the operations that object supports. Compare Python None with SQL NULL, and distinguish missingness from zero and an empty string.

Work through the practice with a tiny fixture, predict the result before running it, and record one boundary case. Use the exit check as evidence before moving on.

## Resources

- [Boot.dev · Python for Beginners](https://www.youtube.com/watch?v=4M87qBgpafk)
- [كورس Python منحة ITI](https://www.youtube.com/playlist?list=PLNFDrRZdysFzSkNWqHZof7NxFHtGNC6bf)
- [Harvard CS50P · lectures & problem sets](https://cs50.harvard.edu/python/)
- [Python language tutorial](https://docs.python.org/3/tutorial/)
- [Python - The Basics - Part 1 | جحر السوعبان](https://www.youtube.com/watch?v=XKQaCF_Om8o)
- [Python Full Course for Beginners (13 Hours) – From Zero to Hero](https://www.youtube.com/watch?v=Rq5gJVxz55Q)
- [03 تعليم الآلة , القسم الثالث : بايثون Machine learning , Python](https://www.youtube.com/playlist?list=PL6-3IRz2XF5UM-FWfQeF1_YhMMa12Eg3s)
- [CS50P Week 0: lecture and problem set](https://cs50.harvard.edu/python/weeks/0/). Solve independently; this repo contains no CS50 problem-set answers.

[Back to the roadmap](../roadmap.md) · [Source and attribution policy](../sources.md)
