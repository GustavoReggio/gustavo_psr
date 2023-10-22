#!/usr/bin/env python3
#shebang line to inform the OS that the content is in python

#use imports here

import cv2
import argparse
from functools import partial
import json

#ver aula savi 2023-2024

#Implemente um programa que permita configurar a segmentação de cor.
#O programa deve executar a segmentação verificando quais os pixeis da imagem que estão dentro de certos limites mínimo e máximo.
#Estes limites deverão ser diferentes para cada canal de cor.
#O programa deve mostrar 6 trackbars no total, para configurar aqueles limites:


# define functions here ...



def onTrackbar(B_min, B_max, G_min, G_max, R_min, R_max, image, window_name):  
    """Esta função permite criar o Trackbar, que fará com que o utilizador deslize por toda a gama de paletas"""

    #_,image_threshold = cv2.threshold(image_gray, threshold, 255, cv2.THRESH_BINARY)
    #cv2.imshow(window_name,image_threshold)

    mask = cv2.inRange(image,(B_min,G_min,R_min),(B_max,G_max,R_max))
    cv2.imshow(window_name, mask)
    

def main():

    window_original = 'Original'
    window_name = 'Window - Ex3'

    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--image', type=str,help='', required = False,
                        default='/home/gustavo/Imagens/imagens_psr/atlascar.png')
    args = vars(parser.parse_args())

    image = cv2.imread(args['image'], cv2.IMREAD_COLOR)
    cv2.imshow(window_original, image)
    
    #threshold = 0
    #image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)    #convert bgr to gray image (single channel)


    # add code to create the trackbar ...

    cv2.namedWindow(window_name)

    B_min = 0
    B_max = 0
    G_min = 0
    G_max = 0
    R_min = 0
    R_max = 0

    cv2.createTrackbar('min B', window_name, 0, 255,
                       partial(onTrackbar, B_min=B_min ,image=image, window_name=window_name))
    cv2.createTrackbar('max B', window_name, 0, 255,
                       partial(onTrackbar,B_max=B_max , image=image, window_name=window_name))
    cv2.createTrackbar('min G', window_name, 0, 255,
                       partial(onTrackbar,G_min=G_min , image=image, window_name=window_name))
    cv2.createTrackbar('max G', window_name, 0, 255,
                       partial(onTrackbar,G_max=G_max , image=image, window_name=window_name))
    cv2.createTrackbar('min R', window_name, 0, 255,
                       partial(onTrackbar,R_min=R_min , image=image, window_name=window_name))
    cv2.createTrackbar('max R', window_name, 0, 255,
                       partial(onTrackbar,R_max=R_max , image=image, window_name=window_name))
    
    cv2.setTrackbarPos('min B', window_name, B_min)
    cv2.setTrackbarPos('max B', window_name, B_max)
    cv2.setTrackbarPos('min G', window_name, G_min)
    cv2.setTrackbarPos('max G', window_name, G_max)
    cv2.setTrackbarPos('min R', window_name, R_min)
    cv2.setTrackbarPos('max R', window_name, R_max)

    onTrackbar(B_min, B_max, G_min, G_max, R_min, R_max, image, window_name)
    cv2.waitKey(0)

if __name__ == '__main__':
    main()