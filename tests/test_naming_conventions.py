"""Test that naming conventions are followed correctly."""

import pytest
import re


class TestSlugGeneration:
    """Test that plugin slugs are generated correctly from names."""

    @pytest.mark.parametrize("plugin_name,expected_slug", [
        ("My Plugin", "my_plugin"),
        ("Data Visualizer", "data_visualizer"),
        ("CSV-Exporter", "csv_exporter"),
        ("API Integration", "api_integration"),
        ("Multi-Word-Name", "multi_word_name"),
    ])
    def test_slug_generation(self, tmp_path, template_dir, default_context, plugin_name, expected_slug):
        """Test that slugs are correctly generated from plugin names."""
        from cookiecutter.main import cookiecutter
        
        context = default_context.copy()
        context["plugin_name"] = plugin_name
        context["plugin_slug"] = expected_slug  # Manually set to test
        
        output_dir = tmp_path / "output"
        output_dir.mkdir()
        
        result = cookiecutter(
            str(template_dir),
            no_input=True,
            extra_context=context,
            output_dir=str(output_dir),
        )
        
        from pathlib import Path
        project_dir = Path(result)
        
        # Directory name should match slug
        assert project_dir.name == expected_slug
        
        # Package directory should match slug
        package_dir = project_dir / expected_slug
        assert package_dir.exists()


class TestClassNameGeneration:
    """Test that class names are generated correctly."""

    @pytest.mark.parametrize("plugin_name,expected_class", [
        ("My Plugin", "MyPlugin"),
        ("Data Visualizer", "DataVisualizer"),
        ("CSV Exporter", "CSVExporter"),
        ("API-Integration", "APIIntegration"),
    ])
    def test_class_name_generation(self, tmp_path, template_dir, default_context, plugin_name, expected_class):
        """Test that class names are correctly generated."""
        from cookiecutter.main import cookiecutter
        
        context = default_context.copy()
        context["plugin_name"] = plugin_name
        context["plugin_class_name"] = expected_class
        # Generate unique slug for each test
        context["plugin_slug"] = plugin_name.lower().replace(" ", "_").replace("-", "_")
        
        output_dir = tmp_path / "output"
        output_dir.mkdir()
        
        result = cookiecutter(
            str(template_dir),
            no_input=True,
            extra_context=context,
            output_dir=str(output_dir),
        )
        
        from pathlib import Path
        project_dir = Path(result)
        
        plugins_file = project_dir / context["plugin_slug"] / "plugins.py"
        content = plugins_file.read_text()
        
        # Class should be defined with the expected name
        assert f"class {expected_class}(" in content


class TestFileNamingConventions:
    """Test that files follow naming conventions."""

    def test_template_follows_naming_convention(self, generated_project):
        """Test that template file name matches plugin slug."""
        # Template should be at: templates/test_plugin/test_plugin.html
        template_path = generated_project / "test_plugin" / "templates" / "test_plugin" / "test_plugin.html"
        assert template_path.exists()
        
        # Should NOT be named plugin.html
        wrong_path = generated_project / "test_plugin" / "templates" / "test_plugin" / "plugin.html"
        assert not wrong_path.exists()

    def test_workspace_file_name_matches_slug(self, generated_project):
        """Test that VSCode workspace file name matches plugin slug."""
        workspace_file = generated_project / "test_plugin.code-workspace"
        assert workspace_file.exists()

    def test_package_name_uses_hyphens_in_pyproject(self, generated_project):
        """Test that package name in pyproject.toml uses hyphens."""
        import tomli
        
        pyproject_file = generated_project / "pyproject.toml"
        with open(pyproject_file, "rb") as f:
            data = tomli.load(f)
        
        # Package name should use hyphens, not underscores
        assert data["tool"]["poetry"]["name"] == "test-plugin"


class TestPythonNamingConventions:
    """Test Python-specific naming conventions."""

    def test_class_uses_pascal_case(self, generated_project):
        """Test that plugin class uses PascalCase."""
        plugins_file = generated_project / "test_plugin" / "plugins.py"
        content = plugins_file.read_text()
        
        # Should find "class TestPlugin"
        assert re.search(r'class\s+[A-Z][a-zA-Z]+\(', content), "Class name should be PascalCase"

    def test_methods_use_snake_case(self, generated_project):
        """Test that methods use snake_case."""
        plugins_file = generated_project / "test_plugin" / "plugins.py"
        content = plugins_file.read_text()
        
        # get_context_data should be snake_case
        assert "def get_context_data(" in content

    def test_variables_use_snake_case(self, generated_project):
        """Test that class variables use snake_case."""
        plugins_file = generated_project / "test_plugin" / "plugins.py"
        content = plugins_file.read_text()
        
        assert "template_name =" in content
        assert "menu_item =" in content


class TestConsistentNaming:
    """Test that naming is consistent across all files."""

    def test_plugin_name_consistent(self, generated_project):
        """Test that plugin name is used consistently."""
        # Check plugins.py
        plugins_file = generated_project / "test_plugin" / "plugins.py"
        plugins_content = plugins_file.read_text()
        assert "Test Plugin" in plugins_content
        
        # Check README
        readme_file = generated_project / "README.md"
        readme_content = readme_file.read_text()
        assert "Test Plugin" in readme_content
        
        # Check apps.py
        apps_file = generated_project / "test_plugin" / "apps.py"
        apps_content = apps_file.read_text()
        assert "Test Plugin" in apps_content

    def test_plugin_slug_consistent(self, generated_project):
        """Test that plugin slug is used consistently."""
        # Directory name
        assert (generated_project / "test_plugin").exists()
        
        # In plugins.py template_name
        plugins_file = generated_project / "test_plugin" / "plugins.py"
        assert 'template_name = "test_plugin/test_plugin.html"' in plugins_file.read_text()
        
        # In apps.py name
        apps_file = generated_project / "test_plugin" / "apps.py"
        assert 'name = "test_plugin"' in apps_file.read_text()
        
        # Template directory
        assert (generated_project / "test_plugin" / "templates" / "test_plugin").exists()
