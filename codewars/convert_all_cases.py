import re

pattern_dict=dict()
pattern_dict['camel']=re.compile(r"^[a-z]+(?:[A-Z][a-z\d]*)*$")
pattern_dict['snake']=re.compile(r"^[a-z]+(?:\_[a-z]+)*$")
pattern_dict['kebab']=re.compile(r"^[a-z]+(?:\-[a-z]+)*$")

def get_case(identifier):
    for k,v in pattern_dict.items():
        if(v.match(identifier)):
            return k
    return None

def change_case(identifier, target_case):
    if(identifier==""):
        return identifier
    if(target_case not in pattern_dict):
        return None
    current_case=get_case(identifier)
    if(current_case==target_case):
        return identifier

    match current_case:
        case 'camel':
            if(target_case=='snake'):
                return (re.sub(r'(.)(?=[A-Z])', r"\1_", identifier)).lower()
            return (re.sub(r'(.)(?=[A-Z])', r"\1-", identifier)).lower()
        case 'snake':
            if(target_case=='kebab'):
                return re.sub(r'_', r"-", identifier)
            return re.sub(r'_([a-z\d])', lambda x: f"{x.group(1).upper()}", identifier)
        case 'kebab':
            if(target_case=='snake'):
                return re.sub(r'-', r"_", identifier)
            return re.sub(r'-([a-z\d])', lambda x: f"{x.group(1).upper()}", identifier)
        case _:
            return current_case