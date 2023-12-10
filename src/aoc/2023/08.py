from io import StringIO
import aoc
import asyncio
from dataclasses import dataclass
from itertools import cycle


data = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)"""

# data = """LR

# 11A = (11B, XXX)
# 11B = (XXX, 11Z)
# 11Z = (11B, XXX)
# 22A = (22B, XXX)
# 22B = (22C, 22C)
# 22C = (22Z, 22Z)
# 22Z = (22B, 22B)
# XXX = (XXX, XXX)"""

# data = aoc.get_data_from_file(8)


STARTING_NODE = "AAA"
TARGET_NODE = "ZZZ"
LR_MAP = {"L": "left", "R": "right"}


@dataclass
class Node:
    value: str
    left: str
    right: str

    def __hash__(self) -> int:
        return hash(self.value)

    @classmethod
    def from_text(cls, text: str):
        value, left_right = text.split(" = ")
        left, right = left_right.strip("()").split(", ")
        return cls(value, left, right)


class Network:
    def __init__(self, lr_sequence: str):
        self.lr_seq = lr_sequence
        self._data = {}
        self._reset()

    def add_node(self, node: Node):
        self._data[node.value] = node

    @classmethod
    def from_file(cls, file):
        network = cls(file.readline().strip())

        for line in file:
            line = line.strip()
            if not line:
                continue
            network.add_node(Node.from_text(line))
        return network

    def steps_to_target(self, start: str = STARTING_NODE, target: str = TARGET_NODE):
        self._reset()
        steps = 0
        node = start

        while node != target:
            direction = LR_MAP[next(self)]
            node = getattr(self._data[node], direction)
            steps += 1
        return steps

    def _reset(self):
        self._lr_iterator = cycle(self.lr_seq)

    def __next__(self):
        return next(self._lr_iterator)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(lr_seq={self.lr_seq}), nodes={self._data})"


@aoc.part(1)
def solution_1():
    network = Network.from_file(StringIO(data))
    return network.steps_to_target()


def main():
    print(solution_1())  # 17263


if __name__ == "__main__":
    main()
