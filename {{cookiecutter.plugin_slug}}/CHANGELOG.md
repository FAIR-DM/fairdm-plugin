# Changelog

All notable changes to {{ cookiecutter.plugin_name }} will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Initial plugin structure
- Basic plugin functionality{% if cookiecutter.register_to_models__project == "yes" %}
- Support for Project model{% endif %}{% if cookiecutter.register_to_models__dataset == "yes" %}
- Support for Dataset model{% endif %}{% if cookiecutter.register_to_models__sample == "yes" %}
- Support for Sample model{% endif %}{% if cookiecutter.register_to_models__measurement == "yes" %}
- Support for Measurement model{% endif %}
- Comprehensive test suite
- Documentation

## [{{ cookiecutter.version }}] - {{ cookiecutter.year }}-XX-XX

### Added
- Initial release of {{ cookiecutter.plugin_name }}
- Core plugin functionality
- Basic templates and components
- Test coverage
- CI/CD pipeline

[Unreleased]: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.plugin_slug }}/compare/v{{ cookiecutter.version }}...HEAD
[{{ cookiecutter.version }}]: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.plugin_slug }}/releases/tag/v{{ cookiecutter.version }}
