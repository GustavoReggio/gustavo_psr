#!/usr/bin/env python3
#shebang line to inform the OS that the content is in python

#use imports here

import cv2
import argparse
from functools import partial
import numpy

"""
Implemente um programa que faça a aquisição de uma imagem da câmara e depois faça o seu display.
    """


# define functions here ...


def main():
    # -----------------------------------------------
    # Initialization 
    # -----------------------------------------------
    
    capture = cv2.VideoCapture(0)
    window_name = 'Ex 2'
    cv2.namedWindow(window_name,cv2.WINDOW_AUTOSIZE)


    # -----------------------------------------------
    # Execution 
    # -----------------------------------------------
    while True:
        _, image = capture.read()  # get an image from the camera
  
    # -----------------------------------------------
    # Visualization 
    # -----------------------------------------------
        cv2.imshow(window_name, image)
        cv2.waitKey(25)
    # -----------------------------------------------
    # Termination 
    # -----------------------------------------------



if __name__ == '__main__':
    main()