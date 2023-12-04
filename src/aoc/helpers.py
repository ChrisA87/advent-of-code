import os
import requests
from pathlib import Path
from datetime import datetime
from functools import wraps

SESSION_ID = os.environ["AOC_SESSION"]
BASE_URL = "https://adventofcode.com/{}/day/{}/input"
ROOT = Path(__file__).parent


def get_year(file):
    return Path(file).parent.name


def get_input_data(day: int, year: int = datetime.today().year) -> str:
    url = BASE_URL.format(year, day)
    res = requests.get(url, headers={"cookie": SESSION_ID})
    data = res.content.decode().rstrip()
    if res.status_code == 200:
        return data
    raise requests.HTTPError(data)


def get_data_from_file(day: int, year: int = datetime.today().year):
    try:
        return ROOT.joinpath(f"{year}/data/{day:0>2}.txt").read_text()
    except FileNotFoundError:
        return (
            f"Could not find data for day {day}, {year} locally. Try running:\n   "
            f"aoc data {day}"
        )


def part(number):
    def decorate(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return f"Part {number}: {func(*args, **kwargs)}"

        return wrapper

    return decorate
