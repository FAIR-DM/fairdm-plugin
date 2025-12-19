"""
README for Test Suite

This directory contains all tests for {{ cookiecutter.plugin_name }}.

## Running Tests

Run all tests:
```bash
poetry run pytest
```

Run with coverage:
```bash
poetry run pytest --cov
```

Run specific test file:
```bash
poetry run pytest tests/test_plugins.py
```

Run specific test:
```bash
poetry run pytest tests/test_plugins.py::Test{{ cookiecutter.plugin_class_name }}Registration::test_plugin_registered_to_models
```

## Test Structure

- `conftest.py` - Pytest fixtures and configuration
- `test_apps.py` - Tests for Django app configuration
- `test_plugins.py` - Tests for plugin registration and functionality

## Writing Tests

Follow these guidelines:
- Use pytest, never unittest
- Test files must be named `test_*.py`
- Use fixtures from `conftest.py`
- Use FairDM factories for creating test data
- Mark database tests with `@pytest.mark.django_db`
- Test both success and failure cases
- Keep tests focused and independent

## Coverage

Aim for >80% code coverage. Check coverage report after running tests.
