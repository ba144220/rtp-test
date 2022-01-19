import random, math
import cv2
import numpy as np

import time
from random import randint
import sys, traceback, threading, socket, os
sys.path.insert(1, '/Users/yuchihsu/Desktop/NTU/110-1/電腦網路導論/final project/Tests/rtp_test/utils')

from rtp_packet import rtp_packet



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





if __name__ == "__main__":
    try:
        SERVER_PORT = int(sys.argv[1])
    except:
        print(" Usage: server.py <server_port> \n")
        sys.exit()


    rtpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    rtpSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    rtpSocket.bind(('', SERVER_PORT))

    print('RTP server started')
    print('wait for connection...')

    res, fc = encodeJpeg('videos/test_180_320.mp4')


    while True:
        
        indata, addr = rtpSocket.recvfrom(1024)
        print('recvfrom ' + str(addr) + ': ' + indata.decode())
        
        for i in range(fc):
            outdata = res[i]
            print('Sending frame: ', i , ' size: ',sys.getsizeof(outdata))

            #outdata = 'echo ' + indata.decode()
            rtpPacket = rtp_packet()
            rtpPacket.encode(2,0,0,0,0,0,i,0,outdata)

            rtpSocket.sendto(rtpPacket.getPacket(), addr)
            time.sleep(0.033)
           
