def valid_ISBN10(isbn:str): 
    if(len(isbn)!=10):
        return False
    total=0
    for i,char in enumerate(isbn):
        if(char.isdigit()):
            total+=int(char)*(i+1)
        elif(char=='X' and i==9):
            total+=10*(i+1)
        else:
            return False
    return total % 11 == 0