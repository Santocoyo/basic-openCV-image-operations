import numpy as np
import cv2

def main():
    img = np.zeros((512,512,3),np.uint8)

    img = cv2.line(img,(0,0),(511,511),(255,0,0),5)

    img = cv2.circle(img, (447,63), 65, (0,0,255), -1)

    img= cv2.ellipse(img, (256, 300), (100, 50), 0, 0, 360, (0,255,0), -1)

    pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
    #pts = pts.reshape((-1,1,2))
    img = cv2.polylines(img,[pts],True,(255,255,255))

    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, "Hola mundo!",(10,500),font,1.5,(0,255,0),2,cv2.LINE_AA)

    cv2.namedWindow("imagen", cv2.WINDOW_NORMAL)
    cv2.imshow("imagen",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return

if __name__ == "__main__":
    main()
