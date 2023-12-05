import aoc
from io import StringIO
from typing import List, Dict


data = aoc.get_data_from_file(5)


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


def parse_numbers(text: str) -> List[int]:
    return list(map(int, text.strip().split()))


def parse_almanac(file):
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
    return Almanac(seeds, maps)


@aoc.part(1)
def solution_1():
    almanac = parse_almanac(StringIO(data))
    return min(almanac.map_seeds_to("location"))


def main():
    print(solution_1())


if __name__ == "__main__":
    main()
