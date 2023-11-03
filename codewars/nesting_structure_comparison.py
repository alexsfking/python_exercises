def same_structure_as(original, other)->bool:
    if(type(original)!=type(other)):
        if(type(original)==list or type(other)==list):
            return False
        else:
            return True
    elif(type(original)!=list):
        return True
    if len(original) != len(other):
        return False
    for elem1, elem2 in zip(original, other):
        if not same_structure_as(elem1, elem2):
            return False
    return True
        
a=[1,'[',']']
b=['[',']',1]
print(same_structure_as(a,b)==True)