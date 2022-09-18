# -*- coding: utf-8 -*-
import sympy as sp
import numpy as np

alpha = sp.Symbol('\\alpha')
beta = sp. Symbol('\\beta')
gamma = sp.Symbol('\\gamma')

def GetLegendre(n):
    
    x = sp.Symbol('x',Real=True)
    y = sp.Symbol('y',Real=True)
    
    y = (x**2 - 1)**n
    
    p = sp.diff(y,x,n)/(2**n * np.math.factorial(n))
    
    return p

Legendre = []
DerLegendre = []

x = sp.Symbol('x',Real=True)
n=2

for i in range(n+1):
    
    poly = GetLegendre(i)
    
    Legendre.append(poly)
    DerLegendre.append(sp.diff(poly,x,1))

# Asignando un coeficiente para cada polinomio de la base,

eq = sp.simplify(alpha*Legendre[0]+beta*Legendre[1]+gamma*Legendre[2])

# se obtiene un sistema lineal al igualar con el polinomio 

# 3 + 5x + x**2 = eq
#               = alpha - (1/2)*gamma + beta*x + 3/2*gamma*(x**2)

s, = sp.linsolve([alpha-1/2*gamma-3, beta-5, gamma*(3/2)-1],(alpha, beta, gamma))

a = s.args[0]
b = s.args[1]
g = s.args[2]

#resultando los coeficientes para cada polinomio de Legendre

p = sp.nsimplify(a), sp.nsimplify(b), sp.nsimplify(g)  

# donde alpha es el coeficiente del primer polinomio, y así sucesivamente

