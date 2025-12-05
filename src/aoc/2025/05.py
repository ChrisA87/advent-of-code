import aoc

data = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""

data = aoc.get_data_from_file(5)


def parse_data(data: str) -> list[tuple[int, int], list[int]]:
    ranges, ingredients = data.split("\n\n")
    ranges = [tuple(map(int, rng.split("-"))) for rng in ranges.splitlines()]
    ranges = merge_intervals(sorted(ranges, key=lambda x: x[0]))
    ingredients = list(map(int, ingredients.splitlines()))
    return ranges, ingredients


def is_fresh(ingredient_id: int, fresh_ids: dict) -> bool:
    for l_bound, u_bound in fresh_ids:
        if l_bound > ingredient_id:
            return False
        if l_bound <= ingredient_id <= u_bound:
            return True
    return False


def merge_intervals(intervals: list[tuple[int, int]]):
    merged = [intervals[0]]

    for current in intervals[1:]:
        last_start, last_end = merged[-1]
        curr_start, curr_end = current

        if curr_start <= last_end:
            merged[-1] = (last_start, max(last_end, curr_end))
        else:
            merged.append(current)

    return merged


@aoc.part(1)
def part_1() -> int:
    fresh_ids, ingredients = parse_data(data)
    result = 0
    for ingredient in ingredients:
        if is_fresh(ingredient, fresh_ids):
            result += 1
    return result


@aoc.part(2)
def part_2() -> int:
    fresh_ids, _ = parse_data((data))
    result = 0
    for lower, upper in fresh_ids:
        result += upper - lower + 1
    return result


def main():
    print(part_1())
    print(part_2())


if __name__ == "__main__":
    main()
