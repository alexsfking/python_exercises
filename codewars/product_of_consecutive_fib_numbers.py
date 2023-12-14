fib_list = [0,1]
product_dict = dict()
largest_product = 0

def productFib(prod:int) -> list:
    global largest_product
    while prod > largest_product:
        product_dict[fib_list[-2] * fib_list[-1]] = (fib_list[-2], fib_list[-1])
        largest_product = fib_list[-2] * fib_list[-1]
        fib_list.append(fib_list[-2] + fib_list[-1])
    if prod in product_dict:
        term_a, term_b = product_dict[prod]
        return [term_a, term_b, True]
    for k, v in product_dict.items():
        if k > prod:
            term_a, term_b = v
            return [term_a, term_b, False]