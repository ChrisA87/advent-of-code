from typing import List
import aoc
import numpy as np

data = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""

data = aoc.get_data_from_file(9)


class Report:
    def __init__(self, values: List[int]):
        self.values = np.array(values)

    @classmethod
    def from_text(cls, text: str):
        return cls(
            list(
                map(int, text.strip().split()),
            )
        )

    def extrapolate(self):
        vals = []
        arr = self.values

        while not np.all(arr == 0):
            arr = np.diff(arr)
            vals.append(arr[-1])
        return self.values[-1] + sum(vals)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(values={self.values})"


def solution_1():
    extrapolated_values = []
    for line in data.split("\n"):
        report = Report.from_text(line)
        extrapolated_values.append(report.extrapolate())
    return sum(extrapolated_values)


def main():
    print(solution_1())


if __name__ == "__main__":
    main()
