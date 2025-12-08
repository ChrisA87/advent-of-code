import aoc

data = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""

data = aoc.get_data_from_file(1)

STARTING_POINT = 50


def parse_line(line: str) -> int:
    direction, number = line[0], int(line[1:])
    if direction == "L":
        return -number
    return number


@aoc.part(1)
def part_1() -> int:
    position = STARTING_POINT
    password = 0
    for line in data.split("\n"):
        position += parse_line(line.strip())
        position %= 100
        if position == 0:
            password += 1
    return password


@aoc.part(2)
def part_2() -> int:
    position = STARTING_POINT
    password = 0
    for line in data.split("\n"):
        rotation = parse_line(line.strip())

        for _ in range(abs(rotation)):
            if rotation < 0:
                position -= 1
            else:
                position += 1
            position %= 100
            if position == 0:
                password += 1
    return password


def main():
    print(part_1())
    print(part_2())


if __name__ == "__main__":
    main()
