class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self.key=key
        self.alphabet_set=set(alphabet)
        self.first=ord(alphabet[0])
        self.last=ord(alphabet[-1])
        self.alphabet_length=len(alphabet)
        '''
        print(alphabet,self.alphabet_length)
        checking=[]
        for c in alphabet:
            checking.append(ord(c))
        print(checking)
        '''
    
    def cyclic_letter_generator(self, string):
        index = 0
        while True:
            yield string[index]
            index = (index + 1) % len(string)
    
    def encode(self, text:str):
        self.letter_gen = self.cyclic_letter_generator(self.key)
        out=[]
        for c in text:
            key_letter=next(self.letter_gen)
            if(c not in self.alphabet_set):
                out.append(c)
                continue
            temp=ord(c)+ord(key_letter)-self.first
            if(temp>self.last):
                temp-=self.alphabet_length
            out.append(chr(temp))
        return ''.join(out)
    
    def decode(self, text:str):
        self.letter_gen = self.cyclic_letter_generator(self.key)
        out=[]
        for c in text:
            key_letter=next(self.letter_gen)
            if(c not in self.alphabet_set):
                out.append(c)
                continue
            temp=ord(c)-(ord(key_letter)-self.first)
            if(temp<self.first):
                temp+=self.alphabet_length
            out.append(chr(temp))
        return ''.join(out)
    

abc = "abcdefghijklmnopqrstuvwxyz"
key = "password"
c = VigenereCipher(key, abc)

print(c.encode('codewars'), 'rovwsoiv')
print(c.decode('rovwsoiv'), 'codewars')

print(c.encode('waffles'), 'laxxhsj')
print(c.decode('laxxhsj'), 'waffles')

print(c.encode('CODEWARS'), 'CODEWARS')
print(c.decode('CODEWARS'), 'CODEWARS')