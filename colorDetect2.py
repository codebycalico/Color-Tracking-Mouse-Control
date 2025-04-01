import cv2
from pynput import mouse
import pyautogui
from PIL import Image
from util import get_limits

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

#centerx = 0, centery = 0

# define colors in BGR colorspace
blue = [255, 0, 0]
green = [0, 255, 0]
red = [0, 0, 255]

def on_click(x, y, button, pressed):
    if pressed:
        print("Button pressed.")

# main
while True:
    ret, frame = cap.read()
    pyautogui.FAILSAFE = False

    with mouse.Listener(
        on_click = on_click
    ) as listener:
        listener.join(0.1)

    # converting original colorspace of RGB to HSV for color tracking
    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # set the color to track / detect
    lowerLimit, upperLimit = get_limits(color=green)

    # get a mask from all the pixels that we want to detect
    # function returns a location of all the pixels containing
    # the values we specified
    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)

    # convert image from numpy to Pillow format
    mask_ = Image.fromarray(mask)

    # get a "bounding box", the square that tracks around
    # color detection
    bbox = mask_.getbbox()

    # bbox returns the coordinates
    # of the four points of the square / rectangle
    # that encompasses the object being color detected
    if bbox is not None:
        x1, y1, x2, y2 = bbox

        # calculate center of box
        centerx = x1 + (x2 - x1)
        centery = y1 + (y2 - y1)

        cv2.circle(frame, (centerx, centery), 10, (0, 0, 255), 5)

        #    pyautogui.moveTo(centerx, centery, 0)

    cv2.imshow('Frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()