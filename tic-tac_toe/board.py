import numpy as np


class Board:

    def __init__(self):
        self.board = np.zeros(9, dtype=np.int16)
        self.axis = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6]
        ]

    def __repr__(self):
        table = ""
        for index, cell in enumerate(self.board):
            table += str(cell)
            if index in [0, 1, 3, 4, 6, 7]:
                table += " │ "
            if index in [2, 5]:
                table += "\n"
                table += "──┼───┼──\n"
        return table.replace("0", " ").replace("1", "X").replace("2", "O")

    def get_free_places(self):
        return np.where(self.board == 0)[0]

    def can_place(self, index: int) -> bool:
        return self.board[index] == 0

    def place(self, index: int, marker: int) -> None:
        if self.can_place(index):
            self.board[index] = marker
        else:
            raise Exception(index, self.board)

    def get_winner(self) -> int | None:
        for a in self.axis:
            numbers, count = np.unique(self.board[a], return_counts=True)
            if count[0] == 3 and numbers[0] != 0:
                return numbers[0]
        return None

    def reset_board(self):
        self.board = np.zeros(9, dtype=np.int16)
