from collections import defaultdict, namedtuple
from itertools import combinations
from typing import Dict, List, Tuple
import aoc

data = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""

data = aoc.get_data_from_file(8)

Position = namedtuple("Position", ["x", "y"])


def parse_antena_positions(data: str) -> Dict[str, List[Tuple[int, int]]]:
    result = defaultdict(list)
    for i, line in enumerate(data):
        for j, val in enumerate(line):
            if val != ".":
                result[val].append(Position(i, j))
    return result


def generate_antena_pairs(antena_positions: List[Tuple[int, int]]):
    yield from combinations(antena_positions, 2)


def is_valid(antinode: Position):
    return (0 <= antinode.x < ROWS) and (0 <= antinode.y < COLS)


def get_valid_antinodes(position1: Position, position2: Position):
    x_diff = position2.x - position1.x
    y_diff = position2.y - position1.y
    antinode1 = Position(position1.x - x_diff, position1.y - y_diff)
    antinode2 = Position(position2.x + x_diff, position2.y + y_diff)
    return [antinode for antinode in [antinode1, antinode2] if is_valid(antinode)]


@aoc.part(1)
def part_1(antena_positions: Dict[str, List[Tuple[int, int]]]) -> int:
    antinodes = set()
    for positions in antena_positions.values():
        for pairs in generate_antena_pairs(positions):
            antinodes.update(get_valid_antinodes(*pairs))
    return len(antinodes)


@aoc.part(2)
def part_2(antena_positions: Dict[str, List[Tuple[int, int]]]) -> int:
    pass


def main():
    lines = data.splitlines()
    global ROWS
    global COLS
    ROWS = len(lines)
    COLS = len(lines[0])

    antena_postitions = parse_antena_positions(lines)

    print(part_1(antena_postitions))
    print(part_2(antena_postitions))


if __name__ == "__main__":
    main()
