import cv2
src = cv2.imread("caotoc.jpg", 1)
dst = src.copy()

alpha = 1
beta = -30
for i in range(0, src.shape[0]):
    for j in range(0, src.shape[1]):
        for k in range(0,3):
            dst[i, j, k] = alpha * src[i, j, k] + beta
cv2.imshow("before", src)
cv2.imshow("after", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
