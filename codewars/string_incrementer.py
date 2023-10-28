import re

number_pattern=re.compile(r"^.*?([\d]+)$")

def increment_string(strng:str)->str:
    match=number_pattern.match(strng)
    if match:
        incremented_number=str(int(match.group(1))+1)
        if(len(match.group(1))>len(incremented_number)):
            incremented_number = incremented_number.zfill(len(match.group(1)))
        return re.sub(r"\d+$",incremented_number,strng)
    return strng + '1'


print(increment_string("foo") == "foo1")
print(increment_string("foobar1") == "foobar2")
print(increment_string("foobar99") == "foobar100")
print(increment_string("foobar00999") == "foobar01000")