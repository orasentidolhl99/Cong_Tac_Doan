import cv2
import numpy as np

# đọc file
src = cv2.imread("aa.jpg", 1)
cv2.imshow("src", src)
gray = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)
hsv = cv2.cvtColor(src,cv2.COLOR_BGR2HSV)
ycrcb = cv2.cvtColor(src,cv2.COLOR_BGR2YCrCb)
#lấy ảnh nhị phân
ret,thresh = cv2.threshold(src,128,128,128, cv2.THRESH_BINARY)
brightLAB = cv2.cvtColor(src, cv2.COLOR_BGR2LAB)
darkLAB = cv2.cvtColor(src, cv2.COLOR_BGR2LAB)
#show ảnh
cv2.imshow("src",src)
cv2.imshow("gray",gray)
cv2.imshow("hsv",hsv)
cv2.imshow("ycrcb",ycrcb)
cv2.imshow('Thresh',thresh)
cv2.imshow('BrightLAB',brightLAB)
cv2.imshow('darktLAB',darkLAB)

anhdo = src(:,:,1)


cv2.waitKey(0)
cv2.destroyAllWindows()

