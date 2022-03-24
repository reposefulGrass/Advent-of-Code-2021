
def determine_depth_increases(input):
    assert len(input) > 2, "input too small."

    increased = 0
    prev_depth = 99999

    for depth in input:
        if depth > prev_depth:
            increased += 1
        prev_depth = depth

    return increased

def determine_window_increases(input):
    assert len(input) > 2, "input too small."

    increased = 0
    prev_window = 99999
    index = 0

    for _ in input[:-2]:
        window = input[index] + input[index + 1] + input[index + 2]
        if window > prev_window:
            increased += 1
        prev_window = window
        index += 1
    
    return increased


if __name__ == '__main__':
    file = open('./day_01/input.txt', 'r')
    input = [int(line) for line in file.readlines()]

    # Part 1
    print(determine_depth_increases(input))

    # Part 2
    print(determine_window_increases(input))

