import chess
import chess.engine

class StockfishPlayer:
    def __init__(self):
        self.engine = chess.engine.SimpleEngine.popen_uci(r"/opt/homebrew/opt/stockfish/bin/stockfish")

    def make_move(self, board):
        
            result = self.engine.play(board, chess.engine.Limit(time=0.1))
            board.push(result.move)
            
            # TODO: call the hardware execution here
            
            print(board)
            print("----------------------------------------------")
            print("----------------------------------------------")
            self.engine.quit()
        
