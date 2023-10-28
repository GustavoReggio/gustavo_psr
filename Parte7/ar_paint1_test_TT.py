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
#import imutils

def arguments():
    parser = argparse.ArgumentParser(description='Menu of Drawing Mode')
    parser.add_argument('-j', '--json', help='Full path to JSON file', required=True)
    args = parser.parse_args()
    return args

def show_webcam(low_H, low_S, low_V, high_H, high_S, high_V , mirror=False):
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
        
        # Find connected components in the binary mask
        num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(mask, connectivity=4)
        print(num_labels)
        # Find the label (component) with the largest area
        if num_labels > 1:
            largest_component_label = np.argmax(stats[1:, cv2.CC_STAT_AREA]) + 1
        
        # Create a mask containing only the largest component
        largest_component_mask = np.uint8(labels == largest_component_label) * 255
        
        # Calculate moments of the largest component
        moments = cv2.moments(largest_component_mask)

        # Calculate the centroid coordinates
        if moments["m00"] != 0:
            cx = int(moments["m10"] / moments["m00"])
            cy = int(moments["m01"] / moments["m00"])
            #print("Centroid X:", cx)
            #print("Centroid Y:", cy)
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
    

def limits(json_file):
 
 with open(json_file, 'r') as file_handle:
        
    low_H = linecache.getline(json_file,4,module_globals=None)
    low_S = linecache.getline(json_file,8,module_globals=None)
    low_V = linecache.getline(json_file,12,module_globals=None)
    high_H = linecache.getline(json_file,5,module_globals=None)
    high_S = linecache.getline(json_file,9,module_globals=None)
    high_V = linecache.getline(json_file,13,module_globals=None)  

    match = re.search(r'\d+', low_H)
    if match:
        low_H = match.group()
    match = re.search(r'\d+', low_S)
    if match:
        low_S = match.group()
    match = re.search(r'\d+', low_V)
    if match:
        low_V = match.group()
    match = re.search(r'\d+', high_H)
    if match:
        high_H = match.group()
    match = re.search(r'\d+', high_S)
    if match:
        high_S = match.group() 
    match = re.search(r'\d+', high_V)
    if match:
        high_V = match.group()
    

    print('Carregou o dcio...')

    print("B min " + str(low_H))
    print("B max " + str(high_H))
    print("G min " + str(low_S))
    print("G max " + str(high_S))
    print("R min " + str(low_V))
    print("R max " + str(high_V))
    
    return low_H, low_S, low_V, high_H, high_S, high_V

def main():

    args = arguments()
    json_file = args.json
    low_H, low_S, low_V, high_H, high_S, high_V= limits(json_file)
    show_webcam(low_H, low_S, low_V, high_H, high_S, high_V, mirror=True)

if __name__ == '__main__':
    main()