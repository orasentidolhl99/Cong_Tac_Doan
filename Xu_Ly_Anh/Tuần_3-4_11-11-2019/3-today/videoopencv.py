import numpy as np
import cv2

img =cv2.imread("anhtrung.jpg",1)
cv2.line(img, (0, 0),(400,800), (25,22,234), 5);
cv2.imwrite('anhxuatra.jpg',img)

#lưu 1 bức ảnh bằng python và vẽ 1 đường thẳng 