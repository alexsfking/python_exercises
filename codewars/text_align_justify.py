def justify_line(words:list[str],gapsize:int,remainder:int)->str:
    out=[]
    for i in range(len(words)-1):
        if(remainder>0):
            out.append(words[i] + ' ' * (gapsize+1))
            remainder-=1
        else:
            out.append(words[i] + ' ' * (gapsize))
    out.append(words[-1])
    return ''.join(out)

def justify(text:str, width:int)->str:
    words=text.split()
    line_length=width
    line_word_start_index=0
    out=[]
    for i,word in enumerate(words):
        line_length-=len(word)
        if line_length - (i-line_word_start_index) <= 0:
            if line_length - (i-line_word_start_index) == 0:
                out.append(" ".join(words[line_word_start_index:i+1]))
                line_word_start_index=i+1
            else:
                num_spaces=width-len(''.join(words[line_word_start_index:i]))
                gap_size, remainder=divmod(num_spaces,i-line_word_start_index-1)
                out.append(justify_line(words[line_word_start_index:i],gap_size,remainder))
                line_word_start_index=i
            line_length=width
    if(line_word_start_index<len(words)):
        num_spaces=width-len(''.join(words[line_word_start_index:]))
        gap_size, remainder=divmod(num_spaces,len(words)-line_word_start_index)
        out.append(justify_line(words[line_word_start_index:],gap_size,remainder))
    return '\n'.join(out)


print(justify('123 45 6', 7) == '123  45\n6')