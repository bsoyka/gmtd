"""Give Me the Docs finds documentation links for Python packages so you don't have to."""

from importlib.metadata import metadata
from typing import Dict, List

__version__ = "1.1.0b2"


def _get_package_metadata(package: str) -> Dict[str, str]:
    """Gets a package's metadata in a parsable format.

    Args:
        package: The name of the package to get metadata for.

    Returns:
        A dictionary of the package's metadata.

    Raises:
        PackageNotFoundError: If the package is not installed.
    """

    return metadata(package).json


def get_documentation(package: str) -> List[str]:
    """Gets the documentation URL for a package.

    Args:
        package: The name of the package to get documentation for.

    Returns:
        A list of possible documentation URLs for the package, ordered
        from most to least likely to be official documentation.

    Raises:
        PackageNotFoundError: If the package is not installed.
    """

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
