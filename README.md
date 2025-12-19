````markdown
# FairDM Plugin Cookiecutter

A [Cookiecutter](https://github.com/cookiecutter/cookiecutter) template for creating FairDM plugins quickly and easily.

This template provides a complete, production-ready plugin structure following all FairDM conventions and best practices. Based on the [fairdm-discussions](https://github.com/FAIR-DM/fairdm-discussions) plugin, it includes everything you need to start building a FairDM plugin immediately.

## Features

- ✨ **Complete plugin structure** - All files and directories set up correctly
- 🧪 **Pre-configured test suite** - pytest with fixtures and example tests
- 📦 **Poetry dependency management** - Modern Python packaging
- 💻 **VSCode workspace configuration** - Recommended extensions and settings
- 🔧 **CI/CD ready** - GitHub Actions workflows included
- 📖 **Comprehensive documentation** - README, CONTRIBUTING, CHANGELOG templates
- 🎯 **Multiple plugin types** - EXPLORE, ACTIONS, or MANAGEMENT categories
- 🚦 **Optional Waffle integration** - Feature flag support
- 🔍 **Code quality tools** - Ruff, mypy, coverage pre-configured
- 🔌 **Uses existing FairDM components** - For UI consistency

## Prerequisites

- Python 3.11 or higher
- [Cookiecutter](https://github.com/cookiecutter/cookiecutter)
- [Poetry](https://python-poetry.org/) (for development)

## Installation

Install cookiecutter if you haven't already:

```bash
pip install cookiecutter
```

Or use pipx for isolated installation:

```bash
pipx install cookiecutter
```

## Usage

### Generate a New Plugin

```bash
# From GitHub (recommended)
cookiecutter gh:FAIR-DM/fairdm-plugin-cookiecutter

# Or from a local clone
cookiecutter /path/to/fairdm-plugin-cookiecutter
```

### Interactive Prompts

You'll be asked to provide:

| Prompt | Description | Example |
|--------|-------------|---------|
| `plugin_name` | Human-readable plugin name | "My FairDM Plugin" |
| `plugin_slug` | Python package name (auto-generated) | "my_fairdm_plugin" |
| `plugin_short_description` | Brief description of the plugin | "Adds awesome functionality to FairDM" |
| `plugin_class_name` | Main plugin class name (auto-generated) | "MyFairDMPlugin" |
| `author_name` | Your full name | "Jane Doe" |
| `author_email` | Your email address | "jane@example.com" |
| `github_username` | Your GitHub username | "janedoe" |
| `version` | Initial version number | "0.1.0" |
| `python_version` | Python version to target | "3.11" |
| `license` | Choose from MIT, BSD-3-Clause, Apache-2.0, GPL-3.0 | "MIT" |
| `register_to_models` | Which FairDM models to register to | See below |
| `plugin_category` | Where to show in plugin menu | EXPLORE, ACTIONS, or MANAGEMENT |
| `icon_name` | django-easy-icons alias | "puzzle-piece" |

#### Model Registration Options

The `register_to_models` option lets you choose which FairDM models your plugin will work with:

- **project**: Register to Project model
- **dataset**: Register to Dataset model  
- **sample**: Register to Sample model
- **measurement**: Register to Measurement model

Set each to "yes" or "no" during the prompts.

## What Gets Generated

The cookiecutter creates a complete, production-ready plugin package:

- **Complete Python package structure** with Poetry configuration
- **Plugin class** that extends `FairDMPlugin` and integrates with the FairDM registry
- **Django app configuration** with automatic plugin registration
- **Template structure** following FairDM conventions (extends `fairdm/plugin.html`)
- **Comprehensive test suite** using pytest with fixtures for all FairDM models
- **CI/CD pipeline** with GitHub Actions (Python 3.11 & 3.12, Ruff, mypy, pytest, coverage)
- **VSCode workspace file** with recommended extensions, debug configs, and tasks
- **Development tools** including pre-commit hooks and code quality checks
- **Documentation** including README, CONTRIBUTING, CHANGELOG, and AI coding instructions
- **Optional features** via prompts:
  - Waffle feature flag integration
  - Custom settings file
  - REST API endpoints

### Generated Structure

```
my-plugin/
├── my_plugin/                      # Main package directory
│   ├── __init__.py                # Package initialization
│   ├── apps.py                    # Django app configuration
│   ├── plugins.py                 # Plugin registration and implementation
│   ├── settings.py                # Plugin-specific settings (optional)
│   └── templates/                 # Template directory
│       └── my_plugin/
│           └── my_plugin.html    # Main plugin template (auto-discovered)
├── tests/                         # Test suite
│   ├── __init__.py
│   ├── conftest.py               # Pytest fixtures for FairDM models
│   ├── test_apps.py              # App configuration tests
│   ├── test_plugins.py           # Plugin registration and functionality tests
│   └── README.md                 # Testing documentation
├── .github/                       # GitHub configuration
│   ├── instructions/             # AI coding agent instructions
│   │   ├── copilot.instructions.md
│   │   └── testing.instructions.md
│   ├── workflows/                # CI/CD workflows
│   │   └── tests.yml
│   ├── ISSUE_TEMPLATE/           # Issue templates
│   │   ├── bug_report.yml
│   │   └── feature_request.yml
│   ├── pull_request_template.md
│   └── dependabot.yml
├── my_plugin.code-workspace      # VSCode workspace configuration
├── pyproject.toml                # Poetry configuration
├── README.md                     # Project documentation
├── LICENSE                       # License file
├── .gitignore                    # Git ignore rules
├── .pre-commit-config.yaml       # Pre-commit hooks
├── codecov.yml                   # Code coverage configuration
├── CHANGELOG.md                  # Version history
└── CONTRIBUTING.md               # Contribution guidelines
```

## After Generation

### 1. Initialize Your Plugin

```bash
cd my-plugin

# Install dependencies
poetry install

# Open in VSCode with recommended settings
code my-plugin.code-workspace

# Run tests to verify everything works
poetry run pytest
```

### 2. Customize Your Plugin

Edit the generated files to implement your plugin's functionality:

- **`my_plugin/plugins.py`** - Main plugin logic and view implementation
- **`my_plugin/templates/my_plugin/my_plugin.html`** - UI template (use existing FairDM components)
- **`tests/`** - Add comprehensive tests for your functionality

### 3. Set Up Git Repository

```bash
git init
git add .
git commit -m "Initial commit from cookiecutter template"

# Create a repository on GitHub, then:
git remote add origin git@github.com:yourusername/my-plugin.git
git push -u origin main
```

### 4. Install in a FairDM Project

```bash
# In your FairDM project
poetry add git+https://github.com/yourusername/my-plugin
```

Then add to `config/settings.py`:

```python
import fairdm

fairdm.setup(addons=["my_plugin"])
```

## Plugin Development Workflow

### Running Tests

```bash
# Run all tests
poetry run pytest

# Run with coverage
poetry run pytest --cov

# Run specific test file
poetry run pytest tests/test_plugins.py

# Run tests in VSCode Test Explorer (recommended)
# Click the beaker icon in the Activity Bar
```

### Code Quality

```bash
# Lint code
poetry run ruff check .

# Format code
poetry run ruff format .

# Type checking
poetry run mypy my_plugin
```

### Pre-commit Hooks

Set up pre-commit hooks to automatically check code quality:

```bash
poetry run pre-commit install
```

### VSCode Integration

The generated workspace file provides:

- **Python environment detection** - Automatically uses Poetry virtual environment
- **Test discovery and debugging** - Run/debug tests directly from editor
- **Integrated linting** - Ruff integration with auto-fix on save
- **Template formatting** - djlint for Django templates
- **Debug configurations** - For Django development server and pytest
- **Recommended extensions** - Automatic prompts to install useful tools

## Examples

### Example 1: Simple Exploration Plugin

```bash
$ cookiecutter gh:FAIR-DM/fairdm-plugin-cookiecutter
plugin_name: Data Visualizer
plugin_slug: data_visualizer
plugin_short_description: Visualize dataset contents with charts and graphs
author_name: John Smith
author_email: john@example.com
github_username: johnsmith
version: 0.1.0
python_version: 3.11
license: MIT
register_to_models.project: no
register_to_models.dataset: yes
register_to_models.sample: no
register_to_models.measurement: no
plugin_category: EXPLORE
icon_name: chart-line
```

### Example 2: Management Action Plugin

```bash
$ cookiecutter gh:FAIR-DM/fairdm-plugin-cookiecutter
plugin_name: Batch Exporter
plugin_slug: batch_exporter
plugin_short_description: Export multiple datasets in various formats
author_name: Jane Doe
author_email: jane@example.com
github_username: janedoe
version: 0.1.0
python_version: 3.11
license: BSD-3-Clause
register_to_models.project: yes
register_to_models.dataset: yes
register_to_models.sample: yes
register_to_models.measurement: yes
plugin_category: ACTIONS
icon_name: download
```

## Architecture Notes

### Plugin URL Auto-Registration

FairDM automatically generates URLs for plugins - you don't need to create a `urls.py` file. The URL pattern follows:

```
/<model-type>/<pk>/plugins/<plugin-slug>/
```

For example:
- `/project/123/plugins/data-visualizer/`
- `/dataset/456/plugins/batch-exporter/`

### Template Naming Convention

The main plugin template must be named to match your plugin slug:

```
templates/{{ plugin_slug }}/{{ plugin_slug }}.html
```

This allows FairDM to automatically discover and load your template.

### Using Existing FairDM Components

For UI consistency, use existing components from FairDM and django-cotton-bs5 where possible:

```django
{% extends "fairdm/plugin.html" %}

{% block plugin %}
{# Use Bootstrap 5 components #}
<div class="card">
  <div class="card-body">
    {{ base_object }}
  </div>
</div>

{# Or Cotton components if needed #}
<c-bs5.alert variant="info">
  Your message here
</c-bs5.alert>
{% endblock %}
```

### Advanced Customization

For advanced features like custom template tags or URL patterns, you can manually add them to your generated plugin. The cookiecutter provides a solid foundation - you're free to extend it as needed.

## Troubleshooting

### Poetry Not Found

Make sure Poetry is installed:

```bash
pipx install poetry
```

### Tests Failing

Ensure you have the correct Python version:

```bash
python --version  # Should be 3.11 or higher
poetry env use python3.11
poetry install
```

### Plugin Not Appearing

1. Check that the plugin is added to `fairdm.setup(addons=[...])`
2. Run migrations: `poetry run python manage.py migrate`
3. Restart the Django development server
4. Clear browser cache

### VSCode Extensions Not Loading

Open the command palette (Ctrl+Shift+P / Cmd+Shift+P) and run:
```
Extensions: Show Recommended Extensions
```

## Contributing

Contributions to the cookiecutter template are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. **Run the test suite** to ensure everything works:
   ```bash
   poetry install
   poetry run pytest --cov
   ```
5. Test by generating a plugin and verifying it works:
   ```bash
   cookiecutter . --no-input
   cd test_plugin
   poetry install
   poetry run pytest
   ```
6. Submit a pull request

### Test Suite

The template includes a comprehensive test suite in `tests/` that validates:

- ✅ Correct file and directory generation
- ✅ Conditional feature inclusion (waffle, settings, API)
- ✅ Python syntax validation
- ✅ Configuration file validity (TOML, JSON, YAML)
- ✅ Plugin class structure and functionality
- ✅ Naming conventions and consistency
- ✅ Generated plugin test suite

See [`tests/README.md`](tests/README.md) for details.

## License

This cookiecutter template is licensed under the MIT License.

Generated plugins use the license you select during generation.

## Resources

- [FairDM Documentation](https://www.fairdm.org/en/latest)
- [FairDM Plugin System Guide](https://www.fairdm.org/en/latest/developer-guide/plugin-system.html)
- [Cookiecutter Documentation](https://cookiecutter.readthedocs.io/)
- [Poetry Documentation](https://python-poetry.org/docs/)

## Support

- **Issues**: [GitHub Issues](https://github.com/FAIR-DM/fairdm-plugin-cookiecutter/issues)
- **Discussions**: [GitHub Discussions](https://github.com/FAIR-DM/fairdm-plugin-cookiecutter/discussions)
- **FairDM Community**: Join the discussion in the main FairDM repository

````