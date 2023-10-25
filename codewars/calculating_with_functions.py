operators = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y,
    '//': lambda x, y: x // y,
    '**': lambda x, y: x ** y
}

def safe_eval(expr:str):
    parts = list(expr)
    if len(parts) == 3 and parts[1] in operators:
        return operators[parts[1]](int(parts[0]), int(parts[2]))
    elif len(parts) == 4 and f"{parts[1]}{parts[2]}" in operators:
        return operators[f"{parts[1]}{parts[2]}"](int(parts[0]), int(parts[3]))
    raise ValueError("Invalid expression format:", expr)

def zero(arg=None): return '0' if arg is None else safe_eval(f"0{arg}")
def one(arg=None): return '1' if arg is None else safe_eval(f"1{arg}")
def two(arg=None): return '2' if arg is None else safe_eval(f"2{arg}")
def three(arg=None): return '3' if arg is None else safe_eval(f"3{arg}")
def four(arg=None): return '4' if arg is None else safe_eval(f"4{arg}")
def five(arg=None): return '5' if arg is None else safe_eval(f"5{arg}")
def six(arg=None): return '6' if arg is None else safe_eval(f"6{arg}")
def seven(arg=None): return '7' if arg is None else safe_eval(f"7{arg}")
def eight(arg=None): return '8' if arg is None else safe_eval(f"8{arg}")
def nine(arg=None): return '9' if arg is None else safe_eval(f"9{arg}")

def plus(arg): return f"+{arg}"
def minus(arg): return f"-{arg}"
def times(arg): return f"*{arg}"
def divided_by(arg): return f"//{arg}"

print(six(divided_by(two())))