"""Post-generation hook to clean up conditional files."""

import os
import shutil
from pathlib import Path


def remove_file_if_exists(filepath):
    """Remove a file if it exists."""
    if os.path.exists(filepath):
        os.remove(filepath)
        print(f"Removed: {filepath}")


def main():
    """Clean up files based on cookiecutter configuration."""
    project_slug = "{{ cookiecutter.plugin_slug }}"
    
    # Remove settings.py if not needed
    if "{{ cookiecutter.include_settings }}" == "no":
        settings_file = Path(project_slug) / "settings.py"
        remove_file_if_exists(settings_file)
    
    print("Post-generation cleanup complete!")


if __name__ == "__main__":
    main()
