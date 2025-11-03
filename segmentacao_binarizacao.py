import cv2
import numpy as np

imagem = cv2.imread("grao.png",0)
metodo = cv2.THRESH_BINARY
ret,imgBinarizada = cv2.threshold(imagem,130,250,metodo)
elemento_estruturante_retangular = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))
fechamento = cv2.morphologyEx(imgBinarizada,cv2.MORPH_CLOSE,elemento_estruturante_retangular)
erosao = cv2.erode(fechamento,elemento_estruturante_retangular,iterations=5)

# binarização adaptativa
circulosOriginal = cv2.imread("circulos.png",0)
circulosTratados = cv2.medianBlur(circulosOriginal,7)
Adaptativa_Binarizada = cv2.adaptiveThreshold(circulosTratados,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,9,5)

cv2.imshow("adaptativaBinarizada",Adaptativa_Binarizada)
cv2.imshow("segmentadaBinarizacao",imgBinarizada)
cv2.imshow("fechamento",fechamento)
cv2.imshow("erosao",erosao)

cv2.waitKey(0)
cv2.destroyAllWindows()