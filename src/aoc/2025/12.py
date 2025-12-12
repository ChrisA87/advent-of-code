import aoc


data = """0:
###
##.
##.

1:
###
##.
.##

2:
.##
###
##.

3:
##.
###
##.

4:
###
#..
###

5:
###
.#.
###

4x4: 0 0 0 0 2 0
12x5: 1 0 1 0 2 2
12x5: 1 0 1 0 3 2"""

# data = aoc.get_data_from_file(12)


class Present:
    def __init__(self, shape: list[list[int]]) -> None:
        self.shape = shape

    @property
    def area(self) -> int:
        return sum(sum(row) for row in self.shape)

    @property
    def height(self) -> int:
        return len(self.shape)

    @property
    def width(self) -> int:
        return len(self.shape[0]) if self.shape else 0

    @property
    def size(self) -> int:
        return self.height * self.width


def parse_data(data: str):
    *presents, regions = data.split("\n\n")
    present = dict([parse_present(p) for p in presents])
    regions = [parse_region(r) for r in regions.splitlines()]
    return present, regions


def parse_present(present: str) -> tuple[str, Present]:
    idx, shape = present.split(":\n")
    return int(idx), Present(
        [[1 if c == "#" else 0 for c in line] for line in shape.splitlines()]
    )


def parse_region(region: str):
    size, present_ids = region.split(": ")
    dimensions = tuple(map(int, size.split("x")))
    present_ids = list(map(int, present_ids.split()))
    return dimensions, present_ids


@aoc.part(1)
def part_1() -> int:
    presents, regions = parse_data(data)
    return presents, regions


@aoc.part(2)
def part_2() -> int:
    pass


def main():
    print(part_1())
    print(part_2())


if __name__ == "__main__":
    main()
