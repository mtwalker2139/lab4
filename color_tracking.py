import cv2
import numpy as np
from matplotlib import pyplot as plt


class colorTracking(object):
    
    def __init__(self, img_file):
        self.img = None
        self.list_of_clicks = []
        self.crop = []
        self.avg_color = []
        
        self._read_image(img_file)
    
    def _read_image(self, img_file):
        self.img = cv2.imread(img_file)
    
    def getXY(self, img):
    
        #define the even
        def getxy_callback(event, x, y, flags, param):
            if event == cv2.EVENT_FLAG_LBUTTON:
                self.list_of_clicks.append([x,y])
                print "click point is..", (x,y)
                
        #read the image
        print "Print reading the image"
        #Set mouse CallBack event
        cv2.namedWindow('image')
        cv2.setMouseCallback('image', getxy_callback)
        #show the image
        print ("please select color by clickign on the screen")
        cv2.imshow('image',img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        #obtain the list of selected points
        print "The clicked points"
        print self.list_of_clicks
            
    def isolate_square(self):
        x = []
        y = []
        for i in range(len(self.list_of_clicks)):
            x.append(self.list_of_clicks[i][0])
            y.append(self.list_of_clicks[i][1])
        x_min = min(x)
        x_max = max(x)
        y_min = min(y)
        y_max = max(y)
        x_range = x_max-x_min
        y_range = y_max-y_min
        
        self.crop = self.img[y_min:y_max, x_min:x_max]
        cv2.imshow('cropped',self.crop)
        cv2.waitKey(0)
        
        avg_color_per_row = np.average(self.crop,axis=0)
        self.avg_color = np.average(avg_color_per_row,axis=0)
        #hsv = cv2.cvtColor(self.crop, cv2.COLOR_BGR2HSV)
        #avg_color_hsv = cv2.cvtColor(avg_color, cv2.COLOR_BGR2HSV)
        print self.avg_color
        #print avg_color_hsv
        cv2.destroyAllWindows
        
    def create_mask(self):
        avg_color = np.round(self.avg_color)
        lower_bound = np.subtract(avg_color,[10,10,10])
        upper_bound = np.add(avg_color,[10,10,10])
        mask = cv2.inRange(self.img,lower_bound,upper_bound)
        cv2.imshow('image',mask)
        cv2.waitKey(0)
        cv2.destroyAllWindows
        
        
        
        