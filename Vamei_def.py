def square_sum(a, b):
    '''计算两个参数的平方和'''
    c = a**2 + b**2
    return c

help(square_sum)

print(square_sum(4, 5))


def sum_test(a, b, c):
    print(a, b, c)

#sum_test(1, c = 2, b = 3)

sum_test(a = 1, 3, c=2)