import aoc


data = """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"""

# data = aoc.get_data_from_file(10)


class Machine:
    def __init__(
        self,
        indicator_lights: list[int],
        button_wirings: list[tuple[int, ...]],
        joltage: list[int],
    ):
        self.indicator_lights = indicator_lights
        self.button_wirings = button_wirings
        self.joltage = joltage

    @classmethod
    def from_string(cls, string: str) -> "Machine":
        il, *bw, j = string.split()
        il = [1 if x == "#" else 0 for x in il[1:-1]]
        bw = [tuple(map(int, x.strip("()").split(","))) for x in bw]
        j = list(map(int, j.strip("{}").split(",")))
        return cls(il, bw, j)

    def __repr__(self) -> str:
        return (
            f"Machine(indicator_lights={self.indicator_lights}, "
            f"button_wirings={self.button_wirings}, "
            f"joltage={self.joltage})"
        )


@aoc.part(1)
def part_1() -> int:
    for line in data.splitlines():
        machine = Machine.from_string(line)
        print(machine)


@aoc.part(2)
def part_2() -> int:
    pass


def main():
    print(part_1())
    print(part_2())


if __name__ == "__main__":
    main()
