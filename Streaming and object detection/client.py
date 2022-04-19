from imutils.video import VideoStream
import imagezmq
import argparse
import socket
import time

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser() 
ap.add_argument("-s", "--server-ip", required=True,
                help = "ip address of the server to whic the client will connect")
args = vars(ap.parse_args())

#initialize the ImageSender object with the socket address of the server
sender = imagezmq.ImageSender(connect_to = "tcp//{}:5555".format(args["server_ip"]))
#Look into the tcp address when testing

#get the host name, initialize the video stream , and allow the camera sensor to warm up
rpiName = socket.gethostname()
vs = VideoStream(usePICamera=True).start() #add ',' in front of True and write
#resolution = (x, y)
#vs = VideoStream(src=0).start()  //If camera is any USB camera, uncomment this and comment
#the line above
time.sleep(2.0)

while True:
    #read the frame from the camera and sent it to the server
    frame = vs.read()
    sender.send_image(rpiName, frame)