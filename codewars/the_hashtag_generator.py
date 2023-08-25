'''
The marketing team is spending way too much time typing in hashtags.
Let's help them with our own Hashtag Generator!

Here's the deal:

It must start with a hashtag (#).
All words must have their first letter capitalized.
If the final result is longer than 140 chars it must return false.
If the input or the result is an empty string it must return false.
'''

def generate_hashtag(s:str):
    out=['#']
    set_capital=True
    for c in s:
        if(c==' '):
            set_capital=True
        elif(set_capital and c.isalpha()):
            out.append(c.capitalize())
            set_capital=False
        else:
            out.append(c.lower())
        if(len(out)>140):
            return False
    if(len(out)==1):
        return False
    return "".join(out)
        
        