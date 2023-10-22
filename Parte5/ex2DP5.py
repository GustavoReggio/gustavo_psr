#!/usr/bin/env python3
#shebang line to inform the OS that the content is in python

#use imports here

import cv2
import argparse
import numpy

#ver aula savi 2023-2024

# define functions here ...

#creating the bounderies
lower_green = numpy.array([36,0,0])
upper_green = numpy.array([86,255,255])


def main():

    parser = argparse.ArgumentParser(description = 'Scrip to comput the perfect numbers.')
    parser.add_argument('-if', '--image_filename', type = str, help = '', required = False,
                        default='/home/gustavo/Imagens/imagens_psr/atlas2000_e_atlasmv.png')

    args = vars(parser.parse_args())                        #Creats a Ditcionary
    print(args)
    
    
    image_filename = args['image_filename']
    image_rgb = cv2.imread(image_filename, cv2.IMREAD_COLOR)    # Load an image

    imag_mask = cv2.inRange(image_rgb, lower_green, upper_green) # Creating mask of the green

    cv2.imshow('Original', image_rgb)
    cv2.imshow('Mascara para verde', imag_mask)
    cv2.waitKey(0)                                          # wait for a key press before proceeding
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()