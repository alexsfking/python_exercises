import re

def justify_line(words:list[str],width:int)->str:
    out=[]
    num_spaces=width-len(''.join(words))
    num_gaps=len(words)-1
    if(num_gaps==0):
        return words[0] #strings with one word do not need gaps
    gap_size=num_spaces // num_gaps
    remainder_spaces=num_spaces % num_gaps
    for i in range(0,len(words)-1):
        if(remainder_spaces>0):
            out.append(words[i]+' '*(gap_size+1))
            remainder_spaces-=1
        else:
            out.append(words[i]+' '*(gap_size))
    out.append(words[-1])
    return ''.join(out)

def justify(text:str, width:int)->str:
    words=text.split()
    line_length=width
    line_word_start_index=0
    out=[]
    for i,word in enumerate(words):
        word=word.strip()
        line_length-=len(word)+1
        if line_length <= 0:
            if line_length == -1 or line_length == 0: #exact
                out.append(justify_line(words[line_word_start_index:i+1],width))
                line_word_start_index=i+1
                line_length=width
            else: #one word too far
                out.append(justify_line(words[line_word_start_index:i],width))
                line_word_start_index=i
                line_length=width-len(word)-1
    if line_word_start_index<len(words):
        out.append(justify_line(words[line_word_start_index:],width))
    out.append(re.sub(r'\s+', ' ', out.pop())) #last line should not be justified.
    return '\n'.join(out)



print(justify('123 45 6', 7) == '123  45\n6')
print(justify('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum sagittis dolor mauris, at elementum ligula tempor eget. In quis rhoncus nunc, at aliquet orci. Fusce at dolor sit amet felis suscipit tristique. Nam a imperdiet tellus. Nulla eu vestibulum urna. Vivamus tincidunt suscipit enim, nec ultrices nisi volutpat ac. Maecenas sit amet lacinia arcu, non dictum justo. Donec sed quam vel risus faucibus euismod. Suspendisse rhoncus rhoncus felis at fermentum. Donec lorem magna, ultricies a nunc sit amet, blandit fringilla nunc. In vestibulum velit ac felis rhoncus pellentesque. Mauris at tellus enim. Aliquam eleifend tempus dapibus. Pellentesque commodo, nisi sit amet hendrerit fringilla, ante odio porta lacus, ut elementum justo nulla et dolor.', 20))