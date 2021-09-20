import cv2
import numpy as np
import streamlit as sl
from PIL import Image  # import a func only from PIL library

# our classifier
clsf = cv2.CascadeClassifier("Day_1_CV/haarcascade_frontalface_default.xml")

def detect(PIL_img):  # pillow (?) format detection
    cv2_img = cv2.cvtColor(np.array(PIL_img), cv2.COLOR_RGB2BGR)
    cv2_img_bw = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2GRAY)

    boxes = clsf.detectMultiScale(cv2_img_bw, 1.3, 5)
    for box in boxes:  # draw the boxes
        x, y, width, height = box
        cv2.rectangle(cv2_img, (x, y), (x+width, y+height), (255, 0, 255), 4)
    sl.image(cv2.cvtColor(cv2_img, cv2.COLOR_BGR2RGB))
    sl.markdown("Detected %d faces" % len(boxes))


sl.header("Face Detection")
sl.text("Provide an image and we'll detect the faces.")

uploaded_file = sl.file_uploader("Upload image here...",  # PIL format
                                        type=[".jpg", ".png", ".jpeg"])
if uploaded_file is not None:
    PIL_img = Image.open(uploaded_file)
    detect(PIL_img)
