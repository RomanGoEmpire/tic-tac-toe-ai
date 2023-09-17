import random
import numpy as np
from player import Player


class RandomPlayer(Player):

    def __init__(self, name: str, marker: int):
        super().__init__(name, marker)

    def play_move(self, board: np.array) -> tuple[int, int]:
        index = self.get_random_item(len(board[0]) - 1)
        return board[0][index], board[1][index]

    @staticmethod
    def get_random_item(length: int) -> int:
        return random.randint(0, length)
