"""Give Me the Docs's command-line interface"""

from argparse import ArgumentParser
from importlib.metadata import PackageNotFoundError
from sys import exit

from colorama import Fore, Style, init

from . import __version__, get_documentation

ERROR_STYLE = Style.BRIGHT + Fore.RED


def main():
    """Main entry point for the CLI"""

    init()

    parser = ArgumentParser(
        prog="gmtds",
        description="Give Me the Docs finds the docs for Python packages so "
        f"you don't have to. (v{__version__})",
    )
    parser.add_argument(
        "package", help="get the documentation links for a package", type=str
    )
    args = parser.parse_args()

    package = args.package

    try:
        urls = get_documentation(package)
    except PackageNotFoundError:
        print(ERROR_STYLE + f"Package {package} not found" + Style.RESET_ALL)
        exit(1)

    if urls:
        print(
            Fore.GREEN
            + f"Found documentation for {package}:\n"
            + Style.RESET_ALL
        )

        for url in urls:
            print("    - " + Fore.BLUE + url + Style.RESET_ALL)
    else:
        print(
            ERROR_STYLE
            + f"No documentation found for {package}"
            + Style.RESET_ALL
        )


if __name__ == "__main__":
    main()