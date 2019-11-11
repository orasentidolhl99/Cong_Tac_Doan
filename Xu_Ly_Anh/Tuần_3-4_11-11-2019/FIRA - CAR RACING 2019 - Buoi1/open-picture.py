import cv2
src = cv2.imread("caotoc.jpg", 1)
cv2.imshow("src", src)
gray = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)
hsv = cv2.cvtColor(src,cv2.COLOR_BGR2HSV)
ycrcb = cv2.cvtColor(src,cv2.COLOR_BGR2YCrCb)
cv2.imshow("src",src)
cv2.imshow("gray",gray)
cv2.imshow("hsv",hsv)
cv2.imshow("ycrcb",ycrcb)
cv2.waitKey(0)
cv2.destroyAllWindows()

