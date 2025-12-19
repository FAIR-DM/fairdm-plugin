"""
Pytest configuration and fixtures for {{ cookiecutter.plugin_name }} tests.

This file contains reusable pytest fixtures that can be used across all test files.
"""

import pytest
from fairdm.factories import (
    DatasetFactory,
    MeasurementFactory,
    ProjectFactory,
    SampleFactory,
    UserFactory,
)


@pytest.fixture
def user():
    """Create a test user."""
    return UserFactory()


@pytest.fixture
def project():
    """Create a test project."""
    return ProjectFactory()


@pytest.fixture
def dataset(project):
    """Create a test dataset."""
    return DatasetFactory(project=project)


@pytest.fixture
def sample(dataset):
    """Create a test sample."""
    return SampleFactory(dataset=dataset)


@pytest.fixture
def measurement(sample):
    """Create a test measurement."""
    return MeasurementFactory(sample=sample)


# Add your plugin-specific fixtures here
# Example:
# @pytest.fixture
# def my_plugin_data():
#     """Create test data for my plugin."""
#     return {"key": "value"}
