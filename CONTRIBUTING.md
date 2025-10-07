# Contributing

Thanks for your interest in contributing!

## How to contribute
1. Fork the repo and create your branch from `main`.
2. Ensure install with dev deps: `pip install -r requirements/dev.txt`.
3. Run quality checks and tests:
   - `ruff check .`
   - `black --check .`
   - `mypy .`
   - `pytest -q`
4. Submit a pull request with a clear description.

## Coding guidelines
- Use type hints and meaningful names.
- Keep functions small and focused.
- Add/maintain docstrings for public functions.

## Commit messages
- Use concise, imperative phrases: "Add", "Fix", "Refactor".
- Reference issues when applicable.

## Reporting issues
- Include steps to reproduce, expected vs actual behavior, logs/tracebacks.

## Code of Conduct
- See `CODE_OF_CONDUCT.md`. By participating, you agree to abide by it.
