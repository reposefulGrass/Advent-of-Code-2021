

class LaternfishSchool:
    def __init__(self, laternfish: list[int]):
        self.laternfish = laternfish

    def simulate(self, days: int) -> list[int]:
        for day in range(days):
            #print(f"day {day}: ", self.laternfish)
            self.pass_time()

    def pass_time(self):
        for i in range(len(self.laternfish)):
            if self.laternfish[i] == 0:
                self.laternfish[i] = 6
                self.laternfish.append(8)
            else:
                self.laternfish[i] -= 1

    def size(self):
        return len(self.laternfish)


if __name__ == '__main__':
    file = open('./day_06/input.txt', 'r')
    input = file.read().strip()

    school = [int(fish) for fish in input.split(',')]

    # Part 1
    lfs = LaternfishSchool(school)
    lfs.simulate(80)
    print(lfs.size())
