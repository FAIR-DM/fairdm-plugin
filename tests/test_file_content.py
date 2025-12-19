"""Test that generated file contents are correct."""

import ast
import json5
import tomllib

import pytest


class TestPythonFiles:
    """Test that Python files have correct content and are valid."""

    def test_plugins_file_is_valid_python(self, generated_project):
        """Test that plugins.py is valid Python code."""
        plugins_file = generated_project / "test_plugin" / "plugins.py"
        content = plugins_file.read_text()
        
        # Should be valid Python
        try:
            ast.parse(content)
        except SyntaxError as e:
            pytest.fail(f"plugins.py has invalid Python syntax: {e}")

    def test_plugins_file_has_correct_template_name(self, generated_project):
        """Test that plugins.py references the correctly named template."""
        plugins_file = generated_project / "test_plugin" / "plugins.py"
        content = plugins_file.read_text()
        
        # Should reference test_plugin/test_plugin.html, not plugin.html
        assert 'template_name = "test_plugin/test_plugin.html"' in content
        assert 'template_name = "test_plugin/plugin.html"' not in content

    def test_plugins_file_has_correct_registration(self, generated_project):
        """Test that @plugins.register decorator has correct models."""
        plugins_file = generated_project / "test_plugin" / "plugins.py"
        content = plugins_file.read_text()
        
        # Default context has project and dataset
        assert "@plugins.register" in content
        assert "Project" in content
        assert "Dataset" in content

    def test_apps_file_is_valid_python(self, generated_project):
        """Test that apps.py is valid Python code."""
        apps_file = generated_project / "test_plugin" / "apps.py"
        content = apps_file.read_text()
        
        try:
            ast.parse(content)
        except SyntaxError as e:
            pytest.fail(f"apps.py has invalid Python syntax: {e}")

    def test_apps_file_imports_plugins(self, generated_project):
        """Test that apps.py imports plugins in ready() method."""
        apps_file = generated_project / "test_plugin" / "apps.py"
        content = apps_file.read_text()
        
        assert "def ready(self):" in content
        assert "from . import plugins" in content

    def test_init_file_has_version(self, generated_project):
        """Test that __init__.py defines __version__."""
        init_file = generated_project / "test_plugin" / "__init__.py"
        content = init_file.read_text()
        
        assert '__version__' in content
        assert '0.1.0' in content

    def test_conftest_has_fixtures(self, generated_project):
        """Test that tests/conftest.py has the expected fixtures."""
        conftest_file = generated_project / "tests" / "conftest.py"
        content = conftest_file.read_text()
        
        # Should have fixtures for FairDM models
        assert "def project(" in content
        assert "def dataset(" in content
        assert "def sample(" in content
        assert "def measurement(" in content


class TestTemplateFiles:
    """Test that template files are correct."""

    def test_main_template_extends_fairdm_plugin(self, generated_project):
        """Test that the main template extends fairdm/plugin.html."""
        template_file = generated_project / "test_plugin" / "templates" / "test_plugin" / "test_plugin.html"
        content = template_file.read_text()
        
        assert '{% extends "fairdm/plugin.html" %}' in content

    def test_main_template_has_plugin_block(self, generated_project):
        """Test that the main template defines the plugin block."""
        template_file = generated_project / "test_plugin" / "templates" / "test_plugin" / "test_plugin.html"
        content = template_file.read_text()
        
        assert '{% block plugin %}' in content
        assert '{% endblock %}' in content

    def test_main_template_mentions_base_object(self, generated_project):
        """Test that the template references base_object."""
        template_file = generated_project / "test_plugin" / "templates" / "test_plugin" / "test_plugin.html"
        content = template_file.read_text()
        
        assert 'base_object' in content


