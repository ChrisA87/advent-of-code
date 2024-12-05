from collections import defaultdict
from typing import List
import aoc

data = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

data = aoc.get_data_from_file(5)


def parse_data(data: str):
    rules, updates = data.split("\n\n")
    return parse_rules(rules), parse_updates(updates)


def parse_rules(rules: str):
    result = defaultdict(list)
    for line in rules.splitlines():
        key, val = map(int, line.split("|"))
        result[key].append(val)
    return result


def get_middle_item(update: List[int]) -> int:
    return update[len(update) // 2]


def parse_updates(updates: str):
    return [list(map(int, line.split(","))) for line in updates.splitlines()]


def in_order(update, rules):
    for i, j in zip(update, update[1:]):
        if j not in rules[i]:
            return False
    return True


def sort_unordered_update(update, rules):
    while not in_order(update, rules):
        print(f"Not sorted: {update}")
        for i, page in enumerate(update):
            for j, next_page in enumerate(update[i + 1 :], i + 1):
                print(f" Checking {i} ({page}), {j} ({next_page})")
                if page in rules.get(next_page):
                    update[j], update[i] = update[i], update[j]
                    print(f"  Swapped: {update}")
    return update


@aoc.part(1)
def part_1(rules, updates) -> int:
    result = 0
    for update in updates:
        if in_order(update, rules):
            result += get_middle_item(update)
    return result


@aoc.part(2)
def part_2(rules, updates) -> int:
    result = 0
    for update in updates:
        if not in_order(update, rules):
            result += get_middle_item(sort_unordered_update(update, rules))
    return result


def main():
    rules, updates = parse_data(data)

    print(part_1(rules, updates))
    print(part_2(rules, updates))


if __name__ == "__main__":
    main()
