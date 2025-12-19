````markdown
# {{ cookiecutter.plugin_name }}

{{ cookiecutter.plugin_short_description }}

This plugin is designed for use with the [FairDM framework](https://www.fairdm.org/).

## Features

- ✨ Seamless integration with FairDM core models{% if cookiecutter.register_to_models__project == "yes" %} (Project{% endif %}{% if cookiecutter.register_to_models__dataset == "yes" %}, Dataset{% endif %}{% if cookiecutter.register_to_models__sample == "yes" %}, Sample{% endif %}{% if cookiecutter.register_to_models__measurement == "yes" %}, Measurement{% endif %})
- 🎨 Bootstrap 5 compatible UI
- 🔌 Uses existing FairDM components for UI consistency
- 🧪 Comprehensive test suite
- 💻 VSCode workspace configuration with recommended extensions
- 📖 Well-documented and maintainable code

## Installation

```bash
poetry add git+https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.plugin_slug }}
```

Then, in your `config/settings.py` module, add the plugin to your `fairdm.setup` call:

```python
import fairdm

fairdm.setup(addons=["{{ cookiecutter.plugin_slug }}"])
```

That's it! The {{ cookiecutter.plugin_name }} plugin is now installed and ready to use.

## Configuration

You can customize plugin behavior by overriding settings in your `config/settings.py`:

```python
# {{ cookiecutter.plugin_slug.upper() }} Settings
# See {{ cookiecutter.plugin_slug }}/settings.py for available options
```

## Usage

Once installed, the plugin will appear in the plugin menu on applicable detail views. {% if cookiecutter.plugin_category == "EXPLORE" %}It appears in the **Explore** section of the plugin menu.{% elif cookiecutter.plugin_category == "ACTIONS" %}It appears in the **Actions** section of the plugin menu.{% elif cookiecutter.plugin_category == "MANAGEMENT" %}It appears in the **Management** section of the plugin menu.{% endif %}

The plugin automatically registers URLs and appears in the navigation. No additional URL configuration is needed.

## Development

### Setup

```bash
# Clone the repository
git clone https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.plugin_slug }}.git
cd {{ cookiecutter.plugin_slug }}

# Install dependencies
poetry install

# Open in VSCode (recommended)
code {{ cookiecutter.plugin_slug }}.code-workspace

# Run tests
poetry run pytest

# Run tests with coverage
poetry run pytest --cov
```

### VSCode Workspace

The generated plugin includes a VSCode workspace file (`{{ cookiecutter.plugin_slug }}.code-workspace`) with:

- **Recommended extensions** for Python, Django, and testing
- **Pre-configured settings** for Poetry, Ruff, and pytest
- **Debug configurations** for Django development and test debugging
- **Tasks** for running tests, linting, and formatting

### Code Quality

```bash
# Run linting
poetry run ruff check .

# Format code
poetry run ruff format .

# Type checking
poetry run mypy {{ cookiecutter.plugin_slug }}
```

## Project Structure

```
{{ cookiecutter.plugin_slug }}/
├── {{ cookiecutter.plugin_slug }}/
│   ├── __init__.py
│   ├── apps.py                    # Django app configuration
│   ├── plugins.py                 # Plugin registration and views
│   ├── settings.py                # Default settings
│   └── templates/
│       └── {{ cookiecutter.plugin_slug }}/
│           └── {{ cookiecutter.plugin_slug }}.html  # Main plugin template
├── tests/
│   ├── conftest.py                # Pytest fixtures
│   ├── test_apps.py               # App configuration tests
│   └── test_plugins.py            # Plugin functionality tests
├── .github/
│   ├── workflows/
│   │   └── tests.yml              # CI/CD pipeline
│   └── instructions/
│       ├── copilot.instructions.md
│       └── testing.instructions.md
├── {{ cookiecutter.plugin_slug }}.code-workspace  # VSCode workspace config
├── pyproject.toml                 # Poetry configuration
├── README.md
└── LICENSE
```

## Testing

This plugin includes a comprehensive test suite. Run tests with:

```bash
poetry run pytest
```

For more details, see [tests/README.md](tests/README.md).

## Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the {{ cookiecutter.license }} License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built for the [FairDM framework](https://www.fairdm.org/)
- Inspired by the [fairdm-discussions](https://github.com/FAIR-DM/fairdm-discussions) plugin

## Support

If you encounter any issues or have questions:
- Open an issue on [GitHub](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.plugin_slug }}/issues)
- Check the [FairDM documentation](https://www.fairdm.org/en/latest)
- Join the FairDM community discussions

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for a list of changes in each version.

````