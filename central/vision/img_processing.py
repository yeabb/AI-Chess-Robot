import cv2 as cv
import numpy as np
import itertools


class ImageProcessing:
    def __init__(self, img):
        # self.img=cv.imread("/Users/yab/Desktop/projects/yolo/corner/contours.jpeg")
        self.img1=img
        self.img = self.add_margin()
        self.gray = cv.cvtColor(self.img, cv.COLOR_RGB2GRAY)
    
    def add_margin(self):
        borderoutput = cv.copyMakeBorder(self.img1, 20, 20, 20, 20, cv.BORDER_CONSTANT, value=(255, 255, 255))
        return borderoutput
    def find_intersections(self, lines, image):
        new_lines_v = []
        new_lines_h = []
        for line in lines:
            x1, y1, x2, y2 = line[0]
            if (x1 == x2):
                m = 10000
            else: m = abs((y2-y1)/(x2-x1))
            # print(x1, y1, x2, y2, m)
            if (m < .5): # Horizontal
                new_lines_h.append((y1+y2)/2)
            elif (m>35): # Vertical
                new_lines_v.append((x1+x2)/2)
            else:
                cv.line(image, (x1,y1), (x2,y2), (255,100,50), 1)
        pts = []
        for hline in new_lines_h:
            for vline in new_lines_v:
                pts.append([hline, vline])
        return pts, image
    
    def dist(self, i,p): # finds distance between pts, kinda
        res = (abs(i[0]-p[0]) + abs(i[1]-p[1]))
        if (res == 0): return 100 # this is just to exclude duplicate pts
        return res
    
    def remove_duplicates(self, list):
        out = []
        l = len(list)
        for i in range(l):
            c = True
            if all(self.dist(list[i], p) > 50 for p in out):
                out.append(list[i])
        return out
    
    def find_edges(self):
        edges = cv.Canny(self.gray, 100, 150)
        return edges
    
    def find_lines(self):
        edges=self.find_edges()
        lines = cv.HoughLinesP(edges, 1, np.pi/180, 60, minLineLength=40, maxLineGap=70)
        return lines
    
    def find_contour(self): # detect contours
        ret, thresh = cv.threshold(self.gray, 125, 255, 0)
        contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
        dic={}
        for i in range (len(contours)):
            dic[int(cv.contourArea(contours[i]))] = contours[i]

        a=sorted(dic.items())
        cv.drawContours(self.img, [a[-1][1]], 0, (0, 0, 255), 23)
         
    def find_coordinates(self):
        lines=self.find_lines()
        pts, image = self.find_intersections(lines, self.gray)
        pts = self.remove_duplicates(pts)
        pts.sort()
        pts=list(pts for pts,_ in itertools.groupby(pts))
        ptsOrder=[]
        row=0
        for i in range(9):
            n=i
            temp=[]
            for j in range(9):
                temp.append(pts[n])
                n+=9
            ptsOrder.append(temp)
            row+=1
        
        
        return ptsOrder
    
    def showBoardStatus(self):
        coords=self.find_coordinates()
        for row in coords:
            for pt in row:
                cv.circle(self.img, (int(pt[1]), int(pt[0])), 3, (0,255,0), 3)
            
        cv.imshow('image', self.img)
        k = cv.waitKey(0)
        cv.destroyAllWindows()
    
    # def copy_image(self):
    #     imageCopy = self.img.copy()
    #     return imageCopy
        
img=cv.imread("/Users/yab/Desktop/projects/yolo/corner/1481228945.jpg")
x=ImageProcessing(img)
y=x.find_coordinates()
x.showBoardStatus()
# print(y)