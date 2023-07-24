import sys
sys.path.append("/Users/yab/Desktop/projects/AI-Chess-Robot/central/data")
import cv2 as cv
from img_processing import ImageProcessing
from board_squares import BoardSquares
from extract_color import ExtractColor
from classify import Classify
from board_squares import BoardSquares
import chess



class GameState:
    def __init__(self):
        self.processedImage = ImageProcessing()
        self.extractColor = ExtractColor()
        self.classify = Classify()
        self.boardSquares = BoardSquares()
        
    def recentHumanMove(self, board):      #use the extracted board status and return the most recent human move
        currBoardStatus = self.extractBoardStatus()
        recentMoveSan = self.findMove(board, currBoardStatus).strip()
        recentMove = chess.Move.from_uci(recentMoveSan)
        return recentMove

    
    def extractBoardStatus(self):    #Get the current status of the board
        image = cv.imread(imagePath, cv.IMREAD_COLOR)
        paddedImage = self.processedImage.add_margin(image) 
        coords = self.processedImage.squareCoords(image)
        features = []
        for i in range(len(coords)):
            croppedImage = self.extractColor.crop_image(paddedImage, coords[i])
            orangePercent, greenPercent, neitherPercent = self.extractColor.detect_color(croppedImage)
            features.append([orangePercent, greenPercent, neitherPercent])
        
        boardStatus = self.classify.predictState(features)
    
    def findMove(self, prevBoardStatus, currBoardStatus):
        prevBoardStatusList = self.chessBoardToList(prevBoardStatus)
        n = len(prevBoardStatusList)
        for i in range(n):
            if prevBoardStatusList[i] != currBoardStatus[i]:
                if currBoardStatus[i] == 0:
                    originSquareIndex = i
                else:
                    destinationSquareIndex = i
        originSquare = self.getSquareNameByIndex(originSquareIndex)
        destinationSquare = self.getSquareNameByIndex(destinationSquareIndex)
        move = originSquare + destinationSquare
        return move

    def chessBoardToList(self, board):
        boardListNum = []
        for rank in range(7, -1, -1):  # Loop through ranks in reverse order (from 8 to 1)
            for file in range(0, 8):  # Loop through files (from 'a' to 'h')
                square = chess.square(file, rank)
                piece = board.piece_at(square)
                if piece is None:
                    boardListNum.append(0)  # Represent empty square with '0'
                    
                elif piece.symbol().islower():
                    boardListNum.append(1)  # Represent green with '1'
                   
                else:
                    boardListNum.append(2)  #Represent orange with '2'
                    
            
            
        return boardListNum
            
    def getSquareNameByIndex(self, index):
        fileAndRank = self.boardSquares.fileAndRank()
        numRows = len(fileAndRank)
        numColumns = len(fileAndRank[0])
        
        rowIndex = index // numColumns
        colIndex = index % numColumns
        
        return fileAndRank[rowIndex][colIndex]
    

# while not board.is_game_over():
       
gameState = GameState()
board=chess.Board()
currList = [1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
recentMove = gameState.findMove(board, currList)
# board.push(recentMove)
print(recentMove)