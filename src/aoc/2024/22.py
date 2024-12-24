from functools import lru_cache
from typing import List
import aoc

data = """1
10
100
2024"""

data = aoc.get_data_from_file(22, 2024)


def parse_data(data: str) -> List[int]:
    return list(map(int, data.splitlines()))


@lru_cache(None)
def mix(n1: int, n2: int) -> int:
    return n1 ^ n2


@lru_cache(None)
def prune(n1: int) -> int:
    return n1 % 16777216


@lru_cache()
def next_secret_number(secret_number: int) -> int:
    secret_number = prune(mix(secret_number, secret_number * 64))
    secret_number = prune(mix(secret_number, secret_number // 32))
    secret_number = prune(mix(secret_number, secret_number * 2048))
    return secret_number


@aoc.part(1)
def part_1() -> int:
    result = 0
    n = 2000
    secret_codes = parse_data(data)
    for secret in secret_codes:
        for _ in range(n):
            secret = next_secret_number(secret)
        result += secret
    return result


@aoc.part(2)
def part_2() -> int:
    pass


def main():
    print(part_1())
    print(part_2())


if __name__ == "__main__":
    main()
