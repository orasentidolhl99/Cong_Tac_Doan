import sys
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

img_eight_pepper = cv.imread("eight_pepper.tif", cv.IMREAD_UNCHANGED)
img_eight_saft = cv.imread("eight_salt.tif", cv.IMREAD_UNCHANGED)
img_baby = cv.imread("baby.png", cv.IMREAD_UNCHANGED) # 378*284

img_blend_add = cv.imread("blend_add.tif", cv.IMREAD_UNCHANGED) # 180*180

def Imcomlement(Img):
    for img_X in range(0, len(Img)):
        for img_Y in range(0, len(Img[0])):
            Img[img_X, img_Y]=255-Img[img_X, img_Y]
    return Img

#Lượm muối tiêu
add_pepper_saft = cv.add(img_eight_pepper, img_eight_saft)
sub_tract = img_eight_saft - img_eight_pepper
pepper_saft = Imcomlement(sub_tract) # 242*308
# Đây là muối tiêu

# Chuẩn size ảnh
width=180
height=180
dim = (width, height)
# Chuẩn hoá size ảnh Baby
resized_baby = cv.resize(img_baby, dim, interpolation = cv.INTER_AREA)
baby_blend = cv.add(resized_baby, img_blend_add)

# Chuẩn size ảnh
width=180
height=180
dim = (width, height)
# Chuẩn hoá size ảnh Muối tiêu
resized_pepper_saft = cv.resize(pepper_saft, dim)
Final_image = resized_pepper_saft + baby_blend[:,:,0]

Tong_Ket_Qua = cv.resize(Final_image, (300,300))
cv.imshow('Muoi', pepper_saft)
cv.imshow('show_Ket_Qua', Tong_Ket_Qua)
cv.waitKey(0)
cv.destroyAllWindows()