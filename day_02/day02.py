
def determine_position(input: str, part_two: bool):
    horizontal_position, depth, aim = 0, 0, 0

    for line in input:
        split_line = line.split(' ')
        assert len(split_line) == 2, "incorrect format."

        direction, amount = split_line[0], int(split_line[1])

        if direction == "forward":
            horizontal_position += amount
            if part_two:
                depth += (amount * aim)

        elif direction == "down":
            if part_two:
                aim += amount
            else:
                depth += amount

        elif direction == "up":
            if part_two:
                aim -= amount
            else:
                depth -= amount

    return horizontal_position * depth

if __name__ == '__main__':
    file = open('./day_02/input.txt', 'r')
    input = file.readlines()

    # Part One
    print(determine_position(input, part_two=False))

    # Part Two
    print(determine_position(input, part_two=True))
