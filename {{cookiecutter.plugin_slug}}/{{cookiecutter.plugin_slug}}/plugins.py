from django.utils.translation import gettext_lazy as _
from django.views.generic.base import TemplateView
from fairdm import plugins
{% if cookiecutter.register_to_models.project == "yes" %}from fairdm.core.project.models import Project
{% endif %}{% if cookiecutter.register_to_models.dataset == "yes" %}from fairdm.core.dataset.models import Dataset
{% endif %}{% if cookiecutter.register_to_models.sample == "yes" %}from fairdm.core.sample.models import Sample
{% endif %}{% if cookiecutter.register_to_models.measurement == "yes" %}from fairdm.core.measurement.models import Measurement
{% endif %}

@plugins.register({% if cookiecutter.register_to_models.project == "yes" %}Project{% endif %}{% if cookiecutter.register_to_models.dataset == "yes" %}{% if cookiecutter.register_to_models.project == "yes" %}, {% endif %}Dataset{% endif %}{% if cookiecutter.register_to_models.sample == "yes" %}{% if cookiecutter.register_to_models.project == "yes" or cookiecutter.register_to_models.dataset == "yes" %}, {% endif %}Sample{% endif %}{% if cookiecutter.register_to_models.measurement == "yes" %}{% if cookiecutter.register_to_models.project == "yes" or cookiecutter.register_to_models.dataset == "yes" or cookiecutter.register_to_models.sample == "yes" %}, {% endif %}Measurement{% endif %})
class {{ cookiecutter.plugin_class_name }}(plugins.FairDMPlugin, TemplateView):
    """
    {{ cookiecutter.plugin_short_description }}
    
    This plugin is registered to the following models:
    {% if cookiecutter.register_to_models.project == "yes" %}- Project
    {% endif %}{% if cookiecutter.register_to_models.dataset == "yes" %}- Dataset
    {% endif %}{% if cookiecutter.register_to_models.sample == "yes" %}- Sample
    {% endif %}{% if cookiecutter.register_to_models.measurement == "yes" %}- Measurement
    {% endif %}
    """

    title = _("{{ cookiecutter.plugin_name }}")
    menu_item = plugins.PluginMenuItem(
        name=_("{{ cookiecutter.plugin_name }}"),
        category=plugins.{{ cookiecutter.plugin_category }},
        icon="{{ cookiecutter.icon_name }}",
    )
    template_name = "{{ cookiecutter.plugin_slug }}/{{ cookiecutter.plugin_slug }}.html"

    def dispatch(self, request, *args, **kwargs):
        """
        Override dispatch to add permission checks or feature flags.
        
        Example: Check if user has permission to view this object:
        
        from django.core.exceptions import PermissionDenied
        if not request.user.has_perm('view_project', self.base_object):
            raise PermissionDenied
        """
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        """
        Add extra context data to the template.
        
        The base_object is automatically available in the context.
        You can access it here via self.base_object.
        """
        context = super().get_context_data(**kwargs)
        
        # Add any additional context data here
        # context['my_data'] = self.get_my_data()
        
        return context
