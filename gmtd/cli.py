"""Give Me the Docs's command-line interface"""

from argparse import ArgumentParser
from importlib.metadata import PackageNotFoundError
from sys import exit
from webbrowser import open as open_url

from colorama import Fore, Style, init

from . import __version__, get_documentation

ERROR_STYLE = Style.BRIGHT + Fore.RED


def main() -> None:
    """Main entry point for the CLI"""

    init()

    parser = ArgumentParser(
        prog="gmtd",
        description="Give Me the Docs finds the docs for Python packages so "
        f"you don't have to. (v{__version__})",
    )
    parser.add_argument(
        "package", help="get the documentation links for a package", type=str
    )
    parser.add_argument(
        "-o",
        "--open",
        action="store_true",
        help="open the first result in your browser",
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

        if args.open:
            open_url(urls[0])
    else:
        print(
            ERROR_STYLE
            + f"No documentation found for {package}"
            + Style.RESET_ALL
        )


if __name__ == "__main__":
    main()
