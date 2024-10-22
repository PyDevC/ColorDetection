from colordetection.detector import detector
import cv2
import sys

if __name__ == "__main__":
    mode = sys.argv[3]
    color = sys.argv[1]
    i = sys.argv[2]

    if mode.lower() == '-i':
        img = cv2.imread(f"../test/{i}")
        detector(img,color)
        cv2.imshow(i,img)
        if cv2.waitKey(0):
            cv2.destroyAllWindows()
    elif mode.lower() == '-v':
        cam = cv2.VideoCapture(0)
        while True:
            _, frame = cam.read()
            detector(frame, color)
            cv2.imshow("Camear", frame)
            if cv2.waitKey(0):
                cv2.destroyAllWindows()
                break