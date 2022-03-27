'''
Классы - в пайтон позволяют описать поведение объектов данного класса путем создания этих классов
Синтаксис:

class MyClass:
    a = 10
    def func(self):
        print('hello')

В этом случае а, func - это атрибуты (то к чему можно обратиться через точку) класса MyClass
Конструктор классов: создает новые объекты каких-то классов
x = MyClass() # создаем объект класса MyClass
y = list() or  = [] # В этом случае мы также создаем объек класса Список 
(в первом случае явно, во втором с помощью синтаксиа Пайтон)



'''
class MyClass:
    a = 10
    def func(self):
        print('hello')

x = MyClass()  # <class '__main__.MyClass'>

#print(type(x))
'''
При создании класса внутри которого есть функция или функции, в первую функцию будет передан аргументом сам объект класса. 
При этом если мы в качестве метода вызываем какуюто другую функцию в неймспейсе класса, тогда также в качестве первого аргумента будет передан сам объект класса.
Функции внутри класса не должны ничего #возвращать#

'''

'''
class A:
    def __init__(self, val=0):
        self.val = val

    def add(self, x):
        self.val += x

    def print_val(self):
        print(self.val)


a = A()
b = A(2)
c = A(4)
a.add(2)
b.add(2)

a.print_val()
b.print_val()
c.print_val()

'''
'''
class MoneyBox:
    
    def __init__(self, capacity = 0):  # конструктор с аргументом – вместимость копилки
        self.capacity = capacity

    def can_add(self, v):  # True, если можно добавить v монет, False иначе
        return self.capacity - v >= 0
 
    def add(self, v):  # положить v монет в копилку
        if self.can_add(v):
            self.capacity -= v
            return self.capacity

x = MoneyBox(15)
print(x.can_add(10))
print(x.add(5))
print(x.add(9))
print(x.add(3))
'''

class Buffer:
    def __init__(self):  # конструктор без аргументов
        self.lst = []

    def add(self, *a):  # добавить следующую часть последовательности
        for int in a:
            self.lst.append(int)
            if len(self.lst) >= 5:
                count, sum = 5, 0
                while count != 0:
                    sum += self.lst.pop(0)
                    count -= 1
                print(sum)

    def get_current_part(self):  # вернуть сохраненные в текущий момент элементы последовательности в порядке, в котором они были     
        return self.lst          # добавлены

buf = Buffer()
buf.add(1, 2, 3)
print(buf.get_current_part()) # вернуть [1, 2, 3]
buf.add(4, 5, 6) # print(15) – вывод суммы первой пятерки элементов
print(buf.get_current_part()) # вернуть [6]
buf.add(7, 8, 9, 10) # print(40) – вывод суммы второй пятерки элементов
print(buf.get_current_part()) # вернуть []
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1) # print(5), print(5) – вывод сумм третьей и четвертой пятерки
print (buf.get_current_part()) # вернуть [1]

# 4 
class A:
    val = 1

    def foo(self):
        A.val += 2

    def bar(self):
        self.val += 1


a = A()
b = A()

a.bar()
a.foo()

c = A()

print(a.val)
print(b.val)
print(c.val)