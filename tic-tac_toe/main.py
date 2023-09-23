from ai_player import AI
from game import Game
from random_player import RandomPlayer

if __name__ == '__main__':

    random_player = RandomPlayer("Random", 1)
    ai = AI("AI", 2, "model.keras")
    game = Game([random_player, ai])
    game.start_game()
