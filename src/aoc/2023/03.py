import aoc

data = aoc.get_data_from_file(3).split("\n")
N_ROWS = len(data)
N_COLS = len(data[0])


def is_symbol(char: str) -> bool:
    return not char.isdigit() and char != "."


def is_gear_symbol(char: str) -> bool:
    return char == "*"


def get_symbol_coords(data: str, symbol_func=is_symbol) -> list:
    results = []
    n_rows = len(data)
    n_cols = len(data[0])
    for i in range(n_rows):
        for j in range(n_cols):
            char = data[i][j]
            if symbol_func(char):
                results.append((i, j))
    return results


def get_adjacent_coords(i: int, j: int) -> set:
    offsets = [
        (i - 1, j - 1),
        (i - 1, j),
        (i - 1, j + 1),
        (i, j - 1),
        (i, j + 1),
        (i + 1, j - 1),
        (i + 1, j),
        (i + 1, j + 1),
    ]
    return set((i, j) for i, j in offsets if 0 <= i <= N_ROWS and 0 <= j <= N_COLS)


def inbounds(index: int) -> bool:
    return 0 <= index < N_COLS


def extract_number_coords(i, j):
    result = ""
    coords = set()

    if data[i][j].isdigit():
        result = data[i][j]
        coords.add((i, j))

    left_idx = j - 1
    while inbounds(left_idx) and data[i][left_idx].isdigit():
        result = data[i][left_idx] + result
        coords.add((i, left_idx))
        left_idx -= 1

    right_idx = j + 1
    while inbounds(right_idx) and data[i][right_idx].isdigit():
        result += data[i][right_idx]
        coords.add((i, right_idx))
        right_idx += 1

    return int(result), coords


def extract_numbers(coords):
    results = []
    while coords:
        i, j = coords.pop()
        if data[i][j].isnumeric():
            number, coords_to_remove = extract_number_coords(i, j)
            coords -= coords_to_remove
            results.append(number)
    return results


def get_gears_ratio_sum(gears: list) -> int:
    result = 0
    for x, y in gears:
        result += x * y
    return result


@aoc.part(1)
def solution_1():
    numbers = []
    symbol_coords = get_symbol_coords(data)
    adjacent_coords = [get_adjacent_coords(i, j) for i, j in symbol_coords]
    for coords_to_check in adjacent_coords:
        numbers.extend(extract_numbers(coords_to_check))

    return sum(numbers)


@aoc.part(2)
def solution_2():
    gears = []
    symbol_coords = get_symbol_coords(data, symbol_func=is_gear_symbol)
    adjacent_coords = [get_adjacent_coords(i, j) for i, j in symbol_coords]
    for coords_to_check in adjacent_coords:
        adjacent_numbers = extract_numbers(coords_to_check)
        if len(adjacent_numbers) == 2:
            gears.append(adjacent_numbers)
    return get_gears_ratio_sum(gears)


def main():
    print(solution_1())
    print(solution_2())


if __name__ == "__main__":
    main()
