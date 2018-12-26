# 类名大写，没有合适的继承类，就是用object
import types


class Student(object):
    pass


bart = Student()

print(bart)
print(Student)
bart.name = 'Bart Simpson'
print(bart.name)


# init方法  类似于构造函数，定义了之后，则必须进行参数传递

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s : %s' % (self.name, self.score))

    def get_grade(self):
        if self.score > 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'


bart = Student('Bart Simpson', 59)
print(bart.name)
print(bart.score)

# def print_score(std):
#     print('%s : %s' % (std.name, std.score))
#
#
# print_score(bart)

bart.print_score()
lisa = Student('Lisa', 99)
bart = Student('Bart', 59)
print(lisa.name, lisa.get_grade())
print(bart.name, bart.get_grade())


# Python允许对实例变量绑定任何数据，也就是说，对于两个实例变量，虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同：

# 如果想让内部属性不被外部访问，属性前加两个下划线（private）

class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def set_name(self, score):
        self.__score = score

    def get_name(self):
        return self.__name


bart = Student('Bart', 59)
# 无法直接访问私有变量  需要setter getter ，除非通过 _xx_xx，但是不推荐
print(bart.get_name())

print(bart._Student__score)


# test
class Student(object):
    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender

    def set_gender(self, gender):
        if gender != 'male' and gender != 'female':
            raise ValueError('error gender')
        self.__gender = gender

    def get_gender(self):
        return self.__gender


bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')


class Animal(object):
    def run(self):
        print('Animal is running ...')


class Dog(Animal):
    def run(self):
        print('Dog is running ...')

    def eat(self):
        print('Eating meat ...')


class Cat(Animal):
    def run(self):
        print('Cat is running ...')

    def eat(self):
        print('Eating fish ...')


dog = Dog()
dog.run()

a = list()
b = Animal()
c = Dog()

print(isinstance(a, list))
print(isinstance(b, Animal))
print(isinstance(c, Dog))


def run_twice(animal):
    animal.run()
    animal.run()


run_twice(Animal())
run_twice(Dog())
print(type(123))
print(type('str'))
print(type(None))
print(type(abs))


def fn():
    pass


print(type(fn) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type(x for x in range(10)) == types.GeneratorType)
# 可以替换为 isinstance() ，并且优先使用isinstance()进行判断
# 获取一个对象的所有属性与方法，dir()
print(dir('ABC'))


class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x


obj = MyObject()

print(hasattr(obj, 'x'))
print(setattr(obj, 'y', 19))
print(hasattr(obj, 'y'))
print(getattr(obj, 'y'))
print(obj.y)
# print(obj.z)
print(getattr(obj, 'z', 404))

print(hasattr(obj, 'power'))
print(getattr(obj, 'power'))
fn = getattr(obj, 'power')
print(fn)
print(fn())


# def readImage(fp):
#     if hasattr(fp, 'read'):
#         return readData(fp)
#     return None

class Student(object):
    name = 'Student'


s = Student()

print(s.name)
s.name = 'Michael'
print(s.name)
print(Student.name)
del s.name
print(s.name)
