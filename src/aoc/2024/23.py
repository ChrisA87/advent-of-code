from typing import List, Set, Tuple
import aoc
import networkx as nx

data = """kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn"""

data = aoc.get_data_from_file(23, 2024)


def create_graph(data: str) -> nx.Graph:
    G = nx.Graph()
    for line in data.splitlines():
        G.add_edge(*line.split("-"))
    return G


def get_connected_triplets(graph: nx.Graph) -> Set[Tuple[str]]:
    triplets = set()
    for node in graph.nodes():
        neighbors = list(graph.neighbors(node))
        for i in range(len(neighbors)):
            for j in range(i + 1, len(neighbors)):
                if graph.has_edge(neighbors[i], neighbors[j]):
                    triplets.add(tuple(sorted([node, neighbors[i], neighbors[j]])))
    return triplets


def get_connected_sets(graph: nx.Graph) -> Set[Tuple[str]]:
    connected_sets = set()
    for connected in nx.find_cliques(graph):
        connected_sets.add(tuple(sorted(list(connected))))
    return connected_sets


@aoc.part(1)
def part_1() -> int:
    result = 0
    G = create_graph(data)
    for triplet in get_connected_triplets(G):
        if any(node.startswith("t") for node in triplet):
            result += 1
    return result


@aoc.part(2)
def part_2() -> int:
    G = create_graph(data)
    connected_sets = sorted(get_connected_sets(G), key=len)
    return ",".join(connected_sets[-1])


def main():
    print(part_1())
    print(part_2())


if __name__ == "__main__":
    main()
