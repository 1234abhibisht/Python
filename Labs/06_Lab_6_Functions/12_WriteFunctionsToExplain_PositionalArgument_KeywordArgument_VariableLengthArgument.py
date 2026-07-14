# positional argument 
def positional_arg(a, b) :
    sum = a + b
    return sum
print(positional_arg(2, 3))  # here 2 will go to a, and 3 will go to b


# keyword argument
def keyword_arg(a, b) :
    sum = a + b
    return sum
print(keyword_arg(b = 3, a = 2)) # we have specify by parameter name that which argument will to which parameter


# variable length argument
def variable_arg(*args) :
    return sum(args)
print(variable_arg(1,2,3,4,5))   # 1,2,3,4,5 will be passed together as tuple
# args = tup(1,2,3,4,5)
