from typing import List
import aoc

data = """7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ"""


class Tile:
    _types = {
        "|": ("vertical", {"north", "south"}),
        "-": ("horizontal", {"west", "east"}),
        "L": ("L-bend", {"north", "east"}),
        "J": ("L-bend", {"north", "west"}),
        "7": ("L-bend", {"west", "south"}),
        "F": ("L-bend", {"east", "south"}),
        ".": ("ground", set()),
        "S": ("starting-point", set()),
    }
    connections = {"north": "south", "south": "north", "east": "west", "west": "east"}

    def __init__(self, i: int, j: int, shape: str):
        self.i = i
        self.j = j
        self.shape = shape
        self.name, self.connections = self._types[shape]

    def __repr__(self):
        return self.shape

    def is_pipe(self) -> bool:
        if self.connections:
            return True
        return False


class PipeMap:
    starting_tile = "S"

    def __init__(self, grid: List[List[Tile]]):
        self.grid = grid

    @classmethod
    def from_data(cls, data: str):
        grid = []
        for i, line in enumerate(data.split("\n")):
            row = []
            for j, char in enumerate(line):
                row.append(Tile(i, j, char))
            grid.append(row)
        return cls(grid)

    def find_start_coords(self):
        for i, row in enumerate(self.grid):
            for j, tile in enumerate(row):
                if tile.shape == self.starting_tile:
                    return (i, j)

    def __str__(self) -> str:
        return "\n" + "\n".join([str(row) for row in self.grid])


@aoc.part(1)
def solution_1():
    pipe_map = PipeMap.from_data(data)
    print(pipe_map.find_start_coords())
    return pipe_map


def main():
    print(solution_1())


if __name__ == "__main__":
    main()
