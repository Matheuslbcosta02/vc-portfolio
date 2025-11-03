import cv2
import numpy as np

imagem = cv2.imread("engrenagem.png")
cv2.imwrite("engrenagem-binaria.bmp",imagem)

imagem_original = cv2.imread("engrenagem-binaria.bmp",0)
elemento_estruturante = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
imagem_processada = cv2.erode (imagem_original,elemento_estruturante,iterations=3)

cv2.imshow("original",imagem_original)
cv2.imshow("resultado",imagem_processada)
cv2.waitKey(0)
cv2.destroyAllWindows()
