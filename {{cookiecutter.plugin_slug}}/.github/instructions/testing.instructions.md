---
applyTo: '**/tests/**'
---

# {{ cookiecutter.plugin_name }} — Testing Instructions

This document provides instructions for creating and running tests.

---

## **General Rules**

- **Always use `pytest`** as the testing framework.  
  **Never** use `unittest`, `TestCase`, or `setUp/tearDown` methods.
- **Test file naming:** All test files must be named `test_*.py`.
- **Running tests:**
  ```bash
  poetry run pytest
  ```
- **Coverage:** Coverage is enabled via `--cov` and configured in `pyproject.toml`.  
  Ensure new tests maintain or improve coverage.

---

## **Directory Structure Rules**

- All production code lives in `{{ cookiecutter.plugin_slug }}/` at the project root.
- All tests live in a single `tests/` directory at the project root.
- The structure of `tests/` **must mirror** the structure of `{{ cookiecutter.plugin_slug }}/` exactly.
- For every module in `{{ cookiecutter.plugin_slug }}/`, there must be a corresponding test module in `tests/` with the same relative path.
- Test files must be named `test_<module>.py`.

**Examples:**

```
{{ cookiecutter.plugin_slug }}/plugins.py
tests/test_plugins.py

{{ cookiecutter.plugin_slug }}/templatetags/{{ cookiecutter.plugin_slug }}.py
tests/test_templatetags/test_{{ cookiecutter.plugin_slug }}.py
```

- Only place tests inside the `tests/` directory — never inside `{{ cookiecutter.plugin_slug }}/`.

### **Allowed Extra Modules Inside `tests/`**

- `conftest.py` — app-specific fixtures
- `factories.py` — factories for the app (if needed)
- `settings.py` — test-specific Django settings (if needed)
- Utility modules such as `helpers.py`, but **only when needed**

---

## **Factories**

- Tests should make use of factories for model creation when required.
- **FairDM core models** have factories available in the FairDM project (e.g., `ProjectFactory`, `DatasetFactory`).
- Import factories from FairDM:
  ```python
  from fairdm.factories import ProjectFactory, DatasetFactory
  ```
- Use `factory_boy` patterns:
  - `SubFactory` for related models
  - `Sequence` for unique fields

---

## **Fixtures and Setup**

- Prefer **pytest fixtures** over any kind of class-based setup.
- Use `conftest.py` for reusable fixtures.
- Use pytest-django built-ins:
  - `db` for database access
  - `client` for Django test client
  - `rf` for RequestFactory
  - `admin_user`, `django_user_model`, etc.
- Fixtures should return the **simplest possible object** needed for the test.

---

## **Test Structure**

Each test file should follow this structure:

```python
"""
Tests for [module description].
"""

import pytest
from {{ cookiecutter.plugin_slug }}.plugins import {{ cookiecutter.plugin_class_name }}


class TestFeatureName:
    """Tests for specific feature."""

    @pytest.mark.django_db
    def test_specific_behavior(self, project):
        """Test description."""
        # Arrange
        plugin = {{ cookiecutter.plugin_class_name }}()
        
        # Act
        result = plugin.some_method()
        
        # Assert
        assert result is not None
```

---

## **Test Naming Conventions**

- **Test files**: `test_<module>.py`
- **Test classes**: `Test<FeatureName>` (PascalCase)
- **Test functions**: `test_<specific_behavior>` (snake_case)
- Test names should clearly describe what is being tested

---

## **Assertions**

- Use pytest's native `assert` statement
- Provide clear assertion messages when helpful:
  ```python
  assert result == expected, f"Expected {expected}, got {result}"
  ```

---

## **Coverage Requirements**

- Aim for **>80% code coverage**
- Run coverage reports:
  ```bash
  poetry run pytest --cov={{ cookiecutter.plugin_slug }} --cov-report=html
  ```
- Focus on testing:
  - Happy path scenarios
  - Edge cases
  - Error handling
  - Permission checks

---

## **Database Tests**

- Mark tests that require database access:
  ```python
  @pytest.mark.django_db
  def test_my_feature():
      pass
  ```
- Use `--reuse-db` flag (configured in `pyproject.toml`) to speed up test runs

---

## **Common Patterns**

### Testing Plugin Registration

```python
@pytest.mark.django_db
def test_plugin_registered_to_model(self):
    """Test that plugin is registered to expected model."""
    from fairdm import plugins
    from fairdm.core.project.models import Project
    
    view_class = plugins.registry.get_view_for_model(Project)
    plugin_names = [p.__name__ for p in view_class.plugins]
    assert "{{ cookiecutter.plugin_class_name }}" in plugin_names
```

### Testing View Context

```python
@pytest.mark.django_db
def test_view_context(self, rf, user, project):
    """Test that view provides correct context."""
    request = rf.get("/")
    request.user = user
    
    view = {{ cookiecutter.plugin_class_name }}()
    view.request = request
    view.base_object = project
    
    context = view.get_context_data()
    assert "base_object" in context
    assert context["base_object"] == project
```

---

## **Running Specific Tests**

```bash
# Run all tests
poetry run pytest

# Run specific file
poetry run pytest tests/test_plugins.py

# Run specific test class
poetry run pytest tests/test_plugins.py::Test{{ cookiecutter.plugin_class_name }}

# Run specific test
poetry run pytest tests/test_plugins.py::Test{{ cookiecutter.plugin_class_name }}::test_specific_feature

# Run with verbose output
poetry run pytest -v

# Run with coverage
poetry run pytest --cov
```

---

## **Test Output**

- Tests should be **silent on success** (no print statements)
- Use pytest's output mechanisms:
  - `-v` for verbose test names
  - `-s` to see print statements during debugging
  - `--pdb` to drop into debugger on failure

---

## **Best Practices**

1. **Keep tests independent** - Each test should run in isolation
2. **Use fixtures** - Don't repeat setup code
3. **Test behavior, not implementation** - Focus on what, not how
4. **One assertion per test** - When possible, test one thing at a time
5. **Use descriptive names** - Test names should explain what they test
6. **Clean up after tests** - Use fixtures for cleanup when needed
7. **Mock external dependencies** - Don't rely on external services in tests

---

## **Debugging Failed Tests**

```bash
# Show print output
poetry run pytest -s

# Drop into debugger on failure
poetry run pytest --pdb

# Show local variables on failure
poetry run pytest -l

# Run last failed tests only
poetry run pytest --lf
```

---

## **CI/CD Integration**

Tests run automatically on:
- Pull requests
- Pushes to main branch

Ensure all tests pass before submitting a PR.
