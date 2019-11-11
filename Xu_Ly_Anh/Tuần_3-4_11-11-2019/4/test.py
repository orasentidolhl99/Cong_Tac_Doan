import cv2 as cv

# đọc file
src = cv.imread("aa.jpg", 1)
cv.imshow("src", src)

#RBG_to_CMYK = cv.cvtColor(src, cv.COLOR_BGR2YCR_CB)
#RBG_to_HSV = cv.cvtColor(src,cv.COLOR_BGR2HSV)
RBG_to_HLS = cv.cvtColor(src,cv.COLOR_BGR2HLS)

#C, M, Y = RBG_to_CMYK[:,:,0], RBG_to_CMYK[:,:,1], RBG_to_CMYK[:,:,2]
#H, S, V = RBG_to_HSV[:,:,0], RBG_to_HSV[:,:,1], RBG_to_HSV[:,:,2]
H, L, S = RBG_to_HLS[:,:,0], RBG_to_HLS[:,:,1], RBG_to_HLS[:,:,2]

#cv.imshow("C", H)
#cv.imshow("M", L)
#cv.imshow("Y", S)

#cv.imshow("H", H)
#cv.imshow("S", S)
#cv.imshow("V", V)

cv.imshow("H", H)
cv.imshow("L", L)
cv.imshow("S", S)

cv.waitKey(0)
cv.destroyAllWindows()