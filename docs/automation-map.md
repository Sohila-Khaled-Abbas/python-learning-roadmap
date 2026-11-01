# How the learning system stays connected

| Change | Automatic result | Trigger |
| --- | --- | --- |
| Push Python roadmap content or UI changes | Rebuild notes/catalog, run checks, publish GitHub Pages | Every push to this repo’s `main` |
| Create or update a public original repo | Refresh portfolio project metadata, README excerpt and searchable project page | Existing portfolio sync, hourly at minute 17; manual run available |
| Add a public original learning repo | Include it in the portfolio learning shelf and profile’s additional learning list | Match a roadmap/lab/course name or learning-related topic; then the next successful sync/build |
| Update portfolio role, bio, skills, training or project status | Regenerate the GitHub profile README from those public portfolio sources | Existing profile sync, hourly at minute 37 |
| Update repository description or Website | Refresh the portfolio and profile overview/link | Next successful source synchronization |
| Change personal learning progress | Save status and plain-text notes in the current browser | Immediately on edit; export/import moves it between browsers |

The portfolio lives in [sohila-k-abbas-website](https://github.com/Sohila-Khaled-Abbas/sohila-k-abbas-website). The GitHub profile generator lives in [Sohila-Khaled-Abbas](https://github.com/Sohila-Khaled-Abbas/Sohila-Khaled-Abbas), with its behavior described in `docs/PROFILE_AUTOMATION.md`. Both scheduled jobs already existed and were extended for this learning path. The profile reads one coherent portfolio source revision. No new personal access token or ChatGPT scheduled task is needed.

Learning discovery uses names containing `roadmap`, `learning-resources`, `second-brain`, a `labs` or `course` segment, or an exact `learning`, `roadmap`, `learning-roadmap`, `tutorial` or `education` topic. Preferred learning links and homepage featured selections are curated; automatically discovered learning resources appear alongside them. New public projects are added to the complete collection without editing those selections.

GitHub schedules are best-effort. This is periodic synchronization, not an instant cross-repository webhook. A new project’s overview can appear in the live collection before its static page is built. Source failures retain the last successful snapshot. Private repos are excluded; activity never marks a project or skill completed.

The DE roadmap receives the Python source and resource links. The FDE roadmap’s Python service-skill node links directly to this branch and publishes through its existing Pages workflow. This task does not change the parent DE site’s separate release controls or hosting audience.

The coding lab is included in the same push-to-Pages workflow. Challenge contracts are shared by the browser and CI; lab drafts and checked history stay in their own browser-local store and have a separate export/import backup. They are not sent to GitHub or the portfolio by the application.
