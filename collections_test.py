import argparse
import os
from collections import namedtuple, deque, defaultdict, OrderedDict, ChainMap, Counter

# 自定义tuple对象

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x)
print(p.y)

print(isinstance(p, Point))
print(isinstance(p, tuple))

Circle = namedtuple('Circle', ['x', 'y', 'r'])

# deque appendleft popleft
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)
# defaultdict

dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print(dd['key1'])
print(dd['key2'])
# 确保key的顺序 OrderedDict 插入顺序
d = dict([('a', 1), ('b', 2), ('c', 3)])
print(d)
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od)


# FIFO
class LastUpdateOrderedDict(OrderedDict):
    def __init__(self, capacity):
        super(LastUpdateOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)


# ChainMap

defaults = {
    'color': 'red',
    'user': 'guest'
}
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')
namespace = parser.parse_args()
command_line_atgs = {k: v for k, v in vars(namespace).items() if v}

combined = ChainMap(command_line_atgs, os.environ, defaults)
print('color=%s' % combined['color'])
print('user=%s' % combined['user'])

# counter

c = Counter()
for ch in 'programing':
    c[ch] = c[ch] + 1
print(c)
