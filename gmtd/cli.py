"""Give Me the Docs's command-line interface"""

from importlib.metadata import PackageNotFoundError
from sys import exit

import click

from . import __version__, get_documentation


@click.command()
@click.help_option("-h", "--help")
@click.version_option(__version__, "-v", "--version", prog_name="Give Me the Docs")
@click.argument("package", required=True)
def main(package: str):
    """Get the documentation link for PACKAGE"""

    try:
        urls = get_documentation(package)
    except PackageNotFoundError:
        click.echo(
            click.style(f"Package {package} not found", fg="red", bold=True)
        )
        exit(1)

    if urls:
        click.echo(
            click.style(f"Found documentation for {package}:\n", fg="green")
        )

        for url in urls:
            click.echo(click.style(f"    - {url}", fg="blue"))
    else:
        click.echo(
            click.style(
                f"No documentation found for {package}", fg="red", bold=True
            )
        )


if __name__ == "__main__":
    main()
