from functools import reduce


def f(x):
    return x * x


r = map(f, {1, 2, 3, 4, 5, 6, 7, 8})
print(type(r))
print(list(r))
print(list(map(str, [1, 2, 3, 4, 5, 6])))


def add(x, y):
    return x + y


print(reduce(add, [1, 2, 3, 4, 5]))


def fn(x, y):
    return x * 10 + y


s = reduce(fn, (1, 2, 3, 4, 5))
print(s)
print(type(s))

# def char2num(s):
#     digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
#     return digits[s]
#
#
# s = reduce(fn, map(char2num, '13579'))
# print(s)
# print(type(s))

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def char2num(s):
    return DIGITS[s]


def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, '12345'))


print(str2int('12345'))
