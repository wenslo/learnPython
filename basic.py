#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 字符串转义使用\
print('i\'m ok.')
print('I\' learning \n Python')
print('\\\n\\')
print('\\\t\\')
print(r'\\\n\\')
# 可以使用'''进行多行输出，使用r''可以使其中字符不转义
print('''
line1...
\tline2...
\tline3...
''')
print(r'''
line1...
\tline2...
\tline3...
''')
# python中 与或非 为 and or not
print(True and False)
print(False and False)
print(True or False)
print(not False)
# 动态语言，变量随意定
a = 0
print(a)
t_007 = 't_007'
print(t_007)
Answer = True
print(Answer)
a = 'ABD'
b = a
a = 'XYZ'
# / 为普通除法 //为扫地除法
print(b)
print(10 / 3)
print(9 / 3)
print(10 // 3)
print(10 % 3)
n = 123
f = 456.789
s1 = 'Hello World'
s2 = 'Hello \'Adam\''
s3 = r'Hello , "Bart"'
s4 = r'''
Hello , Lisa!
'''
print(n)
print(f)
print(s1)
print(s2)
print(s3)
print(s4)

# 使用ord进行查看对应字符串的编码后的内容，chr相反

print('这是一个str')
print(ord('A'))
print(ord('中'))
print(chr(66))
print(chr(25991))
x = b'ABC'
print(x)
'ABC'.encode('ascii')
print(b'ABC')
print('中文'.encode('utf-8'))
# 中文无法使用 ascii编码 ，编码使用encode 解码使用decode，可以使用errors='ignore'忽略错误字节
print(b'ABC'.decode('ascii'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
# 使用len计算字符数，若值为bytes 则计算字节数
print(len('ABC'))
print(len('中文'))
print(len(b'ABC'))
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))
print(len('中文'.encode('utf-8')))

# python源文件加顶上那两行，可以定义编码
# 字符串格式化方式类同于C
print('Hello ,%s' % 'World')
# %d 整数
# %f 浮点数
# %s 字符串
# %f 十六进制整数
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)
# %转义的话，需要两个% 既 %%
print('Hello ,{0},成绩提升了{1:.2f}%'.format('小名', 0.777))

# python 数组定义很方便
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)
print(len(classmates))
print(classmates[0])

# 可以通过-1获取最后一个元素，-2 -3同理
print(classmates[-1])
# append insert demo
classmates.append('Tom')
print(classmates[-1])
classmates.insert(1, 'Lisa')
print(classmates)
# pop 删除指定位置元素
classmates.pop(1)
print(classmates)
s = ['python', 'javascript', ['c', 'c++', 'c#']]
print(s)
# tuple 示例，不可变。如果只有一个元素，需要使用,进行歧义消除
classmates = ('Michael', 'Bob', 'Tracy')
print(classmates)
# tuple 指针不变，但是指针所包含的可变
t = ('a', 'b', ['A', 'B'])
print(t)
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)

age = 20
if age > 18:
    print('you age is ', age)
    print('adult')

age = 3
if age > 18:
    print('you age is ', age)
    print('adult')
else:
    print('you age is ', age)
    print('teenager')

age = 3
if age >= 18:
    print('adult')
elif age >= 8:
    print('teenager')
else:
    print('child')

# 非零数值 非空字符串 非空list 则为True
if x:
    print('True')

# 使用int()进行类型转换
# birth = input('brith:')
# if birth < 2000:
#     print('90后')
# else:
#     print('00后')

weight = 80
height = 1.80

BMI = weight / pow(height, 2)
if BMI < 18.5:
    print('under weight ')
elif 25 > BMI >= 18.5:
    print('normal')
elif 25 <= BMI < 28:
    print('to heavy')
elif 28 <= BMI < 32:
    print('fat')
elif BMI > 32:
    print('so fat')

print('The BMI is ', BMI)

# for in
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum += x
print(sum)
# 通过range函数生成整数序列
print(list(range(5)))
# so，可以这样做
sum = 0
for x in range(101):
    sum += x
print(sum)

sum = 0
n = 99
while n > 0:
    sum += n
    n -= 2
print(sum)

n = 1
while n < 100:
    if n > 10:
        break
    print(n)
    n += 1
print('END')

n = 0
while n < 10:
    n += 1
    if n % 2 == 0:
        continue
    print(n)

# dict hash
d = {'Michael': 95, 'Bob': 95, 'Tracy': 55}
print(d)
print(d['Michael'])
d['Adam'] = 66
print(d)

print('Thomas' in d)
print(d.get('Thomas', 20))
d.pop('Adam')
print(d)
# key值必须不可变，所以list不能用作key,但是tuple可以
k = (1, 2, 3)
print(k)
d[k] = 55
print(d)

s = set([1, 2, 3])
print(s)
s = set([1, 2, 3, 4, 5, 6, 6, 6, 6, 6, 7, 8, 8, 9])
print(s)
s.add(1)
print(s)

s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1 & s2)
print(s1 | s2)
a = ['c', 'b', 'a']
print(a)
a.sort()
print(a)
a = 'abc'
print(a.replace('a', 'A'))
print(a)
