from collections import Counter

def scramble(s1:str, s2:str)->bool:
    c1, c2 = Counter(s1), Counter(s2)
    for char, count in c2.items():
        if c1[char] < count:
            return False
    return True