import cv2
import numpy as np

def hsvmethod(frame, color):
    """Check the color and adds the mask according to color.

    Parameters:
    frame -- the current frame or image read from cam.read() or cv2.imread()
             method.
    color -- the color of the mask (values: 'r', 'g', 'b')

    Calls the functions red_mask, green_mask, blue_mask according the value of
    color.

    returns a tuple (mask, color, color_name).
    where color is the tuple of rgb values of the color choosen,
    color_name is the name of the color
    """
    hsvFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    kernel = np.ones((5,5), "uint8")
    if color.lower() == 'r':
        mask = red_mask()
        return (mask, (), 'Red')
    elif color.lower() == 'g':
        mask = green_mask()
        return (mask, (), 'Green')
    elif color.lower() == 'b':
        mask = blue_mask()
        return (mask, (), 'Blue')


def red_mask():
    """Forms a mask of Red color using lower and upper bounds of the hsv color
    range of OpenCV.
    returns the the mask of red color.
    """
    red_lower = np.array([0, 100, 100], np.uint8)
    red_upper = np.array([10, 255, 255], np.uint8)
    red_mask = cv2.inRange(hsvFrame, red_lower, red_upper)

    red_mask = cv2.dilate(red_mask, kernel)
    res_red = cv2.bitwise_and(frame, frame, mask = red_mask)
    return red_mask

def green_mask():
    """Forms a mask of Green color using lower and upper bounds of the hsv color
    range of OpenCV.
    returns the the mask of Green color.
    """
    green_lower = np.array([0, 100, 100], np.uint8)
    green_upper = np.array([10, 255, 255], np.uint8)
    green_mask = cv2.inRange(hsvFrame, green_lower, green_upper)

    green_mask = cv2.dilate(green_mask, kernel)
    res_green = cv2.bitwise_and(frame, frame, mask = green_mask)
    return green_mask

def blue_mask():
    """Forms a mask of Blue color using lower and upper bounds of the hsv color
    range of OpenCV.
    returns the the mask of blue color.
    """
    blue_lower = np.array([0, 100, 100], np.uint8)
    blue_upper = np.array([10, 255, 255], np.uint8)
    blue_mask = cv2.inRange(hsvFrame, blue_lower, blue_upper)

    blue_mask = cv2.dilate(blue_mask, kernel)
    res_blue = cv2.bitwise_and(frame, frame, mask = blue_mask)
    return blue_mask
