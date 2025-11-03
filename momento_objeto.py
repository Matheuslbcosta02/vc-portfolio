import cv2
import numpy as np

imagem = cv2.imread("cubo.bmp",0)
momentos = cv2.moments(imagem)

print(momentos)
