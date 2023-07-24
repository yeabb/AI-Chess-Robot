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
        recent_move = self.findMove(board, currBoardStatus)
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
    
    def findMove(self, prevBoardStatus, currBoardStatus):
        prevBoardStatusList = self.chessBoardToList(prevBoardStatus)
        n = len(prevBoardStatus)
        for i in range(n):
            if prevBoardStatus[i] != currBoardStatus[i]:
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
        for rank in chess.RANKS[::-1]:  # Loop through ranks in reverse order (from 8 to 1)
            for file in chess.FILES:  # Loop through files (from 'a' to 'h')
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