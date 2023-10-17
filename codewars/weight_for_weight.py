def reduce_str_to_digit(num_str:str)->int:
    out=0
    for c in num_str:
        out+=int(c)
    return out

def sorting_key(num_str)->tuple[int,str]:
    return reduce_str_to_digit(num_str), num_str

def order_weight(strng:str)->str:
    return " ".join(sorted(strng.split(),key=sorting_key))