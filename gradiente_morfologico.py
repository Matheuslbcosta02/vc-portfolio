import cv2
import numpy as np

imagem = cv2.imread("teste.jpg",0)
elemento_estruturante = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
imagem_processada = cv2.morphologyEx(imagem,cv2.MORPH_GRADIENT,elemento_estruturante)
cv2.imshow("original",imagem)
cv2.imshow("gradiente morfologico",imagem_processada)


##top hat
imagem_top_hat = cv2.morphologyEx(imagem,cv2.MORPH_TOPHAT,elemento_estruturante)
#constraste
imagem_final_top_hat = cv2.add(imagem_top_hat,imagem_top_hat)

cv2.imshow("top hat",imagem_final_top_hat)
cv2.waitKey(0)
cv2.destroyAllWindows()
