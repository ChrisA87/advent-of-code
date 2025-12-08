import aoc
from aoc.utils import parse_coords_3d, euclidean_distance, Point3D


data = """162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689"""

# data = aoc.get_data_from_file(8)


def calculate_distances(coords: list[Point3D]) -> list[tuple[Point3D, Point3D, float]]:
    distances = []
    for i, c1 in enumerate(coords):
        for j, c2 in enumerate(coords):
            if i < j:
                dist = euclidean_distance(c1, c2)
                distances.append((c1, c2, dist))
    return distances


def n_shortest_distances(
    coords: list[Point3D], n: int
) -> list[tuple[Point3D, Point3D, float]]:
    distances = calculate_distances(coords)
    distances.sort(key=lambda x: x[2])
    return distances[:n]


@aoc.part(1)
def part_1() -> int:
    junctions = parse_coords_3d(data)
    shortest_connections = n_shortest_distances(junctions, 10)
    for con in shortest_connections:
        print(con)
    # return shortest_connections


@aoc.part(2)
def part_2() -> int:
    pass


def main():
    print(part_1())
    print(part_2())


if __name__ == "__main__":
    main()
