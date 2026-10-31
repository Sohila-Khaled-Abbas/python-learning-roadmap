# Sources, course coverage and attribution

Prepared 31 October 2026. This repository combines a verified chapter index with **original explanations, code, exercises, project briefs and learning sequencing**. The three main resources have complementary roles; studying all of every course is not required.

## Core video

[Python for Beginners: The Complete Course](https://www.youtube.com/watch?v=4M87qBgpafk), published by **Boot dev**, taught by **TrashPuppy**; published June 12, 2024; duration **7:08:28**. The title, channel, duration and chapter starts below were read from the selected YouTube page and expanded description on 31 October 2026.

Transcript export returned unavailable. The course mapping is therefore limited to verified chapter metadata. The examples and detailed learning outcomes here are independently written companion material informed by the chapter topics and official documentation, not claims about everything said in the video. No transcript is included.

| Chapter | Published start | Companion note |
| --- | --- | --- |
| 1 · Introduction | [03:41](https://www.youtube.com/watch?v=4M87qBgpafk&t=221s) | [Run a program](notes/introduction.md) |
| 2 · Variables | [15:02](https://www.youtube.com/watch?v=4M87qBgpafk&t=902s) | [Types and missing values](notes/variables.md) |
| 3 · Functions | [43:06](https://www.youtube.com/watch?v=4M87qBgpafk&t=2586s) | [Explicit contracts](notes/functions.md) |
| 4 · Scope | [01:16:12](https://www.youtube.com/watch?v=4M87qBgpafk&t=4572s) | [Scope and side effects](notes/scope.md) |
| 5 · Testing and Debugging | [01:28:55](https://www.youtube.com/watch?v=4M87qBgpafk&t=5335s) | [Debugging with evidence](notes/debugging.md) |
| 6 · Computing | [01:54:58](https://www.youtube.com/watch?v=4M87qBgpafk&t=6898s) | [Operators](notes/computing.md) |
| 7 · Comparisons | [02:27:43](https://www.youtube.com/watch?v=4M87qBgpafk&t=8863s) | [Branching](notes/comparisons.md) |
| 8 · Loops | [03:24:46](https://www.youtube.com/watch?v=4M87qBgpafk&t=12286s) | [Iteration](notes/loops.md) |
| 9 · Lists | [03:44:14](https://www.youtube.com/watch?v=4M87qBgpafk&t=13454s) | [Sequences](notes/lists.md) |
| 10 · Dictionaries | [05:44:48](https://www.youtube.com/watch?v=4M87qBgpafk&t=20688s) | [Grouping](notes/dictionaries.md) |
| 11 · Sets | [06:19:51](https://www.youtube.com/watch?v=4M87qBgpafk&t=22791s) | [Reconciliation](notes/sets.md) |
| 12 · Errors | [06:37:27](https://www.youtube.com/watch?v=4M87qBgpafk&t=23847s) | [Visible failures](notes/errors.md) |

The introduction at 00:00 and recommendations at 00:35 are available from the original video. Extensions after chapter 12—modules, files, pandas, APIs, SQL and project delivery—are additional curriculum, not attributed to the video.

## Your ITI and Harvard resources

- [كورس Python منحة ITI](https://www.youtube.com/playlist?list=PLNFDrRZdysFzSkNWqHZof7NxFHtGNC6bf): supplied directly by Sohila and already recorded as `V007` in the DE roadmap video catalog. Used as an Arabic companion at playlist level. This repository does not claim a verified lesson-by-lesson index or access to every playlist item.
- [Harvard CS50P public course](https://cs50.harvard.edu/python/): official lecture and problem-set entry point, checked on 31 October 2026. Topic mappings: Week 0 functions/variables, 1 conditionals, 2 loops, 3 exceptions, 5 unit tests, 6 file I/O, 8 OOP. The public course also covers libraries, regular expressions and other topics; use those when a project needs them.
- [HarvardX CS50P on edX](https://learning.edx.org/course/course-v1:HarvardX+CS50P+Python/home): the user-provided course identity is retained for continuing in the enrolled experience. Current enrollment status, private progress and certificate access have not been inferred.

No CS50 problem-set solutions are published. All twelve foundation tasks here are original data-work exercises, distinct from Boot.dev and CS50 assignments.

## Official enrichment

The official Python tutorial, PyPA installation guide, pytest getting-started guide, pandas introductory tutorials, NumPy quickstart and scikit-learn getting-started guide were checked on 31 October 2026. Their canonical links and uses are in [data/roadmap.json](../data/roadmap.json). This repo’s runnable baseline uses Python standard-library features; it does not assume a particular latest third-party package release.

## Existing learning collection

[data/inherited-resources.csv](../data/inherited-resources.csv) preserves fifteen Python-related entries from `data/community-learning-resources.csv` in Sohila’s [DE roadmap](https://github.com/Sohila-Khaled-Abbas/data-engineering-learning-roadmap). It includes IBM/Cognitive Class, Arabic foundations, DataCamp pandas and ingestion courses, and PySpark follow-ups. Titles, URLs, source attribution, intended use and access caveats are preserved. These inherited URLs were not all rechecked, and paid/account access is not assumed. They are alternatives or later references, not a new mandatory course queue.

## Design and licensing

[roadmap.sh/python](https://roadmap.sh/python) is visual inspiration for a branching, clickable skill path. This site’s layout, styles, curriculum, notes and code are original; no roadmap.sh assets or source code were copied. There is no affiliation or endorsement.

The MIT license applies to original repository content. External videos, platform courses, documentation and resources retain their own terms and copyrights. Links and optional embeds send visitors to the original providers. The fixture dataset is original synthetic data; see its [provenance](../data/fixtures/README.md).
