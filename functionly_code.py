import functools
import time
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


# 函数返回
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax


print(calc_sum(1, 2, 3, 4))


def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sum


f = lazy_sum(1, 2, 3, 4)
print(f)
print(f())
f1 = lazy_sum(1, 2, 3, 4)
f2 = lazy_sum(1, 2, 3, 4)
print(f1 == f2)


def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    return fs


f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())


# 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。如果一定要使用，则需要保证该值不变
def count():
    def f(j):
        def g():
            return j * j

        return g

    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs


f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())


def create_counter():
    def add_num(i):
        i = i + 1
        return i

    fs = [0]

    def get_num():
        return fs[-1]

    def counter():
        fs.append(add_num(get_num()))
        return fs[-1]

    return counter


# 测试:
counterA = create_counter()
print(counterA(), counterA(), counterA(), counterA(), counterA())  # 1 2 3 4 5
counterB = create_counter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')
# lambda 本质上为匿名函数 不能写return
print(list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
f = lambda x: x * x
print(f)
print(f(5))


def build(x, y):
    return lambda: x * x + y * y


print(build(2, 2))
f = build(2, 2)
print(f())


def is_odd(n):
    return n % 2 == 1


L = list(filter(is_odd, range(1, 20)))

print(list(filter(lambda x: x % 2 == 1, range(1, 20))))


# 通过__name__可以拿到函数名称
def now():
    print('2015-3-25')


f2 = now
# f = now()
# f()
print("------------")
print(now.__name__)
print(f2.__name__)


def log(func):
    def wrapper(*args, **kw):
        print("call %s():" % func.__name__)
        return func(*args, **kw)

    return wrapper


@log
def now():
    print("2018年12月24日20:37:07")


now()


def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print("%s %s() " % (text, func.__name__))

        return wrapper

    return decorator


@log("execute")
def now():
    print("2018年12月24日20:39:55")


now()
print(now.__name__)


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print("-----------")
        print("call %s():" % func.__name__)
        return func(*args, **kw)

    return wrapper


@log
def now():
    print("2018年12月24日20:43:58")


now()

print(now.__name__)


def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print("%s %s():" % (text, func.__name__))
            return func(*args, **kw)

        return wrapper

    return decorator


@log("test")
def now():
    print("2018年12月24日20:50:27")


now()

print(now.__name__)


# print("===========")
# print(time.time().__format__("yyyy-MM"))

def metric(func):
    start = time.time()

    @functools.wraps(func)
    def decorator(*args, **kw):
        end = time.time()
        print('%s executed in %s ms' % (func.__name__, end - start))
        return func(*args, **kw)

    return decorator


# test1 = time.time()
# time.sleep(4)
# test2 = time.time()
# print("execute time is %s" % (test2 - test1))


@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y


@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z


print("****************************************************")
f = fast(11, 22)
print(f)
s = slow(11, 22, 33)
print(s)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
else:
    print("测试通过！")

print(int('12345', base=8))
print(int('12345', base=16))


def int2(x, base=2):
    return int(x, base)


print(int2('11'))

int2 = functools.partial(int, base=2)
print(int2('100000'))
print(int2('10101010'))
print(int2('1000000', base=10))
max2 = functools.partial(max, 10)
print(max2(5, 6, 7))
