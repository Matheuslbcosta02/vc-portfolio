from PIL import Image
import cv2
import pytesseract

indiceFrame = 0
valorAnterior = 0
video = cv2.VideoCapture(0)

while True:
    indiceFrame +=1
    ret,frame_rgb = video.read()
    imagem = Image.fromarray(frame_rgb)

    if indiceFrame == 15:
        indiceFrame = 0
        valorAtual = pytesseract.image_to_string(imagem)
        if valorAnterior != valorAtual:
            print(valorAtual)

    cv2.imshow("video",frame_rgb)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video.release()
cv2.destroyAllWindows()