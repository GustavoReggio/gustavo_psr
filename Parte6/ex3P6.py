#!/usr/bin/env python3
#shebang line to inform the OS that the content is in python

#use imports here

import cv2
import argparse
import numpy as np
from colorama import Fore, Style
from copy import deepcopy
from functools import partial

"""
Pretende-se que o programa seja capaz de perceber se a pessoa está a falar ou não.
"""


# define functions here ...


def main():
    # -----------------------------------------------
    # Initialization 
    # -----------------------------------------------
    
    capture = cv2.VideoCapture(0)
    window_name = 'Ex 3'
    cv2.namedWindow(window_name,cv2.WINDOW_AUTOSIZE)
    cv2.namedWindow('mask',cv2.WINDOW_AUTOSIZE)

    #para se detectar o rosto precisa de uma serte rede neural, neste cas uma "cascata"
    face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    
    # -----------------------------------------------
    # Execution 
    # -----------------------------------------------
    
    while True:
        _, image_rgb = capture.read()  # get an image from the camera
        heigh, width, nc = image_rgb.shape
        image_gui = deepcopy(image_rgb)
        image_gray = cv2.cvtColor(image_rgb,cv2.COLOR_BGR2GRAY)

        #Facing detection
        faces = face_classifier.detectMultiScale(image_gray, scaleFactor=1.1, minNeighbors=5, minSize=(40, 40))
        print(faces)   

        for face in faces:
            x,y,w,h = face
            cv2.rectangle(image_gui, (x,y), (x+w,h+y), (0,255,0),4)
        
        ##Paint detected face in green
        mask = np.zeros((heigh,width), dtype=np.uint8)
    
        for face in faces:
            x,y,w,h = face
            cv2.rectangle(mask, (x,y), (x+w,h+y), 255,-1)

        b, g, r = cv2.split(image_rgb)  
        

            
        
    # -----------------------------------------------
    # Visualization 
    # -----------------------------------------------
        cv2.imshow(window_name, image_gui)
        cv2.imshow('mask', mask)
        key = cv2.waitKey(25)

        if key == 113: #letra q 
            exit(0)
    # -----------------------------------------------
    # Termination 
    # -----------------------------------------------



if __name__ == '__main__':
    main()