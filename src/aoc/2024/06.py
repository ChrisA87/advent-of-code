from typing import List, Tuple
from tqdm import tqdm

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

class LoopError(Exception): ...

@dataclass
class Guard:
    position: Tuple[int, int]
    direction: str

    @property
    def position_ahead(self) -> Tuple[int, int]:
        return moves.get(self.direction)(*self.position)

    def get_next_position(self):
        return Guard(self.position_ahead, self.direction)

    def turn(self):
        self.direction = directions.get(self.direction)

    def move(self):
        self.position = self.position_ahead

    def copy(self):
        return Guard(self.position, self.direction)

    def __eq__(self, other):
        return self.position == other.position and self.direction == other.direction

    def __hash__(self):
        return hash((self.position, self.direction))


def parse_data(data: str):
    grid = data.splitlines()
    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            if val in directions:
                guard = Guard((i, j), val)
                return grid, guard


def in_bounds(guard: Guard, grid: List[str]) -> bool:
    rows, col = len(grid), len(grid[0])
    i, j = guard.position
    return (0 <= i < rows) and (0 <= j < col)


def obstructed(guard: Guard, grid: List[str]) -> bool:
    i, j = guard.position
    return grid[i][j] == "#"


def get_route(guard: Guard, grid: List[str]):
    route = [guard.copy()]

    while in_bounds(next_position := guard.get_next_position(), grid):
        if not obstructed(next_position, grid):
            guard.move()
        else:
            guard.turn()
        # Already been here
        if guard in route:
            raise LoopError("Loop deteced")

        route.append(guard.copy())

    return route


def insert_obstruction(grid, position):
    i, j = position
    grid = grid[:]
    row = grid[i]
    grid[i] = row[:j] + "#" + row[j + 1 :]
    return grid


@aoc.part(1)
def part_1() -> int:
    grid, guard = parse_data(data)
    route = get_route(guard, grid)
    return len(set(p.position for p in route))


@aoc.part(2)
def part_2() -> int:
    grid, guard = parse_data(data)

    route = get_route(guard, grid)
    checked_obstructions = set()
    seen_positions = set()
    caused_loop = set()

    for starting_state in tqdm(route):
        if (
            ahead := starting_state.position_ahead
        ) in checked_obstructions or starting_state in seen_positions:
            continue

        checked_obstructions.add(ahead)
        seen_positions.add(starting_state)
        try:
            get_route(starting_state, insert_obstruction(grid, ahead))
        except IndexError:
            continue
        except LoopError:
            caused_loop.add(ahead)

    return len(caused_loop - {route[0].position})


def main():
    print(part_1())
    print(part_2())


if __name__ == "__main__":
    main()
