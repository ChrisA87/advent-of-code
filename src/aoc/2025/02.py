import aoc

data = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"""

data = aoc.get_data_from_file(2)


def parse_ranges(line: str) -> list[range]:
    results = []
    for rng in line.split(","):
        start, end = map(int, rng.split("-"))
        results.append(range(start, end + 1))
    return results


def is_repeated(num: int) -> bool:
    num_str = str(num)
    middle = len(num_str) // 2
    return num_str[:middle] == num_str[middle:]


def is_repeated_v2(num: int):
    s = str(num)

    for i in range(1, len(s)):
        if len(s) % i == 0:
            pattern = s[:i]
            if pattern * (len(s) // i) == s:
                return len(str(num)) // i >= 2
    return False


@aoc.part(1)
def part_1() -> int:
    ranges = parse_ranges(data)
    repeated_nums = []
    for rng in ranges:
        for num in rng:
            if is_repeated(num):
                repeated_nums.append(num)
    return sum(repeated_nums)


@aoc.part(2)
def part_2() -> int:
    ranges = parse_ranges(data)
    repeated_nums = []
    for rng in ranges:
        for num in rng:
            if is_repeated_v2(num):
                repeated_nums.append(num)
    return sum(repeated_nums)


def main():
    print(part_1())
    print(part_2())


if __name__ == "__main__":
    main()
