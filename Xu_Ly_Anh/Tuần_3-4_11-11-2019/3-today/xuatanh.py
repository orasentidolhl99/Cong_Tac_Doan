import numpy as np
import cv2
image = cv2.imread("anhtrung.jpg",1)
cv2.imshow("Huong Le", image)
k = cv2.waitKey(0)
if k == 27: # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    print ("width: %d pixels"% (image.shape[1]))
    print ("height: %d pixels" % (image.shape[0]))
    print ("channels: %d channels" % (image.shape[0]))
cv2.imwrite("anhGray.jpg",image)
cv2.destroyAllWindows()