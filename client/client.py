import sys
import os
import time

import numpy as np
import cv2

import socket

sys.path.insert(1, '/Users/yuchihsu/Desktop/NTU/110-1/電腦網路導論/final project/Tests/rtp_test/utils')
from rtp_packet import rtp_packet


def decodeJpeg(data):
    data = np.frombuffer(data, dtype=np.uint8)
    image = cv2.imdecode(data, cv2.IMREAD_ANYCOLOR)   
    return image

if __name__ == "__main__":
    try:
        SERVER_HOST = sys.argv[1]
        SERVER_PORT = int(sys.argv[2])
    except:
        print(" Usage: server.py <server_host> <server_port> \n")
        sys.exit()


    server_addr = (SERVER_HOST, SERVER_PORT)
    rtpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        outdata = input('please input message: ')
        print('sendto ' + str(server_addr) + ': ' + outdata)
        rtpSocket.sendto(outdata.encode(), server_addr)
        while True:
        
            indata, addr = rtpSocket.recvfrom(65536)
            
            rtpPacket = rtp_packet()
            rtpPacket.decode(indata)
            frame = decodeJpeg(rtpPacket.getPayload())

            print('receive: ', rtpPacket.getSequenceNumber())
            #frame = decodeJpeg(indata)
            cv2.imshow('My Video', frame)
            if cv2.waitKey(25) == ord('q'):
                # do not close window, you want to show the frame
                # cv2.destroyAllWindows();
                break
        





