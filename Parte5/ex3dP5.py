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

max_value = 255
max_value_H = 360//2

low_H = 0
low_S = 0
low_V = 0

high_H = max_value_H
high_S = max_value
high_V = max_value

low_H_name = 'Low H'
low_S_name = 'Low S'
low_V_name = 'Low V'

high_H_name = 'High H'
high_S_name = 'High S'
high_V_name = 'High V'

window_original = 'Original'
window_name = 'Exercício 3 a)'

## [low H]
def on_low_H_thresh_trackbar(val):
    global low_H
    global high_H
    low_H = val
    low_H = min(high_H-1, low_H)
    cv2.setTrackbarPos(low_H_name, window_name, low_H)

## [high H]
def on_high_H_thresh_trackbar(val):
    global low_H
    global high_H
    high_H = val
    high_H = max(high_H, low_H+1)
    cv2.setTrackbarPos(high_H_name, window_name, high_H)

## [low S]
def on_low_S_thresh_trackbar(val):
    global low_S
    global high_S
    low_S = val
    low_S = min(high_S-1, low_S)
    cv2.setTrackbarPos(low_S_name, window_name, low_S)

## [high S]
def on_high_S_thresh_trackbar(val):
    global low_S
    global high_S
    high_S = val
    high_S = max(high_S, low_S+1)
    cv2.setTrackbarPos(high_S_name, window_name, high_S)

## [low V]
def on_low_V_thresh_trackbar(val):
    global low_V
    global high_V
    low_V = val
    low_V = min(high_V-1, low_V)
    cv2.setTrackbarPos(low_V_name, window_name, low_V)

## [high V]
def on_high_V_thresh_trackbar(val):
    global low_V
    global high_V
    high_V = val
    high_V = max(high_V, low_V+1)
    cv2.setTrackbarPos(high_V_name, window_name, high_V)


def main():
    

    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--image', type=str,help='', required = False,
                        default='/home/gustavo/Imagens/imagens_psr/atlascar.png')
    args = vars(parser.parse_args())

    image = cv2.imread(args['image'], cv2.IMREAD_COLOR)
    cv2.imshow(window_original, image)


    ## [window]
    cv2.namedWindow(window_name)
    ## [window]


    # add code to create the trackbar ...
    ## [trackbar]
    cv2.createTrackbar(low_H_name, window_name , low_H, max_value_H, on_low_H_thresh_trackbar)
    cv2.createTrackbar(high_H_name, window_name , high_H, max_value_H, on_high_H_thresh_trackbar)
    cv2.createTrackbar(low_S_name, window_name , low_S, max_value, on_low_S_thresh_trackbar)
    cv2.createTrackbar(high_S_name, window_name , high_S, max_value, on_high_S_thresh_trackbar)
    cv2.createTrackbar(low_V_name, window_name , low_V, max_value, on_low_V_thresh_trackbar)
    cv2.createTrackbar(high_V_name, window_name , high_V, max_value, on_high_V_thresh_trackbar)
    ## [trackbar]

    mask = cv2.inRange(image, (low_H, low_S, low_V), (high_H, high_S, high_V))
    cv2.imshow(window_name, mask)
    cv2.waitKey(0)

if __name__ == '__main__':
    main()