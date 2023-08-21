def end_of_list_logic(args, out, start_of_range, i):
    if((args[i]==(args[i-1]+1)) and start_of_range!=-1 and i-start_of_range>=2):
        out.append(str(args[start_of_range])+"-"+str(args[i]))
    elif(start_of_range!=-1 and i-start_of_range>=2):
        out.append(str(args[start_of_range])+"-"+str(args[i-1]))
        out.append(str(args[i]))
    elif(start_of_range!=-1 and i-start_of_range==1):
        out.append(str(args[i-1]))
        out.append(str(args[i]))
    else:
        out.append(str(args[i]))
    return out

def solution(args):
    # your code here
    if not args:
        return ""
    
    out=[]
    start_of_range=-1

    for i in range(1,len(args)):
        if(args[i]==(args[i-1]+1)):
            if(start_of_range==-1):
                start_of_range=i-1
        else:
            if(start_of_range!=-1 and i-1-start_of_range>=2):
                out.append(str(args[start_of_range])+"-"+str(args[i-1]))
            elif(start_of_range!=-1 and i-1-start_of_range==1):
                out.append(str(args[i-2]))
                out.append(str(args[i-1]))
            else:
                out.append(str(args[i-1]))
            start_of_range=-1

    out=end_of_list_logic(args, out, start_of_range, i)
    return ",".join(out)

print(solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]))
print(solution([-3,-2,-1,2,10,15,16,18,19,20]))