import numpy as np
import cv2

def main():

    img=cv2.imread("foto ale.png")

    px = img[140,90]

    img[100,100] = [255,255,255]

    print (px)

    print (img.shape)

    print (img.size)

    print (img.dtype)

    capas()

    return

def capas():
    img = cv2.imread("foto ale.png")
    b, g, r=cv2.split(img)
    img = cv2.merge((b,g,r))

    return

def blending():
    

if __name__ == "__main__":
    main()
