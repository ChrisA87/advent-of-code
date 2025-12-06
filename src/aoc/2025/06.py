from collections import namedtuple
import aoc
from math import prod

data = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   + """

data = aoc.get_data_from_file(6)

Problem = namedtuple("Problem", ["numbers", "operator"])


def parse_data(data: str) -> list[Problem]:
    result = []
    for problem in list(zip(*(line.strip().split() for line in data.splitlines()))):
        nums = tuple(map(int, problem[:-1]))
        result.append(Problem(nums, problem[-1]))
    return result


def solve_problem(problem: Problem) -> int:
    match problem.operator:
        case "+":
            return sum(problem.numbers)
        case "*":
            return prod(problem.numbers)
        case _:
            raise ValueError("Unknown operator")


@aoc.part(1)
def part_1() -> int:
    result = 0
    problems = parse_data(data)
    for problem in problems:
        result += solve_problem(problem)
    return result


@aoc.part(2)
def part_2() -> int:
    pass


def main():
    print(part_1())
    print(part_2())


if __name__ == "__main__":
    main()
