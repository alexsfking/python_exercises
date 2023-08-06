'''
Steganography is the practice of concealing a message within another medium.

In this case, we'll be taking a message string, and concealing it inside of RGB
(Red, Green, Blue) Image Pixels using Least Significant Bit (LSB) Insertion.

Your function will take the string msg and build a Bitmask array that is then
applied to the pixels array, returning the modified pixel values.

Notes 
    1. You can assume that the pixels inner arrays always have a length of 3 (for
    Red, Green, Blue). 

    2. Your code should return nil/None if there aren't enough pixels to conceal the
    message. 

        If the message has been fully concealed and there are remaining pixels, the
        remaining pixels should be left unmodified. 

    3. Since bytes are 8 bits long and pixels are in groups of 3, the last color of
    every 3rd array/ group of pixels should not be modified.
'''

def conceal(msg: str, pixels: list[list[int]]):
    # your code here
    if(len(msg)>len(pixels)//3): # 1 char per 3 pixels - note 3
        return None # message too long
    
    bitmasks=[]
    for character in msg:
        bitmask='0'+bin(ord(character))[2:]
        for bit in bitmask:
            bitmasks.append(bit)

    index=0
    for i,rgb in enumerate(pixels):
        if((i)%3!=2):
            for j,colour in enumerate(rgb):
                pixels[i][j]=int(bin(colour)[:-1]+bitmasks[index],2)
                index+=1
                if(index==len(bitmasks)):
                    return pixels
        else:
            for j,colour in enumerate(rgb):
                if((j)!=2):
                    pixels[i][j]=int(bin(colour)[:-1]+bitmasks[index],2)
                    index+=1
                    if(index==len(bitmasks)):
                        return pixels

    return pixels


message="Well that's alright, lets give this another try"
image = [
    [144,237,136],[171,124,19],[171,207,178],
    [118,87,161],[34,138,229],[202,85,175],
    [160,79,45],[108,79,3],[120,140,129],
    [16,253,191],[190,117,175],[86,126,13],
    [222,12,183],[194,52,14],[92,102,223],
    [180,113,69],[85,80,235],[66,156,110],
    [108,1,179],[70,145,138],[250,172,57],
    [60,19,127],[8,14,144],[232,69,55],
    [56,245,45],[189,130,191],[88,124,74],
    [248,92,27],[126,52,175],[79,247,236],
    [2,157,247],[247,198,154],[91,143,103],
    [180,34,113],[118,226,212],[88,58,85],
    [70,221,105],[14,70,32],[28,233,1],
    [36,25,67],[174,219,219],[6,58,208],
    [52,65,219],[159,228,8],[213,90,228],
    [16,87,141],[134,147,44],[210,127,42],
    [194,243,187],[228,134,161],[243,7,148],
    [80,3,205],[204,247,92],[144,226,128],
    [214,173,255],[133,142,161],[200,118,223],
    [92,106,159],[202,183,133],[2,224,196],
    [34,184,187],[234,156,242],[34,40,161],
    [152,101,55],[60,239,117],[14,62,100],
    [130,177,43],[56,200,235],[158,49,226],
    [240,207,67],[241,16,147],[160,46,100],
    [224,253,51],[139,182,132],[123,185,130],
    [94,68,147],[84,136,142],[202,56,209],
    [164,15,181],[48,54,71],[183,89,223],
    [82,183,223],[240,121,16],[162,63,29],
    [52,75,199],[127,26,145],[7,184,243],
    [62,207,37],[122,64,123],[164,225,240],
    [42,22,161],[14,30,184],[54,134,215],
    [106,215,117],[223,4,115],[56,204,209],
    [56,253,81],[12,23,150],[254,92,192],
    [0,195,89],[66,31,234],[160,39,214],
    [158,87,27],[75,212,74],[215,207,149],
    [36,240,137],[164,50,168],[34,184,185],
    [106,199,191],[6,110,78],[58,13,123],
    [108,143,193],[54,217,185],[47,112,180],
    [194,71,129],[222,65,239],[39,45,30],
    [60,199,93],[199,18,205],[98,182,174],
    [180,153,3],[14,169,58],[212,18,117],
    [164,13,49],[184,120,205],[30,43,254],
    [50,123,97],[77,188,174],[175,66,191],
    [184,144,157],[70,48,236],[246,248,61],
    [230,101,211],[205,118,33],[216,250,80],
    [226,93,255],[205,218,148],[131,200,142],
    [156,49,153],[135,15,170],[234,183,141],
]
print(conceal(message,image))