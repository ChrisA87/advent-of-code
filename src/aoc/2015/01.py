from collections import Counter
import aoc


data = """((()))"""

data = aoc.get_data_from_file(1, 2015)


@aoc.part(1)
def part_1() -> int:
    d = Counter(data)
    return d["("] - d[")"]


@aoc.part(2)
def part_2() -> int:
    floor = 0
    d = {"(": 1, ")": -1}
    for i, step in enumerate(data, 1):
        floor += d[step]
        if floor < 0:
            return i


def main():
    print(part_1())
    print(part_2())


if __name__ == "__main__":
    main()
