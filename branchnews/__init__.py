__version__ = '0.2.0-dev'

import click

from .create import main as create_cmd
from .rename import main as rename_cmd


@click.group()
def cli():
    pass


cli.add_command(create_cmd)
cli.add_command(rename_cmd)
