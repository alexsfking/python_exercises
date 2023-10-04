class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self.key=key
        self.alphabet=alphabet
        self.alphabet_set=set(alphabet)
        self.alphabet_length=len(alphabet)
        self.alphabet_char_to_index_dict=dict()
        for i,c in enumerate(alphabet):
            self.alphabet_char_to_index_dict[c]=i
        self.first=0
        self.last=self.alphabet_char_to_index_dict[alphabet[-1]]
    
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
            index=self.alphabet_char_to_index_dict[c]+self.alphabet_char_to_index_dict[key_letter]
            if(index>self.last):
                index-=self.alphabet_length
            out.append(self.alphabet[index])
        return ''.join(out)
    
    def decode(self, text:str):
        self.letter_gen = self.cyclic_letter_generator(self.key)
        out=[]
        for c in text:
            key_letter=next(self.letter_gen)
            if(c not in self.alphabet_set):
                out.append(c)
                continue
            temp=self.alphabet_char_to_index_dict[c]-self.alphabet_char_to_index_dict[key_letter]
            if(temp<self.first):
                temp+=self.alphabet_length
            out.append(self.alphabet[temp])
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

abc = "アイウエオァィゥェォカキクケコサシスセソタチツッテトナニヌネノハヒフヘホマミムメモヤャユュヨョラリルレロワヲンー"
key = "カタカナ"
c = VigenereCipher(key, abc)

print(c.encode('カタカナ'), 'タモタワ')
print(c.decode('タモタワ'), 'カタカナ')

print(c.encode('ドモアリガトゴザイマス'), 'ドオカセガヨゴザキアニ')
print(c.decode('ドオカセガヨゴザキアニ'), 'ドモアリガトゴザイマス')