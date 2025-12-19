# Contributing to {{ cookiecutter.plugin_name }}

Thank you for your interest in contributing to {{ cookiecutter.plugin_name }}! This document provides guidelines and instructions for contributing.

## Code of Conduct

By participating in this project, you agree to maintain a respectful and inclusive environment for all contributors.

## Getting Started

### Prerequisites

- Python {{ cookiecutter.python_version }} or higher
- Poetry for dependency management
- Git

### Development Setup

1. **Fork and clone the repository**
   ```bash
   git clone https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.plugin_slug }}.git
   cd {{ cookiecutter.plugin_slug }}
   ```

2. **Install dependencies**
   ```bash
   poetry install
   ```

3. **Create a feature branch**
   ```bash
   git checkout -b feature/my-new-feature
   ```

## Development Workflow

### Running Tests

Run the test suite to ensure everything works:

```bash
# Run all tests
poetry run pytest

# Run with coverage report
poetry run pytest --cov

# Run specific test file
poetry run pytest tests/test_plugins.py

# Run specific test
poetry run pytest tests/test_plugins.py::TestMyPlugin::test_specific_feature
```

### Code Quality

Before committing, ensure your code meets quality standards:

```bash
# Run linting
poetry run ruff check .

# Auto-fix linting issues
poetry run ruff check . --fix

# Format code
poetry run ruff format .

# Type checking
poetry run mypy {{ cookiecutter.plugin_slug }}
```

### Writing Tests

- **Always write tests** for new features and bug fixes
- Use **pytest** (never unittest)
- Place tests in the `tests/` directory
- Mirror the package structure in test files
- Aim for >80% code coverage

Example test structure:

```python
import pytest
from {{ cookiecutter.plugin_slug }}.plugins import {{ cookiecutter.plugin_class_name }}


@pytest.mark.django_db
def test_my_feature(project):
    """Test description."""
    # Arrange
    plugin = {{ cookiecutter.plugin_class_name }}()
    
    # Act
    result = plugin.some_method()
    
    # Assert
    assert result is not None
```

## Making Changes

### Commit Messages

Follow conventional commit format:

- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation changes
- `test:` Test additions or modifications
- `refactor:` Code refactoring
- `style:` Code style changes
- `chore:` Build process or auxiliary tool changes

Example:
```
feat: add support for custom filters in plugin view

- Implemented filter_class attribute
- Added tests for filter functionality
- Updated documentation
```

### Pull Request Process

1. **Update documentation** if needed
2. **Add tests** for new functionality
3. **Ensure all tests pass**: `poetry run pytest`
4. **Ensure code is formatted**: `poetry run ruff format .`
5. **Update CHANGELOG.md** with your changes
6. **Push to your fork** and create a pull request

Pull request template:

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
Describe how you tested your changes

## Checklist
- [ ] Tests pass locally
- [ ] Code follows style guidelines
- [ ] Documentation updated
- [ ] CHANGELOG.md updated
```

## Code Style Guidelines

### Python Code

- Follow PEP 8 guidelines (enforced by Ruff)
- Maximum line length: **120 characters**
- Use **f-strings** for string formatting
- Use **pathlib.Path** for file paths
- Add **type hints** where possible
- Write **docstrings** for public functions/classes

Example:

```python
def process_data(obj: Model, threshold: int = 10) -> dict[str, Any]:
    """
    Process data for the given object.
    
    Args:
        obj: The model instance to process
        threshold: Minimum threshold value
        
    Returns:
        Dictionary containing processed results
    """
    # Implementation
    pass
```

### Django/Template Code

- Follow Django best practices
- Use **translation utilities** for user-facing strings: `_()` or `gettext_lazy()`
- Keep templates **semantic and accessible**
- Use **Cotton components** for reusable UI elements

### Testing Code

- One test per specific behavior
- Clear, descriptive test names
- Use **pytest fixtures** from `conftest.py`
- Mark database tests with `@pytest.mark.django_db`

## Documentation

### Docstrings

Use Google-style docstrings:

```python
def my_function(param1: str, param2: int) -> bool:
    """
    Brief description of function.
    
    Longer description if needed, explaining the function's
    purpose and behavior.
    
    Args:
        param1: Description of param1
        param2: Description of param2
        
    Returns:
        Description of return value
        
    Raises:
        ValueError: When param2 is negative
    """
    pass
```

### README Updates

Update the README.md if you:
- Add new configuration options
- Introduce new features
- Change installation/usage instructions

## Release Process

Maintainers handle releases:

1. Update version in `pyproject.toml`
2. Update `CHANGELOG.md`
3. Create git tag: `git tag v0.2.0`
4. Push tag: `git push origin v0.2.0`
5. GitHub Actions handles the rest

## Questions?

- Open an issue for bugs or feature requests
- Check existing issues and discussions
- Refer to [FairDM documentation](https://www.fairdm.org/en/latest)

## License

By contributing, you agree that your contributions will be licensed under the {{ cookiecutter.license }} License.

Thank you for contributing to {{ cookiecutter.plugin_name }}! 🎉
