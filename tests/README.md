# Cookiecutter Template Tests

This directory contains comprehensive tests for the FairDM plugin cookiecutter template.

## Test Structure

### `conftest.py`
Pytest configuration and fixtures:
- `default_context` - Standard test configuration
- `minimal_context` - Minimal plugin configuration
- `full_features_context` - All optional features enabled
- `generated_project` - Auto-generates and cleans up test projects

### `test_generation.py`
Tests basic file and directory generation:
- Correct directory structure
- Required files present
- Conditional features (settings, waffle, etc.)
- No unwanted files (templatetags, urls.py, cotton/sections)
- Different license types

### `test_file_content.py`
Tests generated file contents:
- Python files are syntactically valid
- Configuration files are valid (TOML, JSON, YAML)
- Files contain expected content
- Template files extend correct base
- Documentation is complete

### `test_plugin_functionality.py`
Tests that generated plugin would work in FairDM:
- Plugin class structure
- Inheritance from FairDMPlugin
- Required attributes present
- Correct model registration
- Waffle integration
- Template naming convention

### `test_naming_conventions.py`
Tests naming conventions:
- Slug generation from plugin name
- Class name generation
- File naming patterns
- Python naming conventions (PascalCase, snake_case)
- Consistency across files

## Running Tests

### All Tests
```bash
poetry run pytest
```

### Specific Test File
```bash
poetry run pytest tests/test_generation.py
```

### With Coverage
```bash
poetry run pytest --cov
```

### Verbose Output
```bash
poetry run pytest -v
```

## Test Coverage

The test suite covers:
- ✅ File and directory generation
- ✅ Conditional feature inclusion
- ✅ Multiple license types
- ✅ Python syntax validation
- ✅ Configuration file validity (TOML, JSON, YAML)
- ✅ Plugin class structure
- ✅ Model registration
- ✅ Waffle integration
- ✅ Template naming conventions
- ✅ VSCode workspace configuration
- ✅ Documentation completeness
- ✅ Naming consistency
- ✅ GitHub Actions workflow

## Adding New Tests

When adding new features to the cookiecutter template:

1. Add test fixtures to `conftest.py` if needed
2. Create tests for file generation in `test_generation.py`
3. Add content validation in `test_file_content.py`
4. Test functional aspects in `test_plugin_functionality.py`
5. Verify naming conventions in `test_naming_conventions.py`

## Dependencies

Tests require:
- `pytest` - Test framework
- `cookiecutter` - Template generation
- `tomli` - TOML parsing (Python <3.11)
- `pyyaml` - YAML parsing

These are included in the dev dependencies via `fairdm-dev-tools`.
