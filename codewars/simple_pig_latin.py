def pig_it(text:str)->str:
    out=[]
    for word in text.split():
        if(word.isalnum()):
            out.append(f"{word[1:]}{word[0]}ay")
        else:
            out.append(word)
    return " ".join(out)