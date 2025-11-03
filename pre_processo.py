import cv2
import numpy as np
from matplotlib import pyplot as grafico

imagem = cv2.imread("teste.jpg")
valorPixel = imagem [150,150]
print(valorPixel)

cor_pixel_alterada = imagem[150,150] = [255,255,255]
print(cor_pixel_alterada)

print(imagem.shape)

cv2.imwrite("teste.bmp",imagem)
preto_branco = cv2.imread("teste.bmp",0)
grafico.hist(preto_branco.ravel(),256,range=[0,256])
grafico.show()

imagem_original = cv2.imread("teste.jpg",0)
imagem_equalizada = cv2.equalizeHist(imagem_original)
cv2.imshow("orginal",imagem_original)
cv2.imshow("equalizada",imagem_equalizada)
cv2.waitKey(0)
grafico.hist(imagem_original.ravel(),256,range=[0,256])
grafico.show()
grafico.hist(imagem_equalizada.ravel(),256, range = [0,256])
grafico.show()


