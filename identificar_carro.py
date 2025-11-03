import cv2
import numpy as np

cascadeCarro = cv2.CascadeClassifier("cars.xml")
imagem_original = cv2.imread("ss.png")
imagem = cv2.cvtColor(imagem_original,cv2.COLOR_BGR2GRAY)

carros = cascadeCarro.detectMultiScale(
    imagem,
    scaleFactor= 1.3,
    minNeighbors= 5,
    minSize=(70,70)
)

for(x,y,w,h) in carros:
    cv2.rectangle(imagem_original, (x,y), (x+w, y+h), (0,0,255), 2)

print(len(carros))
cv2.imshow("resultado", imagem_original)
cv2.waitKey(0)
cv2.destroyAllWindows()