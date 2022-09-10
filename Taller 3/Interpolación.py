# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import sympy as sym
import wget

file = 'Experimento.csv'
url = 'https://raw.githubusercontent.com/asegura4488/Database/main/MetodosComputacionalesReforma/Parabolico.csv'
Path_ = wget.download(url,file)
Data=pd.read_csv(Path_,sep=',')

X = np.float64(Data['X'])
Y = np.float64(Data['Y'])
g = 9.8

def Lagrange(x,xi,j): 
    prod = 1
    n=len(xi)
    
    for i in range(n):
        if i != j:
            prod*=(x-xi[i])/(xi[j]-xi[i])
   
    return prod

def Polinomio(x,xi,yi):
    Sum=0
    n = len(yi)
    for j in range(n):
        Sum += yi[j]*Lagrange(x,xi,j)
    return Sum

#x=np.linspace(0.5,6,50)
#y=Polinomio(x,X,Y)

x = sym.Symbol('x')
p = Polinomio(x,X,Y)
func = sym.expand(p)
function = str(func).split(' + ')

#Ecuación de trayectoria en movimiento parabólico
# y = (1)xtan(theta)-(2)gx^2/2v^2cos^2(theta)

# (1) = Bx, donde B es el término lineal de la ecuación de trayectoria

lineal = function[1].split('*')
lcoef = float(lineal[0])

# despejando: 
#   tan(theta)=B, tal que

theta = np.arctan(lcoef) #en radianes
theta_c = round(theta*(180/np.pi)) #en grados

# (2) = Ax^2, reemplazando theta en (2) y despejando para v:

cuadratic = function[0].split('*')
ccoef = float(cuadratic[0])
#vel = sqrt((g/2*((np.cos(theta))^2))/ccoef)
vel = np.sqrt((g/(0.11098*((np.cos(theta))**2))))
velocity = round(vel) #m/s
