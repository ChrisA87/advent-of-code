import click
from datetime import datetime
from aoc import get_input_data, ROOT


@click.command()
@click.argument("day", required=True, type=int)
@click.argument("year", required=False, type=int, default=datetime.today().year)
@click.option("-p", "--print", is_flag=True, default=False, help="Print data to STDOUT")
def data(day, year, print):
    """Gets AOC input data."""
    data = get_input_data(day, year)
    if print:
        click.echo(data)
        return
    ROOT.joinpath(f"{year}/data/{day:0>2}.txt").write_text(data)
