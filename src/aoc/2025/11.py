import networkx as nx

import aoc


data = """aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out"""

data = aoc.get_data_from_file(11)

YOU = "you"
OUT = "out"
SERVER = "svr"
DIGITAL_TO_ANALOG = "dac"
FAST_FOURIER_TRANSFORM = "fft"


def parse_data(data: str) -> dict[str, list[str]]:
    result = {}
    for line in data.splitlines():
        key, vals = line.split(": ")
        result[key] = vals.split()
    return result


def build_graph(edges: dict[str, list[str]]) -> nx.DiGraph:
    G = nx.DiGraph()
    for src, dsts in edges.items():
        for dst in dsts:
            G.add_edge(src, dst)
    return G


@aoc.part(1)
def part_1() -> int:
    G = build_graph(parse_data(data))
    paths = list(nx.all_simple_paths(G, source=YOU, target=OUT))
    return len(paths)


@aoc.part(2)
def part_2() -> int:
    pass
    # G = build_graph(parse_data(data))
    # result = 0
    # paths = nx.all_simple_paths(G, source=SERVER, target=OUT, cutoff=100)
    # for i, path in enumerate(paths):
    #     print(f" Chekcing {i}: {path}")
    #     if DIGITAL_TO_ANALOG in path and FAST_FOURIER_TRANSFORM in path:
    #         result += 1
    # return result


def main():
    print(part_1())
    print(part_2())


if __name__ == "__main__":
    main()
