#!/usr/bin/env python3
#shebang line to inform the OS that the content is in python

#use imports here

import cv2

# define functions here ...

def main():

    imagem_filename = '/home/gustavo/Imagens/imagens_psr/imagem1.png'
    imagem = cv2.imread(imagem_filename, cv2.IMREAD_COLOR)  # Load an image

    cv2.imshow('Imagem Python', imagem)                     # Display the image
    cv2.waitKey(0)                                          # wait for a key press before proceeding

if __name__ == "__main__":
    main()