import cv2
import numpy as np
import time

cam = cv2.VideoCapture(0)

cv2.namedWindow("Trackbars")

def nothing(x):
    pass


cv2.createTrackbar("Lower-Hue","Trackbars", 0, 179, nothing)
cv2.createTrackbar("Upper-Hue","Trackbars", 179, 179, nothing)


cv2.createTrackbar("Lower-Saturation","Trackbars", 0, 255, nothing)
cv2.createTrackbar("Upper-Saturation","Trackbars", 0, 255, nothing)


cv2.createTrackbar("Lower-value","Trackbars",0,255, nothing)
cv2.createTrackbar("Upper-value","Trackbars",0,255, nothing)


while True:
    _,ret = cam.read()
    frame = cv2.flip(ret,1)
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)



    lower_hug = cv2.getTrackbarPos("Lower-Hue","Trackbars")
    upper_hug = cv2.getTrackbarPos("Upper-Hue","Trackbars")

    lower_saturation = cv2.getTrackbarPos("Lower-Saturation","Trackbars")
    upper_saturation = cv2.getTrackbarPos("Upper-Saturation","Trackbars")

    lower_value = cv2.getTrackbarPos("Lower-value","Trackbars")
    upper_value = cv2.getTrackbarPos("Upper-value","Trackbars")


    lower_range = np.array([lower_hug,lower_saturation,lower_value])
    upper_range =np.array([upper_hug,upper_saturation,upper_value])

     
    binary_range = cv2.inRange(hsv,lower_range,upper_range)
    target = cv2.bitwise_and(frame,frame, mask = binary_range)
    mask = cv2.cvtColor(binary_range,cv2.COLOR_GRAY2BGR)
    stack =np.hstack((mask,frame,target))

    cv2.imshow("Trackbars",cv2.resize(stack,None, fx=0.5, fy=0.7))
    key = cv2.waitKey(1)
    if key == 27:
        break

    if key ==ord("s"):
        array = [[lower_hug,lower_saturation,lower_value],[upper_hug,upper_saturation,upper_value]]
        print(array)
        np.save("hsv_value",array)
        break


cam.release()
cv2.destroyAllWindows()













