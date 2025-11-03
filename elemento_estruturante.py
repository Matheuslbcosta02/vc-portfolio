import cv2
import numpy as np

retangular = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
elipse = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
cruz = cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))

elemento_estruturante_personalizado = np.matrix([
    [0,0,1,0,0],
    [0,1,1,1,0],
    [1,1,1,1,1],
    [0,1,1,1,0],
    [0,0,1,0,0]
],np.uint8)

print(retangular)
print("\n\n\n\n")
print(elipse)
print("\n\n\n\n")
print(cruz)
print("\n\n\n\n")
print(elemento_estruturante_personalizado)