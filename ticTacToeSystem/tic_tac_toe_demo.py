from tic_tac_toe_system import TicTacToeSystem
class TicTacToeDemo:
    @staticmethod
    def run():
        game = TicTacToeSystem()
        game.play_game()

if __name__ == "__main__":
    TicTacToeDemo.run()