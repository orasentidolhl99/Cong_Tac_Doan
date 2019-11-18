import sys
import cv2
import numpy as np
from matplotlib import pyplot as plt
def change_brightness(img, alpha, beta):
    img_baby = np.asarray(alpha*img + beta, dtype=int)
    img_baby[img_baby>255] = 255
    img_baby[img_baby<0] = 0
    return img_baby

if __name__ == "__main__":
    alpha = 1.0
    beta = 50
    if len(sys.argv) == 3:
        alpha = float(sys.argv[1])
        beta = int(sys.argv[2])
    imgbaby = cv2.imread('baby.png')

    image1 = cv2.imread('eight_pepper.tif',1)
    image2 = cv2.imread('eight_salt.tif',1)
    image3 = cv2.add(image1,image2)


    image4 = cv2.imread('pepper_salt.jpg',1)
    mask = np.zeros(image4.shape[:2],np.uint8)
    bgdModel = np.zeros((1,65),np.float64)
    fgdModel = np.zeros((1,65),np.float64)
    rect = (50,50,450,290)
    cv2.grabCut(image4,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)
    mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
    image4 = image4*mask2[:,:,np.newaxis]
    plt.imshow(image4),plt.colorbar(),plt.show()

    image5 = cv2.imread('blend_add.tif',1)

    image6 = cv2.imread('pepper_salt.jpg')
    img_baby = change_brightness(imgbaby, alpha = 15, beta = 1)

    imgcrop1 = image4[100:300, 100:400]
    imgcrop2 = image5[100:300, 100:400]
    imgcrop3 = imgbaby[100:300, 100:400]
    #image7 = cv2.add(image4,image5,imgbaby)
    










    #cv2.imshow('Pic_1',image1)
    #cv2.imshow('Pic_2',image2)
    #cv2.imshow('Pic_3',image3)
    cv2.imwrite('show_pic3.jpg', image3)

    cv2.imshow('Pic_4',image4)

    #cv2.imshow('Pic_5',image5)

    #cv2.imshow('Pic_6',image6)
    cv2.imshow('Pic_6_Goc',imgbaby)
    cv2.imshow('After_edit',image5)

    #cv2.imshow('Hinh_Thu_Duoc',image7)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
