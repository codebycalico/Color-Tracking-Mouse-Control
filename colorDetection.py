import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    # convert RGB to HSV from the webcam
    # frame = [[[255, 0, 0]]]
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define a lower and upper bound
    # any colors / hues in that range will be displayed
    lower_blue = np.array([90, 50, 50])
    upper_blue = np.array([130, 255, 255])

    # mask is a portion of an image / frame
    # returns a new image with only the colors in the range
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # apply mask to original image
    # tells us which pixels to keep and which to not keep
    # which pixels are in the range
    # compare pixel by pixel (bit by bit) and only keep ones from the mask
    # turn all other pixels to black
    # bitwise_and 
    # 1 1 = 1
    # 1 0 = 0
    # 0 1 = 0
    # 0 0 = 0
    result = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('frame', result)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()