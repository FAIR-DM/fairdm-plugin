"""
Default settings for {{ cookiecutter.plugin_name }}.

These settings will be automatically loaded when the plugin is added to
fairdm.setup(addons=["{{ cookiecutter.plugin_slug }}"]).

You can override these settings in your project's config/settings.py file.

Example usage:
    # In your plugin code
    from django.conf import settings
    value = getattr(settings, '{{ cookiecutter.plugin_slug.upper() }}_SETTING_NAME', 'default')

Common settings patterns:
    - Feature flags: {{ cookiecutter.plugin_slug.upper() }}_ENABLED = True
    - Configuration: {{ cookiecutter.plugin_slug.upper() }}_MAX_ITEMS = 100
    - API keys: {{ cookiecutter.plugin_slug.upper() }}_API_KEY = env('API_KEY')
"""

# Add your plugin-specific settings here
# {{ cookiecutter.plugin_slug.upper() }}_SETTING_NAME = "default_value"
