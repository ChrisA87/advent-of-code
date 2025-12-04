from functools import cache
import aoc

data = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""

data = aoc.get_data_from_file(4)

ROLL_PAPER = "@"
GRID = list(map(list, data.splitlines()))
DIMS = (len(GRID), len(GRID[0]))
DIRECTIONS = {
    "up": lambda i, j: (i - 1, j),
    "up_right": lambda i, j: (i - 1, j + 1),
    "right": lambda i, j: (i, j + 1),
    "down_right": lambda i, j: (i + 1, j + 1),
    "down": lambda i, j: (i + 1, j),
    "down_left": lambda i, j: (i + 1, j - 1),
    "left": lambda i, j: (i, j - 1),
    "up_left": lambda i, j: (i - 1, j - 1),
}


def in_bounds(i: int, j: int) -> bool:
    rows, cols = DIMS
    return (0 <= i < rows) and (0 <= j < cols)


def is_accessible(i: int, j: int, threshold: int = 3, grid: list[str] = GRID) -> bool:
    if not in_bounds(i, j) or GRID[i][j] != ROLL_PAPER:
        return False
    adjacent = []
    for direction in DIRECTIONS.values():
        ni, nj = direction(i, j)
        if in_bounds(ni, nj) and GRID[ni][nj] == ROLL_PAPER:
            adjacent.append((ni, nj))
    return len(adjacent) <= threshold


def get_accessible(grid: list[list[str]]) -> list[tuple[int, int]]:
    rows, cols = DIMS
    results = []
    for i in range(rows):
        for j in range(cols):
            if is_accessible(i, j, grid=grid):
                results.append((i, j))
    return results


def count_accessible(grid: list[str]) -> int:
    return len(get_accessible(grid))


def remove_accessible(grid: list[str]) -> int:
    result = grid[:]
    for i, j in get_accessible(grid):
        result[i][j] = "."
    return result


def count_accessible_with_removals(grid: list[str]) -> int:
    result = 0
    n_accessible = 1

    while n_accessible:
        n_accessible = count_accessible(grid)
        result += n_accessible
        grid = remove_accessible(grid)
        # render_grid(grid)
        # print()
    return result


def render_grid(grid):
    print("\n".join("".join(x) for x in grid))


@aoc.part(1)
def part_1() -> int:
    return count_accessible(GRID)


@aoc.part(2)
def part_2() -> int:
    return count_accessible_with_removals(GRID)


def main():
    print(part_1())
    print(part_2())


if __name__ == "__main__":
    main()
