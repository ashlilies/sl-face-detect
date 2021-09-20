# data structure to create image
import numpy as np
import matplotlib.pyplot as plt

import cv2   # image processing with cv2

# bw_arr = np.array([   # 2d array?
#     [33,0,128],          # each num represents a pixel
#     [0,100,150],
#     [0,55,234]
# ])
#
# plt.imshow(bw_arr, cmap="gray")  # plt. image show, colourmap - grayscale
# plt.show()   # renders the image on our computer

# rgb_arr = np.array([
#     # [[p1], [p2], [red, green, blue]]   list or tuple okay
#     [[255, 0, 0], [0, 255, 0]],    # list of rgb pixels in row1
#     [[0, 0, 0], [0, 0, 255]]       # list of rgb pixels in row2
# ])
#
# plt.imshow(rgb_arr)
# plt.show()

# CV2 ==> BGR
# PLT ==> RGB
img_bgr = cv2.imread("Day_1_CV/face.jpg")
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
cv2.imshow("Face", img_bgr)  # bgr format, cv2
cv2.waitKey()  # don't close img_bgr automatically


plt.imshow(img_rgb)  # rgb format, matplotlib
plt.show()
print(img_bgr)  # print face.jpg as array