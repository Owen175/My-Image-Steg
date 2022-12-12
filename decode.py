from PIL import Image
import random


seed = 10

random.seed(seed)
im = Image.open('stegged_image.jpg') # Can be many formats.
pix = im.load()

RorGorB = 1 #R = 0, G = 1, B = 2
dim = im.size

indexes = list(range(0,dim[0]*dim[1]))
random.shuffle(indexes)
cont = True
length = ''
i = -1
bitList = []
print(indexes)
for i in range(dim[0] * dim[1]):
    x = indexes[i] % dim[0]
    y = int(indexes[i] / dim[0])
    R, G, B = pix[x, y]
    rgb = [R, G, B]
    den = rgb[RorGorB]
    pixel_bin = list(bin(den)[2:].zfill(8))
    bitList.append(pixel_bin[7])

byteList = []
for i in range(len(bitList)//8):
    byte = ''
    for t in range(8):
        byte += str(bitList[8 * i + t])
    byteList.append(byte)
    #print(byte)
chrList = []
for bt in byteList:
    chrList.append(chr(int(bt, 2)))

#print(''.join(chrList[:100]))
'''
for i, char in enumerate(message):
    ASCII = ord(char)
    binary = bin(ASCII)[2:].zfill(8) # Bin converts to binary. It has a prefix which is removed. .zfill ensures that the integer is 8 bits not removing 0 prefixes.
    #for i in range(8-len(bin(char)))

    for bit in binary:
        x = random.choice(width)
        y = random.choice(height)

        width.remove(x) # Ensures no duplicates
        height.remove(y)

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

    binary = bin(127)[2:].zfill(8)
    if i - 1 == lenlen:
        for bit in binary:
            x = random.choice(width)
            y = random.choice(height)

            width.remove(x)  # Ensures no duplicates
            height.remove(y)

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
'''