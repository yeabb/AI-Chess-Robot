from img_processing import ImageProcessing
import cv2 as cv

class GameState:
    def __init__(self):
        self.img=cv.imread("/Users/yab/Desktop/projects/yolo/corner/contours.jpeg")

    def recent_humanMove(self):
        recent_move=str(input("make a move :"))
        return recent_move
    
    # def mapBoardSquares(self):
        
    def squareCoords(self): #defining a matrix that reprsents the coords of each squares
        coords=self.coords()
        square_coords=[]
        for i in range(8):
            temp=[]
            for j in range(8):
                first_coord, second_coord = coords[i][j], coords[i][j+1]
                third_coord, fourth_coord = coords[i+1][j], coords[i+1][j+1]
                temp.append([first_coord, second_coord, third_coord, fourth_coord])      
            square_coords.append(temp)
    
        files=["a","b","c","d","e","f","g","h"]  
        ranks=["1","2","3","4","5","6","7","8"]
        fileAndRank=[]
        for i in range(8):
            temp=[]
            for j in range(7, -1, -1):
                temp.append(files[i]+ranks[j])
            fileAndRank.append(temp)
        
        return square_coords, fileAndRank
    
    def squaresToCoordsMap(self):
        square_coords,fileAndRank=self.squareCoords()
        squareCoordsMap={}
        for i in range(8):
            for j in range(8):
                squareCoordsMap[fileAndRank[i][j]]=square_coords[i][j]
        return squareCoordsMap
    
    def coordsTosquaresMap(self):
        square_coords,fileAndRank=self.squareCoords()
        coordsSquareMap={}
        for i in range(8):
            for j in range(8):
                coordsSquareMap[str(square_coords[i][j])]=fileAndRank[i][j]
        return coordsSquareMap     
    def coords(self):
        processedImage=ImageProcessing(self.img)
        pts=processedImage.find_coordinates()
        return pts
    
    def board_status(self):
        pass
    
    def show_board_status(self):
        pts=self.coords()
        for pt in pts:
            # print(pt)
            cv.circle(self.img, (int(pt[1]), int(pt[0])), 3, (0,255,0), 3)
            
        cv.imshow('image', self.img)
        k = cv.waitKey(0)
        cv.destroyAllWindows()
