def solution(s:str):
    stack=[]
    out=[]
    increasing,decreasing=False,False
    for i in range(len(s)-1):
        char_value=ord(s[i])
        next_char_value=ord(s[i+1])
        if(char_value==next_char_value+1 and not increasing):
            decreasing=True
            stack.append(s[i])
        elif(char_value==next_char_value-1 and not decreasing):
            increasing=True
            stack.append(s[i])
        elif(increasing):
            stack.append(s[i])
            increasing=False
            while(stack):
                out.append(stack.pop())
        elif(decreasing):
            stack.append(s[i])
            decreasing=False
            while(stack):
                out.append(stack.pop())
        else:
            out.append(s[i])
    if(increasing or decreasing):
        stack.append(s[-1])
    while(stack):
        out.append(stack.pop())
    if(increasing or decreasing):
        pass
    else:
        out.append(s[-1])
    return "".join(out)


print(solution('abcxdef'))