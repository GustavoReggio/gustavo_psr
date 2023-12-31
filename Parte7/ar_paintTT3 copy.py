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
import readchar
import keyboard
from pynput.keyboard import Key, Listener
#import imutils

##arguments
import argparse

def ArgumentS():
    parser = argparse.ArgumentParser(description='Menu of Drawing Mode')
    parser.add_argument('-j', '--json', help='Full path to JSON file', required=True)
    args = parser.parse_args()
    return args



def BrusH(cx,cy, paintWindow):

    drawing_data = {'previous_x': 0,'previous_y': 0, 'color': (0,0,255)}
   
   
         
    key = cv2.waitKey(50)
        
    print('desenhando')
    drawing_data['previous_x'] = cx
    drawing_data['previous_y'] = cy
    cv2.imshow('draw', paintWindow)
    cv2.line(paintWindow, (drawing_data['previous_x'],drawing_data['previous_y']), (cx,cy), drawing_data['color'], 1)

    if key == ord('q'):              #quit program
        print("Quiting Program")
        #break

    
    """while True:
        
        if keyboard.read_key('a'):
            brushsize = brushsize + 5
            
        if keyboard.read_key('s'):
            brushsize = brushsize - 5
            
        if keyboard.read_key('r'):
            brushcolor = (0,0,255)
            
        if keyboard.read_key('g'):
            brushcolor = (0,255,0)
        
        if keyboard.read_key('b'):
            brushcolor = (255,0,0)
        
        return brushcolor,brushsize"""
            
        

def Show_WebcaM(low_H, low_S, low_V, high_H, high_S, high_V , mirror=False):

    cam = cv2.VideoCapture(0)
    paintWindow = np.zeros((500,600,3)) + 255
    brushsize = 5
    brushcolor = (255,255,255)

    while True:
        ret_val, img = cam.read()
        
        if mirror:
            img = cv2.flip(img, 1)
            
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        
        # Define the range of yellow color in HSV
        ###print(type(high_H))
        upper_yellow = np.array([high_H, high_S, high_V])
        lower_yellow = np.array([low_H,low_S,low_V])
        #lower_yellow = np.array([15,50,180])
        #upper_yellow = np.array([40,255,255])
        ###print(upper_yellow,lower_yellow)
        mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
        
        
        # Find connected components in the binary mask
        num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(mask, connectivity=4)
        ###print(num_labels)
        
        
        # Find the label (component) with the largest area
        
        if num_labels > 1:
            #print('video ativo aqui 2')
            largest_component_label = np.argmax(stats[1:, cv2.CC_STAT_AREA]) + 1
            #print('video ativo aqui 3')
        
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
                cv2.circle(img, (cx, cy), 5, (0, 0, 255), -1)  # Red circle at the centroid
                cv2.circle(hsv,(cx,cy),55,(0,0,255),-1)
                cv2.circle(paintWindow,(cx,cy),brushsize,brushcolor,1)
            else:
                print("No centroid found (division by zero)")

            
            BrusH(cx,cy, paintWindow)
           


            # Display the largest component mask and the image with the centroid
            #cv2.imshow('Largest Component Mask', largest_component_mask)
        cv2.imshow('mask',mask)
        cv2.imshow('Image with Centroid', img)
        #cv2.imshow('draw', paintWindow)

        ###
        
        if cv2.waitKey(1) == 27:
            break  # Close the window if the 'Esc' key is pressed

    cam.release()
    cv2.destroyAllWindows()

    
    
    

def LimitS(json_file):
 
    """
    This function is only for reading the values of the json file.
    """
    
    #Reading Values from limits.json
    with open(json_file, 'r') as file_handle:
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
    
    return low_H, low_S, low_V, high_H, high_S, high_V

def main():
    
    args = ArgumentS()
    json_file = args.json
    
    low_H, low_S, low_V, high_H, high_S, high_V = LimitS(json_file)
    Show_WebcaM(low_H, low_S, low_V, high_H, high_S, high_V, mirror=True)
    

if __name__ == '__main__':
    main()