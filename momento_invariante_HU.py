import cv2
import numpy as np

imagem = cv2.imread("cubo.bmp",0)
momentos = cv2.moments(imagem)
momentosdeHU = cv2.HuMoments(momentos)

print(momentosdeHU)

print(-np.sign(momentosdeHU) * np.log10(np.abs(momentosdeHU)))
