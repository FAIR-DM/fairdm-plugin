---
applyTo: '**'
---

# {{ cookiecutter.plugin_name }} — AI Coding Agent Instructions

## IMPORTANT

Always use Context7 when you need code generation, setup or configuration steps, or
library/API documentation. This means you should automatically use the Context7 MCP
tools to resolve library id and get library docs without me having to explicitly ask.

### Context7 Library Reference Guide

Use Context7 to fetch documentation for these libraries based on the task:

**FairDM Integration:**
- `FAIR-DM/fairdm` (GitHub) - Core FairDM framework, plugin system, models, views
- `samueljennings/django-flex-menus` - Menu definitions, rendering, dynamic menus

**Django Core:**
- `django/django` - Core Django functionality, models, views, URLs, settings, middleware
{% if cookiecutter.use_waffle == "yes" %}- `czue/django-waffle` - Feature flags, A/B testing, gradual rollouts
{% endif %}
**Templates & UI:**
- `django/django` (topic: "templates") - Template syntax, tags, filters, template inheritance
- `wrabit/django-cotton` - Cotton template tags, components, layout system
- `twbs/bootstrap` - Bootstrap 5 components, grid system, utilities, responsive design

**Testing & Quality:**
- `pytest-dev/pytest` - Test writing, fixtures, parametrization, assertions
- `pytest-dev/pytest-django` - Django-specific testing, database fixtures, client

When working on a specific task, query the relevant library documentation first to ensure
you're using current APIs and best practices. Use mode='code' for implementation details
and mode='info' for conceptual understanding.

---

## 1. Project Overview

**{{ cookiecutter.plugin_name }}** is a plugin for the FairDM framework.

{{ cookiecutter.plugin_short_description }}

### Key Features:
- Integration with FairDM core models
{% if cookiecutter.use_waffle == "yes" %}- Waffle-enabled feature flag control via the `enable_{{ cookiecutter.plugin_slug }}` switch
{% endif %}- Multi-model support{% if cookiecutter.register_to_models.project == "yes" %} (Project{% endif %}{% if cookiecutter.register_to_models.dataset == "yes" %}, Dataset{% endif %}{% if cookiecutter.register_to_models.sample == "yes" %}, Sample{% endif %}{% if cookiecutter.register_to_models.measurement == "yes" %}, Measurement{% endif %})
- Bootstrap 5 compatible UI

### Core Principles:
- **Minimal footprint** - Add functionality without disrupting existing FairDM features
- **Framework compliance** - Follow FairDM plugin architecture and patterns
- **Reusable** - Should work with any FairDM installation with minimal configuration
- **Configurable** - Settings can be overridden per project needs

---

## 2. Plugin Architecture

This plugin follows the **FairDM plugin system** architecture. The Agent MUST understand:

- **Plugin registration**: Uses `@plugins.register(Model1, Model2, ...)` decorator
- **Base classes**: Inherits from `plugins.FairDMPlugin` + Django view class
- **Menu integration**: Uses `plugins.PluginMenuItem` with category `plugins.{{ cookiecutter.plugin_category }}`
- **Template structure**: Extends `fairdm/plugin.html` with `{% raw %}{% block plugin %}{% endraw %}`
- **Permission checks**: Can use `dispatch()` method for access control

---

## 3. Development Environment & Tools

### Environment Setup
- **Poetry** is the package and environment manager
- All Python commands must be prefixed with `poetry run ...`
  - ✅ `poetry run pytest`
  - ✅ `poetry run python manage.py test`
  - ❌ Do not use bare: `pytest`, `python`

### Quality Standards
- Follow **Ruff** linting rules
- Maximum line length: **120**
- Use **isort-compatible imports**
- Type hints required where possible
- Templates must pass **djlint** validation

### Running Tests
```bash
poetry run pytest                    # Run all tests
poetry run pytest -v                 # Verbose output
poetry run pytest --cov              # With coverage report
```

### Linting & Formatting
```bash
poetry run ruff check .              # Check for issues
poetry run ruff format .             # Format code
poetry run mypy {{ cookiecutter.plugin_slug }}/  # Type checking
```

---

## 4. Testing Guidelines

**Test Framework:**
- Use **pytest** exclusively (never unittest or TestCase)
- Test files must be named `test_*.py`
- Place all tests in `tests/` directory

**Coverage:**
- All new code must have tests
- Maintain or improve coverage percentage
- Test both success and failure cases

---

## 5. Code Style & Conventions

### Python Code:
- Use **f-strings** over `.format()` or `%`
- Prefer `pathlib.Path` over `os.path`
- Always catch specific exceptions, not bare `except:`
- Use type hints where possible
- Import order: stdlib → third-party → local
- Django translation: wrap user-facing strings in `_()` or `gettext_lazy()`

### Template Code:
- Maximum line length: **119**
- Use Cotton components where appropriate
- Keep JavaScript minimal

---

## 6. Integration with FairDM

### Plugin Lifecycle:
1. **Installation**: User adds to `pyproject.toml` and calls `fairdm.setup(addons=["{{ cookiecutter.plugin_slug }}"])`
2. **Plugin Registration**: `plugins.py` registers plugin to core models
3. **URL Generation**: FairDM auto-generates URLs for the plugin
4. **Menu Creation**: Plugin appears in {{ cookiecutter.plugin_category }} menu on detail views

### Accessing FairDM Context:
In plugin methods:
- `self.base_object` - The Project/Dataset/Sample/Measurement instance
- `self.request` - Current HTTP request
- `self.request.user` - Current user

---

## 7. Agent-Specific Notes

When making changes:
1. **Always run tests** after modifications
2. **Update documentation** if behavior changes
3. **Follow FairDM patterns** - this is a plugin, not a standalone app
4. **Check compatibility** with current FairDM development branch
5. **Use Context7** to verify API usage is current

### Temporary Files:
- May create `tmp_*.py` files for experimentation
- Must be deleted after use
- Never commit to version control
