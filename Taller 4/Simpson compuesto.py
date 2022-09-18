#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sympy as sp

A=0
C=[]
x = sp.Symbol('x')
t = sp.Symbol('t')
xk= sp.Symbol('x_k')
xj= sp.Symbol('x_j')
xi= sp.Symbol('x_i')
xs = sp.symbols('x_0:4')
f = sp.Function('f')
C.append(sp.Function('L_0'))
C.append(sp.Function('L_1'))
C.append(sp.Function('L_2'))
C.append(sp.Function('L_3'))

h = sp.Symbol('h') #= (b-a)/3

# Considerando a=xs[0] y b=xs[3]

for k in range(4):
    Poly=f(xs[k])*C[k](x)+f(xs[k-1])*C[k-1](x)+f(xs[k-2])*C[k-2](x)+f(xs[k-3])*C[k-3](x)
    A+= f(xs[k])*sp.integrate(C[k](x), (x, xs[0], xs[3]))

# Al integrar el polinomio interpolador
sp.Integral(Poly, x)

# se tiene 
A
display(A)


# In[2]:


# Expandiendo cada función cardinal a la forma

sp.var('j, n, i')
l = sp.Product((x-xj)/(xi-xj),(j, 0, n)) #con j≠i

# y definiendo para x la forma

x = xs[0] + t*h  #donde t es cada paso de la discretizacion

L_0 = ((h**3*(t-1)*(t-2)*(t-3))/((-6)*h**3))
L_1 = ((h**3*(t)*(t-2)*(t-3))/((2)*h**3))
L_2 = ((h**3*(t)*(t-1)*(t-3))/((-2)*h**3))
L_3 = ((h**3*(t)*(t-1)*(t-2))/((6)*h**3))

# Cambiando la integración respecto a t (límites de 0 a 3 y dx = hdt),
# la integral para cada función cardinal es

L_0 = (h/-6)*(sp.integrate((t-1)*(t-2)*(t-3), (t, 0, 3)))
L_1 = (h/2)*(sp.integrate((t)*(t-2)*(t-3), (t, 0, 3)))
L_2 = (h/-2)*(sp.integrate((t)*(t-1)*(t-3), (t, 0, 3)))
L_3 = (h/6)*(sp.integrate((t)*(t-1)*(t-2), (t, 0, 3)))

# donde la integral finalmente resulta

Integral = sp.simplify(f(xs[0])*L_0+f(xs[1])*L_1+f(xs[2])*L_2+f(xs[3])*L_3)
display(Integral)


# In[4]:


# Así, tomando en cuenta que incialmente se tomaron los límites de integración como los puntos extremos (xs[0] y xs[3]),
# los puntos intermedios xs[1] y xs[2] en términos de a, b y bajo la definción en la linea 40, son: 

x_1=xs[0]+(((xs[3])-xs[0])/3)
x_2=xs[0]+2*(((xs[3])-xs[0])/3)

display(x_1,x_2)


# In[ ]:




