'''
### kyu 5 ###
For a given chemical formula represented by a string, count the number of atoms
of each element contained in the molecule and return an object (associative
array in PHP, Dictionary<string, int> in C#, Map<String,Integer> in Java).


For example:

    water = 'H2O'
    parse_molecule(water)                 # return {H: 2, O: 1}

    magnesium_hydroxide = 'Mg(OH)2'
    parse_molecule(magnesium_hydroxide)   # return {Mg: 1, O: 2, H: 2}

    var fremy_salt = 'K4[ON(SO3)2]2'
    parse_molecule(fremySalt)             # return {K: 4, O: 14, N: 2, S: 4}


As you can see, some formulas have brackets in them. The index outside the
brackets tells you that you have to multiply count of each atom inside the
bracket on this index. For example, in Fe(NO3)2 you have one iron atom, two
nitrogen atoms and six oxygen atoms.

Note that brackets may be round, square or curly and can also be nested. Index
after the braces is optional.
'''
open_bracket_set=set(['[','('])

def contains_brackets(formula:str)->bool:
    for c in formula:
        if c in open_bracket_set:
            return True
    return False

def contains_numbers(formula:str)->bool:
    for c in formula:
        if c.isdigit():
            return True
    return False

def remove_brackets(formula:str)->str:
    bracket = None
    closing_bracket = None
    start_index = None
    multiplier = None
    for i,char in enumerate(formula):
        if not bracket:
            if char in open_bracket_set:
                bracket = char
                if bracket == '[':
                    closing_bracket = ']'
                else:
                    closing_bracket = ')'
                start_index=i
                break
    end_index = formula.index(closing_bracket,i)
    for j in range(end_index+1,len(formula)):
        if not formula[j].isdigit():
            multiplier = int(formula[end_index+1:j])
            break
    if(not multiplier):
        multiplier = int(formula[end_index+1:])
    return formula[:start_index]+formula[start_index+1:end_index]*multiplier+formula[end_index+1+len(str(multiplier)):]

def remove_numbers(formula:str)->str:
    result = ""
    i = 0
    while i < len(formula):
        if formula[i].isalpha() and i + 1 < len(formula) and formula[i + 1].isdigit():
            if(formula[i].isupper()):
                letters=formula[i]
            else:
                letters=formula[i-1:i+1]
            for j in range(i+2,len(formula)):
                if(not formula[j].isdigit()):
                    multiplier=int(formula[i+1:j])
                    break
            else:
                multiplier=int(formula[i+1:])
            result += letters * multiplier
            i += 1 + len(str(multiplier))  # Skip the letter and the following number
        else:
            result += formula[i]
            i += 1

    return result

def parse_molecule (formula:str)->dict:
    print(formula)
    atom_count_dict=dict()
    while(contains_brackets(formula)):
        formula = remove_brackets(formula)
    print(formula)
    while(contains_numbers(formula)):
        formula = remove_numbers(formula)
    print(formula)
    form=list(formula)
    lower_case_char_list=[]
    while(len(form)):
        if(form[-1].isupper()):
            if(len(lower_case_char_list)):
                element = form.pop()+lower_case_char_list.pop()
                if element in atom_count_dict:
                    atom_count_dict[element] += 1
                else:
                    atom_count_dict[element] = 1
            else:
                element = form.pop()
                if element in atom_count_dict:
                    atom_count_dict[element] += 1
                else:
                    atom_count_dict[element] = 1
        else:
            lower_case_char_list.append(form.pop())
    return atom_count_dict


print(parse_molecule("C6H12O6"))
print(parse_molecule("K4[ON(SO3)2]2"))
print(parse_molecule("Mg(OH)2"))
        

# K4[ON(SO3)2]2CO2(SO4)2


