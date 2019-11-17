#Bài tập: Viết chương trình đọc vào 1 ảnh màu, sau đó được chuyển đổi qua ảnh xám gray 
# và được làm trơn đi nhờ hàm GaussianBlur. Sử dụng hàm Canny để tìm ra các điểm biên, 
# sử dụng HoughLines và HoughCircles để tìm ra các đường thẳng, đường tròn trong ảnh.

import cv2
import numpy as np


#https://blog.vietnamlab.vn/2018/02/27/xu-ly-anh-voi-opencv-tut-2-chuyen-doi-anh-mau/
# https://minhng.info/tutorials/xu-ly-anh-opencv-hien-thuc-canny-edge.html
# https://docs.opencv.org/4.0.0/dd/d1a/group__imgproc__feature.html#ga04723e007ed888ddf11d9ba04e2232de
# https://docs.opencv.org/master/da/d22/tutorial_py_canny.html
# https://minhng.info/tutorials/phat-hien-duong-thang-hough-transform.html
# https://kupdf.net/download/m-7897-t-s-7889-h-agrave-m-x-7917-l-yacute-7843-nh-trong-opencv-docx_5908597edc0d60391e959e90_pdf
# https://dsp.stackovernet.com/vi/q/4999
#Show Pic (0, 1, CV_LOAD_IMAGE_COLOR)
#Show ảnh xám dùng gray
img = cv2.imread('12.png',0)
#image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
image = cv2.GaussianBlur(img, (5, 5), 0)
edges = cv2.Canny(img,100,200)
lines = cv2.HoughLines(edges, rho=1, theta=np.pi/180, threshold=100)
circles = cv2.HoughCircles(image, cv2.cv.CV_HOUGH_GRADIENT,  2, 32, param1=200, param2=100)



cv2.imshow('Pic_Girl', img)
#cv2.imshow('Pic_Girl', image)
#cv2.imshow('Pic_Girl',edges)
#cv2.imshow('Pic_Girl', lines)
cv2.imshow('Pic_Girl', circles)

cv2.waitKey(0)
cv2.destroyAllWindows()

imghsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
imghsv[:,:,2] = [[max(pixel - 25, 0) if pixel < 190 else min(pixel + 25, 255) for pixel in row] for row in imghsv[:,:,2]]
cv2.imshow('contrast', cv2.cvtColor(imghsv, cv2.COLOR_HSV2BGR))
#cv2.imwrite('112.png',cv2.cvtColor(imghsv, cv2.COLOR_HSV2BGR))


plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()

for line in lines:
    rho, theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))
    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
#cv2.imwrite('123.png',img)

if circles is not None:
    # convert the (x, y) coordinates and radius of the circles to integers
    circles = np.round(circles[0, :]).astype("int")

   # loop over the (x, y) coordinates and radius of the circles
    for (x, y, r) in circles:
        # draw the circle in the output image, then draw a rectangle
        # corresponding to the centre of the circle
        cv2.circle(output, (x, y), r, (0, 255, 0), 4)
        cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)

    # show the output image
    cv2.imshow("output", np.hstack([image]))
cv2.waitKey(0)


cv2.waitKey(0)
cv2.destroyAllWindows()




