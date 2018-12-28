import re

# 匹配成功 返回一个match对象，否则，返回一个None
print(re.match(r'^\d{3}\-\d{3,8}', '010-12345'))
print(re.match(r'^\d{3}\-\d{3,8}$', '010 12345'))

print('a b    c'.split(' '))
print(re.split(r'\s+', 'a b   c'))
print(re.split(r'[\s\,\;]+', 'a,b;; c d'))

m = re.match(r'^(\d{3})-(\d{3,8})', '010-12345')
print(m)
print(m.group(0))
print(m.group(1))
print(m.group(2))
