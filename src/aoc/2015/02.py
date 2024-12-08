from collections import namedtuple
from typing import List, Tuple

from dataclasses import dataclass
import aoc

data = """2x3x4"""

data = aoc.get_data_from_file(2, 2015)


@dataclass
class Present:
    length: int
    width: int
    height: int

    @property
    def volume(self) -> int:
        return self.length * self.width * self.height

    def get_side_areas(self) -> Tuple[int, int, int]:
        return (
            self.length * self.width,
            self.length * self.height,
            self.width * self.height,
        )

    def get_perimeters(self) -> Tuple[int, int, int]:
        return (
            2 * (self.length + self.width),
            2 * (self.length + self.height),
            2 * (self.width + self.height),
        )

    def get_smallest_area(self) -> int:
        return min(self.get_side_areas())

    def get_smallest_perimeter(self) -> int:
        return min(self.get_perimeters())

    def get_surface_area(self) -> int:
        return 2 * sum(self.get_side_areas())

    def get_wrapping_paper_required(self) -> int:
        return self.get_surface_area() + self.get_smallest_area()

    def get_ribbon_required(self) -> int:
        return self.get_smallest_perimeter() + self.volume


def parse_data(data: str) -> List[Present]:
    result = []
    for line in data.splitlines():
        result.append(Present(*map(int, line.split("x"))))
    return result


@aoc.part(1)
def part_1() -> int:
    presents = parse_data(data)
    result = 0
    for present in presents:
        result += present.get_wrapping_paper_required()
    return result


@aoc.part(2)
def part_2() -> int:
    presents = parse_data(data)
    result = 0
    for present in presents:
        result += present.get_ribbon_required()
    return result


def main():
    print(part_1())
    print(part_2())


if __name__ == "__main__":
    main()
