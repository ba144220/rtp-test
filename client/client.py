import sys, traceback, threading, socket, os, time
sys.path.insert(1, '/Users/yuchihsu/Desktop/NTU/110-1/電腦網路導論/final project/cn-final-proj/utils')
import numpy as np
import cv2

import socket
# def colored(r, g, b, text):
#     return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

# def plot(data, h, w):
#     os.system('cls' if os.name == 'nt' else 'clear')

   
#     display = ' .,-~+=<#&%$@'
#     for i in range(0,h):
#         for j in range(0,w):
#             # val = int(data[i][j]//20)
#             coloredText = colored(data[i][j][0], data[i][j][1], data[i][j][2], '@')
#             print(coloredText, end='')
#         print()

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
        fc = 0
        while True:
        
            indata, addr = rtpSocket.recvfrom(65536)
            print('receive: ',fc)
            frame = decodeJpeg(indata)
            cv2.imshow('My Video', frame)
            if cv2.waitKey(25) == ord('q'):
                # do not close window, you want to show the frame
                # cv2.destroyAllWindows();
                break
        
            fc+=1




