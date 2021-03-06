# python3

'''
Чтобы избежать (в математических расчётах) конструкции типа:

>>> print('f(x, 57))', '=', f(x, 57)))
0.03508771929824561

Я написал функцию, которая избавляет Вас от необходимости дважды писать одно и то же:
>>> print(p42(), f(x, 57))
f(x, 57) = 0.03508771929824561

Есть ещё функция p43, которая делает так:
>>> p43('f(x, 57)')
f(x, 57) = 0.03508771929824561

А функция reprint ващще делает то, что надо:
>>> reprint(f(x, 57))
f(x, 57) = 0.03508771929824561


Sourсe:
https://gisstudio.wordpress.com/2013/04/30/an-easy-way-to-get-the-line-number-of-your-python-code/

Listening:
[gridbug - intact hypervessel]
[legs akimbo records]
[2015]
[extratone, hyperspeedcore, breakcore, bugcore, hardcore, splittercore, terrorcore, flashcore]
https://vk.com/wall-32961164_94033
'''


import inspect
import os


def f(x, y):
    return x / y

x = 2


def p42():
    lineno = inspect.currentframe().f_back.f_lineno
    currentscriptath = os.path.realpath(__file__)
    with open(currentscriptath, 'r', encoding='utf') as file:
        codeline = file.readlines()[lineno - 1]
    container = codeline[12:][:-2] + ' ='
    return container

print(p42(), f(x, 57))


def p43(code):
    print(code, '=', eval(code))

p43('f(x, 57)')


def reprint(*args):
    lineno = inspect.currentframe().f_back.f_lineno
    currentscriptath = os.path.realpath(__file__)
    with open(currentscriptath, 'r', encoding='utf') as file:
        codeline = file.readlines()[lineno - 1]
    codetoeval = ''.join(codeline.split('(', 1)[1:])[:-2]
    print(codetoeval, '=', eval(codetoeval))

reprint(f(x, 57))
reprint(f(x, 57), (42, 57))
