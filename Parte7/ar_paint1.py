#!/usr/bin/env python3
#shebang line to inform the OS that the content is in python

from __future__ import print_function
import cv2
import argparse
from colorama import Fore, Back, Style
import json
import color_segmenter1
import numpy
import linecache

##arguments
def arguments(args):
    parser = argparse.ArgumentParser(description='Menu of Drawing Mode')
    parser.add_argument('-j JSON', '--json JSON', help=Fore.LIGHTYELLOW_EX+'Full path to json file'+Style.RESET_ALL,
                        default='/home/gustavo/Documentos/PSR/gustavo_psr/Parte7/limits.json', type=int, required=True)
    args = parser.parse_args()


def Paint():

    white_secreen = numpy.ones((500,500,3), dtype=numpy.uint8)*255
    drawing_data = {'pencil_down': False,'previous_x': 0,'previous_y': 0, 'color': (255,255,255)}

    if event == cv2.EVENT_LBUTTONDOWN:                  #Se acaso o botão do maouse for precionado.
        drawing_data['pencil_down'] = True                           #Pencil_down tem q ser uma variável imutável e portanto leva [0].
        print('x = ' +str(x), ',y = '+str(y))

    elif event == cv2.EVENT_LBUTTONUP:
        drawing_data['pencil_down'] = False

    if drawing_data['pencil_down'] == True:
        cv2.line(image, (drawing_data['previous_x'],drawing_data['previous_y']), (x,y), drawing_data['color'], 1) #em comparação com o 
                                                                                #outro este desenha linhas contínuas
    
    drawing_data['previous_x'] = x
    drawing_data['previous_y'] = y
    while True:                         #para a imagem ficar se atualizando o desenho 
        cv2.imshow('White Screen', white_secreen)
        key = cv2.waitKey(50)

        if key == ord('q'):              #quit program
            print("Quiting Program")
            break

        elif key == ord('r'):
            print('Selecting red color')
            drawing_data ['color'] = (0,0,255)

        elif key == ord('g'):
            print('Selecting green color')
            drawing_data ['color'] = (255,0,0)

        elif key == ord('b'):
            print('Selecting blue color')
            drawing_data ['color'] = (0,255,0)
        
        elif key == ord('+'):
            print('Increasing the pensil size')
            drawing_data ['tamanho'] = (0)

        elif key == ord('-'):
            print('Decreasing the pensil size')
            drawing_data ['tamanho'] = (0)

        elif key == ord('c'):
            print('Clear')
            drawing_data ['tamanho'] = (0)  

        elif key == ord('w'):
            print('Saving Draw')
            drawing_data ['tamanho'] = (0)

    pass


def limits():
 
 with open('limits.json', 'r') as file_handle:
        
    low_H = linecache.getlin(args,4,module_globals=None)
    low_S = linecache.getlin(args,8,module_globals=None)
    low_V = linecache.getlin(args,12,module_globals=None)
    high_H = linecache.getlin(args,5,module_globals=None)
    high_S = linecache.getlin(args,9,module_globals=None)
    high_V = linecache.getlin(args,13,module_globals=None)  

    return low_H, low_S, low_V, high_H, high_S, high_V


def Frame_HSV():

    cap = cv2.VideoCapture()
    window_capture_name = 'Video Capture'
    window_detection_name = 'Object Detection'

    
    while True:
        ## [while]
        ret, frame = cap.read()
        key = cv2.waitKey(50)

        if frame is None:
            break

        elif key == ord('q'):
            print("Quiting Program without saving limits.")
            break
        
        frame_HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        frame_threshold = cv2.inRange(frame_HSV, (low_H, low_S, low_V), (high_H, high_S, high_V))
        ## [while]

        ## [show]
        cv2.imshow(window_capture_name, frame)
        cv2.imshow(window_detection_name, frame_threshold)
        ## [show]


def main():

    Frame_HSV()
    arguments()

if __name__ == '__main__':
    main()