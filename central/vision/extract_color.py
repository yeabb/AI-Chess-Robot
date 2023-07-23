import os
import sys
sys.path.append("/Users/yab/Desktop/projects/AI-Chess-Robot/central/vision")
import cv2 as cv
import numpy as np

class ExtractColor:
    def __init__(self):
        pass
    
    def color_percentage(self, image, color_spectrum):
        hsv_image = cv.cvtColor(image, cv.COLOR_BGR2HSV)

        # Define the lower and upper bounds of the color spectrum
        lower_bound = np.array(color_spectrum[0], dtype=np.uint8)
        upper_bound = np.array(color_spectrum[1], dtype=np.uint8)

        # Create a binary mask for the specified color spectrum
        mask = cv.inRange(hsv_image, lower_bound, upper_bound)

        # Calculate the number of pixels that fall within the specified color spectrum
        num_pixels_in_spectrum = np.sum(mask == 255)

        return num_pixels_in_spectrum

    def detect_color(self,image):
        
        #color spectrums for Orange and green (in HSV format)
        
        orange_spectrum = ([5, 100, 100], [25, 255, 255])
        # orange_spectrum2 = ([40, 100, 100], [60, 255, 255])
        green_spectrum = ([40, 40, 40], [80, 255, 255])

        # Calculate pixel counts for red and green
        orange_pixels = self.color_percentage(image, orange_spectrum)
        # orange_pixels2 = self.color_percentage(image, orange_spectrum2)
        # orange_pixels = orange_pixels1 + orange_pixels2
        green_pixels = self.color_percentage(image, green_spectrum)

        # Calculate total number of pixels
        total_pixels = image.shape[0] * image.shape[1]

        # Calculate the number of pixels that are neither green nor red
        neither_pixels = total_pixels - (orange_pixels + green_pixels)

        # Calculate the percentages of each color and the neither pixels
        orange_percentage = (orange_pixels / total_pixels) * 100
        green_percentage = (green_pixels / total_pixels) * 100
        neither_percentage = (neither_pixels / total_pixels) * 100

        return orange_percentage, green_percentage, neither_percentage


    def crop_image(self, image, pts):
        
        pts = np.array(pts, dtype=np.float32)

        # Get the bounding rectangle of the region defined by the points
        x, y, w, h = cv.boundingRect(pts)

        # Crop the image using the bounding rectangle
        cropped_img = image[y:y+h, x:x+w]

        return cropped_img