#!/usr/bin/env python3
#shebang line to inform the OS that the content is in python

#use imports here

import cv2
import argparse
import numpy
#ver aula savi 2023-2024

# define functions here ...

def main():

    parser = argparse.ArgumentParser(description = 'Scrip to comput the perfect numbers.')
    parser.add_argument('-if', '--image_filename', type = str, help = '', required = False,
                        default='/home/gustavo/Imagens/imagens_psr/atlascar.png')

    args = vars(parser.parse_args())                        #Creats a Ditcionary
    print(args)
    
    
    image_filename = args['image_filename']
    image_rgb = cv2.imread(image_filename, cv2.IMREAD_COLOR)    # Load an image

    image_gray = cv2.cvtColor(image_rgb, cv2.COLOR_BGR2GRAY)

    retval, image_threshold = cv2.threshold(image_gray, 128,255, cv2.THRESH_BINARY)

    cv2.imshow('Coloridp',image_rgb)                              # Display the image
    cv2.imshow('Preto e branco',image_gray)
    cv2.imshow('Trashold',image_threshold )
    cv2.waitKey(0)                                          # wait for a key press before proceeding

if __name__ == "__main__":
    main()