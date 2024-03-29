import sys
sys.path.append('central/vision')
import chess
from central.logic.human_player import HumanPlayer
from central.logic.ai_player import StockfishPlayer
from central.vision.game_state import GameState



def main():
    board=chess.Board()
    
    while not board.is_game_over():
        game_state = GameState()
        
        #Human makes a move
        human_move = game_state.recentHumanMove(board)
        human_player = HumanPlayer()
        human_player.make_move(board, human_move)
        
        #AI makes a move
        ai_player = StockfishPlayer()
        ai_player.make_move(board)
  
main()
