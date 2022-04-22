from picamera import PiCamera
from time import sleep
import CaptureAndCrop
import object_size
import color_detection
import numpy as np

isEntry = True
while (1):
    if(isEntry):
        sleep(1)
        global dimA
        global dimB
        CaptureAndCrop.capture()
        CaptureAndCrop.crop(1669, 1893, 541, 1645) #captures and crops the image
        #img = Image.open("example.jpg")
        #img.save("example.png")#Converts to png format
        sleep(4)
        #exec("object_size.py")
        dimA, dimB = object_size.dimensionDetection()#Calling the object detection script        
        for i in range(len(dimA)):
            print(dimA[i])
            print(dimB[i], "\n\n")
        isEntry = False
    
    else:
        print("Temp print")
        CaptureAndCrop.crop(593, 1597, 577, 1621)
        sleep(2)
        color_detection.detectYellow()
        dimAParkingLot, dimBParkingLot = object_size.dimensionDetection()
        isEntry = True