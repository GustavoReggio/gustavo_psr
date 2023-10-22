#!/usr/bin/env python3
#shebang line to inform the OS that the content is in python

#use imports here

import cv2
import argparse
from functools import partial
import numpy

#ver aula savi 2023-2024


"""
O objetivo é carregar uma imagem e escrever um texto na mesma.
"""


# define functions here ...
def main():
    # -----------------------------------------------
    # Initialization 
    # -----------------------------------------------
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--image', type=str,help='', required = False,
                        default='/home/gustavo/Imagens/imagens_psr/atlascar.png')
    args = vars(parser.parse_args())
    # -----------------------------------------------
    # Execution 
    # -----------------------------------------------
    image= cv2.imread(args['image'], cv2.IMREAD_COLOR)     #Load an image

    #Para saber o tamanho da nossa imagem: h = altura, w = larcura, nc = número de canais
    h,w,nc = image.shape

    xc = int(w/2)
    yc = int(h/2)
    cv2.circle(image,(xc,yc),55,(0,0,255),4)

    #Para escrever o texto na imagem:
    font = cv2.FONT_HERSHEY_SIMPLEX
    org = (50,100)          # origem(x,y)
    fontScale = 2
    color = (255,0,0)
    thickness = 2

    image = cv2.putText(image, 'PSR', org,font,fontScale,color,thickness,cv2.LINE_AA)
    # -----------------------------------------------
    # Visualization 
    # -----------------------------------------------
    cv2.imshow('Original', image)
    cv2.waitKey(0)
    # -----------------------------------------------
    # Termination 
    # -----------------------------------------------
    cv2.destroyWindow('Original')


if __name__ == '__main__':
    main()