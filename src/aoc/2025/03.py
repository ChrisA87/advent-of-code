from functools import cache
import aoc

data = """987654321111111
811111111111119
234234234234278
818181911112111"""

data = aoc.get_data_from_file(3)


def parse_line(line: str) -> int:
    return list(map(int, line))


def get_max(numbers: list[int]) -> int:
    result = 0
    max_first = 0

    for i in range(len(numbers) - 1):
        if (first := numbers[i]) > max_first:
            max_first = first
            max_line = int(f"{max_first}{max(numbers[i + 1 :])}")
            if max_line > result:
                result = max_line
    return result


def get_max_v2(numbers: list[int], n: int) -> list[int]:
    n_numbers = len(numbers)

    @cache
    def _get_max(start: int, n: int) -> list[int]:
        if n == 0:
            return []
        max_seq = []
        for i in range(start, n_numbers - n + 1):
            current = [numbers[i]] + _get_max(i + 1, n - 1)
            if current > max_seq:
                max_seq = current
        return max_seq

    return _get_max(0, n)


@aoc.part(1)
def part_1() -> int:
    result = 0
    for line in data.split("\n"):
        result += get_max(parse_line(line))
    return result


@aoc.part(2)
def part_2() -> int:
    result = 0
    for line in data.split("\n"):
        batteries = get_max_v2(parse_line(line), 12)
        print(batteries)
        result += int("".join(map(str, batteries)))
    return result


def main():
    print(part_1())
    print(part_2())


if __name__ == "__main__":
    main()
