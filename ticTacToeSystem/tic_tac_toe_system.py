from tic_tac_toe import TicTacToe
from player_enum import Player
from users import User
class TicTacToeSystem:
    def __init__(self):
        self.game = TicTacToe()
    
    def play_game(self):
        player1 = User(input("Enter player 1 name"), Player.x1.value)
        player2 = User(input("Enter player 2 name "), Player.x2.value)
        moves = 1
        while moves is not 9:
            if moves % 2 == 1:
                name = player1.name
            else:
                name = player2.name
            coordinates = input(f"{name} - Enter row and col value seperated with space")

            row, col = map(int, coordinates.split())
            val = player1.symbol if name==player1.name else player2.symbol
            result = self.game.place_position(row,col,val)
            if result == True:
                print(f"Congrats {name} you won")
                break
            elif result is None:
                moves+=1
            if moves == 9:
                print("It's a tie")
                break