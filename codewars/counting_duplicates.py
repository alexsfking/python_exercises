from collections import Counter

def duplicate_count(text:str)->int:
    counter=Counter(text.lower())
    uniq_duplicates=0
    for _,v in counter.items():
        if(v>1):
            uniq_duplicates+=1
    return uniq_duplicates