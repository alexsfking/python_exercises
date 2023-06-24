s,k=input().split()
k=int(k)
suffixes=[]
for i in range(0,len(s)):
    suffixes.append(s[i:])
suffixes.sort()
print(suffixes[k-1])