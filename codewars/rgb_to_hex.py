# min 0 max 255
hex_converter = lambda num: format(max(0, min(num, 255)), '02X') 

def rgb(r, g, b):
    return(''.join(map(hex_converter, (r, g, b))))

print(rgb(1, 2, 3))
print(rgb(-20, 275, 125))