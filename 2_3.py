'''
Итераторы и генераторы

Итератор (iterator) - это объект, который возвращает свои элементы по одному за раз. С точки зрения Python - это любой объект, 
у которого есть метод __next__ . 
Этот метод возвращает следующий элемент, если он есть, или возвращает исключение StopIteration, когда элементы закончились.

'''
# Для создания итератора необходимо:
'''
from random import random


class RandomIterator():

    def __init__(self, k):
        self.k = k
        self.i = 0

    def __iter__ (self):  # Для того, чтобы мочь использовать наш  класс в цикле for нужно определить метод iter
        return self

    def __next__(self):
        if self.i < self.k:
            self.i += 1
            return random()
        else:
            raise StopIteration


for x in RandomIterator(4):
    print(x)

#####

class Any:
    def __init__(self, iterable):
        self.iterable = iterable

    def __iter__(self):
        for i in self.iterable:
            if i != 2:
                yield i


list_a = [1, 2, 3]
obj = Any(list_a)
list_b = list(obj)

print(list_a)
print(obj)
print(list_b)
'''

# 1
'''
class multifilter:

    def judge_half(pos, neg):
        if pos >= neg:
            return True  # допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg)

    def judge_any(pos, neg):
        if pos >= 1:
            return True  # допускает элемент, если его допускает хотя бы одна функция (pos >= 1)

    def judge_all(pos, neg):
        if neg == 0:
            return True  # допускает элемент, если его допускают все функции (neg == 0)

    def __init__(self, iterable, *funcs, judge=judge_any):
        self.iterable = iterable  # iterable - исходная последовательность
        self.funcs = funcs  # funcs - допускающие функции
        self.judge = judge  # judge - решающая функция

    def __iter__(self):
        for x in self.iterable:
            pos, neg = 0, 0
            for func in self.funcs:
                res = func(x)
                if res is True: pos += 1
                else: neg += 1
            if self.judge(pos, neg) is True:
                yield x  # возвращает итератор по результирующей последовательности


def mul2(x):
    return x % 2 == 0

def mul3(x):
    return x % 3 == 0

def mul5(x):
    return x % 5 == 0


a = [i for i in range(31)] # [0, 1, 2, ... , 30]

print(list(multifilter(a, mul2, mul3, mul5))) 
# [0, 2, 3, 4, 5, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30]

print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_half))) 
# [0, 6, 10, 12, 15, 18, 20, 24, 30]

print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_all))) 
# [0, 30]
'''

# 2

import itertools
from math import factorial

def primes():
    number = 1
    while True:
        number += 1
        if (factorial(number - 1) + 1) % number == 0:
            yield number


print(list(itertools.takewhile(lambda x: x <= 31, primes())))
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
