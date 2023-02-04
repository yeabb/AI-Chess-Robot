import chess

class HumanPlayer:
    def __init__(self):
        pass
    def make_move(self, board, move):
        board.push_san(move)
        print(board)
