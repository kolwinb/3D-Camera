#!/usr/bin/python

import numpy as np
import cv2

cap1 = cv2.VideoCapture(1)
cap2 = cv2.VideoCapture(2)
cap1.set(3,1280) #width
cap1.set(4,720) #height
cap2.set(3,1280)
cap2.set(4,720)
print cap1
#out = cv2.VideoWriter("test-DIVX.avi",cv2.VideoWriter_fourcc(*'DIVX'),25,(2560,720))
out = cv2.VideoWriter("disini-1st-birthday-2-MJPG.avi",cv2.VideoWriter_fourcc(*'MJPG'),25,(2560,720))
#    out = cv2.VideoWriter("test-AVC1.avi",cv2.VideoWriter_fourcc(*'AVC1'),25,(2560,720))
#out = cv2.VideoWriter("test-H264-3.avi",cv2.VideoWriter_fourcc(*'H264'),25,(2560,720))
#out = cv2.VideoWriter("test-XVID.avi",cv2.VideoWriter_fourcc(*'XVID'),25,(2560,720))
#    out=cv2.VideoWriter('video.avi',-1,1,(2560,720))

while(True):
    # Capture frame-by-frame
    ret, frame1 = cap1.read()
    ret, frame2 = cap2.read()
    h1,w1 = frame1.shape[:2]
    h2,w2 = frame2.shape[:2]
    concat=np.concatenate((frame1,frame2),axis=1)
    cv2.imshow('blank',concat)
#    out = cv2.VideoWriter('output.avi',-1,1,(720,2560))
#    cv2.imwrite('3d-test.avi',concat)	
    out.write(concat)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
out.release()
cv2.destroyAllWindows()
