# __slots__
from enum import Enum, unique
from types import MethodType


class Student(object):
    pass


s = Student()
s.name = 'Warren'
print(s.name)


def set_age(self, age):
    self.age = age


s.set_age = MethodType(set_age, s)
s.set_age(25)
print(s.age)

s2 = Student()


# s2.set_age(25)
# class 绑定方法
def set_score(self, score):
    self.score = score


Student.set_score = set_score

s.set_score(100)
print(s.score)
s2.set_score(99)
print(s2.score)

# slots 只能对当前类生效，对子类不起作用，除非子类也定义一个 slots
# class Student(object):
#     __slots__ = ('name', 'age')
#
#
# s = Student()
# s.name = 'Warren'
# s.age = 25
# s.score = 99

s = Student()
s.score = 99

print(s.score)


class Student(object):
    def get_score(self):
        return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an interger!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100')
        self._score = value


s = Student()
s.set_score(60)
print(s.get_score())


# s.set_score(9999)

class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an interger!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100')
        self._score = value


s = Student()
s.score = 60
print(s.score)
# s.score = 99999999999
print(s.score)


class Animal(object):
    pass


# 大类:
class Mammal(Animal):
    pass


class Bird(Animal):
    pass


# 各种动物:
class Dog(Mammal):
    pass


class Bat(Mammal):
    pass


class Parrot(Bird):
    pass


class Ostrich(Bird):
    pass


class Runnable(object):
    def run(self):
        print('Running...')


class Flyable(object):
    def fly(self):
        print('Flying...')


class Dog(Mammal, Runnable):
    pass


class Bat(Mammal, Runnable):
    pass


# __str__ __repr__

class Student(object):
    def __init__(self, name):
        self.name = name

    # to str
    def __str__(self):
        return 'Student object (name : %s)' % self.name

    __repr__ = __str__


print(Student('Warren'))
s = Student('Warren')


# __iter__  __next__ 迭代
# class Fib(object):
#     def __init__(self):
#         self.a, self.b = 0, 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.a, self.b = self.b, self.a + self.b
#         if self.a > 100000:
#             raise StopIteration
#         return self.a
#
#
# for n in Fib():
#     print(n)


# __getitem__


class Fib(object):
    def __getitem__(self, n):
        # a, b = 1, 1
        # for x in range(n):
        #     a, b = b, a + b
        # return a
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L


f = Fib()

print(f[100])

f = Fib()
print(f[0:5])


class Student(object):
    def __init__(self):
        self.name = 'Marren'

    def __getattr__(self, item):
        if item == 'score':
            return 99
        if item == 'age':
            return lambda: 25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % item)


s = Student()
print(s.name)
print(s.score)
print(s.age())


class Chain(object):
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__


print(Chain().status.user.timeline.list)


# 实例调用方法 __call__()

class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self, *args, **kwargs):
        print('My name is %s' % self.name)


s = Student('Marren')
s()
# 判断是否可调用
print(callable(Student('')))

print(callable(max))
print(callable(None))
print(callable('str'))

Month = Enum('Month', (
    'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
    'December'))
Month

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)


# 检查保证没有重复值
@unique
class Weekday(Enum):
    Sunday = 0
    Monday = 1
    Tuesday = 2
    Wednesday = 3
    Thursday = 4
    Friday = 5
    Saturday = 6


day1 = Weekday.Monday
print(day1)
print(Weekday['Tuesday'])
print(Weekday.Saturday.value)
print(day1 == Weekday.Saturday)
print(day1 == Weekday.Monday)


# test
class Gender(Enum):
    Male = 0
    Female = 1


class Student(object):
    def __init__(self, name, gender):
        if not isinstance(gender, Gender):
            raise AttributeError('Gender is not usable variable')
        self.name = name
        self.gender = gender


# 测试:
bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')

print(bart.gender)


class Hello(object):
    def hellp(self, name='world'):
        print('Hello , %s.' % name)


print(type(Hello))


def fn(self, name='world'):
    print('Hello, %s.' % name)


Hello = type('Hello', (object,), dict(hello=fn))

h = Hello()
h.hello()


class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


class MyList(list, metaclass=ListMetaclass):
    pass


L = MyList()
L.add(1)
print(L)


class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)


class StringField(Field):

    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')


class IntegerField(Field):

    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')


class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        print('Found model : %s' % name)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping:%s ==> %s' % (k, v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)

        attrs['__mappings__'] = mappings  # 保存属性和列的映射关系
        attrs['__table__'] = name  # 假设表名和类名一致
        return type.__new__(cls, name, bases, attrs)


class Model(dict, metaclass=ModelMetaclass):
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))

        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))


class User(Model):
    # 定义类的属性到列的映射：
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')


# 创建一个实例：
u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
# 保存到数据库：
u.save()
