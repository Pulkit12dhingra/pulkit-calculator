# Pulkit Calculator

A tiny example calculator package providing simple arithmetic helpers.

Install (from PyPI after publishing):

	pip install pulkit-calculator

Usage:

	>>> from pulkit_calculator import add
	>>> add(2, 3)
	5

Publishing
-----------
This repository uses a `src/` layout and a `pyproject.toml`. The recommended local workflow is:

1. Create a venv and activate it.
2. Install build tools: `python -m pip install --upgrade build twine`.
3. Build: `python -m build`.
4. Upload to Test PyPI: `python -m twine upload --repository testpypi dist/*`.

A GitHub Actions workflow is provided to publish on tag push.
