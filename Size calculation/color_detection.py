import numpy as np
import cv2

def detectYellow():
    frame = cv2.imread("examplecrop.png")
    height, width, channels = frame.shape #[:2]
    print(height, " ", width)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    upper_yellow  = np.array([45, 255, 255])
    lower_yellow = np.array([22, 93, 0])

    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

    result = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('frame', result)

    if cv2.waitKey() == ord('q'):
        exit()

    cv2.destroyAllWindows()
    
    
detectYellow()