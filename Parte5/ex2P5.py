#!/usr/bin/env python3
#shebang line to inform the OS that the content is in python

#use imports here

import cv2
import argparse

#ver aula savi 2023-2024

# define functions here ...

def main():

    parser = argparse.ArgumentParser(description = "Scrip used to test your typing")
    parser.add_argument("-if", '--image_filename',type = str, help = '', required = True, default= 'home/gustavo/Imagens/imagens_psr/.png')

    args = vars(parser.parse_args())
    print(args)
    exit(0)
    
    imagem_filename = args['imagem_filename']
    imagem = cv2.imread(imagem_filename, cv2.IMREAD_COLOR)  # Load an image

    cv2.imshow('Imagem Python', imagem)                     # Display the image
    cv2.waitKey(0)                                          # wait for a key press before proceeding

if __name__ == "__main__":
    main()