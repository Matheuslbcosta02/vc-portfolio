import cv2
import numpy as np

imagem_original = cv2.imread("teste.jpg",0)
totalLinhas, totalColunas = imagem_original.shape

matriz = cv2.getRotationMatrix2D((totalColunas/2,totalLinhas/2),180,1)
matriz_deslocada = np.float32([[1,0,100],[0,1,100]])
imagemRotacionada = cv2.warpAffine(imagem_original,matriz,(totalColunas,totalLinhas))
imagemTransladada = cv2.warpAffine(imagem_original,matriz_deslocada,(totalColunas,totalLinhas))
cv2.imshow("transladada",imagemTransladada)
cv2.imshow("inicial",imagem_original)
cv2.imshow("resultado",imagemRotacionada)
cv2.waitKey(0)
cv2.destroyAllWindows()
primeiro_carro = cv2.imread("teste.jpg")
imagem_resolucao_nova = cv2.resize(primeiro_carro,None, fx = 2.0, fy = 2.0 , interpolation= cv2.INTER_CUBIC)
cv2.imshow("resolucao",imagem_resolucao_nova)
cv2.waitKey(0)
cv2.destroyAllWindows()
segundo_carro = cv2.imread("baixados.jpg")
altura, largura = imagem_resolucao_nova.shape[:2]
carro_resolucao_nova = cv2.resize(segundo_carro,(largura,altura) , interpolation= cv2.INTER_CUBIC)
imagem_Mesclada = cv2.addWeighted(imagem_resolucao_nova,0.4,carro_resolucao_nova,1.0,0)
cv2.imshow("mesclado", imagem_Mesclada)
cv2.waitKey(0)
cv2.destroyAllWindows()