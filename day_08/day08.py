
def determine_unique_digits(lines: list[str]) -> int:
    count = 0

    for line in lines:
        line = line.strip().split(" | ")
        input_value, output_value = line[0], line[1]
        digits = output_value.split(" ")
        for digit in digits:
            if len(digit) in (2, 3, 4, 7):
                count += 1
    
    return count

if __name__ == '__main__':
    file = open('./day_08/input.txt', 'r')
    input = file.readlines()

    # Part 1
    print(determine_unique_digits(input))
