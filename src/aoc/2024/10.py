from collections import namedtuple
from dataclasses import dataclass
from functools import lru_cache
from typing import List, Tuple

import aoc

data = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""

data = aoc.get_data_from_file(10, 2024)


DIRECTIONS = {"up": (-1, 0), "right": (0, 1), "down": (1, 0), "left": (0, -1)}


@dataclass
class Position:
    x: int
    y: int

    def in_bounds(self):
        return (0 <= self.x < ROWS) and (0 <= self.y < COLS)

    def __hash__(self):
        return hash((self.x, self.y))


def parse_data(data: str) -> Tuple[Tuple[int]]:
    return tuple(tuple(map(int, line)) for line in data.splitlines())


def get_trailheads(trail_map: List[List[int]], target: int = 0) -> List[Position]:
    result = []
    for i, row in enumerate(trail_map):
        for j, val in enumerate(row):
            if val == target:
                result.append(Position(i, j))
    return result


def get_adjacent_positions(
    position: Position, trail_map: Tuple[Tuple[int]], target: int
) -> List[Position]:
    adjacent = [
        Position(position.x + x, position.y + y) for x, y in DIRECTIONS.values()
    ]
    return [
        position
        for position in adjacent
        if position.in_bounds() and trail_map[position.x][position.y] == target
    ]


@lru_cache()
def traverse(position: Position, trail_map: Tuple[Tuple[int]]) -> List[Position]:
    if not position.in_bounds():
        return []

    # reached a peak
    if (val := trail_map[position.x][position.y]) == 9:
        return [position]

    to_check = get_adjacent_positions(position, trail_map, val + 1)
    result = []
    while to_check:
        next_position = to_check.pop()
        result += traverse(next_position, trail_map)
    return result


@aoc.part(1)
def part_1(trail_map: Tuple[Tuple[int]]) -> int:
    trailheads = get_trailheads(trail_map)
    result = 0
    for trailhead in trailheads:
        result += len(set(traverse(trailhead, trail_map)))
    return result


@aoc.part(2)
def part_2(trail_map: Tuple[Tuple[int]]) -> int:
    trailheads = get_trailheads(trail_map)
    result = 0
    for trailhead in trailheads:
        result += len(traverse(trailhead, trail_map))
    return result


def main():
    global ROWS
    global COLS

    trail_map = parse_data(data)
    ROWS = len(trail_map)
    COLS = len(trail_map[0])

    print(part_1(trail_map))
    print(part_2(trail_map))


if __name__ == "__main__":
    main()
