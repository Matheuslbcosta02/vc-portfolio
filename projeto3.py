import cv2
import numpy as np

video = cv2.VideoCapture(0)

while True:
    ret, frame_BGR = video.read()
    hsv = cv2.cvtColor(frame_BGR,cv2.COLOR_BGR2HSV)
    tomClaroAzul = np.array([100,100,100])
    tomEscuroAzul = np.array([130,255,255])
    mascara_azul = cv2.inRange(hsv,tomClaroAzul,tomEscuroAzul)

    elementoEstruturante = np.ones((10,10),np.uint8)
    mascara_azul = cv2.morphologyEx(mascara_azul,cv2.MORPH_CLOSE,elementoEstruturante)

    contornos, hierarquia = cv2.findContours(mascara_azul,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    if len(contornos)>= 1:
        objeto = contornos[0]
        momentos = cv2.moments(objeto)
        if momentos["m00"] != 0:
            x = momentos["m10"] / momentos["m00"]
            y = momentos["m01"] / momentos["m00"]
            print("posição %d, %d" % (x,y))
            x,y,w,h = cv2.boundingRect(objeto)
            vertice1 = (x-10,y-10)
            vertice2 = (x+w+10, y+h+10)
            cv2.rectangle(frame_BGR,vertice1,vertice2,(255,0,0),2)

    cv2.imshow("video",frame_BGR)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video.release()
cv2.destroyAllWindows()