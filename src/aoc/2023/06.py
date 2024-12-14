import aoc

data = """Time:      7  15   30
Distance:  9  40  200"""

data = aoc.get_data_from_file(6)


def parse_line(text: str) -> list[int]:
    _, numbers = text.split(":")
    return list(map(int, numbers.strip().split()))


def parse_data(data: str) -> tuple[list]:
    return [parse_line(line) for line in data.split("\n")]


def calc_distance(hold_duration, race_time):
    return hold_duration * (race_time - hold_duration)


def calc_margin_of_error(time, record):
    result = 0
    l_mid = r_mid = time // 2

    # Mehh, brute force didnt actuallty take too long...
    # TODO optimize to find min & max values
    left, right = (l_mid - 0) // 2, (r_mid + time) // 2
    for i in range(time):
        distance = calc_distance(i, time)
        result += distance > record
    return result


def combine_numbers(numbers: list[int]) -> int:
    return int("".join(map(str, numbers)))


@aoc.part(1)
def solution_1():
    times, distances = parse_data(data)
    results = []
    for time, distance in zip(times, distances):
        results.append(calc_margin_of_error(time, distance))
    result = 1
    for r in results:
        result *= r
    return result


@aoc.part(2)
def solution_2():
    times, distances = parse_data(data)
    time, distance = combine_numbers(times), combine_numbers(distances)
    result = calc_margin_of_error(time, distance)
    return result


def main():
    print(solution_1())
    print(solution_2())


if __name__ == "__main__":
    main()
