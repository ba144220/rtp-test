import cv2
import numpy as np
import os
import time
import sys


def encodeJpeg(fileName):
    cap = cv2.VideoCapture(fileName)
    print('check')
    frameCount = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frameWidth = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frameHeight = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    print("Single Frame Size: " , frameHeight*frameWidth*3)
    fc = 0
    ret = True

    res = []

    while (fc < frameCount  and ret):
        print('Preprocessing Frame: ',fc)
        ret, frame = cap.read()

        _, fr = cv2.imencode('.JPEG', frame)

        fr = fr.tostring()
        print('size: ',sys.getsizeof(fr))
        print('-'*60)
        res.append(fr)
        fc += 1
    cap.release()
    return res, fc

def decodeJpeg(data):
    data = np.frombuffer(data, dtype=np.uint8)
    image = cv2.imdecode(data, cv2.IMREAD_ANYCOLOR)   
    return image




res, fc = encodeJpeg('videos/test_90_160.mp4')

for i in range(fc):
    
    image = decodeJpeg(res[i])
    cv2.imshow('Frame', image)
    # add waitKey for video to display
    time.sleep(0.01)
    if cv2.waitKey(25) == ord('q'):
        # do not close window, you want to show the frame
        # cv2.destroyAllWindows();
        break
   






