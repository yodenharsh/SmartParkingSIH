from picamera import PiCamera
from time import sleep
import os

camera = PiCamera()
sleep(7)
while True :
    camera.start_preview()
    sleep(4)
    camera.stop_preview()
    camera.capture('/tmp/example.jpg')
    #exec("jpgToPng.py")
    os.popen("python /home/pi/Bookshelf/Size\ calculation/jpgToPng.py")
    sleep(4)
    #exec("object_size.py")
    os.popen("python object_size.py")