import cv2
import numpy as np

retangular = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
elipse = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
cruz = cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))

elemento_estruturante_personalizado = np.matrix([
    [0,0,1,0,0],
    [0,1,1,1,0],
    [1,1,1,1,1],
    [0,1,1,1,0],
    [0,0,1,0,0]
],np.uint8)

imagem_original = cv2.imread("teste.jpg",0)
imagem_processada_retangular = cv2.erode(imagem_original,retangular, iterations= 2)
imagem_processada_elipse  = cv2.erode(imagem_original,elipse,iterations=2)
imagem_processada_cruz = cv2.erode(imagem_original,cruz,iterations=2)
imagem_dilatada_retangular = cv2.dilate(imagem_original,retangular,iterations=2)
imagem_dilatada_elipse = cv2.dilate(imagem_original,elipse,iterations=2)
imagem_dilatada_cruz = cv2.dilate(imagem_original,cruz,iterations=2)

cv2.imshow("dilatada_R",imagem_dilatada_retangular)
cv2.imshow("dilatadaE",imagem_dilatada_elipse)
cv2.imshow("dilatadC",imagem_dilatada_cruz)


cv2.imshow("retangular", imagem_processada_retangular)
cv2.imshow("elipse", imagem_processada_elipse)
cv2.imshow("cruz",imagem_processada_cruz)
cv2.waitKey(0)
cv2.destroyAllWindows()
