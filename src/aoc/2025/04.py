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
GRID = data.splitlines()
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


def is_accessible(i: int, j: int, threshold: int = 3) -> bool:
    if not in_bounds(i, j) or GRID[i][j] != ROLL_PAPER:
        return False
    adjacent = []
    for direction in DIRECTIONS.values():
        ni, nj = direction(i, j)
        if in_bounds(ni, nj) and GRID[ni][nj] == ROLL_PAPER:
            adjacent.append((ni, nj))
    return len(adjacent) <= threshold


@aoc.part(1)
def part_1() -> int:
    rows, cols = DIMS
    result = 0
    for i in range(rows):
        for j in range(cols):
            if is_accessible(i, j):
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
