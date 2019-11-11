import os, sys
import cv2

def convert_to_binary(img_grayscale, thresh=100):
    thresh, img_binary = cv2.threshold(img_grayscale, thresh, maxval=255, type=cv2.THRESH_BINARY)
    return img_binary

if __name__ == "__main__":
    assert len(sys.argv) == 2, '[USAGE] $ python anhnhiphan.py img_5.jpg'
    input_image_path = sys.argv[1]
    
    assert os.path.isfile(input_image_path), 'Image not found @ %s' % input_image_path
    
    # read color image with grayscale flag: "cv2.IMREAD_GRAYSCALE"
    img_grayscale = cv2.imread(input_image_path, cv2.IMREAD_GRAYSCALE)       # shape: (960, 960)
    # in ảnh ở thang độ xám 
    cv2.imwrite('grey_%s' % input_image_path, img_grayscale)
    #Xuất ảnh đen
    print('Lưu hình ảnh thang độ xám @ màu xám_%s' % input_image_path)
    
    img_binary = convert_to_binary(img_grayscale, thresh=100)
    cv2.imwrite('binary_%s' % input_image_path, img_binary)
    #Xuất ảnh trắng đen
    print('Lưu hình ảnh nhị phân @ nhị phân_%s' % input_image_path)