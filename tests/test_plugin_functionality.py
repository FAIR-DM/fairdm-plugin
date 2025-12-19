"""Test that the generated plugin would work correctly in a FairDM project."""

import ast
import pytest


class TestPluginClass:
    """Test that the generated plugin class is correctly structured."""

    def test_plugin_inherits_from_fairdm_plugin(self, generated_project):
        """Test that plugin class inherits from FairDMPlugin."""
        plugins_file = generated_project / "test_plugin" / "plugins.py"
        content = plugins_file.read_text()
        
        # Parse the Python file
        tree = ast.parse(content)
        
        # Find the plugin class
        plugin_class = None
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef) and node.name == "TestPlugin":
                plugin_class = node
                break
        
        assert plugin_class is not None, "Plugin class 'TestPlugin' not found"
        
        # Check inheritance
        base_names = [base.id if hasattr(base, 'id') else str(base.attr) for base in plugin_class.bases]
        assert any('FairDMPlugin' in name for name in base_names), "Plugin doesn't inherit from FairDMPlugin"

    def test_plugin_has_required_attributes(self, generated_project):
        """Test that plugin class has required attributes."""
        plugins_file = generated_project / "test_plugin" / "plugins.py"
        content = plugins_file.read_text()
        
        # Should have required attributes
        assert 'title =' in content
        assert 'menu_item =' in content
        assert 'template_name =' in content

    def test_plugin_has_menu_item_with_category(self, generated_project):
        """Test that menu_item has a category."""
        plugins_file = generated_project / "test_plugin" / "plugins.py"
        content = plugins_file.read_text()
        
        assert 'PluginMenuItem' in content
        assert 'category=plugins.EXPLORE' in content

    def test_plugin_has_get_context_data_method(self, generated_project):
        """Test that plugin has get_context_data method."""
        plugins_file = generated_project / "test_plugin" / "plugins.py"
        content = plugins_file.read_text()
        
        assert 'def get_context_data(self, **kwargs):' in content
        assert 'super().get_context_data(**kwargs)' in content

    def test_plugin_category_matches_context(self, minimal_project):
        """Test that plugin category matches the selected category."""
        plugins_file = minimal_project / "minimal_plugin" / "plugins.py"
        content = plugins_file.read_text()
        
        # Minimal context uses ACTIONS category
        assert 'category=plugins.ACTIONS' in content

    def test_plugin_icon_matches_context(self, generated_project):
        """Test that plugin icon matches the context."""
        plugins_file = generated_project / "test_plugin" / "plugins.py"
        content = plugins_file.read_text()
        
        # Default context uses puzzle-piece icon
        assert 'icon="puzzle-piece"' in content


class TestPluginRegistration:
    """Test that plugin registration is correct."""

    def test_register_decorator_present(self, generated_project):
        """Test that @plugins.register decorator is present."""
        plugins_file = generated_project / "test_plugin" / "plugins.py"
        content = plugins_file.read_text()
        
        assert '@plugins.register(' in content

    def test_register_decorator_has_correct_models(self, generated_project):
        """Test that decorator registers to correct models."""
        plugins_file = generated_project / "test_plugin" / "plugins.py"
        
        # Parse the file to find the decorator
        tree = ast.parse(plugins_file.read_text())
        
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef) and node.name == "TestPlugin":
                # Find the decorator
                for decorator in node.decorator_list:
                    if isinstance(decorator, ast.Call):
                        if hasattr(decorator.func, 'attr') and decorator.func.attr == 'register':
                            # Check that it has arguments (models)
                            assert len(decorator.args) > 0, "No models registered"
                            return
        
        pytest.fail("@plugins.register decorator not found")

    def test_only_selected_models_imported(self, minimal_project):
        """Test that only selected models are imported."""
        plugins_file = minimal_project / "minimal_plugin" / "plugins.py"
        content = plugins_file.read_text()
        
        # Minimal context only registers to Project
        assert "from fairdm.core.project.models import Project" in content
        
        # Should NOT import other models
        assert "from fairdm.core.dataset.models import Dataset" not in content
        assert "from fairdm.core.sample.models import Sample" not in content
        assert "from fairdm.core.measurement.models import Measurement" not in content


class TestAppConfig:
    """Test Django app configuration."""

    def test_app_config_name_matches_plugin(self, generated_project):
        """Test that AppConfig name matches plugin slug."""
        apps_file = generated_project / "test_plugin" / "apps.py"
        content = apps_file.read_text()
        
        assert 'name = "test_plugin"' in content

    def test_app_config_imports_plugins_in_ready(self, generated_project):
        """Test that ready() method imports plugins."""
        apps_file = generated_project / "test_plugin" / "apps.py"
        content = apps_file.read_text()
        
        # Parse to find ready method
        tree = ast.parse(content)
        
        ready_method_found = False
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == "ready":
                ready_method_found = True
                break
        
        assert ready_method_found, "ready() method not found in apps.py"


class TestTemplateStructure:
    """Test template structure and content."""

    def test_template_name_matches_plugin_slug(self, generated_project):
        """Test that template filename matches plugin slug."""
        template_path = generated_project / "test_plugin" / "templates" / "test_plugin" / "test_plugin.html"
        assert template_path.exists()

    def test_template_uses_bootstrap(self, generated_project):
        """Test that template uses Bootstrap classes."""
        template_file = generated_project / "test_plugin" / "templates" / "test_plugin" / "test_plugin.html"
        content = template_file.read_text()
        
        # Should use Bootstrap classes
        assert 'class="' in content
        # Common Bootstrap classes
        bootstrap_present = any(cls in content for cls in ['card', 'container', 'row', 'col'])
        assert bootstrap_present, "No Bootstrap classes found in template"

    def test_template_accesses_base_object(self, generated_project):
        """Test that template accesses base_object variable."""
        template_file = generated_project / "test_plugin" / "templates" / "test_plugin" / "test_plugin.html"
        content = template_file.read_text()
        
        assert "base_object" in content


class TestTestSuite:
    """Test that the generated test suite is valid."""

    def test_conftest_is_valid_python(self, generated_project):
        """Test that conftest.py is valid Python."""
        conftest_file = generated_project / "tests" / "conftest.py"
        content = conftest_file.read_text()
        
        try:
            ast.parse(content)
        except SyntaxError as e:
            pytest.fail(f"tests/conftest.py has invalid Python syntax: {e}")

    def test_test_apps_is_valid_python(self, generated_project):
        """Test that test_apps.py is valid Python."""
        test_file = generated_project / "tests" / "test_apps.py"
        content = test_file.read_text()
        
        try:
            ast.parse(content)
        except SyntaxError as e:
            pytest.fail(f"tests/test_apps.py has invalid Python syntax: {e}")

    def test_test_plugins_is_valid_python(self, generated_project):
        """Test that test_plugins.py is valid Python."""
        test_file = generated_project / "tests" / "test_plugins.py"
        content = test_file.read_text()
        
        try:
            ast.parse(content)
        except SyntaxError as e:
            pytest.fail(f"tests/test_plugins.py has invalid Python syntax: {e}")

    def test_test_plugins_uses_parametrize(self, generated_project):
        """Test that test_plugins.py uses parametrization for models."""
        test_file = generated_project / "tests" / "test_plugins.py"
        content = test_file.read_text()
        
        # Should use pytest.mark.parametrize for testing different models
        assert "@pytest.mark.parametrize" in content
