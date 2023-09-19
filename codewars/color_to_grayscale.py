def rgb_to_grayscale(color:str)->str:
    r=0.299*int(color[1:3],16)
    g=0.587*int(color[3:5],16)
    b=0.114*int(color[5:7],16)
    y=hex(round(r+g+b))[2:].upper()
    if(len(y)==1):
        y = '0' + y
    return '#' + y * 3
