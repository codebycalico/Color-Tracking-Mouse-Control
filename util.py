import numpy as np
import cv2

# input a color to get the lower and upper limits
# of the HSV values for that color to use
# for the mask
def get_limits(color):
    # insert the bgr values which you want to convert to hsv
    c = np.uint8([[color]]) 
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)

    # define a lower and upper bound
    # any colors / hues in that range will be displayed
    lowerLimit = hsvC[0][0][0] - 10, 100, 100
    upperLimit = hsvC[0][0][0] + 10, 255, 255

    lowerLimit = np.array(lowerLimit, dtype=np.uint8)
    upperLimit = np.array(upperLimit, dtype=np.uint8)

    return lowerLimit, upperLimit