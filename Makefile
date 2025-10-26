SHELL := /bin/bash
PY := python

.PHONY: help check lint type test git-commit git-push git-release release-pypi push

help:
	@echo "Makefile targets:"
	@echo "  make check         # run lint, type checks and tests"
	@echo "  make lint          # run ruff"
	@echo "  make type          # run mypy"
	@echo "  make test          # run pytest"
	@echo "  make git-commit m='<message>'   # git add, commit (handles .git/index.lock)"
	@echo "  make git-push      # push current branch to origin"
	@echo "  make git-release m='<message>' v='<version>'  # commit, tag and push"
	@echo "  make release-pypi  # build and upload to PyPI (requires TWINE_PASSWORD env var)"
	@echo "  make push          # commit all changes with version, tag and push"
push:
	@version=$$(grep '^version' pyproject.toml | head -1 | cut -d'=' -f2 | tr -d '" '); \
	if [ -z "$$version" ]; then \
	  echo 'ERROR: Could not find version in pyproject.toml'; exit 1; \
	fi; \
	if [ -f .git/index.lock ]; then \
	  echo ".git/index.lock found — removing to avoid deadlock"; \
	  rm -f .git/index.lock; \
	fi; \
	git add -A; \
	git commit -m "chore: release v$$version"; \
	git tag -a v$$version -m "Release v$$version"; \
	git push origin HEAD --tags

lint:
	@echo "Running ruff..."
	$(PY) -m ruff check src tests

type:
	@echo "Running mypy..."
	$(PY) -m mypy src || true

test:
	@echo "Running pytest..."
	$(PY) -m pytest -q

check: lint type test

git-commit:
	@if [ -f .git/index.lock ]; then \
	  echo ".git/index.lock found — removing to avoid deadlock"; \
	  rm -f .git/index.lock; \
	fi
	@git add -A
	@if [ -z "$(m)" ]; then \
	  echo 'ERROR: pass a commit message with m="your message"'; exit 1; \
	fi
	@git commit -m "$(m)"

git-push:
	@git push origin HEAD

git-release:
	@if [ -z "$(m)" -o -z "$(v)" ]; then \
	  echo 'Usage: make git-release m="message" v="0.1.1"'; exit 1; \
	fi
	@$(MAKE) git-commit m="$(m)"
	@git tag -a v$(v) -m "$(m)"
	@git push origin HEAD --tags

release-pypi:
	@echo "Building and uploading to PyPI..."
	@python -m build
	@TWINE_USERNAME=__token__ TWINE_PASSWORD="$$PYPI_API_TOKEN" python -m twine upload dist/*
	@echo "Done."
