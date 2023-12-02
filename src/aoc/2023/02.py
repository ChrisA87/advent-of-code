import aoc


data = aoc.get_data_from_file(2).split("\n")

bag = {"red": 12, "green": 13, "blue": 14}


def process_id(text: str) -> int:
    return int(text.replace("Game ", ""))


def process_result(text: str) -> dict:
    result = {}
    for v in text.split(", "):
        number, color = v.split(" ")
        result[color] = int(number)
    return result


def process_results(text: str) -> list:
    return [process_result(result) for result in text.split("; ")]


def process_game(text: str) -> dict:
    id_, results = text.split(": ")
    return process_id(id_), process_results(results)


def result_is_possible(result: dict):
    return all([number <= bag.get(color) for color, number in result.items()])


def game_is_possible(game: dict):
    return all([result_is_possible(result) for result in game])


def get_min_cubes(game: list):
    result = {}
    for cubes in game:
        for color, number in cubes.items():
            if result.get(color, 0) < number:
                result[color] = number
    return result


def product(values: list) -> int:
    result = 1
    for value in values:
        result *= value
    return result


@aoc.part(1)
def solution_1():
    possible_ids = []

    for line in data:
        id_, game = process_game(line)
        if game_is_possible(game):
            possible_ids.append(id_)
    return sum(possible_ids)


@aoc.part(2)
def solution_2():
    powers = []
    for line in data:
        _, game = process_game(line)
        min_cubes = get_min_cubes(game)
        powers.append(product(min_cubes.values()))
    return sum(powers)


def main():
    print(solution_1())
    print(solution_2())


if __name__ == "__main__":
    main()
