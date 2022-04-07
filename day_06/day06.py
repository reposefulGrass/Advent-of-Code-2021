
MAX_FISH_TIMER = 8

class LaternfishSchool:
    def __init__(self, laternfish: list[int]):
        self.laternfish = [0 for _ in range(MAX_FISH_TIMER + 1)]
        for fish in laternfish:
            self.laternfish[fish] += 1

    def simulate(self, days: int) -> list[int]:
        for day in range(days):
            #print(f"day {day}: ", self.laternfish)
            self.pass_time()

    def pass_time(self) -> None:
        temp = [0 for _ in range(MAX_FISH_TIMER + 1)]
        
        temp[6] += self.laternfish[0]
        temp[8] += self.laternfish[0]
        for i in range(0, 8):
            temp[i] += self.laternfish[i+1]

        self.laternfish = temp

    def size(self) -> int:
        return sum(self.laternfish)


if __name__ == '__main__':
    file = open('./day_06/input.txt', 'r')
    input = file.read().strip()

    school = [int(fish) for fish in input.split(',')]

    # Part 1
    lfs1 = LaternfishSchool(school)
    lfs1.simulate(80)
    print(lfs1.size())

    # Part 2
    lfs2 = LaternfishSchool(school)
    lfs2.simulate(256)
    print(lfs2.size())
