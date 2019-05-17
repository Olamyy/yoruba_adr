# -*- coding: utf-8 -*-

"""Console script for yoruba_adr."""
import sys
import click


@click.command()
def main(args=None):
    """Console script for yoruba_adr."""
    click.echo("Replace this message by putting your code into "
               "yoruba_adr.cli.main")
    click.echo("See click documentation at http://click.pocoo.org/")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
