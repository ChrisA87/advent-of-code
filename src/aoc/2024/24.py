from typing import Dict, Tuple
import aoc

data = """x00: 1
x01: 0
x02: 1
x03: 1
x04: 0
y00: 1
y01: 1
y02: 1
y03: 1
y04: 1

ntg XOR fgs -> mjb
y02 OR x01 -> tnw
kwq OR kpj -> z05
x00 OR x03 -> fst
tgd XOR rvg -> z01
vdt OR tnw -> bfw
bfw AND frj -> z10
ffh OR nrd -> bqk
y00 AND y03 -> djm
y03 OR y00 -> psh
bqk OR frj -> z08
tnw OR fst -> frj
gnj AND tgd -> z11
bfw XOR mjb -> z00
x03 OR x00 -> vdt
gnj AND wpb -> z02
x04 AND y00 -> kjc
djm OR pbm -> qhw
nrd AND vdt -> hwm
kjc AND fst -> rvg
y04 OR y02 -> fgs
y01 AND x02 -> pbm
ntg OR kjc -> kwq
psh XOR fgs -> tgd
qhw XOR tgd -> z09
pbm OR djm -> kpj
x03 XOR y03 -> ffh
x00 XOR y04 -> ntg
bfw OR bqk -> z06
nrd XOR fgs -> wpb
frj XOR qhw -> z04
bqk OR frj -> z07
y03 OR x01 -> nrd
hwm AND bqk -> z03
tgd XOR rvg -> z12
tnw OR pbm -> gnj"""

data = aoc.get_data_from_file(24, 2024)


def parse_data(data: str) -> Tuple[Dict[str, int], Dict[str, str]]:
    wire_values, gate_connections = data.split("\n\n")
    wire_values = {
        k: int(v) for k, v in (line.split(": ") for line in wire_values.splitlines())
    }
    gate_connections = [
        (tuple(k.split()), v)
        for k, v in (line.split(" -> ") for line in gate_connections.splitlines())
    ]
    return wire_values, gate_connections


def eval_gates(gate1, logic, gate2) -> int:
    if logic == "AND":
        return gate1 & gate2
    elif logic == "OR":
        return gate1 | gate2
    return gate1 ^ gate2


def solve(wire_values: Dict[str, int]) -> int:
    bin_str = "".join(
        map(
            str,
            (
                wire_values.get(k)
                for k in sorted(
                    (k for k in wire_values if k.startswith("z")), reverse=True
                )
            ),
        )
    )
    return int(bin_str, 2)


@aoc.part(1)
def part_1() -> int:
    wire_values, gate_connections = parse_data(data)
    while gate_connections:
        (g1, op, g2), g3 = gate_connections.pop()
        if (g1_val := wire_values.get(g1)) is None or (
            g2_val := wire_values.get(g2)
        ) is None:
            gate_connections.insert(0, ((g1, op, g2), g3))
            continue

        wire_values[g3] = eval_gates(g1_val, op, g2_val)
    return solve(wire_values)


@aoc.part(2)
def part_2() -> int:
    pass


def main():
    print(part_1())
    print(part_2())


if __name__ == "__main__":
    main()
