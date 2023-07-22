import os
import sys
sys.path.append("/Users/yab/Desktop/projects/AI-Chess-Robot/central/vision")
import cv2 as cv
import numpy as np
from img_processing import ImageProcessing



def color_percentage(image, color_spectrum):
    
    
    hsv_image = cv.cvtColor(image, cv.COLOR_BGR2HSV)

    # Define the lower and upper bounds of the color spectrum
    lower_bound = np.array(color_spectrum[0], dtype=np.uint8)
    upper_bound = np.array(color_spectrum[1], dtype=np.uint8)

    # Create a binary mask for the specified color spectrum
    mask = cv.inRange(hsv_image, lower_bound, upper_bound)

    # Calculate the number of pixels that fall within the specified color spectrum
    num_pixels_in_spectrum = np.sum(mask == 255)

    return num_pixels_in_spectrum

def detect_color(image):
    
    #color spectrums for Orange and green (in HSV format)
    
    orange_spectrum = ([5, 100, 100], [25, 255, 255])
    # orange_spectrum2 = ([40, 100, 100], [60, 255, 255])
    green_spectrum = ([40, 40, 40], [80, 255, 255])

    # Calculate pixel counts for red and green
    orange_pixels = color_percentage(image, orange_spectrum)
    # orange_pixels2 = color_percentage(image, orange_spectrum2)
    # orange_pixels = orange_pixels1 + orange_pixels2
    green_pixels = color_percentage(image, green_spectrum)

    # Calculate total number of pixels
    total_pixels = image.shape[0] * image.shape[1]

    # Calculate the number of pixels that are neither green nor red
    neither_pixels = total_pixels - (orange_pixels + green_pixels)

    # Calculate the percentages of each color and the neither pixels
    orange_percentage = (orange_pixels / total_pixels) * 100
    green_percentage = (green_pixels / total_pixels) * 100
    neither_percentage = (neither_pixels / total_pixels) * 100

    return orange_percentage, green_percentage, neither_percentage


def crop_image(image, pts):
    
    pts = np.array(pts, dtype=np.float32)

    # Get the bounding rectangle of the region defined by the points
    x, y, w, h = cv.boundingRect(pts)

    # Crop the image using the bounding rectangle
    cropped_img = image[y:y+h, x:x+w]

    return cropped_img




processedImage=ImageProcessing()
x_train, y_train= [], []
folderPath = "/Users/yab/Desktop/projects/AI-Chess-Robot/raw/1"
for i in range(1):
    subFolder = os.path.join(folderPath, str(i))
    fileList = os.listdir(subFolder)
    imageFiles = [file for file in fileList if file.endswith(('.jpg'))]
    for imageFile in imageFiles:
        imagePath = os.path.join(subFolder, imageFile)
        image = cv.imread(imagePath, cv.IMREAD_COLOR)
        paddedImage = processedImage.add_margin(image)
        coords = processedImage.squareCoords(image)
        
        
        for pts in coords:
            
            croppedImage = crop_image(paddedImage, pts)
            # cv.imshow('Cropped Image', croppedImage)
            # cv.waitKey(2000)
            # cv.destroyAllWindows()
            orangePercent, greenPercent, neitherPercent = detect_color(croppedImage)
            x_train.append([orangePercent, greenPercent, neitherPercent])
            # catagory = folderPath
            # y_train.append(catagory)
         
    
        
    


# image_path = "/Users/yab/Desktop/projects/yolo/corner/check6.jpg"
# image = cv2.imread(image_path)
# orange_percent, green_percent, neither_percent = detect_color(image)
# print("Orange percentage:", orange_percent)
# print("Green percentage:", green_percent)
# print("Neither (Other) percentage:", neither_percent)
