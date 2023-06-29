'''
minimum and xor or
'''

def print_output(some_dict:dict):
    for key, value in some_dict.items():
        print(key[0],key[1],value)

a=[i for i in range(0,7)]
and_dict=dict()
or_dict=dict()
xor_dict=dict()
for x in range(len(a)):
    for y in range(len(a)):
        if(x==y):
            continue
        and_dict[(a[x],a[y])]=a[x] & a[y]
        or_dict[(a[x],a[y])]=a[x] | a[y]
        xor_dict[(a[x],a[y])]=a[x] ^ a[y]

print("AND: ")
print_output(and_dict)
print("OR: ")
print_output(or_dict)
print("XOR: ")
print_output(xor_dict)
