from functools import lru_cache
from itertools import chain
from typing import List
import aoc

data = """125 17"""

data = aoc.get_data_from_file(11, 2024)


def blink(numbers: List[int]):
    for i, n in enumerate(numbers):
        if n == 0:
            numbers[i] = [1]
        elif has_even_number_of_digits(n):
            numbers[i] = split_number(n)
        else:
            numbers[i] = [n * 2024]
    return list(chain(*numbers))


@lru_cache(maxsize=None)
def blink_v2(number: int, n_blinks: int) -> int:
    while n_blinks > 0:
        n_blinks -= 1
        if number == 0:
            number = 1
        elif has_even_number_of_digits(number):
            left, right = split_number(number)
            return blink_v2(left, n_blinks) + blink_v2(right, n_blinks)
        else:
            number *= 2024
    return 1


def has_even_number_of_digits(n: int):
    return len(str(n)) % 2 == 0


def split_number(n: int) -> List[int]:
    mid = len(n_str := str(n)) // 2
    return [int(n_str[:mid]), int(n_str[mid:])]


def parse_data(data: str) -> List[int]:
    return list(map(int, data.split(" ")))


@aoc.part(1)
def part_1() -> int:
    numbers = parse_data(data)
    for _ in range(25):
        numbers = blink(numbers)
    return len(numbers)


@aoc.part(2)
def part_2() -> int:
    numbers = parse_data(data)
    result = 0
    for number in numbers:
        result += blink_v2(number, 75)
    return result


def main():
    print(part_1())
    print(part_2())


if __name__ == "__main__":
    main()
