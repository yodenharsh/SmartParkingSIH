from picamera import PiCamera
from time import sleep
from PIL import Image
import os
import cv2
sleep(2)

while (1):
    camera = PiCamera()
    camera.start_preview()
    sleep(3)   
    camera.stop_preview()
    camera.capture('example.jpg')
    camera.close()
    os.popen("python temp.py")
    #camera prolly not needed?
    #cap = cv2.VideoCapture(0) 

    #cap.set(3, 2592)  # Set horizontal resolution
    #cap.set(4, 1944)  # Set vertical resolution

    #_, im = cap.read()
    #img = im[445:1525 , 479:1725]
    #cv2.imwrite("example.jpg", img) 
    #exec("jpgToPng.py")
    img = Image.open("example.jpg")
    img.save("example.png")
    sleep(4)
    #exec("object_size.py")
    os.popen("python object_size.py")
