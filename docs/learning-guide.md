# Learning Guide: Project Structure & Tooling

This guide explains the tools and files used in this project, and how to set
everything up on your own machine. It's meant as a reference while working
through the training exercises.

## 1. Project structure

```
readme.md                  # project intro
pyproject.toml             # project metadata & dependencies (Poetry)
poetry.lock                # exact, locked dependency versions
.pre-commit-config.yaml    # local code-quality checks run before each commit
.gitignore                 # files/folders git should not track
.github/workflows/ci.yml   # GitHub Actions pipeline (runs on push/PR)
src/                       # application/package source code
tests/                     # automated tests (pytest)
data/                      # mock CSV data used in the exercises
```

## 2. `.gitignore`

Tells git which files/folders to never track (so they aren't committed),
for example:
- Virtual environments (`.venv/`)
- Cache/build artifacts (`__pycache__/`, `.pytest_cache/`, `.ruff_cache/`)
- Editor/IDE settings (`.vscode/`, `.idea/`)

These files are usually machine-specific or regenerated automatically, so
sharing them in git would only cause noise and merge conflicts.

## 3. Dependency management with Poetry

[Poetry](https://python-poetry.org/) manages both your virtual environment
and your project's dependencies.

- `pyproject.toml` — the source of truth. Lists the project's metadata
  (name, version, authors) and the dependencies you asked for
  (e.g. `pandas`, `pytest`), each with a version constraint (e.g. `^3.11`
  means "compatible with 3.11, but allow newer minor/patch versions").
- `poetry.lock` — the exact versions Poetry resolved for every dependency
  (including sub-dependencies). This file is committed so every machine
  (yours, a teammate's, CI) installs the *identical* set of versions —
  this is what makes builds reproducible.

Common commands:

```bash
poetry install          # create venv (if needed) and install all dependencies
poetry add <package>    # add a new runtime dependency
poetry add --group dev <package>  # add a dependency only needed for development
poetry run <command>    # run a command inside the project's virtual environment
poetry shell            # activate the virtual environment in your terminal
```

## 4. Package creation

`src/` contains an `__init__.py`, which marks it as a Python *package* —
this allows other code (and your tests) to `import src.process` instead of
relying on file paths. Poetry uses the `[tool.poetry]` section in
`pyproject.toml` (name, version, readme, etc.) to know how to package and
distribute your project if you ever publish it.

## 5. Unit testing

Tests live in `tests/` and are written with [pytest](https://docs.pytest.org/).

- Test files/functions must start with `test_` so pytest discovers them
  automatically.
- Each test typically follows the **Arrange / Act / Assert** pattern:
  1. **Arrange** — set up inputs and expected output.
  2. **Act** — call the function you're testing.
  3. **Assert** — check the actual result matches what you expected.
- Pandas has its own assertion helpers (e.g. `pd.testing.assert_frame_equal`)
  since `==` doesn't work well for comparing DataFrames.

Run the tests:

```bash
poetry run pytest
```

## 6. Pre-commit

[pre-commit](https://pre-commit.com/) runs automated checks ("hooks") on
your code every time you `git commit`, catching issues before they even
reach CI. Configured in `.pre-commit-config.yaml`:

- `trailing-whitespace`, `end-of-file-fixer` — tidy up whitespace
- `check-yaml`, `check-toml` — make sure config files are valid
- `check-added-large-files`, `check-merge-conflict` — catch common mistakes
- `ruff` / `ruff-format` — lint and auto-format Python code

Install the git hook once per clone so it runs automatically on every commit:

```bash
poetry run pre-commit install
```

Run it manually against all files (useful the first time, or in CI):

```bash
poetry run pre-commit run --all-files
```

## 7. Continuous Integration (CI)

`.github/workflows/ci.yml` defines a [GitHub Actions](https://docs.github.com/actions)
workflow that runs automatically on every push and pull request. It:

1. Checks out the repository.
2. Installs Python 3.11 and Poetry.
3. Installs the project's dependencies (`poetry install`).
4. Runs `pre-commit run --all-files` — the same checks you run locally.
5. Runs `pytest` — the automated test suite.

This ensures every change is checked the same way, regardless of who wrote
it or what's on their machine, before it can be merged.

---

## Install guide

Follow these steps to set up the project locally.

### 1. Install Python

Install Python 3.11 (matching the version in `pyproject.toml`), e.g. via
[pyenv](https://github.com/pyenv/pyenv) or from [python.org](https://www.python.org/downloads/).

```bash
python3 --version
```

### 2. Install Poetry

```bash
curl -sSL https://install.python-poetry.org | python3 -
poetry --version
```

### 3. Install project dependencies

From the project root:

```bash
poetry install
```

This creates a virtual environment and installs everything listed in
`pyproject.toml`/`poetry.lock`.

### 4. Install the pre-commit git hook

```bash
poetry run pre-commit install
```

From now on, the checks in `.pre-commit-config.yaml` run automatically
whenever you `git commit`.

### 5. Run the tests

```bash
poetry run pytest
```

### 6. (Optional) Run all pre-commit checks manually

```bash
poetry run pre-commit run --all-files
```

Once these all pass locally, pushing your changes should also pass CI.
