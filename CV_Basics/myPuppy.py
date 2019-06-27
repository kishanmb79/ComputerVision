import cv2
import numpy as np
#
img  = cv2.imread('DATA/00-puppy.jpg')
#
# while the above img is true and you are able to read it 
# 
while True:
    # if you are able to read img show it 
    cv2.imshow('Puppy',img)
    # now wait until hit esc key 
    # 
    # here 0xFF is a hexadecimal constant which is 11111111 in binary. 
    # By using bitwise AND (&) with this constant, 
    # it leaves only the last 8 bits of the original 
    # (in this case, whatever cv2.waitKey(0) is)
    #
    # if we waited at least 1ms AND press esc key 
    if cv2.waitKey(1) & 0xFF == 27:
        # once hit the esc key break out of it 
        # and do not show the image 
        break

cv2.destroyAllWindows()

