import img_processing
from game_state import GameState
import cv2 as cv
import chess

def main():
    # img=cv.imread("/Users/yab/Desktop/projects/yolo/corner/contours.jpeg")
    # x=GameState()
    # # y=x.mapBoardSquares()
    # z=x.coordsTosquaresMap()
    # print(z)
    board=chess.Board()
    print(type(board))

main()