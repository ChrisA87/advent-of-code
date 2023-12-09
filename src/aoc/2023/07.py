from dataclasses import dataclass
from typing import List
from collections import Counter
from functools import total_ordering
import aoc


data = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""

data = aoc.get_data_from_file(7)

CARD_VALUE_ORDER = "23456789TJQKA"
CARD_VALUE_DICT = {c: i for i, c in enumerate(CARD_VALUE_ORDER, 2)}
HAND_RANK_DICT = {
    7: "5 of a kind",
    6: "4 of a kind",
    5: "fullhouse",
    4: "3 of a kind",
    3: "2 pair",
    2: "1 pair",
    1: "high card",
}
WILDCARD_VALUE = "J"


@dataclass
@total_ordering
class Card:
    label: str
    use_wildcards: bool = False

    @property
    def strength(self):
        if self.use_wildcards and self.is_wildcard():
            return 0
        return CARD_VALUE_DICT[self.label]

    def is_wildcard(self):
        return self.label == WILDCARD_VALUE and self.use_wildcards

    def __hash__(self):
        return hash(self.label)

    def __eq__(self, other):
        return self.strength == other.strength

    def __gt__(self, other):
        return self.strength > other.strength

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"label={self.label}, "
            f"strength={self.strength}, "
            f"is_wild={self.is_wildcard()}"
            ")"
        )


@dataclass
@total_ordering
class Hand:
    cards: List[Card]
    bid: int
    use_wildcards: bool = False

    @classmethod
    def from_text(cls, text: str, use_wildcards: bool = False):
        cards, bid = text.split()

        return cls(
            cards=[Card(c, use_wildcards) for c in cards],
            bid=int(bid),
            use_wildcards=use_wildcards,
        )

    @property
    def card_counts(self):
        results = self._base_counts()
        if self.use_wildcards and WILDCARD_VALUE in results:
            n_wildcards = results.pop(WILDCARD_VALUE)
            most_common = [
                card for (card, _) in results.most_common() if card != WILDCARD_VALUE
            ]
            if not most_common:
                return Counter({"A": 5})
            else:
                results[most_common[0]] += n_wildcards
        return results

    @property
    def n_wildcards(self):
        return str(self).count(WILDCARD_VALUE)

    @property
    def name(self):
        return HAND_RANK_DICT[self.strength]

    @property
    def strength(self):
        card_counts = self.card_counts

        # 5 of a kind
        if not card_counts or card_counts.most_common()[0][1] == 5:
            return 7
        # 4 of a kind
        elif card_counts.most_common()[0][1] == 4:
            return 6
        # full house
        elif [c for _, c in card_counts.most_common()[:2]] == [3, 2]:
            return 5
        # 3 of a kind
        elif card_counts.most_common()[0][1] == 3:
            return 4
        # 2 pair
        elif all(c == 2 for _, c in card_counts.most_common()[:2]):
            return 3
        # 1 pair
        elif sum(1 for _, c in card_counts.most_common()[:2] if c == 2) == 1:
            return 2
        # high card
        return 1

    def _base_counts(self):
        return Counter(str(self))

    def __eq__(self, other):
        return self._base_counts() == other._base_counts()

    def __gt__(self, other):
        if self.strength > other.strength:
            return True

        if self.strength < other.strength:
            return False

        for card, other_card in zip(self.cards, other.cards):
            if card.strength == other_card.strength:
                continue
            return card > other_card
        return False

    def __str__(self):
        return "".join([card.label for card in self.cards])

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"cards={str(self)}, "
            f"n_wildcards={self.n_wildcards}, "
            f"strength={self.strength}, "
            f"name='{self.name}', "
            f"bid={self.bid}"
            ")"
        )


def calculate_solution(use_wildcards: bool = False):
    hands = sorted([Hand.from_text(line, use_wildcards) for line in data.split("\n")])
    return sum(hand.bid * rank for rank, hand in enumerate(hands, 1))


@aoc.part(1)
def solution_1():
    return calculate_solution(use_wildcards=False)


@aoc.part(2)
def solution_2():
    return calculate_solution(use_wildcards=True)


def main():
    print(solution_1())  # 251545216
    print(solution_2())  # 250384185


if __name__ == "__main__":
    main()
