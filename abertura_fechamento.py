import cv2
import numpy as np

imagem = cv2.imread("teste.jpg",0)
elemento_estruturante = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
imagem_processada_fechamento = cv2.morphologyEx(imagem,cv2.MORPH_CLOSE,elemento_estruturante)
imagem_processada_abertura = cv2.morphologyEx(imagem, cv2.MORPH_OPEN,elemento_estruturante)
imagem_subtraida = cv2.subtract(imagem,imagem_processada_abertura)
imagem_tratada = cv2.add(imagem_subtraida,imagem_subtraida)

cv2.imshow("original",imagem)
cv2.imshow("fechamento",imagem_processada_fechamento)
cv2.imshow("abertura", imagem_processada_abertura)
cv2.imshow("subtraida",imagem_subtraida)
cv2.imshow("tratada", imagem_tratada)

cv2.waitKey(0)
cv2.destroyAllWindows()
