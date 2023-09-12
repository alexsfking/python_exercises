def loneliest(strng:str):
    spaces_dict=dict()
    count=0
    last_c=None
    for c in strng.strip():
        if(c!=" "):
            spaces_dict[c]=count
            if(last_c):
                spaces_dict[last_c]+=count
            last_c=c
            count=0
        else:
            count+=1
    maximum=max(spaces_dict.values())
    return [key for key, value in spaces_dict.items() if value == maximum]