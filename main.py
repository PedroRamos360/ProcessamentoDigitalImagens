import cv2
import numpy as np

# Carrega a imagem em cores
image = cv2.imread('imagem.png')

# Converte a imagem para escala de cinza
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite('gray_image.png', gray_image)

# Exibe a imagem em escala de cinza
gaussian_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
laplassian = cv2.Laplacian(gaussian_image, cv2.CV_64F)
cv2.imshow('Imagem em Escala de Cinza', laplassian)
cv2.imwrite('laplassian.png', laplassian)
cv2.waitKey(0)
cv2.destroyAllWindows()
