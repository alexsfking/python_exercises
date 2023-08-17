class Cipher():
    def __init__(self) -> None:
        self.wheel='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,? '
        self.cipher_dict=dict()
        for c in self.wheel:
            result=encode(c*65)
            for i in range(len(result)):
                self.cipher_dict[(result[i],i)]=c

cipher=Cipher()

def decode(s):
    out=[]
    for i,c in enumerate(s):
        if (c, i%66) in cipher.cipher_dict:
            out.append(cipher.cipher_dict[c,i%66])
        else:
            out.append(c)
    return "".join(out)









def encode(s):
    '''
   hidden
    '''
    return s


'''

def decode(s):
    print(encode("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
    print(encode("bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"))
    print(encode("ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc"))
    print(encode("ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd"))
    print(encode("                                                                               "))
    print(encode("..............................................................................."))
    print(encode("???????????????????????????????????????????????????????????????????????????????"))
    print(encode(",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,"))
    print(encode("!@#$%^&*()_+-"))
    print(encode("HcGDEFGHIJKLMNOPQRSTUVYWXYZ"))
    print("0123456789012345678901234567890")
    a,b,c = "", "", ""
    for w in "abcdefghijklmnopqrstuvwxyz":
        a += encode(  "" + w)[0]
        b += encode( "_" + w)[1]
        c += encode("__" + w)[2]
    print(a)
    print(b)
    print(c)
    c=""
    for w in "abcdefghijklmnopqrstuvwxyz":
        c+=encode(w)
    print(c)
    print("0123456789012345678901234567890123456789012345678901234567890")
    c=""
    for w in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        c+=encode(w)
    print(c)
    print("0123456789012345678901234567890123456789012345678901234567890")
    c=""
    for w in "0123456789":
        c+=encode(w)
    print(c)
    print("0123456789012345678901234567890123456789012345678901234567890")
    c=""
    for w in " ,./?;:{}[]`\~|":
        c+=encode(w)
    print(c)
    print("0123456789012345678901234567890123456789012345678901234567890")
    return s;

'''