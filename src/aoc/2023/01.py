import aoc
import regex as re

data = aoc.get_data_from_file(1).split("\n")

NUMBERS = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def strip_alpha(text: str):
    return "".join(char for char in text if char.isnumeric())


def get_first_last_digits(text: str):
    if len(text) == 1:
        first = last = text
    else:
        first, *_, last = text
    return int(first + last)


def get_first_last_matches(matches: list):
    if len(matches) == 1:
        first = last = matches[0]
    else:
        first, *_, last = matches

    return int(normalize_digit(first) + normalize_digit(last))


def normalize_digit(digit: str):
    if digit.isnumeric():
        return digit
    return NUMBERS.get(digit)


@aoc.part(1)
def part_1():
    values = []

    for line in data:
        numeric = strip_alpha(line)
        values.append(get_first_last_digits(numeric))

    return sum(values)


@aoc.part(2)
def part_2():
    pattern = re.compile(f"({'|'.join(list(NUMBERS) + ['[0-9]'])})")
    values = []
    for line in data:
        matches = re.findall(pattern, line, overlapped=True)
        values.append(get_first_last_matches(matches))
    return sum(values)


def main():
    print(part_1())
    print(part_2())


if __name__ == "__main__":
    main()
