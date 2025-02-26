from collections import defaultdict, namedtuple
from itertools import combinations
from typing import Dict, Generator, List, Set, Tuple
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


def parse_antena_positions(data: str) -> Dict[str, List[Position]]:
    result = defaultdict(list)
    for i, line in enumerate(data):
        for j, val in enumerate(line):
            if val != ".":
                result[val].append(Position(i, j))
    return result


def generate_antena_pairs(
    antena_positions: List[Position],
) -> Generator[Tuple[Position], None, None]:
    yield from combinations(antena_positions, 2)


def is_valid(antinode: Position) -> bool:
    return (0 <= antinode.x < ROWS) and (0 <= antinode.y < COLS)


def get_antinode(position: Position, x_diff: int, y_diff: int) -> Position:
    return Position(position.x + x_diff, position.y + y_diff)


def get_diffs(position1: Position, position2: Position) -> Tuple[int, int]:
    return position2.x - position1.x, position2.y - position1.y


def get_valid_antinodes(position1: Position, position2: Position) -> List[Position]:
    x_diff, y_diff = get_diffs(position1, position2)
    antinode1 = get_antinode(position1, -x_diff, -y_diff)
    antinode2 = get_antinode(position2, x_diff, y_diff)
    return [antinode for antinode in [antinode1, antinode2] if is_valid(antinode)]


def get_valid_antinodes_v2(position1: Position, position2: Position) -> Set[Position]:
    x_diff, y_diff = get_diffs(position1, position2)
    antinodes = {position1, position2}

    while any(
        (
            is_valid(antinode1 := get_antinode(position1, -x_diff, -y_diff)),
            is_valid(antinode2 := get_antinode(position2, x_diff, y_diff)),
        )
    ):
        antinodes.update(
            [antinode for antinode in (antinode1, antinode2) if is_valid(antinode)]
        )
        position1 = antinode1
        position2 = antinode2
    return antinodes


@aoc.part(1)
def part_1(antena_positions: Dict[str, List[Tuple[int, int]]]) -> int:
    antinodes = set()
    for positions in antena_positions.values():
        for pairs in generate_antena_pairs(positions):
            antinodes.update(get_valid_antinodes(*pairs))
    return len(antinodes)


@aoc.part(2)
def part_2(antena_positions: Dict[str, List[Tuple[int, int]]]) -> int:
    antinodes = set()
    for positions in antena_positions.values():
        for pairs in generate_antena_pairs(positions):
            antinodes.update(get_valid_antinodes_v2(*pairs))
    return len(antinodes)


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
