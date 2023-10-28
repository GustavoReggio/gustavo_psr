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

def PainT():

    white_secreen = numpy.ones((500,500,3), dtype=numpy.uint8)*255
    drawing_data = {'pencil_down': False,'previous_x': 0,'previous_y': 0, 'color': (255,255,255), 'tamanho': ()}

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

    #return low_H, low_S, low_V, high_H, high_S, high_V
    Frame_HSV(low_H, low_S, low_V, high_H, high_S, high_V)


def Frame_HSV(low_H, low_S, low_V, high_H, high_S, high_V):

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

    Object_locatiN(frame_threshold)


def Object_locatiN(frame_threshold):
    
    connectivity = 4

    # Perform the operation
    object_detection = cv2.connectedComponentsWithStats(frame_threshold, connectivity, cv2.CV_32S)
    # Get the results
    # The first cell is the number of labels
    num_labels = object_detection[0]
    # The second cell is the label matrix
    labels = object_detection[1]
    # The third cell is the stat matrix
    stats = object_detection[2]
    # The fourth cell is the centroid matrix
    centroids = object_detection[3]
    
    # Initialize a new image to store  
    # all the output components 
    output = numpy.zeros(frame_threshold.shape, dtype="uint8") 
    
    # Loop through each component 
    for i in range(1, num_labels): 
        
        # Area of the image 
        area = stats[i, cv2.CC_STAT_AREA]  
        
        if (area > 140) and (area < 400): 
            componentMask = (labels == i).astype("uint8") * 255
            output = cv2.bitwise_or(output, componentMask) 
    

def main():
    
    parser = argparse.ArgumentParser(description='Menu of Drawing Mode')
    parser.add_argument('-j', '--json',type=str, help=Fore.LIGHTYELLOW_EX+'Full path to json file'+Style.RESET_ALL,
                        default='/home/gustavo/Documentos/PSR/gustavo_psr/Parte7/limits.json', required=False)
    args = vars(parser.parse_args())
    
    if args == False:
            print('File should be in another directory.')
        
   

    LimitS(args['json'])
    #Frame_HSV()
    
if __name__ == '__main__':
    main()