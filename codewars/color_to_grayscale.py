def rgb_to_grayscale(color:str)->str:
    return '#' + (hex(round(0.299 * int(color[1:3], 16) + 0.587 * int(color[3:5], 16) + 0.114 * int(color[5:7], 16)))[2:].upper()).zfill(2) * 3