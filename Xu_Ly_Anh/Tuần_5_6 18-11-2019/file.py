import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt

def change_brightness(img, alpha, beta):
    img_baby = np.asarray(alpha*img + beta, dtype=int)
    img_baby[img_baby>255] = 255
    img_baby[img_baby<0] = 0
    return img_baby

def XoayImage(image, angle): 
    center=tuple(np.array(image.shape[0:2])/2) 
    rot_mat = cv2.getRotationMatrix2D(center,angle,1.0) 
    return cv2.warpAffine(image, rot_mat, image.shape[0:2],flags=cv2.INTER_LINEAR) 
        
if __name__ == "__main__":
    alpha = 1.0
    beta = 50
    if len(sys.argv) == 3:
        alpha = float(sys.argv[1])
        beta = int(sys.argv[2])
    imgbaby = cv2.imread('baby.png') 

    
    # Đọc 2 bức ảnh
    img = cv2.imread('car-left.tif',1)
    image = cv2.imread('car-right.tif',1)

    # Cộng 2 bức ảnh
    imag = cv2.add(img,image)

    # Trừ 2 bức ảnh
    image4 = imag - img

    # Tăng độ sáng cho hình
    image5 = cv2.imread('after.jpg')
    img_baby = change_brightness(imgbaby, alpha = 15, beta = 1)

    # Nghịch đảo hình ảnh
    image6 = cv2.imread('boy.tf')
    #image6_Chuyen = imcomplement(image6)
    #gray = cv2.cvtColor(image6, cv2.COLOR_BGR2GRAY)
    #edgeMap = imutils.auto_canny(gray)
    

    # Hàm nhân ma trận cho ảnh số 

    # Phép Toán nhị phân

    # Phép toán di chuyển, thay đổi, xoay
    #-------------Xoay--------------
    image10 = cv2.imread('car-left.tif',1)
    image10 = XoayImage(image10, angle = 70)
    
    #---------------Zoom--------------->
    image10_zoom = cv2.imread(r'after.jpg')
    scale_percent = 100
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    resized = cv2.resize(image10_zoom, dim, interpolation=cv2.INTER_AREA)
    
    # Tăng độ tương phản
    #image1111 = cv2.imread('salzburg.png',1)
    #cv2.imshow("Original image",image1111)
    #imagehot = cv2.createCLAHE(clipLimit=10., tileGridSize=(8,8))

    #lab = cv2.cvtColor(image1111, cv2.COLOR_BGR2LAB) 
    #l, a, b = cv2.split(lab) 

    #l2 = imagehot.apply(l)

    #lab = cv2.merge((l2,a,b))
    #img2 = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)

    # Hàm cân bằng Histogram
    image_dau = cv2.imread(r"pollen_image.tif", 0)
    image_copy = image_dau.copy()
    cv2.equalizeHist(image_dau,image_copy)
    

    # Xử lý bộ lọc, nhiễu

    
    #>>>>>>>>>--------------------------------------------------------------->>>>>>>>>
    #cv2.imshow('Pic_2',image)

    #cv2.imshow('Pic_3',imag)

    #cv2.imshow('Pic_4',image4)

    #cv2.imshow('Pic_5_Goc',imgbaby)
    #cv2.imwrite('after.jpg', img_new)
    #cv2.imshow('After_edit',image5)

    #cv2.imshow('Show',image6)
    #cv2.imshow("Original", logo)
    #cv2.imshow("Automatic Edge Map", edgeMap)

    #cv2.imshow('Show_pic10',image10)
    #cv2.imshow("Resized image", resized)

    #cv2.imshow('Increased contrast', img2)

    #cv2.imshow('Anh Goc',image_dau)
    #cv2.imshow('Anh_after',image_copy)
    

    cv2.waitKey(0)
    cv2.destroyAllWindows()

