# Windows-first setup

Start in a terminal and inspect your existing tools:

```powershell
Get-Command python, py, git, node -ErrorAction SilentlyContinue
python --version
git --version
node --version
```

Use an installed Python 3.11+ interpreter. If `python` is not the right interpreter but `py` is available, inspect `py --list` and choose an existing version. Do not reinstall, remove or replace working tooling just for this repository. Docker, WSL and an additional database server are unnecessary for the first stages.

From the cloned repository root:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -c "import sys; print(sys.executable)"
.\.venv\Scripts\python.exe -m scripts.check_exercises
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
```

The executable path should end with this repo’s `.venv\Scripts\python.exe`. This method needs no activation and no execution-policy edits. Select the same interpreter in VS Code. `.venv` and generated outputs are ignored by Git.

For the website, use an existing Node 22+ installation. No package installation is needed. Run `npm test`, `npm run build`, then `npm run check`. If `npm.ps1` is blocked by your current PowerShell policy, use `npm.cmd` with the same arguments; do not change policy just for this task.

Only the later pandas/NumPy/ML exercises need third-party packages. Install those into the project environment when the stage requires them, following the linked official documentation, and record the actual working versions. Keep foundation practice lightweight.

On Linux/macOS, use `python3 -m venv .venv` and `.venv/bin/python` for the same module commands. No environment activation is necessary there either.
