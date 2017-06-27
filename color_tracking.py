import cv2
import numpy as np
from matplotlib import pyplot as plt


class colorTracking(object):
    
    def __init__(self, img_file):
        self.img = None
        self.list_of_clicks = []
        
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
        cv2.destroyAllWindows
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
        
        sqr = self.img[y_min:y_max, x_min:x_max]
        #plt.imshow(sqr)
        cv2.imshow('cropped',sqr)
        cv2.waitKey(0)
        cv2.destroyAllWindows