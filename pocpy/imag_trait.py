'''
Ce POC utilise OpenCV pour lire une image depuis le disque, convertir cette image en 
niveaux de gris, puis affiche les deux images à l'écran.
'''

import cv2

image_path = 'path/to/your/image.jpg'
image = cv2.imread(image_path)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow('Image originale', image)
cv2.imshow('Image en niveaux de gris', gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
