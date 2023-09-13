def spin_words(sentence):
    words=sentence.split()
    out=[]
    for word in words:
        if(len(word)>4):
            out.append(word[::-1])
        else:
            out.append(word)
    return ' '.join(out)