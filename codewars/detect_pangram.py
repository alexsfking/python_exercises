lower_case_alphabet_set = set(chr(letter) for letter in range(ord('a'), ord('z')+1))

def is_pangram(s:str)->bool:
    uniq_chars_set=set(s.lower())
    return uniq_chars_set.issuperset(lower_case_alphabet_set)