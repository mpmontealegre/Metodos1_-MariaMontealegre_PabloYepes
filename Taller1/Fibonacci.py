# -*- coding: utf-8 -*-
from sympy import limit, oo, Symbol

def sucesion_fibonacci(cantidad_numeros:int):
    fibo = [0,1] 
    sumatoria = str(0)
    
    if cantidad_numeros==1:
        sucesion=[fibo[0]]
    if  cantidad_numeros==2:
        sucesion=fibo
    for cantidad_numeros in range(2,(cantidad_numeros)):
      sumatoria = fibo[(len(fibo)-2)] + fibo[(len(fibo)-1)]
      fibo.append(sumatoria)
    
      cadena = (fibo)
      sucesion = (cadena[0:len(cadena)])
     
    return sucesion

def aureo_fibonacci(n: int):
    x=Symbol('x')
    y=((sucesion_fibonacci(n+1)[-1])/sucesion_fibonacci(n)[-1])
    
    return limit(y,x,oo)

def aureo(x):
    return 1.6180339985
