# -*- coding: utf-8 -*-
import sympy as sp
import sympy.abc as abc

xi = sp.Symbol('\\xi')
xs = sp.symbols('x_0:4')
h = sp.Symbol('h')
t = sp.Symbol('t')
x1 = sp.Symbol('x')
f = sp.Function('f')

# Definiendo

x = xs[0] + t*h #donde t es cada paso en la discretización

# Si se considera a = 0*h = xs[0] y b = 3*h = xs[3] (extremos de la discretización)

# x - xs[0] = x
# x - xs[1] = x - 1*h
# x - xs[2] = x - 2*h
# x - xs[3] = x - 3*h

# Por lo que la integral que multiplica a la cuarta derivada resulta

I = sp.Integral((x1*(x1-h)*(x1-2*h)*(x1-3*h)), (x1, 0, 3*h))

# así, el error es igual a 

E = (f(xi).diff(xi, 4))/sp.factorial(4))*sp.integrate((x1*(x1-h)*(x1-2*h)*(x1-3*h)), (x1, 0, 3*h))



