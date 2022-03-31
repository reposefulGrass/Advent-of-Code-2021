
from dataclasses import dataclass
from termcolor import colored


@dataclass
class Slot:
    value: int
    marked: bool

    def __repr__(self):
        if self.marked:
            return colored(f"{self.value:02}", 'blue')
        else:
            return f"{self.value:02}"


class Board:
    def __init__(self, width: int):
        self.width = width
        self.board = [[None for _ in range(width)] for _ in range(width)]

    def __repr__(self):
        result = ""
        for row in range(self.width):
            for col in range(self.width):
                result += (str(self.board[row][col]) + " ")
            result += "\n"
        return result

    def read_board(self, input: list[str]) -> None:
        row = 0
        col = 0
        for line in input:
            for number in [int(num) for num in line.strip().split()]:
                self.board[row][col] = Slot(number, False)
                col += 1
            row += 1
            col = 0

    def mark(self, number: int) -> None:
        for row in range(self.width):
            for col in range(self.width):
                if self.board[row][col].value == number:
                    self.board[row][col].marked = True
                    return

    def has_bingo(self) -> bool:
        bingo = False

        for i in range(self.width):
            # Horizontal Check
            entire_row = True

            for j in range(self.width):
                if self.board[i][j].marked == False:
                    entire_row = False

            if entire_row == True:
                bingo = True

            # Vertical Check
            entire_col = True

            for j in range(self.width):
                if self.board[j][i].marked == False:
                    entire_col = False
            
            if entire_col == True:
                bingo = True
        
        return bingo

    def unmarked_sum(self) -> int:
        sum = 0
        for row in range(self.width):
            for col in range(self.width):
                if self.board[row][col].marked == False:
                    sum += self.board[row][col].value
        return sum


class Bingo:
    def __init__(self, input: list[str]):
        self.balls = [int(number) for number in input[0].strip().split(",")]
        self.boards = []

        for lineno in range(2, len(input), 6):
            board = Board(5)
            board.read_board(input[lineno:lineno+5])
            self.boards.append(board)

    def play(self) -> int:
        for ball in self.balls:
            for board in self.boards:
                board.mark(ball)
                if board.has_bingo():
                    #print(board)
                    return (board.unmarked_sum() * ball)

    def play_till_last(self) -> int:
        wins = [0 for _ in range(len(self.boards))]

        for ball in self.balls:
            boardno = 0
            for board in self.boards:
                board.mark(ball)

                if board.has_bingo():
                    wins[boardno] = 1

                if sum(wins) == len(self.boards):
                    return (board.unmarked_sum() * ball)
                
                boardno += 1


if __name__ == '__main__':
    file = open('./day_04/input.txt', 'r')
    input = file.readlines()

    # Part 1
    print(Bingo(input).play())

    # Part 2
    print(Bingo(input).play_till_last())
