import cv2
import numpy as np
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
contornos, hierarquia = cv2.findContours(objeto,modo,metodo)
objetos = contornos[0]
x,y,w,h = cv2.boundingRect(objetos)
cv2.rectangle(original,(x+20,y+20),(x+w-20, y+h-20),(0,255,0),12)
cv2.imshow("retângulo envolvendo o cubo",original)
cv2.waitKey(0)
cv2.destroyAllWindows()
