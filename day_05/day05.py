

from dataclasses import dataclass
from enum import Enum

@dataclass
class Line:
    x1: int
    y1: int
    x2: int
    y2: int

    def __repr__(self):
        return f"({self.x1}, {self.y1}) -> ({self.x2}, {self.y2})"


class LineType(Enum):
    HORIZONTAL = 1
    VERTICAL = 2
    DIAGONAL = 3


class Map:
    def __init__(self, size):
        self.ocean_floor = [['.' for _ in range(size)] for _ in range(size)]

    def determine_linetype(self, line: Line) -> LineType:
        if line.x1 == line.x2:
            return LineType.HORIZONTAL
        elif line.y1 == line.y2:
            return LineType.VERTICAL
        elif abs(line.y2 - line.y1) == abs(line.x2 - line.x1):
            return LineType.DIAGONAL
        else:
            raise ValueError("Invalid line type.")

    def place_line(self, line: Line) -> None:
        match self.determine_linetype(line):
            case LineType.HORIZONTAL:
                if line.y1 <= line.y2:
                    for y in range(line.y1, line.y2 + 1):
                        self.update_spot(line.x1, y)
                else:
                    for y in range(line.y2, line.y1 + 1):
                        self.update_spot(line.x1, y)

            case LineType.VERTICAL:
                if line.x1 <= line.x2:
                    for x in range(line.x1, line.x2 + 1):
                        self.update_spot(x, line.y1)
                else:
                    for x in range(line.x2, line.x1 + 1):
                        self.update_spot(x, line.y1)

            case LineType.DIAGONAL:
                for d in range(abs(line.x2 - line.x1) + 1):
                    if line.x1 <= line.x2:
                        if line.y1 <= line.y2:
                            self.update_spot(line.x1 + d, line.y1 + d)
                        else:
                            self.update_spot(line.x1 + d, line.y1 - d)
                    else:
                        if line.y1 <= line.y2:
                            self.update_spot(line.x1 - d, line.y1 + d)
                        else:
                            self.update_spot(line.x1 - d, line.y1 - d)

    def update_spot(self, x: int, y: int) -> None:
        if self.ocean_floor[y][x] == '.':
            self.ocean_floor[y][x] = '1'
        else:
            self.ocean_floor[y][x] = str(int(self.ocean_floor[y][x]) + 1)

    def compute_overlaps(self, num: int) -> int:
        overlaps = 0
        for row in self.ocean_floor:
            for col in row:
                if col == '.':
                    continue
                else:
                    if int(col) >= num:
                        overlaps += 1
        return overlaps

    def __repr__(self):
        result = ""
        for row in self.ocean_floor:
            for col in row:
                result += col
            result += "\n"
        return result


def parse_line(line: str) -> Line:
    s = line.split(' -> ')
    begin, end = s[0], s[1]

    begin = begin.split(',')
    end = end.split(',')

    return Line(int(begin[0]), int(begin[1]), int(end[0]), int(end[1]))
    

def parse_lines(lines: list[str]) -> list[Line]:
    list_of_lines = []
    for line in lines:
        list_of_lines.append(parse_line(line))
    return list_of_lines


def find_dangerous_vents(lines: list[Line], map_size: int, num_overlaps: int) -> int:
    map = Map(map_size)
    for line in lines:
        map.place_line(line)
    return map.compute_overlaps(num_overlaps) 
    

if __name__ == '__main__':
    file = open('./day_05/input.txt', 'r')
    input = file.readlines()

    lines = parse_lines(input)

    # Part 1 & 2
    map_size = 1000
    num_overlaps = 2
    print(find_dangerous_vents(lines, map_size, num_overlaps))
