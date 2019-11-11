import cv2 as cv
src = cv.imread("caotoc.jpg", 0)
ret, image_binary = cv.threshold(src, 50, 255, cv.THRESH_BINARY)
bin = cv.adaptiveThreshold(src, 255, cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY, 15, 12)
cv.imshow("sss", image_binary)

cv.imshow("Thresh", image_binary)
cv.imshow("adaptive_Thresh", bin)

cv.waitKey(0)
cv.destroyAllWindows()
