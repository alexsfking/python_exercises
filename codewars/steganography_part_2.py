'''
Inverse of part 1
'''

def extract(pixels: list[list[int]]):
    # your code here
    temp=[]
    out=[]
    for i,rgb in enumerate(pixels):
        if(i%3!=2):
            for j,color in enumerate(rgb):
                temp.append(bin(color)[-1])
        else:
            for j,color in enumerate(rgb):
                if((j)!=2):
                    temp.append(bin(color)[-1])
                else:
                    #convert temp to a char
                    out.append(chr(int("".join(temp),2)))
                    temp=[]
    return "".join(out)