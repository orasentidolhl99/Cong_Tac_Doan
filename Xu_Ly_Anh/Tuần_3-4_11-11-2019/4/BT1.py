import cv2
import numpy as np


doc_file = cv2.imread("rubik.jpg", 1)

gray_image = cv2.cvtColor(doc_file, cv2.COLOR_BGR2GRAY)
hsv = cv2.cvtColor(doc_file, cv2.COLOR_BGR2HSV)
ycrcb = cv2.cvtColor(doc_file, cv2.COLOR_BGR2YCrCb)
ret,thresh = cv2.threshold(doc_file,128,128,128, cv2.THRESH_BINARY)#lấy ảnh nhị phân
brightLAB = cv2.cvtColor(doc_file, cv2.COLOR_BGR2LAB)
darkLAB = cv2.cvtColor(doc_file, cv2.COLOR_BGR2LAB)

bgr = [40, 158, 16]
thresh = 40
B = np.array([])
G = np.array([])
R = np.array([])

im = cv2.imread("rubik.jpg")

nBGR = np.array([bgr[0] - thresh, bgr[1] - thresh, bgr[2] - thresh])
maxBGR = np.array([bgr[0] + thresh, bgr[1] + thresh, bgr[2] + thresh])
#convert mảng 1D thành 3D, sau đó chuyển đổi nó thành HSV và lấy phần tử đầu tiên
# cái này sẽ giống như trong hình trên [65, 229, 158]
hsv = cv2.cvtColor( np.uint8([[bgr]] ), cv2.COLOR_BGR2HSV)[0][0]

minHSV = np.array([hsv[0] - thresh, hsv[1] - thresh, hsv[2] - thresh])
maxHSV = np.array([hsv[0] + thresh, hsv[1] + thresh, hsv[2] + thresh])

maskHSV = cv2.inRange(brightHSV, minHSV, maxHSV)
resultHSV = cv2.bitwise_and(brightHSV, brightHSV, mask = maskHSV)
#convert mảng 1D thành 3D, sau đó chuyển đổi nó thành YCrCb và lấy phần tử đầu tiên
ycb = cv2.cvtColor( np.uint8([[bgr]] ), cv2.COLOR_BGR2YCrCb)[0][0]

minYCB = np.array([ycb[0] - thresh, ycb[1] - thresh, ycb[2] - thresh])
maxYCB = np.array([ycb[0] + thresh, ycb[1] + thresh, ycb[2] + thresh])
 
maskYCB = cv2.inRange(brightYCB, minYCB, maxYCB)
resultYCB = cv2.bitwise_and(brightYCB, brightYCB, mask = maskYCB)
 
#convert mảng 1D thành 3D, sau đó chuyển đổi nó thành LAB và lấy phần tử đầu tiên 
lab = cv2.cvtColor( np.uint8([[bgr]] ), cv2.COLOR_BGR2LAB)[0][0]
 
minLAB = np.array([lab[0] - thresh, lab[1] - thresh, lab[2] - thresh])
maxLAB = np.array([lab[0] + thresh, lab[1] + thresh, lab[2] + thresh])
 
maskLAB = cv2.inRange(brightLAB, minLAB, maxLAB)
resultLAB = cv2.bitwise_and(brightLAB, brightLAB, mask = maskLAB)
 
cv2.imshow("Result BGR", resultBGR)
cv2.imshow("Result HSV", resultHSV)
cv2.imshow("Result YCB", resultYCB)
cv2.imshow("Output LAB", resultLAB)


cv2.imshow('hinh goc',doc_file)
cv2.imshow('Gray',gray_image)
cv2.imshow('HSV',hsv)
cv2.imshow('YCRCB',ycrcb)
cv2.imshow('Thresh',thresh)
cv2.imshow('BrightLAB',brightLAB)
cv2.imshow('darktLAB',darkLAB)
                  
cv2.waitKey(0)
cv2.destroyAllWindows()
