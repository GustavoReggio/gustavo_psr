#!/usr/bin/env python3
#shebang line to inform the OS that the content is in python

#use imports here

import cv2
import argparse

#ver aula savi 2023-2024

# define functions here ...

# Global variables

threshold = 0
window_name = 'window - Ex3a'


def onTrackbar(threshold):
    """Esta função permite criar o Trackbar, que fará com que o utilizador deslize por toda a gama de paletas"""

    _,image_threshold = cv2.threshold(image_gray, threshold, 255, cv2.THRESH_BINARY)
    cv2.imshow(window_name,image_threshold)
    

def main():

    global image_gray                                       #use global var

    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--image', type=str,help='', required = False,
                        default='/home/gustavo/Imagens/imagens_psr/atlascar.png')
    args = vars(parser.parse_args())

    image = cv2.imread(args['image'], cv2.IMREAD_COLOR)     #Load an image
    cv2.imshow('Original', image)

    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)    #convert bgr to gray image (single channel)
     
    
    # add code to create the trackbar ...
    cv2.namedWindow(window_name)

    trackbar_name = 'Threshold' 
    cv2.createTrackbar(trackbar_name, window_name, 0, 255, onTrackbar)

    cv2.setTrackbarPos(trackbar_name, window_name, threshold)    
    onTrackbar(threshold)
    cv2.waitKey(0)

if __name__ == '__main__':
    main()