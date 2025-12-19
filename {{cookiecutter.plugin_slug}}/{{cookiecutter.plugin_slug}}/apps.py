from django.apps import AppConfig


class {{ cookiecutter.plugin_class_name }}Config(AppConfig):
    """Django app configuration for {{ cookiecutter.plugin_name }}."""
    
    name = "{{ cookiecutter.plugin_slug }}"
    verbose_name = "{{ cookiecutter.plugin_name }}"
    default_auto_field = "django.db.models.BigAutoField"

    def ready(self):
        """
        Perform initialization when Django starts.
        
        Import plugins to ensure they are registered with FairDM.
        """
        # Import plugins to register them
        from . import plugins  # noqa: F401
