{% if cookiecutter.include_settings == "yes" -%}
"""
Default settings for {{ cookiecutter.plugin_name }}.

These settings will be automatically loaded when the plugin is added to
fairdm.setup(addons=["{{ cookiecutter.plugin_slug }}"]).

You can override these settings in your project's config/settings.py file.
"""

# Add your plugin-specific settings here
# Example:
# {{ cookiecutter.plugin_slug.upper() }}_SETTING_NAME = "default_value"
{% else %}# Settings file not needed for this plugin
# Delete this file if not using custom settings
{% endif %}
