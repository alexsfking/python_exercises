def solution(*args):
    arg_set=set()
    for arg in args:
        if arg in arg_set:
            return True
        arg_set.add(arg)
    return False