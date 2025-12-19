"""
Tests for {{ cookiecutter.plugin_name }} Django app configuration.
"""

import pytest
from django.apps import apps


@pytest.mark.django_db
def test_app_config_exists():
    """Test that the app configuration exists and is properly configured."""
    app_config = apps.get_app_config("{{ cookiecutter.plugin_slug }}")
    assert app_config is not None
    assert app_config.name == "{{ cookiecutter.plugin_slug }}"
    assert app_config.verbose_name == "{{ cookiecutter.plugin_name }}"
