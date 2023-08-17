import chess

class HumanPlayer:
    def __init__(self):
        pass
    
    def make_move(self, board, humanMove):
        board.push(humanMove)
        print(board)