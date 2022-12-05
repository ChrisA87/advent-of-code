import os
import requests

SESSION_ID = os.environ['AOC_SESSION']
BASE_URL = 'https://adventofcode.com/{}/day/{}/input'

def get_input_data(day, year=2022):
    url = BASE_URL.format(year, day)
    res = requests.get(url, headers={'cookie': SESSION_ID})
    data = res.content.decode().rstrip()
    if res.status_code == 200:
        return data
    raise requests.HTTPError(data)
