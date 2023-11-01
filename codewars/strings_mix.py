from collections import Counter
import re

def mix(s1:str, s2:str)->str:
    c1,c2=Counter(),Counter()
    for c in re.sub(r'[^a-z]', '', s1):
        c1[c]+=1
    for c in re.sub(r'[^a-z]', '', s2):
        c2[c]+=1

    c3 = c1 | c2
    out,one,two,equal = [],[],[],[]
    _,last=c3.most_common(1)[0]
    for k,v in sorted(c3.most_common(),key=lambda x: (-x[1], x[0])):
        if(v<last):
            out.extend(one + two + equal)
            one,two,equal = [],[],[]
            last = v
        if(v==1):
            break
        if(c1[k] == c2[k]):
            equal.append('=:'+k*v)
        elif(c1[k] == v):
            one.append('1:'+k*v)
        else:
            two.append('2:'+k*v)
    out.extend(one + two + equal)
    return('/'.join(out))

print(mix("Are they here", "yes, they are here") == "2:eeeee/2:yy/=:hh/=:rr")