from collections import namedtuple
from itertools import islice
import aoc
from math import prod
import re

data = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +   """

data = aoc.get_data_from_file(6)

Problem = namedtuple("Problem", ["numbers", "operator"])


def parse_data(data: str) -> list[Problem]:
    result = []
    for problem in list(zip(*(line.strip().split() for line in data.splitlines()))):
        nums = tuple(map(int, problem[:-1]))
        result.append(Problem(nums, problem[-1]))
    return result


def parse_data_v2(data: str):
    lines = data.splitlines()
    widths = get_widths(lines[-1])
    cols = zip(*lines)
    results = []
    for width in widths:
        chunk = list(islice(cols, width))
        results.append(chunk)
    return results


def get_widths(operator_line: str) -> list[int]:
    return [len(g) for g in re.findall("([+*]\s+)", operator_line)]


def solve_problem(problem: Problem) -> int:
    match problem.operator:
        case "+":
            return sum(problem.numbers)
        case "*":
            return prod(problem.numbers)
        case _:
            raise ValueError("Unknown operator")


def solve_problem_v2(problem) -> int:
    op = problem[0][-1]
    match op:
        case "+":
            func = sum
        case "*":
            func = prod
        case _:
            raise ValueError(f"Unknown operator: {op}")

    numbers = []
    for col in problem[::-1]:
        num = "".join(col[:-1]).strip()
        if num:
            numbers.append(int(num))
    return func(numbers)


@aoc.part(1)
def part_1() -> int:
    result = 0
    problems = parse_data(data)
    for problem in problems:
        result += solve_problem(problem)
    return result


@aoc.part(2)
def part_2() -> int:
    problems = parse_data_v2(data)
    result = 0
    for problem in problems:
        result += solve_problem_v2(problem)
    return result


def main():
    print(part_1())
    print(part_2())


if __name__ == "__main__":
    main()
