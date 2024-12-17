from dataclasses import dataclass
from typing import Callable
import aoc

data = """Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0"""

data = aoc.get_data_from_file(17, 2024)


def three_bit(n: int):
    return bin(n)[2:].zfill(3)


@dataclass
class Registry:
    A: int
    B: int
    C: int


class Program:

    def __init__(self, registry: Registry, *ops):
        self.registry = registry
        self.ops = ops
        self.pointer = 0
        self.output = []

    def __repr__(self):
        return f"Program(registry={self.registry}, ops={self.ops})"

    def opcode(self, code: int) -> Callable:
        opcodes = {
            0: self.adv,
            1: self.bxl,
            2: self.bst,
            3: self.jnz,
            4: self.bxc,
            5: self.out,
            6: self.bdv,
            7: self.cdv,
        }
        return opcodes[code]

    def eval_combo(self, combo: int):
        if 0 <= combo <= 3:
            return combo
        elif combo == 4:
            return self.registry.A
        elif combo == 5:
            return self.registry.B
        elif combo == 6:
            return self.registry.C
        raise ValueError(f"{combo} is not a valid combo operand.")

    def adv(self, combo: int):
        numerator = self.registry.A
        denominator = 2 ** self.eval_combo(combo)
        self.registry.A = numerator // denominator

    def bxl(self, literal: int):
        self.registry.B = self.registry.B ^ literal

    def bst(self, combo: int):
        self.registry.B = self.eval_combo(combo) % 8

    def jnz(self, literal: int):
        if self.registry.A == 0:
            return
        return literal

    def bxc(self, literal: int):
        self.registry.B = self.registry.B ^ self.registry.C

    def out(self, combo: int):
        self.output.append(self.eval_combo(combo) % 8)

    def bdv(self, combo: int):
        numerator = self.registry.A
        denominator = 2 ** self.eval_combo(combo)
        self.registry.B = numerator // denominator

    def cdv(self, combo: int):
        numerator = self.registry.A
        denominator = 2 ** self.eval_combo(combo)
        self.registry.C = numerator // denominator

    def run(self):
        while self.pointer <= len(self.ops) - 1:
            op = self.ops[self.pointer]
            operand = self.ops[self.pointer + 1]
            func = self.opcode(op)
            if (result := func(operand)) is None:
                self.pointer += 2
            else:
                self.pointer = result
        return ",".join(map(str, self.output))


def parse_data(data: str) -> Program:
    registry, ops = data.split("\n\n")
    registry = Registry(
        *map(int, (line.split(" ")[-1] for line in registry.splitlines()))
    )
    return Program(registry, *map(int, ops.strip().split(" ")[-1].split(",")))


@aoc.part(1)
def part_1() -> int:
    program = parse_data(data)
    return program.run()


@aoc.part(2)
def part_2() -> int:
    pass


def main():
    print(part_1())
    print(part_2())


if __name__ == "__main__":
    main()
