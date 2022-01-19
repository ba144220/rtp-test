import cv2
import numpy as np
import os
import time


cap = cv2.VideoCapture('test.mp4')
frameCount = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
frameWidth = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frameHeight = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))


buf = np.empty((frameCount, frameHeight, frameWidth, 3), np.dtype('uint8'))

fc = 0
ret = True

while (fc < frameCount  and ret):
    ret, buf[fc] = cap.read()
    fc += 1



print('C1')
cap.release()

print('C2')

display = '  .-:;=!#$@'

for fr in range(frameCount):
    os.system('cls' if os.name == 'nt' else 'clear')
    for i in range(0,frameHeight,10):
        for j in range(0,frameWidth,4):
            val = (buf[fr][i][j][0]+buf[fr][i][j][1]+buf[fr][i][j][2])//25
            print(display[val], end='')
        print()
    time.sleep(0.1)
    
print('C3')

print('C4')
#cv2.waitKey(0)

