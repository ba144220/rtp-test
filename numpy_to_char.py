
import os, time, cv2
import numpy as np

def convertFileToNumPy(fileName):
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
        print(fc)
        ret, frame = cap.read()
        dt = frame.dtype

        fr = bytearray(frameWidth*frameHeight*3)
        c = 0
        for color in range(3):
            for i in range(frameHeight):
                for j in range(frameWidth):    
                    fr[c] = frame[i][j][color] % 256
                    c += 1
        print(len(fr))

        res.append(fr)
        fc += 1

    return res, fc

res, fc = convertFileToNumPy("test.mp4")