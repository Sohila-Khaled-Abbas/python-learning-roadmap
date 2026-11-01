# Packages & reproducible dependencies

Make the tool runnable from a clean environment with declared requirements.

Extension beyond the Boot.dev video

## Connect to your work

Apply this to your Python data tools, PixelFed quality work, n8n integrations or BI delivery when the project needs it.

## Learn by doing

- Separate import package, distribution name and project directory.
- Describe metadata and interpreter constraints in pyproject.toml.
- Record a repeatable dependency set and test it in a clean environment.

## Original practice

Package the quality CLI with a console entry point and run it after a clean install in a new virtual environment.

## Exit check

The command works outside the repository working directory and the setup documentation identifies the tested interpreter and dependencies.

## Understand the idea

A working notebook environment is not a reproducible installation contract. A project should declare what it imports and which interpreter it supports. Use a virtual environment so another project’s upgrades do not silently change this one.

Distinguish allowed dependency ranges from the exact set tested for an application release. Record the tool and versions used to reproduce that set. Build and install the package in a clean environment to catch accidental imports from the current directory.

## Resources

- [PyPA · environments & packages](https://packaging.python.org/en/latest/tutorials/installing-packages/)
- [PyPA · packaging a Python project](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
- [The Complete Guide to Python Virtual Environments!](https://www.youtube.com/watch?v=KxvKCSwlUv8)

[Back to the roadmap](../roadmap.md) · [Source and attribution policy](../sources.md)
