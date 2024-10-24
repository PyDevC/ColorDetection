import colordetection.mask as m
import numpy as np
import cv2

def detector(frame, color):
    mask, color, color_name = m.hsvmethod(frame, color)

    contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > 300):
            x, y, w, h = cv2.boundingRect(contour)
            frame = cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
            cv2.putText(frame, color_name, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255))
