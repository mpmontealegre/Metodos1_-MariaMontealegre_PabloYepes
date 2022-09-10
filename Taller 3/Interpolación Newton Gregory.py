# -*- coding: utf-8 -*-
import numpy as np
import sympy as sym
import pandas as pd
import os.path as path
import wget

file='InterpolacionNewtonGregory.csv'
url='https://raw.githubusercontent.com/asegura4488/Database/main/MetodosComputacionalesReforma/InterpolacionNewtonNoequi.csv'
if not path.exists(file):
    Path_ = wget.download(url,file)
else:
    Path_ = file

Data = pd.read_csv(Path_,sep=',')
X = np.float64(Data['X'])
Y = np.float64(Data['Y'])
        
def NewtonGregory(X,Y,x):
    
    Sum_ = Y[0]
    
    Diff = np.zeros((len(X),len(Y)))
    Diff[:,0] = Y

    h = X[1] - X[0]
            
    poly = 2.0
    
    for i in range(1,len(X)):
        
        poly *= ( x - X[i-1] )
        
        for j in range(i, len(X)):
            
            Diff[j,i] = Diff[j,i-1]-Diff[j-1,i-1]
            
        Sum_ += poly*(Diff[i,i])/(np.math.factorial(i)*h**(i))
    
    return Sum_,np.round(Diff,2)

x = sym.Symbol('x',Real='True')
y = y,_=NewtonGregory(X, Y, x)
p = y.simplify()

