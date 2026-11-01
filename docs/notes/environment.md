# Interpreter & virtual environments

Keep each project isolated and make the interpreter explicit.

Extension beyond the Boot.dev video

## Connect to your work

Use your existing Windows setup. Docker and WSL are optional for this roadmap.

## Learn by doing

- Inspect the installed interpreter before changing anything.
- Create a project .venv and run Python through its explicit path.
- Keep .venv, secrets and generated files out of Git.

## Original practice

Follow docs/setup-windows.md and print sys.executable from the project interpreter.

## Exit check

A fresh terminal runs the tests with the same interpreter, without changing PowerShell policy.

## Understand the idea

An environment isolates project dependencies, while the interpreter still has its own version and executable path. Confirm both before installing or upgrading packages.

On your Windows workflow, invoking .venv\Scripts\python.exe directly avoids needing to change activation policy. Keep the environment reproducible rather than copying it between machines.

## Resources

- [PyPA · environments & packages](https://packaging.python.org/en/latest/tutorials/installing-packages/)
- [Python language tutorial](https://docs.python.org/3/tutorial/)
- [Python - The Basics - Part 1 | جحر السوعبان](https://www.youtube.com/watch?v=XKQaCF_Om8o)
- [The Complete Guide to Python Virtual Environments!](https://www.youtube.com/watch?v=KxvKCSwlUv8)

[Back to the roadmap](../roadmap.md) · [Source and attribution policy](../sources.md)
