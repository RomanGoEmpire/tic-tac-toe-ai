import numpy as np


class Board:

    def __init__(self):
        self.board = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])

    def __repr__(self):
        table = ""
        for i, row in enumerate(self.board):
            for j, cell in enumerate(row):
                table += str(cell)
                if j < 2:
                    table += " │ "
            table += "\n"
            if i < 2:
                table += "──┼───┼──\n"
        return table.replace("0", " ").replace("1", "X").replace("2", "O")

    def get_free_places(self):
        return np.where(self.board == 0)

    def can_place(self, x, y) -> bool:
        return self.board[x, y] == 0

    def place(self, x: int, y: int, marker: int) -> None:
        if self.can_place(x, y):
            self.board[x, y] = marker
        else:
            raise Exception(x, y, self.board)

    def get_winner(self) -> int | None:
        for row in self.board:
            unique, counts = np.unique(row, return_counts=True)
            if counts[0] == 3 and unique[0] != 0:
                return unique[0]
        for index in range(3):
            unique, counts = np.unique(self.board[:, index], return_counts=True)
            if counts[0] == 3 and unique[0] != 0:
                return unique[0]
        if (self.board[0, 0] == self.board[1, 1] == self.board[2, 2] and self.board[1, 1]) != 0 or \
                (self.board[0, 2] == self.board[1, 1] == self.board[2, 0] and self.board[1, 1] != 0):
            return self.board[1, 1]
        return None

    def reset_board(self):
        self.board = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])

