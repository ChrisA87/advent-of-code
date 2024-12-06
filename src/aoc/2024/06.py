from typing import List, Tuple

from dataclasses import dataclass
import aoc

data = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""

data = aoc.get_data_from_file(6)

directions = {"^": ">", ">": "v", "v": "<", "<": "^"}
moves = {
    "^": lambda i, j: (i - 1, j),
    ">": lambda i, j: (i, j + 1),
    "v": lambda i, j: (i + 1, j),
    "<": lambda i, j: (i, j - 1),
}


@dataclass
class Guard:
    position: Tuple[int, int]
    direction: str

    @property
    def next_position(self) -> Tuple[int, int]:
        return moves.get(self.direction)(*self.position)

    def turn(self):
        self.direction = directions.get(self.direction)

    def move(self):
        self.position = self.next_position


def parse_data(data: str):
    grid = data.splitlines()
    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            if val in directions:
                position = Guard((i, j), val)
                return grid, position


def in_bounds(position: Tuple[int, int], grid: List[str]) -> bool:
    rows, col = len(grid), len(grid[0])
    i, j = position
    return (0 <= i < rows) and (0 <= j < col)


def obstructed(position: Tuple[int, int], grid: List[str]) -> bool:
    i, j = position
    return grid[i][j] == "#"


@aoc.part(1)
def part_1() -> int:
    grid, guard = parse_data(data)
    seen = {guard.position}

    while in_bounds(guard.next_position, grid):
        if not obstructed(guard.next_position, grid):
            guard.move()
            seen.add(guard.position)
        else:
            guard.turn()
    return len(seen)


@aoc.part(2)
def part_2() -> int:
    pass


def main():
    print(part_1())
    print(part_2())


if __name__ == "__main__":
    main()
