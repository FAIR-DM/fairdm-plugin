"""
Tests for {{ cookiecutter.plugin_name }} plugin.
"""

import pytest
from django.test import RequestFactory
from fairdm import plugins
{% if cookiecutter.register_to_models.project == "yes" %}from fairdm.core.project.models import Project
{% endif %}{% if cookiecutter.register_to_models.dataset == "yes" %}from fairdm.core.dataset.models import Dataset
{% endif %}{% if cookiecutter.register_to_models.sample == "yes" %}from fairdm.core.sample.models import Sample
{% endif %}{% if cookiecutter.register_to_models.measurement == "yes" %}from fairdm.core.measurement.models import Measurement
{% endif %}
from {{ cookiecutter.plugin_slug }}.plugins import {{ cookiecutter.plugin_class_name }}


class Test{{ cookiecutter.plugin_class_name }}Registration:
    """Tests for {{ cookiecutter.plugin_class_name }} plugin registration."""
{% if cookiecutter.register_to_models.project == "yes" or cookiecutter.register_to_models.dataset == "yes" or cookiecutter.register_to_models.sample == "yes" or cookiecutter.register_to_models.measurement == "yes" %}
    @pytest.mark.parametrize(
        "model_class",
        [{% if cookiecutter.register_to_models.project == "yes" %}Project, {% endif %}{% if cookiecutter.register_to_models.dataset == "yes" %}Dataset, {% endif %}{% if cookiecutter.register_to_models.sample == "yes" %}Sample, {% endif %}{% if cookiecutter.register_to_models.measurement == "yes" %}Measurement{% endif %}],
    )
    @pytest.mark.django_db
    def test_plugin_registered_to_models(self, model_class):
        """Test that {{ cookiecutter.plugin_class_name }} is registered to the expected models."""
        view_class = plugins.registry.get_view_for_model(model_class)
        plugin_names = [p.__name__ for p in view_class.plugins]
        assert "{{ cookiecutter.plugin_class_name }}" in plugin_names

    @pytest.mark.parametrize(
        "model_class",
        [{% if cookiecutter.register_to_models.project == "yes" %}Project, {% endif %}{% if cookiecutter.register_to_models.dataset == "yes" %}Dataset, {% endif %}{% if cookiecutter.register_to_models.sample == "yes" %}Sample, {% endif %}{% if cookiecutter.register_to_models.measurement == "yes" %}Measurement{% endif %}],
    )
    @pytest.mark.django_db
    def test_plugin_registered_only_once(self, model_class):
        """Test that {{ cookiecutter.plugin_class_name }} is registered exactly once per model."""
        view_class = plugins.registry.get_view_for_model(model_class)
        registered_plugins = [p for p in view_class.plugins if p.__name__ == "{{ cookiecutter.plugin_class_name }}"]
        assert len(registered_plugins) == 1
{% endif %}

class Test{{ cookiecutter.plugin_class_name }}Attributes:
    """Tests for {{ cookiecutter.plugin_class_name }} plugin attributes."""

    def test_plugin_has_title(self):
        """Test that the plugin has a title."""
        assert {{ cookiecutter.plugin_class_name }}.title == "{{ cookiecutter.plugin_name }}"

    def test_plugin_has_menu_item(self):
        """Test that the plugin has a menu item configuration."""
        assert {{ cookiecutter.plugin_class_name }}.menu_item is not None
        assert {{ cookiecutter.plugin_class_name }}.menu_item.name == "{{ cookiecutter.plugin_name }}"
        assert {{ cookiecutter.plugin_class_name }}.menu_item.category == plugins.{{ cookiecutter.plugin_category }}
        assert {{ cookiecutter.plugin_class_name }}.menu_item.icon == "{{ cookiecutter.icon_name }}"

    def test_plugin_has_template_name(self):
        """Test that the plugin has a template name."""
        assert {{ cookiecutter.plugin_class_name }}.template_name == "{{ cookiecutter.plugin_slug }}/plugin.html"


class Test{{ cookiecutter.plugin_class_name }}View:
    """Tests for {{ cookiecutter.plugin_class_name }} view functionality."""
{% if cookiecutter.register_to_models.project == "yes" %}
    @pytest.mark.django_db
    def test_plugin_view_with_project(self, rf, user, project):
        """Test that the plugin view works with a Project instance."""
        request = rf.get("/")
        request.user = user
        
        view = {{ cookiecutter.plugin_class_name }}()
        view.request = request
        view.base_object = project
        
        context = view.get_context_data()
        assert "base_object" in context
        assert context["base_object"] == project
{% endif %}{% if cookiecutter.register_to_models.dataset == "yes" %}
    @pytest.mark.django_db
    def test_plugin_view_with_dataset(self, rf, user, dataset):
        """Test that the plugin view works with a Dataset instance."""
        request = rf.get("/")
        request.user = user
        
        view = {{ cookiecutter.plugin_class_name }}()
        view.request = request
        view.base_object = dataset
        
        context = view.get_context_data()
        assert "base_object" in context
        assert context["base_object"] == dataset
{% endif %}
    # Add more view tests here
    # Example:
    # @pytest.mark.django_db
    # def test_custom_functionality(self, rf, user, project):
    #     """Test custom plugin functionality."""
    #     pass
