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

