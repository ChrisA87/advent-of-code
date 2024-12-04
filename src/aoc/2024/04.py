from typing import Callable, List, Tuple
import aoc

data = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""

data = aoc.get_data_from_file(4)

TARGET = "XMAS"

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


def parse_data(data: str) -> List[str]:
    return data.splitlines()


def check_coords(i: int, j: int, word_search: List[str]) -> int:
    result = 0
    for direction in DIRECTIONS.values():
        result += is_match(i, j, direction, word_search)
    return result


def is_match(i: int, j: int, move: Callable, word_search: List[str]) -> bool:
    step = 0
    matches = True

    while within_bounds(i, j, word_search) and (step < len(TARGET)) and matches:
        if word_search[i][j] != TARGET[step]:
            matches = False
        i, j = move(i, j)
        step += 1

    return matches and step == len(TARGET)


def within_bounds(i, j, word_search):
    rows, cols = len(word_search), len(word_search[0])
    return (0 <= i < rows) and (0 <= j < cols)


def is_x_mas(i: int, j: int, word_search: List[str]):
    diagonals = get_diagonals(i, j, word_search)

    if diagonals is not None:
        up_right, down_right, down_left, up_left = diagonals

        return (
            (up_right == "M" and down_left == "S")
            or (up_right == "S" and down_left == "M")
        ) and (
            (up_left == "M" and down_right == "S")
            or (up_left == "S" and down_right == "M")
        )
    return False


def get_diagonals(
    i: int, j: int, word_search: List[str]
) -> Tuple[str, str, str, str] | None:
    results = []

    try:
        for direction in ["up_right", "down_right", "down_left", "up_left"]:
            ii, jj = DIRECTIONS.get(direction)(i, j)
            results.append(word_search[ii][jj])
    except IndexError:
        return None
    return tuple(results)


@aoc.part(1)
def part_1(word_search: List[str]) -> int:
    result = 0

    for i, row in enumerate(word_search):
        for j, val in enumerate(row):
            if val == "X":
                result += check_coords(i, j, word_search)
    return result


@aoc.part(2)
def part_2(word_search: List[str]) -> int:
    result = 0

    for i, row in enumerate(word_search):
        for j, val in enumerate(row):
            if val == "A":
                result += is_x_mas(i, j, word_search)
    return result


def main():
    word_search = data.splitlines()
    print(part_1(word_search))
    print(part_2(word_search))


if __name__ == "__main__":
    main()
