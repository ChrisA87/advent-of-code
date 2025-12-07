def parse_grid(data: str) -> list[list[str]]:
    return list(map(list, data.splitlines()))
