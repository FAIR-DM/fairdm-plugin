# GitHub Configuration

This directory contains GitHub-specific configuration for the cookiecutter template repository.

## Workflows

### `test-template.yml`
Comprehensive CI/CD pipeline that:

1. **Runs Template Tests** (Python 3.11 & 3.12)
   - Lints the test suite with Ruff
   - Type checks with mypy
   - Runs pytest with coverage
   - Uploads coverage to Codecov

2. **Tests Template Generation**
   - Generates a test plugin using cookiecutter
   - Verifies correct directory structure
   - Confirms removed files don't exist (urls.py, templatetags/, cotton/)
   - Installs dependencies in generated plugin
   - Runs the generated plugin's test suite

This ensures both the template itself and generated plugins work correctly.

## Running Locally

### Test the Template
```bash
# Run template tests
poetry install
poetry run pytest

# With coverage
poetry run pytest --cov
```

### Test Template Generation
```bash
# Generate a test plugin
cookiecutter . --no-input

# Verify the generated plugin
cd test_plugin
poetry install
poetry run pytest
```

## Coverage Reporting

Coverage reports are uploaded to Codecov on every push. The target is 80% coverage for both the template tests and generated plugin code.
