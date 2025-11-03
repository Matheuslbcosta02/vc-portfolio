import cv2
import numpy as np

indiceframe = totalVerticesAnterior = 0
valoresMedidos = np.zeros(7)
video = cv2.VideoCapture(0)

while True:
    ret, frameRGB = video.read()
    framecinza = cv2.cvtColor(frameRGB,cv2.COLOR_RGB2GRAY)
    tipo = cv2.THRESH_BINARY
    ret, frameBinarizado = cv2.threshold(framecinza,127,255,tipo)
    contornos = []
    forma = ""
    valormedioAtual = int(cv2.mean(frameBinarizado)[0])
    if valormedioAtual != 0:
        if valormedioAtual == int(cv2.mean(valoresMedidos)[0]):
            contornos, hierarquia = cv2.findContours(frameBinarizado,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        if len(contornos)>0:
            objeto = max(contornos,key = cv2.contourArea)
            area = cv2.contourArea(objeto)
            if area > 1000:
                perimetro = cv2.arcLength(objeto,True)
                poligono = cv2.approxPolyDP(objeto,0.03*perimetro,True)
                totalVertices = len(poligono)
                cv2.drawContours(frameRGB,[poligono],0, (0,255,0),3)

            if totalVertices != totalVerticesAnterior:
                totalVerticesAnterior = totalVertices
                if totalVertices == 3 : print("triangulo")
                if totalVertices == 4 : print("quadrado")
                if totalVertices > 7 : print("circulo")

            if forma != "":
                cv2.putText(frameRGB,forma,(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)

    valoresMedidos[indiceframe] = valormedioAtual
    if indiceframe == 6:
        indiceframe = -1
    indiceframe +=1
    cv2.imshow("video",frameRGB)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video.release()
cv2.destroyAllWindows()