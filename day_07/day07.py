

def calculate_median_fuel_cost(positions: list[int]) -> int:
    positions.sort()
    median_position = positions[len(positions) // 2]
    return sum(list(map(lambda p: abs(p - median_position), positions)))


def average_cost(position: int, average: int) -> int:
    d = abs(position - average)
    return (d * (d + 1)) // 2


def calculate_average_fuel_cost(positions: list[int]) -> int:
    average = sum(positions) // len(positions)
    return sum(list(map(lambda p: average_cost(p, average), positions)))


if __name__ == '__main__':
    file = open('./day_07/input.txt', 'r')
    input = file.read().strip()

    positions = [int(pos) for pos in input.split(',')]

    # Part 1
    print(calculate_median_fuel_cost(positions))

    # Part 2
    print(calculate_average_fuel_cost(positions))
