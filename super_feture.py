import os
from collections import Iterable
from collections import Iterator

# 切片操作 倒数第一个元素 下标为 -1
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(L[0:3])
print(L[1:2])

L = list(range(100))
print(L)
print(L[:10])
print(L[-10:])
print(L[10:20])
print(L[:-10:2])
print(L[::5])
# 什么都不写 则复制一个list
print(L[:])
# 字符串也可以看为一个list
print('ABCDEFG'[:3])
print('ABCDEFG'[::2])

# 迭代

d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)
for k, v in d.items():
    print('%s : %s' % (k, v))
# 判断是否可迭代
print(isinstance('abc', Iterable))
print(isinstance((1, 23, 4), Iterable))
print(isinstance(123, Iterable))

for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

# 两个变量在循环里
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)

# 列表生成式
print([x * x for x in range(1, 11)])
print([x * x for x in range(1, 11) if x % 2 == 0])
# 双层循环
print([m + n for m in 'ABC' for n in 'DEF'])

print([d for d in os.listdir('/home/wen/Work')])
d = {'x': 'A', 'y': 'B', 'z': 'Z'}
for k, v in d.items():
    print(k, '=', v)
print([k + '=' + v for k, v in d.items()])

L = ['HELLO', 'WORLD', 'APPLE', 'IBM']
print([n.lower() for n in L])

L1 = ['Hello', 'World', 18, 'Apple', None]
print([n.lower() for n in L1 if isinstance(n, str)])

# generator
g = (x * x for x in range(10))
print(g)
print(next(g))
print(next(g))
for n in g:
    print(n)


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'


fib(6)


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


f = fib(6)
for n in fib(6):
    print(n)
g = fib(6)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break
# 迭代器
print(isinstance([], Iterator))
print(isinstance({}, Iterator))
print(isinstance('abc', Iterator))
print(isinstance((x for x in range(10)), Iterator))
print(isinstance(100, Iterator))
