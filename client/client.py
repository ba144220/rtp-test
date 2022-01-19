import sys, traceback, threading, socket, os, time
sys.path.insert(1, '/Users/yuchihsu/Desktop/NTU/110-1/電腦網路導論/final project/cn-final-proj/utils')


import socket
def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

def plot(data, h, w):
    os.system('cls' if os.name == 'nt' else 'clear')

   
    display = ' .,-~+=<#&%$@'
    for i in range(0,h):
        for j in range(0,w):
            # val = int(data[i][j]//20)
            coloredText = colored(data[i][j][0], data[i][j][1], data[i][j][2], '@')
            print(coloredText, end='')
        print()



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

            height = indata[0]<<8|indata[1]
            width = indata[2]<<8|indata[3]
            fr = indata[4:]
            print(height,  end=', ')
            print(width)
            length = height*width
            frame=[]
            c=0
            for i in range(height):
                tmp = []
                for j in range(width):  
                    tmp.append([int(fr[c]), int(fr[c+length]),int(fr[c]+length*2)])
                    c+=1
                frame.append(tmp)
            plot(frame, height,width)



            #print('recvfrom ' + str(addr) + ': ' + indata.decode())
