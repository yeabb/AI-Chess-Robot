from img_processing import ImageProcessing
import cv2 as cv
from board_squares import BoardSquares

class GameState:
    def __init__(self):
        self.img=cv.imread("/Users/yab/Desktop/projects/yolo/corner/contours.jpeg")
        
    def recent_humanMove(self):      #use the extracted board status and return the most recent human move
        recent_move = input("make a move")
        return recent_move

    
    def extractBoardStatus(self):    #Get the current status of the board
        pass
    
    

# x=GameState()
# y=x.showGameState()
    