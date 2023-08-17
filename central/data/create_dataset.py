import os
import sys
sys.path.append("/Users/yab/Desktop/projects/AI-Chess-Robot/central/vision")
import cv2 as cv
from img_processing import ImageProcessing
from board_squares import BoardSquares
from extract_color import ExtractColor

class CreateDataset:
    def __init__(self):
        pass


    def dataset(self):
        extractColor = ExtractColor()
        processedImage=ImageProcessing()
        features, classes= [], []
        folderPath = "/Users/yab/Desktop/projects/AI-Chess-Robot/raw/1"
        for i in range(65):
            subFolder = os.path.join(folderPath, str(i))
            fileList = os.listdir(subFolder)
            imageFiles = [file for file in fileList if file.endswith(('.jpg'))]
            boardSquares = BoardSquares()
            fenPath = os.path.join(subFolder, "board.fen")
            boardState= boardSquares.readFen(fenPath)
            
            for imageFile in imageFiles:
                imagePath = os.path.join(subFolder, imageFile)
                image = cv.imread(imagePath, cv.IMREAD_COLOR)
                paddedImage = processedImage.add_margin(image)
                coords = processedImage.squareCoords(image)
                
                
                for i in range(len(coords)):
                    croppedImage = extractColor.crop_image(paddedImage, coords[i])
                    # cv.imshow('Cropped Image', croppedImage)
                    # cv.waitKey(2000)
                    # cv.destroyAllWindows()
                    orangePercent, greenPercent, neitherPercent = extractColor.detect_color(croppedImage)
                    features.append([orangePercent, greenPercent, neitherPercent])
                    catagory = boardState[i]
                    classes.append(catagory)    
                
        return features, classes




