import aoc
from io import StringIO
from typing import List, Dict

data = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""


class IdMap:
    def __init__(self, name: str):
        self.name = name
        self._map = {}
    
    def update(self, d: dict):
        self._map.update(d)
        
    def __getitem__(self, key: int):
        return self._map.get(key, key)
    
    def __call__(self, key: int) -> int:
        return self.__getitem__(key)
    
    def __repr__(self):
        return f"IdMap(name={self.name}, n={len(self._map)})"

class Almanac:
    processing_order = (
        "seed_to_soil", "soil_to_fertilizer", "fertilizer_to_water", "water_to_light",
        "light_to_temperature", "temperature_to_humidity", "humidity_to_location")
    
    def __init__(self, seeds: List[int], maps: Dict[str, IdMap]):
        self.seeds = seeds
        self.maps = maps
    
    def __getattr__(self, name):
        try:
            return self.maps[name]
        except KeyError:
            raise AttributeError(f"{self.__class__.__name__} has no attribute '{name}'")
    
    def map_seeds_to(self, stage: str) -> List[int]:
        assert any(f"to_{stage}" in x for x in self.processing_order), f"{stage} is not a valid stage"
        results = []

        for seed in self.seeds:
            mapped_value = seed
            for process in self.processing_order:
                mapped_value = getattr(self, process)(mapped_value)
                if f"to_{stage}" in process:
                    break
            results.append(mapped_value)
        return results



def map_from_ranges(ranges):
    destination, source, length = parse_numbers(ranges)
    return dict(zip(range(source, source + length), range(destination, destination + length)))
    
    
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
            maps[current_map_name] = IdMap(current_map_name)
        elif line:
            maps[current_map_name].update(map_from_ranges(line))
    return Almanac(seeds, maps)

@aoc.part(1)
def solution_1():
    almanac = parse_almanac(StringIO(data))
    return min(almanac.map_seeds_to("location"))


def main():
    print(solution_1())
    
if __name__ == "__main__":
    main()
