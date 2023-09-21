def stray(arr):
    stray_dict=dict()
    for a in arr:
        stray_dict[a] = stray_dict.get(a, 0) + 1
    return next(k for k, v in stray_dict.items() if v == 1)