def solution(pairs):
    out=[]
    for k,v in sorted(pairs.items(), key=lambda item: str(item[0])):
        out.append(str(k) + " = " + str(v))
    return ",".join(out)