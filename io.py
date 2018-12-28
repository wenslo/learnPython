# read file
import os

from io import StringIO, BytesIO

f = open('test.txt', 'r')
# 一次性读取
str = f.read()
print(str)
# 完毕后关闭
f.close()

try:
    f = open('test.txt', 'r')
    print(f.read())
finally:
    if f:
        f.close()

# try with
with open('test.txt', 'r') as f:
    print(f.read())
# 用read()会一次性读取文件的全部内容，如果文件有10G，内存就爆了，所以，要保险起见，可以反复调用read(size)方法，每次最多读取size个字节的内容。另外，调用readline()可以每次读取一行内容，调用readlines()一次读取所有内容并按行返回list。因此，要根据需要决定怎么调用
for line in f.readlines():
    print(line.strip())  # 把末尾的'\n'删掉

# 读取二进制文件
f = open('test.jpg', 'rb')
print(f.read())

# 字符编码
f = open('gbk.txt', 'r', encoding='gbk')
print(f.read())
# 编码错误忽略
f = open('gbk.txt', 'r', encoding='gbk', errors='ignore')
# 写文件
with open('test.txt', 'w') as f1:
    f1.write('Hello World')

# StringIO ByteIO

f = StringIO()
f.write('hello')
f.write('')
f.write('world')
print(f.getvalue())

f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue)

# 系统名称
print(os.name)
# 系统详细信息
print(os.uname())
# 环境变量
print(os.environ)
# Path
print(os.environ.get('PATH'))
# 当前目录绝对路径
print(os.path.abspath('.'))
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来，使用join能正确处理不同系统之间的分隔符
os.path.join('/Users/wen', 'testdir')
os.mkdir('# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:')
os.rmdir('/Users/wen/testdir')

# 拆分路径用 split
print(os.path.split('/Users/wen/testdir'))
# 获取阔爱站名
print(os.path.splitext('/Users/wen/testdir'))
