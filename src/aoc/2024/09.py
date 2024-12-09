from itertools import chain
from typing import List
import aoc

data = """2333133121414131402"""

data = aoc.get_data_from_file(9, 2024)


def parse_data(data: str) -> List[int | str]:
    files = [[i] * int(n) for i, n in enumerate(data[::2])]
    free = [["."] * int(n) for n in data[1::2]]
    if len(free) < len(files):
        free.append([])
    return files, free


def compact_drive(files: List[List[int]], free: List[List[str]]) -> List[int | str]:
    drive = list(chain(*chain(*zip(files, free))))
    i = 0
    j = len(drive) - 1
    while i < j:
        if drive[i] != ".":
            i += 1
        if drive[j] == ".":
            j -= 1
        if drive[i] == "." and drive[j] != ".":
            drive[i], drive[j] = drive[j], drive[i]
    return drive


def compact_drive_v2(files: List[List[int]], free: List[str]) -> List[int | str]:
    drive = list(chain(*zip(files, free)))
    j = len(drive) - 1

    while j > 0:
        data_block = drive[j]
        n = len(data_block)
        for i in range(1, len(drive[:j]), 2):
            free_block = drive[i]
            if n > 0 and free_block.count(".") >= n:
                idx = free_block.index(".")
                drive[i][idx : idx + n] = data_block
                drive[j] = ["."] * n
                break
        j -= 1

    return list(chain(*drive))


def get_checksum(drive: List[int | str]) -> int:
    result = 0
    for i, val in enumerate(drive):
        if val == ".":
            continue
        result += i * int(val)
    return result


@aoc.part(1)
def part_1() -> int:
    files, free = parse_data(data)
    drive = compact_drive(files, free)
    return get_checksum(drive)


@aoc.part(2)
def part_2() -> int:
    files, free = parse_data(data)
    drive = compact_drive_v2(files, free)
    return get_checksum(drive)


def main():
    print(part_1())
    print(part_2())


if __name__ == "__main__":
    main()
