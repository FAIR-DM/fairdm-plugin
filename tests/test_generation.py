"""Test basic cookiecutter template generation."""

import pytest
from pathlib import Path


class TestBasicGeneration:
    """Test that the cookiecutter generates the expected files and directories."""

    def test_project_directory_created(self, generated_project):
        """Test that the project directory is created."""
        assert generated_project.exists()
        assert generated_project.is_dir()
        assert generated_project.name == "test_plugin"

    def test_package_directory_structure(self, generated_project):
        """Test that the package directory structure is correct."""
        package_dir = generated_project / "test_plugin"
        assert package_dir.exists()
        assert package_dir.is_dir()

        # Check core Python files
        assert (package_dir / "__init__.py").exists()
        assert (package_dir / "apps.py").exists()
        assert (package_dir / "plugins.py").exists()

    def test_templates_directory_structure(self, generated_project):
        """Test that templates are structured correctly."""
        templates_dir = generated_project / "test_plugin" / "templates" / "test_plugin"
        assert templates_dir.exists()
        
        # Check that the main template exists with correct naming
        main_template = templates_dir / "test_plugin.html"
        assert main_template.exists()
        assert main_template.is_file()

    def test_no_cotton_sections_directory(self, generated_project):
        """Test that cotton/sections directory is not created."""
        cotton_dir = generated_project / "test_plugin" / "templates" / "cotton"
        assert not cotton_dir.exists()

    def test_no_templatetags_directory(self, generated_project):
        """Test that templatetags directory is not created."""
        templatetags_dir = generated_project / "test_plugin" / "templatetags"
        assert not templatetags_dir.exists()

    def test_no_urls_file(self, generated_project):
        """Test that urls.py is not created."""
        urls_file = generated_project / "test_plugin" / "urls.py"
        assert not urls_file.exists()

    def test_tests_directory_structure(self, generated_project):
        """Test that test directory is structured correctly."""
        tests_dir = generated_project / "tests"
        assert tests_dir.exists()
        
        assert (tests_dir / "__init__.py").exists()
        assert (tests_dir / "conftest.py").exists()
        assert (tests_dir / "test_apps.py").exists()
        assert (tests_dir / "test_plugins.py").exists()
        assert (tests_dir / "README.md").exists()

    def test_github_directory_structure(self, generated_project):
        """Test that .github directory is structured correctly."""
        github_dir = generated_project / ".github"
        assert github_dir.exists()
        
        # Instructions
        assert (github_dir / "instructions" / "copilot.instructions.md").exists()
        assert (github_dir / "instructions" / "testing.instructions.md").exists()
        
        # Workflows
        assert (github_dir / "workflows" / "tests.yml").exists()
        
        # Issue templates
        assert (github_dir / "ISSUE_TEMPLATE" / "bug_report.yml").exists()
        assert (github_dir / "ISSUE_TEMPLATE" / "feature_request.yml").exists()
        
        # PR template and dependabot
        assert (github_dir / "pull_request_template.md").exists()
        assert (github_dir / "dependabot.yml").exists()

    def test_root_configuration_files(self, generated_project):
        """Test that root configuration files are present."""
        assert (generated_project / "pyproject.toml").exists()
        assert (generated_project / ".gitignore").exists()
        assert (generated_project / ".pre-commit-config.yaml").exists()
        assert (generated_project / "codecov.yml").exists()

    def test_documentation_files(self, generated_project):
        """Test that documentation files are present."""
        assert (generated_project / "README.md").exists()
        assert (generated_project / "LICENSE").exists()
        assert (generated_project / "CHANGELOG.md").exists()
        assert (generated_project / "CONTRIBUTING.md").exists()

    def test_vscode_workspace_file(self, generated_project):
        """Test that VSCode workspace file is created."""
        workspace_file = generated_project / "test_plugin.code-workspace"
        assert workspace_file.exists()
        assert workspace_file.is_file()


class TestConditionalGeneration:
    """Test that conditional features are generated correctly."""

    def test_settings_file_not_included_by_default(self, generated_project):
        """Test that settings.py is not created when include_settings=no."""
        settings_file = generated_project / "test_plugin" / "settings.py"
        assert not settings_file.exists()

    def test_settings_file_included_when_enabled(self, full_features_project):
        """Test that settings.py is created when include_settings=yes."""
        settings_file = full_features_project / "full_features_plugin" / "settings.py"
        assert settings_file.exists()

    def test_minimal_model_registration(self, minimal_project):
        """Test generation with minimal model registration (project only)."""
        plugins_file = minimal_project / "minimal_plugin" / "plugins.py"
        assert plugins_file.exists()
        
        content = plugins_file.read_text()
        
        # Should import Project
        assert "from fairdm.core.project.models import Project" in content
        
        # Should NOT import other models
        assert "from fairdm.core.dataset.models import Dataset" not in content
        assert "from fairdm.core.sample.models import Sample" not in content
        assert "from fairdm.core.measurement.models import Measurement" not in content

    def test_full_model_registration(self, full_features_project):
        """Test generation with all models registered."""
        plugins_file = full_features_project / "full_features_plugin" / "plugins.py"
        content = plugins_file.read_text()
        
        # Should import all models
        assert "from fairdm.core.project.models import Project" in content
        assert "from fairdm.core.dataset.models import Dataset" in content
        assert "from fairdm.core.sample.models import Sample" in content
        assert "from fairdm.core.measurement.models import Measurement" in content

    def test_waffle_integration_not_included_by_default(self, generated_project):
        """Test that Waffle code is not included when use_waffle=no."""
        plugins_file = generated_project / "test_plugin" / "plugins.py"
        content = plugins_file.read_text()
        
        assert "import waffle" not in content
        assert "waffle.switch_is_active" not in content

    def test_waffle_integration_included_when_enabled(self, full_features_project):
        """Test that Waffle code is included when use_waffle=yes."""
        plugins_file = full_features_project / "full_features_plugin" / "plugins.py"
        content = plugins_file.read_text()
        
        assert "import waffle" in content
        assert "waffle.switch_is_active" in content
        assert 'enable_full_features_plugin' in content


class TestLicenseGeneration:
    """Test that different license files are generated correctly."""

    @pytest.mark.parametrize("license_type", ["MIT", "BSD-3-Clause", "Apache-2.0", "GPL-3.0"])
    def test_license_file_created(self, tmp_path, template_dir, default_context, license_type):
        """Test that license file is created for each license type."""
        context = default_context.copy()
        context["license"] = license_type
        context["plugin_slug"] = f"test_{license_type.lower().replace('-', '_').replace('.', '_')}"
        
        from cookiecutter.main import cookiecutter
        output_dir = tmp_path / "output"
        output_dir.mkdir()
        
        result = cookiecutter(
            str(template_dir),
            no_input=True,
            extra_context=context,
            output_dir=str(output_dir),
        )
        
        project_dir = Path(result)
        license_file = project_dir / "LICENSE"
        
        assert license_file.exists()
        content = license_file.read_text()
        
        # Basic validation that it's not empty
        assert len(content) > 100
        assert "2025" in content or context["author_name"] in content
