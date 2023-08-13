hex_converter = lambda num: format(num, '02X')

def rgb(r, g, b):
    return(''.join(map(hex_converter, (r, g, b))))

rgb(1, 2, 3)