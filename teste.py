import cv2
import os

caminho = os.path.join(os.path.dirname(__file__),"teste.jpg")

imagem = cv2.imread(caminho)
azul, verde , vermelho = cv2.split(imagem)
cv2.imshow("R" , vermelho)
cv2.imshow("G",verde)
cv2.imshow("B",azul)
cv2.imwrite("carro_vermelho.jpeg",vermelho)
cv2.imwrite("carro_verde.jpeg",verde)
cv2.imwrite("carro_azul.jpeg",azul)
cv2.imshow("Imagem", imagem)
carro_misturado = cv2.merge((azul,verde,vermelho))
cv2.imshow("carro",carro_misturado)
carro_cinza = cv2.cvtColor(imagem,cv2.COLOR_RGB2GRAY)
cv2.imshow("CINZA",carro_cinza)


nova_imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)
matriz, saturacao , valor = cv2.split(nova_imagem)
cv2.imshow("H",matriz)
cv2.imshow("S", saturacao)
cv2.imshow("V",valor)
carro_hsv = cv2.merge((matriz,saturacao,valor))
carro_hsv = cv2.cvtColor(carro_hsv,cv2.COLOR_HSV2BGR)
cv2.imshow("carro_hsv",carro_hsv)
cv2.waitKey(0)
cv2.destroyAllWindows