import math as m
b = True
a = 0
x, y = float(input('x=')), float(input('y='))
hp1 = x/y > 0
hp2 = x/y < 0
hp3 = x/y == 0


def fx1(y):
    return m.tanh(m.radians(y))


def fx2(x):
    return x**5


def fx3(x, y):
    return x**y


while b:
    gh = input('f1 == 1, f2 == 2, f3 == 3: ')
    if gh == '1':
        a = fx1(y)
        b = False
    elif gh == '2':
        a = fx2(x)
        b = False
    elif gh == '3':
        a = fx3(x, y)
        b = False
    else:
        print('Ошибка')
        gh = ''
if hp1:
    c = m.log(a - a**1/3)
elif hp2:
    c = m.log(abs(a)/y)*(x+y)**3
else:
    c = (a**2 + y)**3
print('c=', c)
