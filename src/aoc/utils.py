from collections import namedtuple


Point = namedtuple("Point", ["x", "y"])
Point3D = namedtuple("Point3D", ["x", "y", "z"])


def parse_grid(data: str) -> list[list[str]]:
    return list(map(list, data.splitlines()))


def parse_coords(data: str) -> list[Point]:
    return [Point(*tuple(map(int, line.split(",")))) for line in data.splitlines()]


def parse_coords_3d(data: str) -> list[Point3D]:
    return [Point3D(*tuple(map(int, line.split(",")))) for line in data.splitlines()]


def manhattan_distance(p1: Point | Point3D, p2: Point | Point3D) -> int:
    return sum(abs(a - b) for a, b in zip(p1, p2))


def euclidean_distance(p1: Point | Point3D, p2: Point | Point3D) -> float:
    return sum((a - b) ** 2 for a, b in zip(p1, p2)) ** 0.5
