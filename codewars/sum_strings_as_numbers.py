def sum_strings(x:str, y:str)->str:
    if(not(x and y)):
        if(x): return x.lstrip('0') or '0'
        if(y): return y.lstrip('0') or '0'
        if(not x and not y): return '0'
    x = x.lstrip('0') or '0'
    y = y.lstrip('0') or '0'
    max_length=max(len(x),len(y)) + 1
    x, y = x.zfill(max_length), y.zfill(max_length)
    x_list, y_list = [int(a) for a in x], [int(b) for b in y]
    carry, result = [0 for _ in range(max_length + 1)], ['' for _ in range(max_length + 1)]
    for i in range(len(x_list) - 1, -1, -1):
        digit_sum = x_list[i] + y_list[i] + carry[i]
        carry[i-1], result[i] = digit_sum // 10, str(digit_sum % 10)
    return ''.join(result).lstrip('0') or '0'