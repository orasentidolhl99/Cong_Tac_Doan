import numpy as np
import cv2
img = cv2.imread ("anhtrung.jpg", 0)
print(img.shape) # xem thuộc tính của ảnh (kích thước chiều cao, chiều rộng và kênh màu)
Y= (img.shape[0]) #lấy chiều cao của ảnh
print (Y)
y = Y//2 #phép chia lấy phần nguyên - đọc thêm các toán tử trong python

X= (img.shape[1]) # lấy chiều rộng của ảnh
print (X)

#cắt 1 ảnh từ ảnh lớn, chiều cao từ pixel 20 đến y; chiều rộng từ pixel 20 đến 450)
#subimg = img [20:y, 20:450] 
subimg = img [50:y, 50:850]
cv2.imwrite("anhcat1.jpg", subimg) # lưu thành 1 file ảnh mới
#subimg = subimg[:,:,1] #đổi thang màu của ảnh có các kênh: 0; 1; 2;
cv2.imshow("anhcat1", subimg)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow("anhtrung",img)

k = cv2.waitKey() # đoạn này chỉ là mình thử các lệnh rẽ nhánh If.... elif với else
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
# k == ord('s'):
    cv2.imwrite("anhxam.jpg",img)
    cv2.destroyAllWindows()
else:
    cv2.destroyAllWindows()