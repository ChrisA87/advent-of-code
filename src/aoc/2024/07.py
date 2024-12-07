from itertools import product, chain
from typing import Generator, List, Tuple
import aoc

data = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""

data = aoc.get_data_from_file(7)


def parse_data(data: str) -> List[Tuple[int, List[int]]]:
    result = []
    for line in data.splitlines():
        target, numbers = line.split(": ")
        numbers = list(map(int, numbers.split()))
        result.append((int(target), numbers))
    return result


def generate_equations(
    numbers: List[int], operators: List[str]
) -> Generator[List, None, None]:
    operator_combinations = product(operators, repeat=len(numbers) - 1)
    for oc in operator_combinations:
        yield list(chain(*zip(numbers, oc))) + [numbers[-1]]


def evaluate_equation(equation: List[int | str]):
    result = equation[0]

    for i in range(1, len(equation), 2):
        op = equation[i]
        num = equation[i + 1]
        if op == "+":
            result += num
        elif op == "*":
            result *= num
        elif op == "||":
            result = int(str(result) + str(num))
    return result


@aoc.part(1)
def part_1() -> int:
    result = 0
    for target, numbers in parse_data(data):
        for equation in generate_equations(numbers, ["+", "*"]):
            if evaluate_equation(equation) == target:
                result += target
                break
    return result


@aoc.part(2)
def part_2() -> int:
    result = 0
    for target, numbers in parse_data(data):
        for equation in generate_equations(numbers, ["+", "*", "||"]):
            if evaluate_equation(equation) == target:
                result += target
                break
    return result


def main():
    print(part_1())
    print(part_2())


if __name__ == "__main__":
    main()
