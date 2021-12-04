class Board:
    def __init__(self, grid):
        self._grid = []
        self._marked = set()
        for line in grid:
            self._grid.append(list(map(lambda x: int(x), line)))

    def unmarked_sum(self):
        res = 0
        for line in self._grid:
            for n in line:
                if n not in self._marked:
                    res += n
        return res

    def bingo(self, x):
        self._marked.add(x)
        # check rows:
        for line in self._grid:
            found = True
            for n in line:
                if n not in self._marked:
                    found = False
            if found:
                return True
        # check columns:
        for i in range(len(self._grid[0])):
            found = True
            for line in self._grid:
                if line[i] not in self._marked:
                    found = False
            if found:
                return True
        return False


class BingoGame:
    def __init__(self, input_lines):
        self._sequence = list(map(lambda x: int(x), input_lines[0].strip().split(',')))
        self._boards = []
        i = 2
        while i < len(input_lines):
            grid = []
            while i < len(input_lines) and input_lines[i].strip() != '':
                grid.append(list(input_lines[i].split()))
                i += 1
            self._boards.append(Board(grid))
            i += 1

    def play_to_win(self):
        for x in self._sequence:
            for board in self._boards:
                if board.bingo(x):
                    print(board.unmarked_sum() * x)
                    return

        print("no winner")

    def play_to_lose(self):
        for x in self._sequence:
            boards_to_remove = []
            for board in self._boards:
                if board.bingo(x):
                    boards_to_remove.append(board)
            for board in boards_to_remove:
                self._boards.remove(board)
            if len(self._boards) == 0:
                if len(boards_to_remove) != 1:
                    print("Unexpected multiple losers")
                else:
                    print(boards_to_remove[0].unmarked_sum() * x)
                return


def main():
    f = open("day04.txt")
    lines = f.readlines()
    # part I:
    game = BingoGame(lines)
    game.play_to_win()
    # part II:
    game = BingoGame(lines)
    game.play_to_lose()


if __name__ == '__main__':
    main()
