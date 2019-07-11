import numpy
import cv2
import matplotlib.pyplot as plt

img=cv2.imread("foto ale.png")
img=cv2.imread("foto ale.png", cv2.IMREAD_GRAYSCALE)
cv2.imwrite("foto ale2.png", img)
cv2.imshow("imagen",img)
plt.imshow(img)
plt.xticks([]), plt.yticks([])
plt.show()
