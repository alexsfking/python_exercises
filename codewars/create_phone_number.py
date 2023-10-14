def create_phone_number(array):
    return f"({''.join(map(str, array[:3]))}) {''.join(map(str, array[3:6]))}-{''.join(map(str, array[6:]))}"
