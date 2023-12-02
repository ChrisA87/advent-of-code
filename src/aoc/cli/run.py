import click
from datetime import datetime
from importlib import import_module


@click.command()
@click.argument("day", required=True, type=int)
@click.argument("year", required=False, type=int, default=datetime.today().year)
def run(day, year):
    """Runs an AOC solution."""
    try:
        solution_module = import_module(f"aoc.{year}.{day:0>2}")
        getattr(solution_module, "main")()
    except ModuleNotFoundError:
        click.echo(f"No solution found for day {day}, {year}.")
