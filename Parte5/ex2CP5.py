#!/usr/bin/env python3
#shebang line to inform the OS that the content is in python

#use imports here

import cv2
import argparse

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

    image_b, image_g, image_r = cv2.split(image_rgb)

    retval, image_b_threshold = cv2.threshold(image_b, 50,255, cv2.THRESH_BINARY)
    retval, image_g_threshold = cv2.threshold(image_g, 100,255, cv2.THRESH_BINARY)
    retval, image_r_threshold = cv2.threshold(image_r, 150,255, cv2.THRESH_BINARY)

    image_rgb_threshold = cv2.merge([image_b_threshold,image_g_threshold,image_r_threshold])

    cv2.imshow('Colorida',image_rgb)                              # Display the image
    cv2.imshow('Trashold',image_rgb_threshold )
    cv2.waitKey(0)                                          # wait for a key press before proceeding

if __name__ == "__main__":
    main()