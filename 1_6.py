'''
Наследоване класса
 - нужно в случсе если необходимо создать класс, включающий все атрибуты другого класса с каким-то отличием (например, добавлением нового атрибута)
 Например, наследование от класса list всех атрибутов с добавлением возможности подсчета четных и нечетных значений

Синтаксис наследования класса

class DerivedClassName(BaseClass1, BaseClass2, BaseClass3):

Функция issubclass(A, A) # == True возвращает значение True
если переданные в качестве аргументов классы являются наследниками

Функция isinstance (x, A) возвращает True в случае,
если экземпляр x является наследником класса A

'''
'''
class list_len(list):
    def list_lenth(self):
        return len(self) % 2 == 0

x = list_len()
print(x)  # []
x.append(1)
print(x)  # [1]
print(x.list_lenth())  # False
print(isinstance(x, list))  # True

'''
'''
Наследование классов предполагает
порядок нахождения тех или иных методов внутри наследуемых классов
В Python существует четкое описание порядка наследования методов, 
увидить который можно с помощью метода .mro

'''
'''
print(list_len.mro())  # [<class '__main__.list_len'>, <class 'list'>, <class 'object'>]

class Base:
    def __init__(self):
        self.val = 0

    def add_one(self):
        self.val += 1

    def add_many(self, x):
        for i in range(x):
            self.add_one()

class Derived(Base):
    def add_one(self):
        self.val += 10


a = Derived()
a.add_one()

b = Derived()
b.add_many(3)

print(a.val)
print(b.val)
'''

#1
'''
number_of_classes = int(input())
lines = [input() for _ in range(number_of_classes)]

grafs = {}
for line in lines:
    if ':' in line:
        key, val = line.strip().split(':')
        key = key.strip(' ')
        if key in grafs:
            grafs[key] = val.split()
        else:
            grafs.update({key : val.split()})
    else:
        key = line.strip()
        grafs.update({key : []})

number_of_requests = int(input())
requests = [input().split() for _ in range(number_of_requests)]

def search(grafs, class1, class2):
    if class1 in grafs[class2] or class1 == class2:
        return True
    else:
        for classes in grafs[class2]:
            if classes not in grafs:
                continue
            x = search(grafs, class1, classes)
            if x == None:
                continue
            elif x == True:
                return True
                
#print(grafs)

for request in requests:
    class1, class2 = request[0], request[1]
    if class2 not in grafs:
        print('No')
        continue
    if search(grafs, class1, class2) == True:
        print('Yes')
    elif search(grafs, class1, class2) == None:
        print('No')
'''
# 2
'''

class ExtendedStack(list):

    def sum(self):  # операция сложения
        summa = self.pop() + self.pop()
        self.append(summa)
    
    def sub(self):  # операция вычитания
        subtract = self.pop() - self.pop()
        self.append(subtract)

    def mul(self):  # операция умножения
        multiplication = self.pop() * self.pop()
        self.append(multiplication)

    def div(self):  # операция целочисленного деления
        integer_division = self.pop() // self.pop()
        self.append(integer_division)


x = ExtendedStack()
print(type(x))
x = ExtendedStack([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(type(x))
print(x.sum())
print(x)
'''
import time


class Loggable:

    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))


class LoggableList(list, Loggable):

    def append(self, meaning):
        x = super(LoggableList, self).append(meaning)
        self.log(meaning)


y = LoggableList([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
y.append(9836738)
print(y)
