import aoc
import re
from typing import List
from collections import defaultdict

data = aoc.get_data_from_file(4)


class ScratchCard:
    def __init__(self, id_: int, winning_numbers: List[int], numbers: List[int]):
        self.id_ = id_
        self.winning_numbers = set(winning_numbers)
        self.numbers = set(numbers)

    @classmethod
    def from_table_line(cls, table_line):
        id_, winning_numbers, numbers = parse_line(table_line)
        return cls(id_, winning_numbers, numbers)

    @property
    def matches(self):
        return self.winning_numbers.intersection(self.numbers)

    @property
    def n_matches(self):
        return len(self.matches)

    @property
    def score(self):
        n = len(self.matches)
        if n == 0:
            return 0
        return 2 ** (n - 1)

    def get_won_copy_ids(self):
        return [self.id_ + (i + 1) for i in range(self.n_matches)]

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(id_={self.id_}, score={self.score}, n_matches={self.n_matches})"


def parse_numbers(text):
    return list(map(int, re.split(r"\s+", text.strip())))


def parse_line(line):
    id_, values = line.split(": ")
    id_ = int(id_.replace("Card ", ""))
    winning_numbers, numbers = values.split(" | ")
    return id_, parse_numbers(winning_numbers), parse_numbers(numbers)


@aoc.part(1)
def solution_1():
    result = 0
    for line in data.split("\n"):
        scratch_card = ScratchCard.from_table_line(line)
        result += scratch_card.score
    return result


@aoc.part(2)
def solution_2():
    processed = defaultdict(int)

    for line in data.split("\n"):
        scratch_card = ScratchCard.from_table_line(line)
        processed[scratch_card.id_] += 1
        for won_id in scratch_card.get_won_copy_ids():
            processed[won_id] += processed[scratch_card.id_]

    return sum(processed.values())


def main():
    print(solution_1())
    print(solution_2())


if __name__ == "__main__":
    main()
