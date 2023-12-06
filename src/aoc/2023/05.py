import aoc
from io import StringIO
from typing import List, Dict


data = aoc.get_data_from_file(5)

# data = """seeds: 79 14 55 13

# seed-to-soil map:
# 50 98 2
# 52 50 48

# soil-to-fertilizer map:
# 0 15 37
# 37 52 2
# 39 0 15

# fertilizer-to-water map:
# 49 53 8
# 0 11 42
# 42 0 7
# 57 7 4

# water-to-light map:
# 88 18 7
# 18 25 70

# light-to-temperature map:
# 45 77 23
# 81 45 19
# 68 64 13

# temperature-to-humidity map:
# 0 69 1
# 1 0 69

# humidity-to-location map:
# 60 56 37
# 56 93 4"""


class IdMap:
    def __init__(self, destination, source, length):
        self.destination = destination
        self.source = source
        self.length = length
        self.offset = destination - source
        self._source_range = range(source, source + length)

    def __contains__(self, value):
        return value in self._source_range

    def __getitem__(self, item):
        return item + self.offset

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(source={self.source}, dest={self.destination}, length={self.length})"


class IdMapper:
    def __init__(self, name: str):
        self.name = name
        self.maps = []

    def add_map(self, map_: IdMap):
        self.maps.append(map_)

    def __getitem__(self, key: int) -> int:
        for m in self.maps:
            if key in m:
                return m[key]
        return key

    def __call__(self, key: int) -> int:
        return self.__getitem__(key)

    def __repr__(self):
        return f"IdMapper(name={self.name}, n_ranges={len(self.maps)})"


class Almanac:
    processing_order = (
        "seed_to_soil",
        "soil_to_fertilizer",
        "fertilizer_to_water",
        "water_to_light",
        "light_to_temperature",
        "temperature_to_humidity",
        "humidity_to_location",
    )

    def __init__(self, seeds: List[int], maps: Dict[str, IdMapper]):
        self.seeds = seeds
        self.mappers = maps

    def __getattr__(self, name):
        try:
            return self.mappers[name]
        except KeyError:
            raise AttributeError(f"{self.__class__.__name__} has no attribute '{name}'")

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(n_seeds={len(self.seeds)}, n_mappers={len(self.mappers)})"

    def map_seeds_to(self, stage: str) -> List[int]:
        assert any(
            f"to_{stage}" in x for x in self.processing_order
        ), f"{stage} is not a valid stage"
        results = []

        for seed in self.seeds:
            mapped_value = seed
            for process in self.processing_order:
                mapped_value = getattr(self, process)(mapped_value)
                if f"to_{stage}" in process:
                    break
            results.append(mapped_value)
        return results


class AlmanacV2(Almanac):
    def __init__(self, seeds: List[int], maps: Dict[str, IdMapper]):
        super().__init__(seeds, maps)
        self._seeds_processed = False
        self.seeds = self._process_seed_ranges()

    def _process_seed_ranges(self):
        if self._seeds_processed:
            return self.seeds

        results = []
        for i in range(0, len(self.seeds), 2):
            start = self.seeds[i]
            length = self.seeds[i + 1]
            results.append(range(start, start + length))
        self._seeds_processed = True
        return results


def parse_numbers(text: str) -> List[int]:
    return list(map(int, text.strip().split()))


def parse_almanac(file, almanac_cls=Almanac):
    seeds = parse_numbers(file.readline().replace("seeds: ", ""))
    maps = {}

    current_map_name = None

    for line in file:
        line = line.strip()

        if line.endswith("map:"):
            current_map_name = line.split()[0].replace("-", "_")
            maps[current_map_name] = IdMapper(current_map_name)
        elif line:
            maps[current_map_name].add_map(IdMap(*parse_numbers(line)))
    return almanac_cls(seeds, maps)


@aoc.part(1)
def solution_1():
    almanac = parse_almanac(StringIO(data))
    return min(almanac.map_seeds_to("location"))


@aoc.part(2)
def solution_2():
    almanac = parse_almanac(StringIO(data), almanac_cls=AlmanacV2)
    print(almanac)
    # return min(almanac.map_seeds_to("location"))


def main():
    print(solution_1())
    print(solution_2())


if __name__ == "__main__":
    main()
