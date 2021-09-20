# object (face) detection using pre-trained cv2 cascade classifier
# import numpy as np
# import matplotlib.pyplot as plt
import cv2   # image processing with cv2

# download parameters as an .xml file and load into CV2 CascadeClassifier fn
# we are using faces for now, so get a faces cascade
clsf = cv2.CascadeClassifier("Day_1_CV/haarcascade_frontalface_default.xml")

# Running the cascade classifier (clsf)
# ScaleFactor - reduce image size, minNeighbours - higher val more accurate
# Pass in grayscale image to our clsf
img = cv2.imread("Day_1_CV/face.jpg")
img_bw = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # conv to b/w; cascade only b/w
boxes = clsf.detectMultiScale(img_bw, 1.3, 5)   # performs recognition
print(boxes)  # 4 vals [xCoord rightwards, yCoord downwards, width, height]

for box in boxes:  # draw rectangles
    x, y, width, height = box
    cv2.rectangle(img, (x, y), (x+width, y+height), (0, 0, 255), 4)

cv2.imshow("Detection", img)
cv2.waitKey()