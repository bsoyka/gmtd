"""Give Me the Docs finds documentation links for Python packages so you don't have to."""

from enum import Enum
from importlib.metadata import metadata
from typing import Dict, List, Tuple

import click
from loguru import logger

__version__ = "1.0.0b1"


def _get_package_metadata(package: str) -> Dict[str, str]:
    """Get a package's metadata in a parsable format"""

    return metadata(package).json


def get_documentation(package: str) -> List[str]:
    """Get the documentation URL for a package"""

    package_metadata = _get_package_metadata(package)

    results = []

    # Try project URLs for documentation link first
    if "project_url" in package_metadata:
        for url_string in package_metadata["project_url"]:
            if url_string.lower().startswith("documentation"):
                results.append(url_string.split(",")[1].strip())

    if "home_page" in package_metadata:
        results.append(package_metadata["home_page"])

    return results
