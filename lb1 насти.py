import math as m
x, y, z = float(input('x=')), float(input('y=')), float(input('z='))
a = (9+(x+y)**2)**1/3
b = x**2 +y**2 + 2
c = m.exp(x-y)*(m.tan(z)**3)
s = (a/b) - c
print('s=', round(s, 5))
