def strip_comments(strng:str, markers:list[str]):
    out=[]
    markers_set=set(markers)
    for line in strng.split('\n'):
        for i,c in enumerate(line):
            if(c in markers_set):
                out.append(line[:i].rstrip())
                break
        else:
            out.append(line.rstrip())
    return '\n'.join(out)

print(strip_comments('apples, pears # and bananas\ngrapes\nbananas !apples', ['#', '!']) == 'apples, pears\ngrapes\nbananas')