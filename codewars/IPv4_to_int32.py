def ip_to_int32(ip:str)->int:
    bits_per_octet=8
    binary_strings = [bin(int(octet))[2:].zfill(bits_per_octet) for octet in ip.split('.')]
    return int(''.join(binary_strings),2)