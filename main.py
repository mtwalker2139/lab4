from color_tracking import colorTracking
import cv2
import numpy as np

filename = 'hockney.jpg'

def main():
    ct = colorTracking(filename)
    ct.getXY(ct.img)
    ct.isolate_square()
    ct.create_mask()


if __name__ == '__main__':
    main()