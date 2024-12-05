class TicTacToe:
    def __init__(self):
        self.board = [["-" for _ in range(3)] for _ in range(3)]
    
    def get_board(self):
        for row in self.board:
            for cell in row:
                print(cell, end=" ")
            print()
    
    def get_score(self, value):
        max_score = 0
        for row in self.board:
            score = 0
            for cell in row:
                if cell != value:
                    break
                score += 1
            max_score = max(max_score, score)
        
        for col in range(3):
            score = 0
            for row in range(3):
                if self.board[row][col]!=value:
                    break
                score += 1
            max_score = max(max_score, score)
        
        score = 0
        for val in range(3):
            if self.board[val][val]!=value:
                break
            score += 1
        max_score = max(max_score, score)
        
        score = 0
        for val in range(3):
            if self.board[val][2-val]!=value:
                break
            score += 1
        max_score = max(max_score, score)
        return max_score


    def place_position(self, row, cell, value):
        if row>2 or cell>2 or self.board[row][cell] != "-":
            print("Invalid position")
            return False

        self.board[row][cell] = value
        self.get_board()
        score = self.get_score(value)

        if score == 3:
            return True
    