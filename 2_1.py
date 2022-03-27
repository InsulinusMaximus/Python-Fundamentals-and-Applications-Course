'''
Ошибки при интерпретации в Python
1. Синтактические - видны до исполнения кода
2. Исключения - возникают в процессе исполнения кода

Если необходимо продолжать выполнение кода даже после ошибки, нужно описать тип этой ошибки и что делать при ее возникновениии(except <Тип ошибки>:),
кроме того сам код с вероятной ошибкой должен быть в теле конструкции try:

'''
'''
from asyncio import exceptions
from logging import exception

try:
    lst = [1, 2, 3, 'a', 5]
    print(sorted(lst))
except TypeError:
    print('Type error happened\n')
    '''
'''
В случае возможного возникновения нескольких ошибок, их можно обработать несколькими except-ами или создать кортеж в первом except-е: 
'''
'''
#1
def fun1(x, y):
    try:
        return x / y
    except TypeError:
        print('Type error happened')
    except ZeroDivisionError:
        print('Zero division error happened')
'''

#print(fun1(4, 0))

#2
'''

def fun2(x, y):
    try:
        return x / y
    except (TypeError, ZeroDivisionError):
        print('An error happened\n')
'''

#print(fun2(4, []))
'''
Можно ловить объект ошибки путем использования as:
'''
'''
def fun_as(x, y):
    try:
        return x / y
    except (TypeError, ZeroDivisionError) as er:
        print(type(er))
        print(er)
        print(er.args)
'''

#print(fun_as(4, []))
'''
Если не известы типы возмоных ошибок с помощью использования пустого except:
'''
'''
def fun_empty(x, y):
    try:
        return x / y
    except:
        print('Error')

'''
#print(fun_empty(4, []))

#11
'''
def foo():
    return 1 / 0


try:
    foo()
except AssertionError as e:
    print('AssertionError')
except ZeroDivisionError as e:
    print('ZeroDivisionError')
except ArithmeticError as e:
    print('ArithmeticError')
'''

#33


class NonPositiveError(Exception):
    pass


class PositiveList(list):

    def append(self, meaning):
        if meaning > 0:
            x = super(PositiveList, self).append(meaning)
        else:
            raise NonPositiveError


y = PositiveList([1, 2, 3, 4, 5, 6])
y.append(-1)
print(y)