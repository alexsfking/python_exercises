memo_dict = {0: 1, 1: 0}
def all_permuted(n):
    if(n in memo_dict):
        return memo_dict[n]
    else:
        memo_dict[n]=((n-1)*(all_permuted(n-1)+all_permuted(n-2)))
        return memo_dict[n]