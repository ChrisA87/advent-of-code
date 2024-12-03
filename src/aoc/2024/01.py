from typing import List, Tuple
from collections import Counter

import aoc

# data = """3   4
# 4   3
# 2   5
# 1   3
# 3   9
# 3   3"""

data = aoc.get_data_from_file(1)


def parse_data(data: str) -> Tuple[List[int], List[int]]:
    left, right = zip(*[line.split() for line in data.split("\n")])
    return to_sorted_ints(left), to_sorted_ints(right)


def to_sorted_ints(data: List[str]) -> List[int]:
    return sorted(map(int, data))


@aoc.part(1)
def part_1(left: List[int], right: List[int]) -> int:
    return sum(abs(l - r) for r, l in zip(left, right))


@aoc.part(2)
def part_2(left: List[str], right: List[int]) -> int:
    right_counts = Counter(right)
    return sum(x * right_counts.get(x, 0) for x in left)


def main():
    left, right = parse_data(data)
    print(part_1(left, right))
    print(part_2(left, right))


if __name__ == "__main__":
    main()
