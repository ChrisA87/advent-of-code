from collections import defaultdict
from dataclasses import dataclass
from math import prod
from time import sleep
from typing import List

import numpy as np
import aoc

data = """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3"""

data = aoc.get_data_from_file(14, 2024)

# WIDTH = 11
# HEIGHT = 7

WIDTH = 101
HEIGHT = 103


@dataclass
class Position:
    x: int
    y: int

    @property
    def quadrant(self) -> int | None:
        mid_x, mid_y = WIDTH // 2, HEIGHT // 2
        if self.x == mid_x or self.y == mid_y:
            return None
        if self.x < mid_x and self.y < mid_y:
            return 1
        elif self.x > mid_x and self.y < mid_y:
            return 2
        elif self.x < mid_x and self.y > mid_y:
            return 3
        return 4


@dataclass
class Velocity:
    x: int
    y: int


@dataclass
class Robot:
    position: Position
    velocity: Velocity

    def future_position(self, n_seconds: int) -> Position:
        return Position(
            x=(self.position.x + n_seconds * self.velocity.x) % WIDTH,
            y=(self.position.y + n_seconds * self.velocity.y) % HEIGHT,
        )


def render_positions(grid: np.ndarray) -> str:
    def render_row(row):
        return "".join(list(map(str, row))).replace("0", " ")

    result = ""
    for row in grid:
        result += f"{render_row(row)}\n"
    return result


def get_grid_positions(positions):
    grid = np.zeros((HEIGHT, WIDTH), dtype=np.int32)
    for position in positions:
        grid[position.y][position.x] += 1
    return grid


def parse_data(data: str) -> List[Robot]:
    result = []
    for line in data.splitlines():
        position, velocity = line.lstrip("p=").split(" v=")
        position, velocity = [parse_numbers(text) for text in (position, velocity)]
        result.append(Robot(Position(*position), Velocity(*velocity)))
    return result


def parse_numbers(text: str) -> List[int]:
    return list(map(int, text.split(",")))


@aoc.part(1)
def part_1() -> int:
    # robot = Robot(Position(2, 4), Velocity(2, -3))
    # for i in range(6):
    #     print(f"Step {i}")
    #     print(robot)
    #     print(robot.future_position(i))
    #     print(robot.future_position(i).quadrant)
    #     print()
    # return None

    robots = parse_data(data)
    quadrants = defaultdict(int)
    for robot in robots:
        future_pos = robot.future_position(100)
        quadrants[future_pos.quadrant] += 1
    return prod(v for k, v in quadrants.items() if k is not None)


@aoc.part(2)
def part_2() -> int:
    robots = parse_data(data)
    for i in range(100000):
        grid_positions = get_grid_positions(
            [robot.future_position(i) for robot in robots]
        )
        if np.all(grid_positions <= 1):
            result = f"{i}\n\n"
            return result + render_positions(grid_positions)


def main():
    print(part_1())
    print(part_2())


if __name__ == "__main__":
    main()
