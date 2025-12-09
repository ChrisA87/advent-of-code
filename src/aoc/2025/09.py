from math import prod
import aoc
from aoc.utils import parse_coords, Point


data = """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3"""

data = aoc.get_data_from_file(9)


@aoc.part(1)
def part_1() -> int:
    result = 0
    points = parse_coords(data)
    for i, p1 in enumerate(points):
        for j, p2 in enumerate(points):
            if i >= j:
                continue
            area = (abs(p2.y - p1.y) + 1) * (abs(p2.x - p1.x) + 1)
            # print(f" Comparing {p1} & {p2}: {area}")
            if area > result:
                result = area
    return result


@aoc.part(2)
def part_2() -> int:
    pass


def main():
    print(part_1())
    print(part_2())


if __name__ == "__main__":
    main()
