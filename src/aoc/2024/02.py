from typing import List

import aoc

data = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""

data = aoc.get_data_from_file(2)


def parse_data(data: str) -> List[List[int]]:
    return [list(map(int, row.split())) for row in data.splitlines()]


def get_differences(report: List[int]) -> List[int]:
    return [report[i + 1] - report[i] for i in range(len(report) - 1)]


def decreasing(report: List[int]) -> bool:
    return (report[i] > report[i + 1] for i in range(len(report) - 1))


def increasing(report: List[int]) -> bool:
    return (report[i] < report[i + 1] for i in range(len(report) - 1))


def within_threshold(report: List[int], lower: int = 1, upper: int = 3) -> bool:
    return ((abs(level) >= lower) and (abs(level) <= upper) for level in report)


def is_safe(report: List[int]) -> bool:
    all_increasing_or_decreasing = all(increasing(report)) or all(decreasing(report))
    all_within_threshold = all(within_threshold(get_differences(report)))
    return all_increasing_or_decreasing and all_within_threshold


@aoc.part(1)
def part_1(reports: List[List[int]]) -> int:
    return sum(is_safe(report) for report in reports)


@aoc.part(2)
def part_2(reports: List[List[int]]) -> int:
    result = 0

    for report in reports:
        if is_safe(report):
            result += 1
            continue

        for i in range(len(report)):
            if is_safe(report[:i] + report[i + 1 :]):
                result += 1
                break
    return result


def main():
    arr = parse_data(data)
    print(part_1(arr))
    print(part_2(arr))


if __name__ == "__main__":
    main()
