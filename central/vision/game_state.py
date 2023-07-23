from img_processing import ImageProcessing
import cv2 as cv
from board_squares import BoardSquares
from extract_color import ExtractColor
from classify import Classify



class GameState:
    def __init__(self):
        self.processedImage = ImageProcessing()
        self.extractColor = ExtractColor()
        self.classify = Classify()
        
    def recent_humanMove(self):      #use the extracted board status and return the most recent human move
        recent_move = input("make a move")
        return recent_move

    
    def extractBoardStatus(self):    #Get the current status of the board
        image = cv.imread(imagePath, cv.IMREAD_COLOR)
        paddedImage = self.processedImage.add_margin(image) 
        coords = self.processedImage.squareCoords(image)
        features = []
        for i in range(len(coords)):
            croppedImage = self.extractColor.crop_image(paddedImage, coords[i])
            orangePercent, greenPercent, neitherPercent = self.extractColor.detect_color(croppedImage)
            features.append([orangePercent, greenPercent, neitherPercent])
        
        boardStatus = self.classify.predicState(features)
    
    

# x=GameState()
# y=x.showGameState()
    