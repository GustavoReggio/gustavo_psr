#!/usr/bin/env python3
#shebang line to inform the OS that the content is in python

#use imports here

import cv2
import argparse
from functools import partial
import numpy

"""
O objetivo é criar um programa parecido com o paint.
O programa deve ter um callback que recolhe a posição do rato e quando o botão esquerdo for pressionado 
o programa desenha pixeis de uma certa cor no ecrã.
"""


# define functions here ...
def MouseCallback(event, x, y, flags, param, image, pencil_down):           #Flags e param tem que esxistir para respeitar o formato printado.
    
    if event == cv2.EVENT_LBUTTONDOWN:                  #Se acaso o botão do maouse for precionado.
        pencil_down[0] = True                           #Pencil_down tem q ser uma variável imutável e portanto leva [0].
        print('x = ' +str(x), ',y = '+str(y))

    elif event == cv2.EVENT_LBUTTONUP:
        pencil_down[0] = False

    if pencil_down[0] == True:

        image[y,x,0] = 255
        image[y,x,1] = 255
        image[y,x,2] = 255 



def main():
    # -----------------------------------------------
    # Initialization 
    # -----------------------------------------------

    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--image', type=str,help='', required = False,
                        default='/home/gustavo/Imagens/imagens_psr/atlascar.png')
    args = vars(parser.parse_args())
    
    
    image= cv2.imread(args['image'], cv2.IMREAD_COLOR)     #Load an image

   
    pencil_down = [False]
    cv2.namedWindow('Images')                               #criar janela:
    cv2.setMouseCallback('Images', partial(MouseCallback, image=image, pencil_down=pencil_down))

    # -----------------------------------------------
    # Execution 
    # -----------------------------------------------

    h,w,nc = image.shape     #Para saber o tamanho da nossa imagem: h = altura, w = larcura, nc = número de canais

    xc = int(w/2)
    yc = int(h/2)
    cv2.circle(image,(xc,yc),55,(0,0,255),-1)

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

    while True:                         #para a imagem ficar se atualizando o nosso desenho com o mouse.
        cv2.imshow('Images', image)
        cv2.waitKey(50)

    # -----------------------------------------------
    # Termination 
    # -----------------------------------------------

    cv2.destroyWindow('Original')


if __name__ == '__main__':
    main()