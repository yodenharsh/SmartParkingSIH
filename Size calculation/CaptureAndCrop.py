import cv2
from PIL import Image
import os
from time import sleep
import PIL
import picamera

#camera = picamera.PiCamera()
#camera.resolution = (2592, 1944)
#sleep(2)
#camera.capture('example.png')
#camera.close()
def capture():
    #camera = picamera.PiCamera()
    #camera.start_preview()
    #camera.capture("example.png")
    #camera.stop_preview()
    #camera.close()
    os.popen("raspistill -o example.png --nopreview")

def crop(x_start, x_end, y_start, y_end):
    image = cv2.imread("example.png")
    cropped_img = image[y_start:y_end, x_start:x_end]
    cv2.imshow("Cropped image", cropped_img)
    cv2.imwrite("examplecrop.png", cropped_img)
    sleep(5)
    cv2.imshow("Cropped image", cropped_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
