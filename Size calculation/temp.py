import cv2

cap = cv2.VideoCapture(0)

cap.set(3, 2592)  # Set horizontal resolution
cap.set(4, 1944)  # Set vertical resolution

_, im = cap.read()
img = im[445:1525 , 479:1725]
cv2.imwrite("example.jpg", img)
