import cv2
import statistics

imgBinaria = cv2.imread("cubo.png")
imgBinaria2 = cv2.imwrite("cubo.bmp",imgBinaria)
binaria = cv2.imread("cubo.bmp",0)
tons_cinza = cv2.imread("cubo.png",0)

rolBinaria = binaria.ravel()
rol_tons_cinza = tons_cinza.ravel()

valor_medioRGB = cv2.mean(imgBinaria)
valor_medio_cinza = cv2.mean(tons_cinza)

print(valor_medioRGB)
print(valor_medio_cinza)

print(statistics.mode(rolBinaria))
print(statistics.mode(rol_tons_cinza))