# -*- coding: utf-8 -*-
import numpy as np

def coordenadas():
    
    coord=[]
    theta=np.arange(0,2*np.pi,0.01)
    a=0
    b=1
    r=a+b*theta
    
    for i in range(0,len(theta)):
        coord.append((theta[i], r[i]))
    return coord

