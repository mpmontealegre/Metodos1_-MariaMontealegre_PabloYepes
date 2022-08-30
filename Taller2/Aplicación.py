# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

xi,xf,N=-4,4,25
x = np.linspace(xi,xf,N)
y = x.copy()
h = 0.001
r=2
v=2
def funcion(x,y):
    return (v*x*np.sqrt( 1-(r**2/(x**2+y**2)) ))

X,Y = np.meshgrid(x,y)

PartialOperator = (lambda f,x,y,h : (f(x+h,y)-f(x-h,y))/(2*h),\
           lambda f,x,y,h: (f(x,y+h)-f(x,y-h))/(2*h))

Vx = PartialOperator[0](funcion,X,Y,h)
Vy = -PartialOperator[1](funcion,X,Y,h)

fig1 = plt.figure(figsize=(10,8))
ax = fig1.add_subplot()

for i in range(1,N):
    for j in range(1,N):
        ax.quiver(x[i],y[j],Vx[i,j],Vy[i,j],color='blue')


