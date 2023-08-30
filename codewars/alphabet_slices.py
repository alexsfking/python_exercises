def solution(s:str):
    stack,out=[],[]
    for i in range(len(s)-1):
        if(ord(s[i])+1==ord(s[i+1])):
            stack.append(s[i])
        elif(stack):
            stack.append(s[i])
            while(stack):
                out.append(stack.pop())
        else:
            out.append(s[i])
    
    if stack and ord(s[-1]) == ord(stack[-1]) + 1:
        stack.append(s[-1])
        while stack:
            out.append(stack.pop())
    else:
        while stack:
            out.append(stack.pop())
        out.append(s[-1])
    return "".join(out)


print(solution('abcxdef'))