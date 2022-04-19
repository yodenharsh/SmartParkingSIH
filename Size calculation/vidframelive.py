import cv2
from time import sleep
from picamera import PiCamera

cap = PiCamera()
i = 0

while(cap.isOpened()):
	ret, frame = cap.read()

	if ret == False:
		break

	cv2.imwrite('Frame'+'.png', frame)
	sleep(1)

cap.release()
cv2.destroyAllWindows()

