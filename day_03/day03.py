

def most_common_bits(binary_strings: list[str]) -> str:
    num_bits = len(binary_strings[0])
    mcb_string = ""

    for i in range(num_bits):
        mcb_string += most_common_bit(binary_strings, i)

    return mcb_string


def most_common_bit(binary_strings: list[str], index: int) -> str:
    length = len(binary_strings)
    count = 0

    for line in binary_strings:
        if line[index] == "0":
            count += 1

    if count == length / 2:
        return "1"
    elif count > length / 2:
        return "0"
    else:
        return "1"
    

def flip(bitstring: str) -> str:
    result = ""
    for bitchar in bitstring:
        if bitchar == '0':
            result += "1"
        else:
            result += "0"
    return result


def calculate_power_consumption(bitstrings: list[str]) -> int:
    gamma = most_common_bits(bitstrings)
    gamma_rate = int(gamma, base=2)

    epsilon = flip(gamma)
    epsilon_rate = int(epsilon, base=2)

    return gamma_rate * epsilon_rate


def calculate_life_support_ratings(bitstrings: list[str]) -> str:
    num_bits = len(bitstrings[0])

    oxygen_generator = bitstrings.copy()
    C02_scrubber = bitstrings.copy()

    for i in range(num_bits):
        mcb = most_common_bit(oxygen_generator, i)

        oxygen_generator = list(filter(lambda bs: bs[i] == mcb, oxygen_generator))
        if len(oxygen_generator) == 1:
            break
    
    for i in range(num_bits):
        mcb = most_common_bit(C02_scrubber, i)
        lcb = flip(mcb)

        C02_scrubber = list(filter(lambda bs: bs[i] == lcb, C02_scrubber))
        if len(C02_scrubber) == 1:
            break

    oxygen_generator_rate = int(oxygen_generator[0], base=2)
    C02_scrubber_rate = int(C02_scrubber[0], base=2)

    return oxygen_generator_rate * C02_scrubber_rate


if __name__ == '__main__':
    file = open('./day_03/input.txt', 'r')
    input = [line.strip() for line in file.readlines()]

    # part 1
    print(calculate_power_consumption(input))

    # part 2
    print(calculate_life_support_ratings(input))
