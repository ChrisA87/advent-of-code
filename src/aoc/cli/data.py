import click
from datetime import datetime
from aoc.helpers import get_input_data


@click.command()
@click.argument("day", required=True, type=int)
@click.argument("year", required=False, type=int, default=datetime.today().year)
def data(day, year):
    """Gets AOC input data."""
    click.echo(get_input_data(day, year))
