import cv2
import numpy as np

imagem = cv2.imread("grao.png",0)

tipo = cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU

limiar, imgBinarizada = cv2.threshold(imagem,0,255,tipo)

print(limiar)

cv2.imshow("original", imagem)
cv2.imshow("tratada",imgBinarizada)
cv2.waitKey(0)
cv2.destroyAllWindows()
