from functools import lru_cache
from typing import List, Tuple

import aoc

data = """r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb"""

data = aoc.get_data_from_file(19, 2024)


@lru_cache(maxsize=None)
def check_design(desired_design: str):
    if desired_design == "":
        return 1

    result = 0
    for pattern in patterns:
        if desired_design.startswith(pattern):
            result += check_design(desired_design[len(pattern) :])
    return result


def parse_data(data: str) -> Tuple[List[str], List[str]]:
    patterns, designs = data.split("\n\n")
    return patterns.split(", "), designs.splitlines()


@aoc.part(1)
def part_1() -> int:
    possible = 0
    for design in designs:
        if check_design(design):
            possible += 1
    return possible


@aoc.part(2)
def part_2() -> int:
    possible = 0
    for design in designs:
        possible += check_design(design)
    return possible


def main():
    global patterns
    global designs
    patterns, designs = parse_data(data)
    print(part_1())
    print(part_2())


if __name__ == "__main__":
    main()
