from PIL import Image
import random


seed = 10

random.seed(seed)
im = Image.open('steg_image.jpg') # Can be many formats.
pix = im.load()

message = 'Hello, my name is Owen Clark. I go to St Birinus school, and am currently head boy there. ' \
          'Do you like mustard or cheese on your noodles? Bye.'
RorGorB = 1 #R = 0, G = 1, B = 2
dim = im.size

indexes = list(range(0,dim[0]*dim[1]))
random.shuffle(indexes)
print(indexes)
message = str(len(message)) + '||||' + message
lenlen = len(str(len(message)))

for i, char in enumerate(message):
    ASCII = ord(char)
    binary = bin(ASCII)[2:].zfill(8) # Bin converts to binary. It has a prefix which is removed. .zfill ensures that the integer is 8 bits not removing 0 prefixes.
    #for i in range(8-len(bin(char)))
    #print(binary)
    #print(chr(int(''.join(binary), 2)))
    for j, bit in enumerate(binary):
        x = indexes[8*i + j] % dim[0]
        y = int(indexes[8*i + j]/dim[0])

        RGB = pix[x, y]
        pixel_bin = list(bin(RGB[RorGorB])[2:].zfill(8))
        pixel_bin[7] = bit

        pb = ''
        for b in pixel_bin:
            pb += b

        if RorGorB == 0:
            RGB = (int(pb, 2), RGB[1], RGB[2])
        elif RorGorB == 1:
            RGB = (RGB[0], int(pb, 2), RGB[2])
        elif RorGorB == 2:
            RGB = (RGB[0], RGB[1], int(pb, 2))

        pix[x, y] = RGB



im.save(f'stegged_image.jpg')
print('Done')