class TestConfigurationFiles:
    """Test that configuration files are valid."""

    def test_pyproject_toml_is_valid(self, generated_project):
        """Test that pyproject.toml is valid TOML."""
        pyproject_file = generated_project / "pyproject.toml"
        
        try:
            with open(pyproject_file, "rb") as f:
                data = tomllib.load(f)
        except Exception as e:
            pytest.fail(f"pyproject.toml is invalid TOML: {e}")
        
        # Check basic structure
        assert "tool" in data
        assert "poetry" in data["tool"]
        assert "name" in data["tool"]["poetry"]
        assert data["tool"]["poetry"]["name"] == "test-plugin"

    def test_pyproject_has_correct_dependencies(self, generated_project):
        """Test that pyproject.toml has required dependencies."""
        pyproject_file = generated_project / "pyproject.toml"
        
        with open(pyproject_file, "rb") as f:
            data = tomllib.load(f)
        
        deps = data["tool"]["poetry"]["dependencies"]
        
        # Should have Python version constraint
        assert "python" in deps
        assert "^3.11" in deps["python"]
        
        # Should have Django
        assert "django" in deps

    def test_pyproject_has_dev_dependencies(self, generated_project):
        """Test that pyproject.toml has dev dependencies."""
        pyproject_file = generated_project / "pyproject.toml"
        
        with open(pyproject_file, "rb") as f:
            data = tomllib.load(f)
        
        # Dev dependencies should be from fairdm-dev-tools
        assert "group" in data["tool"]["poetry"]
        assert "dev" in data["tool"]["poetry"]["group"]

    def test_vscode_workspace_is_valid_json(self, generated_project):
        """Test that VSCode workspace file is valid JSON."""
        workspace_file = generated_project / "test_plugin.code-workspace"
        
        try:
            with open(workspace_file) as f:
                data = json5.load(f)
        except Exception as e:
            pytest.fail(f"VSCode workspace file is invalid JSONC: {e}")
        
        # Check basic structure
        assert "folders" in data
        assert "settings" in data
        assert "extensions" in data
        assert "launch" in data

    def test_vscode_workspace_has_recommendations(self, generated_project):
        """Test that VSCode workspace has extension recommendations."""
        workspace_file = generated_project / "test_plugin.code-workspace"
        
        with open(workspace_file) as f:
            data = json5.load(f)
        
        recommendations = data["extensions"]["recommendations"]
        
        # Should recommend essential extensions
        assert "ms-python.python" in recommendations
        assert "charliermarsh.ruff" in recommendations
        assert "batisteo.vscode-django" in recommendations

    def test_gitignore_excludes_common_files(self, generated_project):
        """Test that .gitignore excludes common Python/Django files."""
        gitignore_file = generated_project / ".gitignore"
        content = gitignore_file.read_text()
        
        assert "__pycache__" in content
        assert "*.py[cod]" in content
        assert ".venv" in content
        assert "db.sqlite3" in content

    def test_codecov_yaml_is_valid(self, generated_project):
        """Test that codecov.yml is present and valid YAML."""
        codecov_file = generated_project / "codecov.yml"
        assert codecov_file.exists()
        
        # Basic YAML syntax check
        import yaml
        try:
            with open(codecov_file) as f:
                data = yaml.safe_load(f)
        except yaml.YAMLError as e:
            pytest.fail(f"codecov.yml is invalid YAML: {e}")
        
        assert "coverage" in data


class TestDocumentation:
    """Test that documentation files are properly generated."""

    def test_readme_has_plugin_name(self, generated_project):
        """Test that README.md contains the plugin name."""
        readme_file = generated_project / "README.md"
        content = readme_file.read_text()
        
        assert "Test Plugin" in content

    def test_readme_has_installation_instructions(self, generated_project):
        """Test that README.md has installation instructions."""
        readme_file = generated_project / "README.md"
        content = readme_file.read_text()
        
        assert "Installation" in content
        assert "poetry add" in content or "fairdm.setup" in content

    def test_contributing_has_guidelines(self, generated_project):
        """Test that CONTRIBUTING.md exists and has content."""
        contributing_file = generated_project / "CONTRIBUTING.md"
        content = contributing_file.read_text()
        
        assert "Contributing" in content or "contribute" in content.lower()

    def test_changelog_exists(self, generated_project):
        """Test that CHANGELOG.md exists."""
        changelog_file = generated_project / "CHANGELOG.md"
        assert changelog_file.exists()
        
        content = changelog_file.read_text()
        assert "0.1.0" in content


class TestGitHubFiles:
    """Test that GitHub-specific files are correct."""

    def test_bug_report_template_is_valid_yaml(self, generated_project):
        """Test that bug report template is valid YAML."""
        bug_report = generated_project / ".github" / "ISSUE_TEMPLATE" / "bug_report.yml"
        
        import yaml
        try:
            with open(bug_report) as f:
                data = yaml.safe_load(f)
        except yaml.YAMLError as e:
            pytest.fail(f"bug_report.yml is invalid YAML: {e}")
        
        assert "name" in data
        assert "body" in data

    def test_github_workflow_is_valid_yaml(self, generated_project):
        """Test that GitHub Actions workflow is valid YAML."""
        workflow = generated_project / ".github" / "workflows" / "tests.yml"
        
        import yaml
        try:
            with open(workflow) as f:
                data = yaml.safe_load(f)
        except yaml.YAMLError as e:
            pytest.fail(f"tests.yml is invalid YAML: {e}")
        
        assert "name" in data
        # PyYAML parses 'on' as boolean True
        assert ("on" in data or True in data)
        assert "jobs" in data

    def test_workflow_tests_multiple_python_versions(self, generated_project):
        """Test that workflow tests multiple Python versions."""
        workflow = generated_project / ".github" / "workflows" / "tests.yml"
        
        import yaml
        with open(workflow) as f:
            data = yaml.safe_load(f)
        
        # Should have a matrix strategy
        jobs = data["jobs"]
        test_job = jobs["test"]
        
        assert "strategy" in test_job
        assert "matrix" in test_job["strategy"]
        assert "python-version" in test_job["strategy"]["matrix"]
