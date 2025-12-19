# Contributing to FairDM Plugin Cookiecutter

Thank you for your interest in improving this cookiecutter template!

## How to Contribute

### Testing the Template

Before submitting changes, test the template generation:

```bash
# Generate a test project
cookiecutter /path/to/fairdm-plugin-cookiecutter

# Enter test values when prompted
# Then verify the generated project:
cd test-plugin
poetry install
poetry run pytest
```

### Making Changes

1. **Fork the repository**
   ```bash
   git clone https://github.com/yourusername/fairdm-plugin-cookiecutter.git
   cd fairdm-plugin-cookiecutter
   ```

2. **Create a feature branch**
   ```bash
   git checkout -b feature/my-improvement
   ```

3. **Make your changes**
   - Edit files in `{{cookiecutter.plugin_slug}}/`
   - Update `cookiecutter.json` if adding new variables
   - Update README.md if changing usage

4. **Test thoroughly**
   - Generate multiple test projects with different configurations
   - Verify all features work (waffle, templatetags, etc.)
   - Test with different model registration combinations

5. **Commit and push**
   ```bash
   git add .
   git commit -m "feat: description of changes"
   git push origin feature/my-improvement
   ```

6. **Open a pull request**

## Template Structure Guidelines

### File Organization

- **Template files** go in `{{cookiecutter.plugin_slug}}/`
- **Configuration** goes in `cookiecutter.json`
- **Documentation** goes in README.md

### Using Jinja2 Templates

Template files use Jinja2 syntax:

```jinja2
{# Comments #}
{{ cookiecutter.variable_name }}  {# Variable substitution #}
{% if cookiecutter.option == "yes" %}  {# Conditional #}
    ...
{% endif %}
```

### Adding New Variables

When adding to `cookiecutter.json`:

1. Add the variable with a default value
2. Document it in README.md
3. Use it appropriately in template files
4. Test all combinations

### Conditional Features

Use conditionals for optional features:

```python
{% if cookiecutter.register_to_models.project == "yes" %}
from fairdm.core.project.models import Project
{% endif %}
```

## Testing Checklist

Test the generated project with:

- [ ] All models selected
- [ ] Single model selected
- [ ] No models selected (should fail gracefully or warn)
- [ ] Template tags enabled and disabled
- [ ] All license types
- [ ] All plugin categories
- [ ] Different Python versions

## Code Style

- Keep templates clean and well-commented
- Use descriptive variable names in `cookiecutter.json`
- Follow Django/Python best practices in generated code
- Keep documentation up-to-date

## Documentation

When changing functionality:

1. Update README.md with new features
2. Update examples if needed
3. Add troubleshooting entries for common issues
4. Update the feature list

## Questions?

Open an issue or discussion on GitHub if you have questions!

Thank you for contributing! 🎉
