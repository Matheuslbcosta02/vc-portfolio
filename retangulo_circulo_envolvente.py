import cv2
import numpy as np

original_elipse = cv2.imread("cubo.bmp")
original_circulo = cv2.imread("cubo.bmp")
original = cv2.imread("cubo.bmp")
objeto = cv2.imread("cubo.bmp",0)
momentos = cv2.moments(objeto)
cx = int(momentos['m10']/momentos['m00'])
cy = int(momentos['m01']/momentos['m00'])
print(cx,cy)
tipo = cv2.THRESH_BINARY
ret, imgBinarizada = cv2.threshold(objeto,127,255,tipo)
modo = cv2.RETR_TREE
metodo = cv2.CHAIN_APPROX_SIMPLE
contornos, hierarquia = cv2.findContours(imgBinarizada, modo, metodo)
objeto = contornos[43]
## muito importante -> escolher o maior contorno
## objeto = max(contornos, key=cv2.contourArea)
print(f"quantidade de contornos: {len(contornos)}")
for i,c in enumerate(contornos):
    print(f"contorno {i}: {len(c)} pontos")


#obter vertices do retangulo
x,y,w,h = cv2.boundingRect(objeto)

#desenhar retangulo
cv2.rectangle(original, (x+20,y+20), (x+w-20, y+h-20),(255,0,0),10)
cv2.imshow("retangulo envolvente", original)
print(x,y,w,h)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Circunferencia envolvente

## obtendo o ponto central e o raio da circunferencia
(x,y),raio = cv2.minEnclosingCircle(objeto)
centro = (int(x),int(y))
raio = int(raio)

#desenhando a circunferencia na imagem 
cv2.circle(original_circulo,centro, raio, (255,0,0),20)
cv2.imshow("circulo envolvente", original_circulo)
cv2.waitKey(0)
cv2.destroyAllWindows()

#elipse
elipse = cv2.fitEllipse(objeto)

#desenhar elipse na imagem
cv2.ellipse(original_elipse,elipse,(0,0,255),6)
cv2.imshow("elipse",original_elipse)
print(elipse)
cv2.waitKey(0)
cv2.destroyAllWindows()