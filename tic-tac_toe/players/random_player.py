import random
import numpy as np
from player import Player


class RandomPlayer(Player):

    def __init__(self, name: str, marker: int):
        super().__init__(name, marker)

    def play_move(self, free_places: np.array) -> int:
        return np.random.choice(free_places)
