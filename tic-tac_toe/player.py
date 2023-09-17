import numpy as np


class Player:

    def __init__(self, name: str, marker: int):
        self.name = name
        self.marker = marker

    def play_move(self, board: np.array) -> tuple[int, int]:
        return 0, 0
