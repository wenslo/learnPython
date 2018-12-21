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


def is_odd(n):
    return n % 2 == 1


print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))


def not_empty(s):
    return s and s.strip()


print(list(filter(not_empty, ['A', '', 'B', None, 'C', ''])))


def _odd_iter():
    n = 1
    while True:
        n += 2
        yield n


def _not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)


# for n in primes():
#     if n < 1000:
#         print(n)
#     else:
#         break

#
# def is_palindrome(n):
#     if isinstance(n, Iterator):
#         print("not Iterable")
#         return
#     for x in n:
#         if not isinstance(x, int):
#             continue
#         num_str = str(x)
#         length = len(num_str)
#         # 如果小于10,不进行判断
#         if length < 2:
#             print(x)
#         elif length % 2 == 0:
#             mid = int(length / 2)
#             a = num_str[0:mid]
#             b = num_str[mid:length]
#             if a == b:
#                 print(x)
#         else:
#             mid = length // 2
#             a = num_str[0:mid]
#             b = num_str[mid + 1:length]
#             if a == b:
#                 print(x)


# is_palindrome(range(1, 200))


# 现在改为filter
def is_palindrome(x):
    num_str = str(x)
    length = len(num_str)
    mid = length // 2
    a = num_str[0:mid]
    # 如果小于10,不进行判断
    if length < 2:
        return True
    elif length % 2 == 0:
        b = num_str[mid:length]
        if a == b:
            return True
    else:
        b = num_str[mid + 1:length]
        if a == b:
            return True


output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101,
                                                  111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')

print(sorted([36, 5, -12, 9, -21], key=abs))

print(sorted(['bob', 'about', 'Zoo', 'Credit']))
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))
