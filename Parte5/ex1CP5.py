#!/usr/bin/env python3
#shebang line to inform the OS that the content is in python

#use imports here

import cv2
import time
import argparse


# define functions here ...

def main():

    imagem1_filename = '/home/gustavo/Imagens/imagens_psr/atlascar.png'
    imagem2_filename = '/home/gustavo/Imagens/imagens_psr/atlascar2.png'

    imagem1 = cv2.imread(imagem1_filename, cv2.IMREAD_COLOR)  # Load an image AND select how it gonna read it, in color or gray 
    imagem2 = cv2.imread(imagem2_filename, cv2.IMREAD_COLOR)  # Load an image AND select how it gonna read it, in color or gray 
    
    

    cv2.imshow('Imagem 1', imagem1)                            # Display the image
    cv2.waitKey(3000)                                          # wait 3 sec before proceeding
    cv2.destroyAllWindows()                                    # Remove the picture
    

    cv2.imshow('Imagem 2', imagem2)
    cv2.waitKey(3000) 
    cv2.destroyAllWindows()
    


if __name__ == "__main__":
    main()