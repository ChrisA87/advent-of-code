import click
from .data import data
from .run import run


@click.group(context_settings=dict(help_option_names=["-h", "--help"]))
def main():
    """CLI tool for advent of code inputs and solutions."""


main.add_command(data)
main.add_command(run)
