from PIL import Image
import io, sys


fileName = 'videos/video.mjpeg'


try:
    videoFile = open(fileName, 'rb')
    print('-'*60 +  "\nVideo file : |" + fileName +  "| read\n" + '-'*60)
except:
    print("read " + fileName + " error")
    raise IOError

frameNum = 0

"""Get next frame."""

data = videoFile.read(5) # Get the framelength from the first 5 bytes
#data_ints = struct.unpack('<' + 'B'*len(data),data)
data = bytearray(data)

data_int = (data[0] - 48) * 10000 + (data[1] - 48) * 1000 + (data[2] - 48) * 100 + (data[3] - 48) * 10 + (data[4] - 48)# = #int(data.encode('hex'),16)

final_data_int = data_int

print(final_data_int)


if data:

    framelength = final_data_int#int(data)#final_data_int/8  # xx bytes
    # Read the current frame
    frame = videoFile.read(framelength)
    if len(frame) != framelength:
        raise ValueError('incomplete frame data')


    frameNum += 1
    print('-'*10 + "\nNext Frame (#" + str(frameNum) + ") length:" + str(framelength) + "\n" + '-'*10)

    print(frame)
    print(sys.getsizeof(frame))
    image = Image.open(io.BytesIO(frame))
    image.show()

