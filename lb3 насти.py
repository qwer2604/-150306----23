import math as m
import numpy as np
x1 = 0
xn = 5
step_x = 0.5
a = 0.5
b = 0.7


def fx(x):
    return m.sin(a*x)+3*m.cos(b*x**2+1)


n = x1
print('цикл while')
while not n >= xn:
    n += step_x
    print('x= ', round(n, 3), 'f(x) = ', round(fx(n), 7))
print('цикл for')
for i in np.arange(x1, xn, step_x):
    print('x= ', round(i, 3), 'f(x) = ', round(fx(i), 7))
