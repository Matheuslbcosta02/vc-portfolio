import cv2
import numpy as np
imagem = cv2.imread("cubo.bmp",0)
tipo = cv2.THRESH_BINARY
ret, imgBinarizada = cv2.threshold(imagem,127,255,tipo)

modo = cv2.RETR_TREE
metodo = cv2.CHAIN_APPROX_SIMPLE
contornos , hierarquia = cv2.findContours(imgBinarizada,modo,metodo)
objeto = contornos[0]
area = cv2.contourArea(objeto)
perimetro = cv2.arcLength(objeto,True)

bordas = cv2.Canny(imagem,100,200)
contornos_canny , hierarquia_canny = cv2.findContours(bordas,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
for i, c in enumerate(contornos_canny):
    perimetro_c = cv2.arcLength(c, True)
    print(f"perimetro do contorno {i}: {perimetro_c}")
    



print(area)
print(perimetro)


cv2.waitKey(0)
cv2.destroyAllWindows()