import cv2
import numpy as np

ultimaTela = indiceFrame = 0
video = cv2.VideoCapture(0)

tomClaro_verde = np.array([35,100,100])
tomEscuro_verde = np.array([85,255,255])
tomClaro_vermelho = np.array([160,100,100])
tomEscuro_vermelho = np.array([200,255,255])
tomClaro_vermelho2 = np.array([0,100,100])
tomEscuro_vermelho2 = np.array([10,255,255])
tomclaro_amarelo = np.array([20,100,100])
tomEscuro_amarelo = np.array([30,255,255])
tomClaroAzul = np.array([100,100,100])
tomEscuroAzul = np.array([130,255,255])

while True:
    ret, frameRGB = video.read()
    hsv = cv2.cvtColor(frameRGB, cv2.COLOR_BGR2HSV)
    imagem_segmentada_verde = cv2.inRange(hsv,tomClaro_verde,tomEscuro_verde)
    imagem_segmentada_vermelho1 = cv2.inRange(hsv,tomClaro_vermelho,tomEscuro_vermelho)
    imagem_segmentada_vermelho2 = cv2.inRange(hsv,tomClaro_vermelho2,tomEscuro_vermelho2)
    imagem_segmentada_amarelo = cv2.inRange(hsv,tomclaro_amarelo,tomEscuro_amarelo)
    imagem_segmentada_azul = cv2.inRange(hsv,tomClaroAzul,tomEscuroAzul)
    
    cores = {
        "verde":  {"mask": imagem_segmentada_verde,  "cor": (0,255,0)},
        "vermelho1": {"mask": imagem_segmentada_vermelho1, "cor": (0,0,255)},
        "vermelho2": {"mask": imagem_segmentada_vermelho2, "cor": (0,0,255)},
        "amarelo": {"mask": imagem_segmentada_amarelo, "cor": (0,255,255)},
        "azul":   {"mask": imagem_segmentada_azul,   "cor": (255,0,0)}
    }

    for nome, dados in cores.items():
        mascara = dados["mask"]
        cor = dados["cor"]

        contornos, hierarquia = cv2.findContours(mascara,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

        if contornos:
            objeto = max(contornos,key = cv2.contourArea)
            area = cv2.contourArea(objeto)

            if area > 500:
                cv2.drawContours(frameRGB,[objeto],-1,cor,3)
                x,y,w,h = cv2.boundingRect(objeto)
                cv2.putText(frameRGB,nome,(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.6,cor,2)

    cv2.imshow("video",frameRGB)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video.release()
cv2.destroyAllWindows()