#!/usr/bin/evn python3.6
# -*_ coding:utf-8 -*-

' a test module'

__author__ = 'Warren Wen'


def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello World')
    elif len(args) == 2:
        print('Hello, %s!' % args[1])
    else:
        print('Too may argyments!')


# if __name__ == '__main__':
#     test()


# __xxx__ 特殊变量 能被直接引用，但最好不要
# _x __xxx 为私有变量 不能被直接引用

def _private_1(name):
    return 'Hello, %s' % name


def _private_2(name):
    return 'Hi, %s' % name


def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2()


import sys

print(sys.path)
