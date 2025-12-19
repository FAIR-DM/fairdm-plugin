"""Pytest configuration and fixtures for cookiecutter template tests."""

import shutil
from pathlib import Path

import pytest
from cookiecutter.main import cookiecutter


@pytest.fixture
def default_context():
    """Provide default context for cookiecutter generation."""
    return {
        "plugin_name": "Test Plugin",
        "plugin_slug": "test_plugin",
        "plugin_short_description": "A test plugin for validation",
        "plugin_class_name": "TestPlugin",
        "author_name": "Test Author",
        "author_email": "test@example.com",
        "github_username": "testuser",
        "version": "0.1.0",
        "python_version": "3.11",
        "license": "MIT",
        "register_to_models__project": "yes",
        "register_to_models__dataset": "yes",
        "register_to_models__sample": "no",
        "register_to_models__measurement": "no",
        "plugin_category": "EXPLORE",
        "icon_name": "puzzle-piece",
    }


@pytest.fixture
def minimal_context():
    """Provide minimal context with only required fields."""
    return {
        "plugin_name": "Minimal Plugin",
        "plugin_slug": "minimal_plugin",
        "plugin_short_description": "Minimal test plugin",
        "plugin_class_name": "MinimalPlugin",
        "author_name": "Test Author",
        "author_email": "test@example.com",
        "github_username": "testuser",
        "version": "0.1.0",
        "python_version": "3.11",
        "license": "MIT",
        "register_to_models__project": "yes",
        "register_to_models__dataset": "no",
        "register_to_models__sample": "no",
        "register_to_models__measurement": "no",
        "plugin_category": "ACTIONS",
        "icon_name": "cog",
    }


@pytest.fixture
def full_features_context():
    """Provide context with all optional features enabled."""
    return {
        "plugin_name": "Full Features Plugin",
        "plugin_slug": "full_features_plugin",
        "plugin_short_description": "Plugin with all features enabled",
        "plugin_class_name": "FullFeaturesPlugin",
        "author_name": "Test Author",
        "author_email": "test@example.com",
        "github_username": "testuser",
        "version": "0.1.0",
        "python_version": "3.11",
        "license": "MIT",
        "register_to_models__project": "yes",
        "register_to_models__dataset": "yes",
        "register_to_models__sample": "yes",
        "register_to_models__measurement": "yes",
        "plugin_category": "MANAGEMENT",
        "icon_name": "shield",
    }


@pytest.fixture
def template_dir():
    """Return the path to the cookiecutter template directory."""
    return Path(__file__).parent.parent.resolve()


@pytest.fixture
def generated_project(tmp_path, template_dir, default_context):
    """Generate a project using the cookiecutter template and return its path."""
    output_dir = tmp_path / "output"
    output_dir.mkdir()

    result = cookiecutter(
        str(template_dir),
        no_input=True,
        extra_context=default_context,
        output_dir=str(output_dir),
    )

    project_dir = Path(result)
    yield project_dir

    # Cleanup
    if project_dir.exists():
        shutil.rmtree(project_dir)


@pytest.fixture
def minimal_project(tmp_path, template_dir, minimal_context):
    """Generate a minimal project and return its path."""
    output_dir = tmp_path / "output"
    output_dir.mkdir()

    result = cookiecutter(
        str(template_dir),
        no_input=True,
        extra_context=minimal_context,
        output_dir=str(output_dir),
    )

    project_dir = Path(result)
    yield project_dir

    # Cleanup
    if project_dir.exists():
        shutil.rmtree(project_dir)


@pytest.fixture
def full_features_project(tmp_path, template_dir, full_features_context):
    """Generate a project with all features and return its path."""
    output_dir = tmp_path / "output"
    output_dir.mkdir()

    result = cookiecutter(
        str(template_dir),
        no_input=True,
        extra_context=full_features_context,
        output_dir=str(output_dir),
    )

    project_dir = Path(result)
    yield project_dir

    # Cleanup
    if project_dir.exists():
        shutil.rmtree(project_dir)
