import cv2

imagem = cv2.imread("teste.jpg",0)
imagem_canny = cv2.Canny(imagem,100,200)
cv2.imshow("original",imagem)
cv2.imshow("canny",imagem_canny)
cv2.waitKey(0)
cv2.destroyAllWindows()
