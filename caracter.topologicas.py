#obter perimetro do objeto
import cv2
import numpy as np

original = cv2.imread("cubo.png")
ob = cv2.imread("cubo.bmp",0)

ret, binarizada = cv2.threshold(ob,127,255,cv2.THRESH_BINARY)
contornos, hierarquia = cv2.findContours(binarizada,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
objeto = max(contornos, key=cv2.contourArea)
perimetro = cv2.arcLength(objeto,True) 

#obter pontos dos vertices
poligono = cv2.approxPolyDP(objeto,0.1*perimetro,True)

#obter total vertices
totalVertices = len(poligono)
print(totalVertices)

#furos do objeto
ret, imagem_binarizada = cv2.threshold(ob,127,255,cv2.THRESH_BINARY)
contornos2 , hierarquia2 = cv2.findContours(imagem_binarizada,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
furos = len(contornos) - 1
print(furos)
cv2.waitKey(0)
cv2.destroyAllWindows()

