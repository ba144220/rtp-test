import random, math
import cv2
import numpy as np

import time
from random import randint
import sys, traceback, threading, socket, os
sys.path.insert(1, '/Users/yuchihsu/Desktop/NTU/110-1/電腦網路導論/final project/Tests/rtp_test/utils')

from rtp_packet import rtp_packet


def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)


def plot(data, h, w):
    os.system('cls' if os.name == 'nt' else 'clear')

   
    display = ' .,-~+=<#&%$@'
    for i in range(0,h):
        for j in range(0,w):
            # val = int(data[i][j]0)
            coloredText = colored(data[i][j][0], data[i][j][1], data[i][j][2], '@')
            print(coloredText, end='')
        print()



def convertFileToNumPy(fileName):
    cap = cv2.VideoCapture(fileName)
    print('check')
    frameCount = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frameWidth = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frameHeight = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    print(frameHeight, ' ,', frameWidth)
    print("Single Frame Size: " , frameHeight*frameWidth*3)
    fc = 0
    ret = True

    res = []

    header = bytearray(4)
    header[0] = (frameHeight) >> 8
    header[1] = (frameHeight) % 256
    header[2] = (frameWidth) >> 8
    header[3] = (frameWidth) % 256
    print(header)
    input('type anything to continue...')

    while (fc < frameCount  and ret):
        print(fc)
        ret, frame = cap.read()
        dt = frame.dtype

        fr = bytearray((frameWidth)*(frameHeight)*3)


        c = 0
        for color in range(3):
            for i in range(frameHeight):
                for j in range(frameWidth):    
                    fr[c] = frame[i][j][color] % 256
                    c += 1
        
        frame = []
        c = 0
        length = (frameHeight)*(frameWidth)
        for i in range(frameHeight):
            tmp = []
            for j in range(frameWidth):  
                tmp.append([int(fr[c]), int(fr[c+length]),int(fr[c]+length*2)])
                c+=1
            frame.append(tmp)
            
        
        #plot(frame, frameHeight, frameWidth)

        print(len(fr))
        
        res.append(header + fr)
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

    res, fc = convertFileToNumPy('test.mp4')


    while True:
        
        indata, addr = rtpSocket.recvfrom(1024)
        print('recvfrom ' + str(addr) + ': ' + indata.decode())

        
        
        for i in range(fc):
            outdata = res[i]
            print('Sending frame: ', i , ' size: ',sys.getsizeof(outdata))

            #outdata = 'echo ' + indata.decode()
            rtpSocket.sendto(outdata, addr)
            time.sleep(0.033)
           
