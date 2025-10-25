# Contributing to pulkit-calculator

Thank you for your interest in contributing!

## How to Contribute

1. **Fork the repository** on GitHub and clone your fork locally.
2. **Create a new branch** for your feature or fix:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Install dev dependencies**:
   ```bash
   pip install -e .[dev]
   pre-commit install
   ```
4. **Run checks before committing**:
   - `make check` (runs lint, type, and tests)
   - `pre-commit run --all-files` (optional, runs hooks on all files)
5. **Commit your changes**:
   - Use `make git-commit m="your message"` to avoid git deadlocks.
6. **Push your branch**:
   ```bash
   git push origin feature/your-feature-name
   ```
7. **Open a Pull Request** on GitHub.

## Code Style & Quality
- Use type hints for new functions.
- Run `ruff` and `mypy` before pushing.
- Write unit tests for new features in `tests/test_core.py`.
- Document new functions in code and README if relevant.

## PR Review Process
- All PRs are checked by CI (lint, type, test).
- Only PRs passing all checks will be merged.
- Squash commits if possible for a clean history.

## Security & Secrets
- Never commit `.env` or any secret tokens.
- If you accidentally commit a secret, revoke it immediately and notify a maintainer.

## Release Process
- Maintainers will bump the version, tag, and publish to PyPI after merging.
- Contributors can suggest changelog entries in PRs.

## Questions or Help
- Open an issue for bugs, feature requests, or questions.
- For urgent security issues, email the maintainer directly.

---
Happy coding!
