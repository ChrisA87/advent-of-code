from typing import Tuple
from itertools import product

import numpy as np
import aoc

data = """#####
.####
.####
.####
.#.#.
.#...
.....

#####
##.##
.#.##
...##
...#.
...#.
.....

.....
#....
#....
#...#
#.#.#
#.###
#####

.....
.....
#.#..
###..
###.#
###.#
#####

.....
.....
.....
#....
#.#..
#.#.#
#####"""

data = aoc.get_data_from_file(25, 2024)


def parse_data(data: str) -> Tuple[np.ndarray, np.ndarray]:
    keys = []
    locks = []
    for chunk in data.split("\n\n"):
        if chunk[0] == "#":
            locks.append(chunk_to_array(chunk))
        else:
            keys.append(chunk_to_array(chunk))
    return keys, locks


def chunk_to_array(chunk: str):
    return (np.array([list(line) for line in chunk.splitlines()]) == "#").astype(int)


@aoc.part(1)
def part_1() -> int:
    keys, locks = parse_data(data)
    result = 0
    for key, lock in product(keys, locks):
        if np.all((key + lock) <= 1):
            result += 1
    return result


@aoc.part(2)
def part_2() -> int:
    pass


def main():
    print(part_1())
    print(part_2())


if __name__ == "__main__":
    main()
