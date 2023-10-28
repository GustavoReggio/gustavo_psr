#!/usr/bin/env python3
#shebang line to inform the OS that the content is in python

from __future__ import print_function
import cv2
import argparse
from colorama import Fore, Back, Style
import json
import color_segmenter1
import numpy as np
import linecache
import re


def LimitS(args):

    """
    This function is only for reading the values of the json file.
    """
    
    #Reading Values from limits.json
    with open(args, 'r') as file_handle:
        load_file = json.load(file_handle)
           

    limits_file = load_file['limits']
    print('Carregou o dcio...')

    #loading Limits B
    B_limits = limits_file['B']
    low_H = B_limits['min']
    print("B min " + str(low_H))

    high_H = B_limits['max']
    print("B min " + str(high_H))

    #loading Limits G 
    G_limits = limits_file['G']
    low_S = G_limits['min']
    print("G max " + str(low_S))

    high_S = G_limits['max']
    print("G max " + str(high_S))

    #loading Limits R
    R_limits = limits_file['R']
    low_V = R_limits['min']
    print("R max " + str(low_V))

    high_V = R_limits['max']
    print("R max " + str(high_V))


    #Frame_HSV(low_H, low_S, low_V, high_H, high_S, high_V)
    Show_webcaM(low_H, low_S, low_V, high_H, high_S, high_V, mirror=False)

def Show_webcaM(low_H, low_S, low_V, high_H, high_S, high_V , mirror=False):

    print('vídeo ativo')
    
    cam = cv2.VideoCapture(0)
    
    while True:

        ret_val, img = cam.read()
        
        if mirror:
            img = cv2.flip(img, 1)
          
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        
        # Define the range of yellow color in HSV
        lower_yellow = np.array([int(high_H), int(high_S), int(high_V)])
        upper_yellow = np.array([int(low_H), int(low_S), int(low_V)])
        mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
        print('vídeo ativo aqui')
        # Find connected components in the binary mask
        num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(mask, connectivity=4)

        print(num_labels)
        # Find the label (component) with the largest area
        if num_labels > 0:
            print('vídeo ativo aqui 2')
            largest_component_label = np.argmax(stats[1:, cv2.CC_STAT_AREA]) + 1
            print('vídeo ativo aqui 3')
        # Create a mask containing only the largest component
        largest_component_mask = np.uint8(labels == largest_component_label) * 255
        
        # Calculate moments of the largest component
        moments = cv2.moments(largest_component_mask)

        # Calculate the centroid coordinates
        if moments["m00"] != 0:
            cx = int(moments["m10"] / moments["m00"])
            cy = int(moments["m01"] / moments["m00"])
            print("Centroid X:", cx)
            print("Centroid Y:", cy)
        else:
            print("No centroid found (division by zero)")

        # Draw a circle at the centroid for visualization
        cv2.circle(img, (cx, cy), 5, (0, 0, 255), -1)  # Red circle at the centroid
        
        # Display the largest component mask and the image with the centroid
        cv2.imshow('Largest Component Mask', largest_component_mask)
        cv2.imshow('Image with Centroid', img)

        cv2.circle(hsv,(cx,cy),55,(0,0,255),-1)
        
        if cv2.waitKey(1) == 27:
            break  # Close the window if the 'Esc' key is pressed

    cam.release()
    cv2.destroyAllWindows()

"""def Frame_HSV(low_H, low_S, low_V, high_H, high_S, high_V):

    window_capture_name = 'Video Capture'
    window_detection_name = 'Object Detection'
    
    print('vídeo ativo')

    parser = argparse.ArgumentParser('Menu of Saving limits')
    parser.add_argument('-c','--camera', help='', default=0, type=int, required=False)
    args = parser.parse_args()

    cap = cv2.VideoCapture(args.camera)
    
    cv2.namedWindow(window_capture_name)
    cv2.namedWindow(window_detection_name)
    
    
    while True:
        ## [while]
        ret, frame = cap.read()
        key = cv2.waitKey(50)

        if frame is None:
            break

        elif key == ord('q'):
            print("Quiting Program.")
            break
        
        frame_HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        frame_threshold = cv2.inRange(frame_HSV, (low_H, low_S, low_V), (high_H, high_S, high_V))
        ## [while]

        ## [show]
        cv2.imshow(window_capture_name, frame)
        cv2.imshow(window_detection_name, frame_threshold)
        ## [show]

"""


    

def main():
    
    parser = argparse.ArgumentParser(description='Menu of Drawing Mode')
    parser.add_argument('-j', '--json',type=str, help=Fore.LIGHTYELLOW_EX+'Full path to json file'+Style.RESET_ALL,
                        default='/home/gustavo/Documentos/PSR/gustavo_psr/Parte7/limits.json', required=False)
    args = vars(parser.parse_args())
    
    if args == False:
            print('File should be in another directory.')
        
   

    LimitS(args['json'])

    
if __name__ == '__main__':
    main()