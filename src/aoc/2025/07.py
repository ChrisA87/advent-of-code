import time
import aoc
from aoc.utils import parse_grid


data = """.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
..............."""

data = aoc.get_data_from_file(7)


@aoc.part(1)
def part_1() -> int:
    result = 0
    grid = parse_grid(data)
    beam_indices = {
        0: {
            grid[0].index("S"),
        }
    }
    for row, line in enumerate(grid[1:], 1):
        beams = beam_indices[row - 1].copy()
        for idx in beams.copy():
            if line[idx] == "^":
                result += 1
                beams.remove(idx)
                beams.update({idx - 1, idx + 1})
        beam_indices[row] = beams
    return result


@aoc.part(2)
def part_2() -> int:
    grid = parse_grid(data)
    timelines = [[1 if x == "S" else 0 for x in grid[0]]]

    beam_indices = {
        0: {
            grid[0].index("S"),
        }
    }
    for row, line in enumerate(grid[1:], 1):
        beams = beam_indices[row - 1].copy()
        timeline = timelines[-1][:]
        for idx in beams.copy():
            prev = timelines[-1][idx]
            if line[idx] == "^":
                timeline[idx - 1] += prev
                timeline[idx + 1] += prev
                timeline[idx] = 0
                beams.remove(idx)
                beams.update({idx - 1, idx + 1})
        beam_indices[row] = beams
        timelines.append(timeline)
    # for t in timelines:
    #     print(t)
    return sum(timelines[-1])


def main():
    print(part_1())
    print(part_2())


if __name__ == "__main__":
    main()
