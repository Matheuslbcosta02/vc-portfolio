import cv2
imagem_original = cv2.imread("teste.jpg",0)
imagem_filtrada = cv2.Laplacian(imagem_original,cv2.CV_8U)
imagem_realcada = cv2.subtract(imagem_original,imagem_filtrada)

cv2.imshow("original",imagem_original)
cv2.imshow("filtroLaplace",imagem_filtrada)
cv2.imshow("realce",imagem_realcada)
cv2.waitKey(0)
cv2.destroyAllWindows()