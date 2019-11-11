import cv2

# read image
img = cv2.imread('anh1.jpg')

# replace blue channel with zero
img[:,:,1] = 1

# write / save modified image
cv2.imwrite('anh1-1.jpg', img)