import cv2
import numpy as np

#carregando arquivo de caracterist.
cascadeFace = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

imagem_original = cv2.imread("selecao.png")
imagem = cv2.cvtColor(imagem_original,cv2.COLOR_BGR2GRAY)

faces = cascadeFace.detectMultiScale(
    imagem,
    scaleFactor=1.3,
    minNeighbors=5,
    minSize=(30,30)
)

#desenhar retangulo nas faces detectadas
for(x,y,w,h) in faces:
    cv2.rectangle(imagem_original, (x,y), (x+w,y+h), (000,255,0),2)

print(len(faces))
cv2.imshow("resultado", imagem_original)
cv2.waitKey(0)
cv2.destroyAllWindows()
