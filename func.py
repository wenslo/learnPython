import math

# 绝对值 abs() 只能为数值类型数字，且只能一个参数
print(abs(-20))
# 最大值 max()
print(max(1, 23, 56))
# 数据转换 int() float() str() bool()
print(int('1234'))
print(float('1234'))
print(str(55.55))
print(bool(''))
# 函数引用
a = abs
print(a(-1))
# hex 转十六进制 bin 转二进制
print(hex(17))
print(bin(15))


# 函数定义使用def
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x


print(my_abs(-9))


# 应用其他文件的函数或者变量 from filename import fun/field

# pass do nothing
def nop():
    pass


# 参数检查，使用 isinstance()，raise 类似于java的throw
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


# 一个函数可以返回多个值(其实还是一个，不过是用tuple封装，类似于kotlin的翻译)
def move(x, y, step, angle=0.0):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx, ny


x, y = move(100, 100, 60, math.pi / 6)
print(x, y)
r = move(100, 100, 60, math.pi / 6)
print(r)


def power(x):
    return x * x


print(power(8))


# 必须是必选参数在前，默认参数在后
def power(x, n=2):
    s = 1
    while n > 0:
        n -= 1
        s = s * x
    return s


print(power(2, 5))
print(power(2))


# 默认参数必须指向不变对象
def enroll(name, gender, age=6, city='Beijing'):
    print('name: %s' % name)
    print('gender: %s' % gender)
    print('age: %s' % age)
    print('city: %s' % city)


enroll('Sarah', 'F')


def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print(calc([1, 2, 3]))


# 可变参数 *numbers

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print(calc(1, 2, 3, 4, 5))
# 使用*将list变为可变参数
nums = [1, 2, 3]
print(calc(*nums))


# 关键字参数
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other', kw)


person('Michael', 30)
person('Bob', 20, gender='F', job='softwareEngineer')
extra = {'city': 'Beijing', 'job': 'softwareEngineer'}
person('Jack', 24, **extra)


# 关键字参数检查
def person(name, age, **kw):
    if 'city' in kw:
        pass
    if 'job' in kw:
        pass
    print('name:', name, 'age', age, 'other:', kw)


person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)


# 关键字参数名字限制 使用 * 分隔
def person(name, age, *, city, job):
    print('name:', name, 'age:', age, 'city:', city, 'job:', job)


person('Jack', 24, city='Beijing', job='Engineer')


# 如果函数定义中已经有了一个可变参数，则后面跟着的命名关键字参数就不再需要一个特殊分隔符*
def person(name, age, *args, city, job):
    print('name:', name, 'age:', age, 'city:', city, 'job:', job)


# 有*,则视为关键字参数，否则，视为位置参数

def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


def f2(a, b, c=0, *d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


f1(1, 2)
f1(1, 2, c=3)
f1(1, 2, 3, 'a', 'b')

f1(1, 2, 3, 'a', 'b', x=99)
f2(1, 2, d=99, ext=None)

args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, *kw)

args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
f2(*args, **kw)


# 任意函数，都可以通过func(*args,**kw)的形式调用


def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


print(fact(100))


def fact(n):
    return fact_iter(n, 1)


def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)


print(fact_iter(100, 1))
