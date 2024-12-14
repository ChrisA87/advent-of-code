import re
from typing import List, Tuple
import aoc
import sympy as sym

data = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279"""

data = aoc.get_data_from_file(13, 2024)

A_COST: int = 3
B_COST: int = 1
CONV_ERROR: int = 1e13


def parse_data(data: str):
    result = []
    for chunk in data.split("\n\n"):
        result.append(parse_chunk(chunk))
    return result


def parse_chunk(data: str):
    return [parse_line(line) for line in data.splitlines()]


def parse_line(text: str):
    pattern = re.compile(r"^[^X]+X[+=](\d+),\sY[+=](\d+)$")
    return tuple(map(int, pattern.findall(text)[0]))


def solve_simultaneous_equation(chunk: List[Tuple[int, int]], conv_err=0):
    (a1, a2), (b1, b2), (z1, z2) = chunk
    x, y = sym.symbols("x,y")
    eq1 = sym.Eq(a1 * x + b1 * y, z1 + conv_err)
    eq2 = sym.Eq(a2 * x + b2 * y, z2 + conv_err)
    return sym.solve([eq1, eq2], (x, y)).values()


def is_solvable(*args):
    return all(x % 1 == 0 for x in args)


@aoc.part(1)
def part_1() -> int:
    result = 0
    for chunk in parse_data(data):
        x, y = solve_simultaneous_equation(chunk)
        if is_solvable(x, y):
            print(chunk)
            print(x, y)
            result += x * A_COST + y * B_COST
    return result


@aoc.part(2)
def part_2() -> int:
    result = 0
    for chunk in parse_data(data):
        x, y = solve_simultaneous_equation(chunk, conv_err=CONV_ERROR)
        if is_solvable(x, y):
            print(chunk)
            print(x, y)
            result += x * A_COST + y * B_COST
    return result


def main():
    print(part_1())
    print(part_2())


if __name__ == "__main__":
    main()
