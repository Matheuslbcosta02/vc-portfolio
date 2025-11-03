import cv2
import numpy as np

imgRGB = cv2.imread("cubo.png")
imgHSV = cv2.cvtColor(imgRGB,cv2.COLOR_BGR2HSV)
print(imgHSV)

tomClaro_verde = np.array([35,100,100])
tomEscuro_verde = np.array([85,255,255])
tomClaro_vermelho = np.array([160,100,100])
tomEscuro_vermelho = np.array([200,255,255])
tomclaro_amarelo = np.array([20,100,100])
tomEscuro_amarelo = np.array([30,255,255])

imagem_segmentada_parte_verde = cv2.inRange(imgHSV, tomClaro_verde, tomEscuro_verde)
imagem_segmentada_parte_vermelha = cv2.inRange(imgHSV,tomClaro_vermelho,tomEscuro_vermelho)
imagem_segmentada_parte_amarela = cv2.inRange(imgHSV,tomclaro_amarelo,tomEscuro_amarelo)
cv2.imshow("original",imgRGB)
cv2.imshow("verde",imagem_segmentada_parte_verde)
cv2.imshow("amarelo", imagem_segmentada_parte_amarela)
cv2.imshow("vermelho",imagem_segmentada_parte_vermelha)
cv2.waitKey(0)
cv2.destroyAllWindows()