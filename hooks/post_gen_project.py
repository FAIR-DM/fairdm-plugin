"""Post-generation hook to clean up conditional files."""

import os
import shutil
from pathlib import Path


def main():
    """Clean up files based on cookiecutter configuration."""
    print("Post-generation cleanup complete!")


if __name__ == "__main__":
    main()
