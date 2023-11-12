def alphabet_position(text:str)->str:
    alphabet = set(chr(i) for i in range(ord('a'), ord('z') + 1)).union(set(chr(i) for i in range(ord('A'), ord('Z') + 1)))
    out = [str(ord(c.lower()) - ord('a') + 1) for c in text if c in alphabet]
    return ' '.join(out)