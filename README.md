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

Status
------

[![PyPI version](https://img.shields.io/pypi/v/pulkit-calculator.svg)](https://pypi.org/project/pulkit-calculator/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pulkit-calculator.svg)](https://pypi.org/project/pulkit-calculator/)
[![License](https://img.shields.io/pypi/l/pulkit-calculator.svg)](https://pypi.org/project/pulkit-calculator/)
[![CI](https://github.com/Pulkit12dhingra/pulkit-calculator/actions/workflows/publish.yml/badge.svg)](https://github.com/Pulkit12dhingra/pulkit-calculator/actions)

These badges show the current PyPI release, supported Python versions, license, and CI status. The package is published as `pulkit-calculator` on PyPI; import it in Python as `pulkit_calculator`.

Try it quickly:

	python -m pip install --upgrade pip
	pip install pulkit-calculator
	python -c "import pulkit_calculator; print(pulkit_calculator.add(2,3))"

