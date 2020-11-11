
from itertools import product
 
 
def expression(p):
    return "{}1{}2{}3{}4{}5{}6{}7{}8{}9".format(*p)
 
 
def gen_expression():
    operator = ['+', '-', '']
    return [expression(product) for product in product(operator, repeat=9) if product[0] != '+']
 
 
def all_exprs():
    values = {}
    for expression in gen_expression():
        val = eval(expression)
        if val not in values:
            values[val] = 1
        else:
            values[val] += 1
    return values
 
 
def sum_to(val):
    for s in filter(lambda x: x[0] == val, map(lambda x: (eval(x), x), gen_expression())):
        print(s)

sum_to(100)
