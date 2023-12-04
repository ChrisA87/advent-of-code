import aoc
import numpy as np
from typing import Tuple

year = aoc.get_year(__file__)
data = aoc.get_data_from_file(8, year)


def input_to_array(data):
    return np.array([list(map(int, x)) for x in data.split("\n")])


def is_visible(array: np.array, coord: Tuple[int]) -> bool:
    i, j = coord
    n, m = array.shape
    val = array[i][j]

    # Is edge coord
    if i == 0 or i == n or j == 0 or j == m:
        return True

    # Visible from top
    if (array[:i, j] < val).all():
        return True

    # Visible from right
    if (array[i, j + 1 :] < val).all():
        return True

    # Visible from below
    if (array[i + 1 :, j] < val).all():
        return True

    # Visible from left
    if (array[i, :j] < val).all():
        return True

    return False


def count_visible(array, coord, direction):
    n, m = array.shape
    i, j = coord
    val = array[i][j]
    target = -1
    result = 0

    while (0 < i <= n) and (0 < j <= m) and target < val:
        if direction == "up":
            i -= 1
        if direction == "right":
            j += 1
        if direction == "down":
            i += 1
        if direction == "left":
            j -= 1

        try:
            target = array[i][j]
        except IndexError:
            break
        result += 1
    return result


def calculate_scenic_score(array, coord):
    i, j = coord
    n, m = array.shape
    score = 1

    # Edges have score of 0
    if i == 0 or i == n or j == 0 or j == m:
        return 0

    for direction in ("up", "right", "down", "left"):
        score *= count_visible(array, coord, direction)
    return score


@aoc.part(1)
def solution_1():
    A = input_to_array(data)
    n, m = A.shape
    visible = 0

    for i in range(n):
        for j in range(m):
            visible += is_visible(A, (i, j))
    return visible


@aoc.part(2)
def solution_2():
    A = input_to_array(data)
    n, m = A.shape
    scenic_scores = []

    for i in range(n):
        for j in range(m):
            scenic_scores.append(calculate_scenic_score(A, (i, j)))
    return max(scenic_scores)


def main():
    print(solution_1())
    print(solution_2())


if __name__ == "__main__":
    main()
