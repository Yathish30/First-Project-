import os
import re
import cv2
import numpy as np
from tqdm import tqdm_notebook as TQ
import matplotlib.pyplot as plt

# accessing the dwonloaded frame
Frames_clr = os.listdir('Y:\\LANE LINE\\frames\\')
Frames_clr.sort(key=lambda f: int(re.sub('\D', '', f)))

# loading the frame
Images_clr=[]
for i in TQ(Frames_clr):
    img = cv2.imread('Y:\\LANE LINE\\frames\\'+i)
    Images_clr.append(img)

#specify frame index
idx = int(input("Select any random frames betwwe 0 - 1108: \n"))

#plot frame
plt.figure(figsize=(10,10))
plt.imshow(Images_clr[idx][:,:,0],cmap= "gray")
plt.show()


# create a zero array
stencil = np.zeros_like(Images_clr[idx][:,:,0])

# specifying coordinates of the polygon
polygon = np.array([[50,270], [220,160], [360,160], [480,270]])

# filling polygon with ones
cv2.fillConvexPoly(stencil, polygon, 1)

# ploting polygon
plt.figure(figsize=(10,10))
plt.imshow(stencil, interpolation='nearest',cmap= "gray")
plt.show()

image = cv2.bitwise_and(Images_clr[idx][:,:,0], Images_clr[idx][:,:,0], mask=stencil)

# ploting masked frame
plt.figure(figsize=(10,10))
plt.imshow(image, cmap= "gray")
plt.show()

############# IMAGE THRESHOLDING ###############

# applying  image thresholding
ret, thresh = cv2.threshold(image, 130, 145, cv2.THRESH_BINARY)

# ploting image
plt.figure(figsize=(10,10))
plt.imshow(thresh, cmap= "gray")
plt.show()


#################### Hough Line Transformation ###################


lines = cv2.HoughLinesP(thresh, 1, np.pi/180, 30, maxLineGap=200)

# create a copy of the original frame
HLT= Images_clr[idx][:,:,0].copy()

# drawing Hough lines
for line in lines:
  x1, y1, x2, y2 = line[0]
  cv2.line(HLT, (x1, y1), (x2, y2), (255, 0, 0), 3)

# ploting frame
plt.figure(figsize=(10,10))
plt.imshow(HLT, cmap= "gray")
plt.show()
