from img_processing import ImageProcessing
import cv2 as cv

"""
This class will help us in translating between numerical coords values of squares and their square name
"""
class BoardSquares:   
    def __init__(self):
        pass

    def squareCoords(self): #defining a matrix that reprsents the coords of each squares
        square_coords=[]
        coords=self.coords()
        for i in range(8):
            temp=[]
            for j in range(8):
                first_coord, second_coord = coords[i][j], coords[i][j+1]
                third_coord, fourth_coord = coords[i+1][j], coords[i+1][j+1]
                temp.append([first_coord, second_coord, third_coord, fourth_coord])      
            square_coords.append(temp)
        
        return square_coords
    
    
    #return all the cords with no grouping into rows and cols
    def coords(self):     
        processedImage=ImageProcessing()
        pts=processedImage.find_coordinates()
        return pts
    
    #define a matrix to represent square names like "a8"
    def fileAndRank(self):
        
        files=["a","b","c","d","e","f","g","h"]  
        ranks=["1","2","3","4","5","6","7","8"]
        fileAndRank=[]
        for i in range(8):
            temp=[]
            for j in range(7, -1, -1):
                temp.append(files[i]+ranks[j])
            fileAndRank.append(temp)
        
        return fileAndRank
    
    #map each square names with it's coord values, 
    def squaresToCoordsMap(self):
        square_coords,fileAndRank=self.squareCoords(), self.fileAndRank()
        squareCoordsMap={}
        for i in range(8):
            for j in range(8):
                squareCoordsMap[fileAndRank[i][j]]=square_coords[i][j]
        
        return squareCoordsMap
    
    #map coord value of each square with it's square name
    def coordsTosquaresMap(self):
        square_coords,fileAndRank=self.squareCoords()
        coordsSquareMap={}
        for i in range(8):
            for j in range(8):
                coordsSquareMap[str(square_coords[i][j])]=fileAndRank[i][j]
        
        return coordsSquareMap     
    
    

# x=BoardSquares()
# y=x.squaresToCoordsMap()
# print(y)
