# video capture using cv2
import numpy as np
import matplotlib.pyplot as plt
import cv2   # image processing with cv2

cap = cv2.VideoCapture(0)

while 1:
    ret, frame = cap.read()  # take snapshot of camera, put into arr
    cv2.imshow("Face Camera", frame)
    print(frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
