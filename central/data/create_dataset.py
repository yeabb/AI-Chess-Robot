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
        extraColor = ExtractColor()
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
                    croppedImage = extraColor.crop_image(paddedImage, coords[i])
                    # cv.imshow('Cropped Image', croppedImage)
                    # cv.waitKey(2000)
                    # cv.destroyAllWindows()
                    orangePercent, greenPercent, neitherPercent = extraColor.detect_color(croppedImage)
                    features.append([orangePercent, greenPercent, neitherPercent])
                    catagory = boardState[i]
                    classes.append(catagory)
                    
        return features, classes


# image_path = "/Users/yab/Desktop/projects/yolo/corner/check6.jpg"
# image = cv2.imread(image_path)
# orange_percent, green_percent, neither_percent = detect_color(image)
# print("Orange percentage:", orange_percent)
# print("Green percentage:", green_percent)
# print("Neither (Other) percentage:", neither_percent)
