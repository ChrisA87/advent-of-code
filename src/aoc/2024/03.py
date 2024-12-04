from typing import List, Tuple
import re

import aoc

data = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
data = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
data = aoc.get_data_from_file(3)


def get_mul_tuples(data: str) -> List[Tuple[int, int]]:
    pattern = re.compile(r"mul\((\d{1,3},\d{1,3})\)")
    matches = pattern.findall(data)
    return [parse_numbers(match) for match in matches]


def parse_numbers(numbers: str) -> Tuple[int, int]:
    return tuple(map(int, numbers.split(",")))

def remove_dont_sequences(data: str) -> str:
    return re.sub(r"(don't\(\).*?)(do\(\))", "$2", data)

@aoc.part(1)
def part_1() -> int:
    mul_tuples = get_mul_tuples(data)
    return sum(a * b for a, b in mul_tuples)


@aoc.part(2)
def part_2() -> int:
    mul_tuples = get_mul_tuples(remove_dont_sequences(data.replace("\n", "")))
    return sum(a * b for a, b in mul_tuples)


def main():
    print(part_1())
    print(part_2())


if __name__ == "__main__":
    main()
