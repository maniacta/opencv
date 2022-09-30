import cv2
import numpy as np
import matplotlib.pyplot as plt

imgfile = "hw2\\2\\11.png"

img = cv2.imread(imgfile)
b, g, r = cv2.split(img)
bH = cv2.equalizeHist(b)
gH = cv2.equalizeHist(g)
rH = cv2.equalizeHist(r)
result = cv2.merge((bH, gH, rH))
cv2.HoughLinesP
cv2.namedWindow("Input", 0)
cv2.resizeWindow("Input", 640, 480)
cv2.imshow("Input", img)
cv2.namedWindow("Result", 0)
cv2.resizeWindow("Result", 640, 480)
cv2.imshow("Result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()

# imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# plt.imshow(imgRGB)
# plt.show()
