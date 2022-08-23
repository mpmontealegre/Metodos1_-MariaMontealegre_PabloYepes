# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
A=1
nx=(5,4,3,2,1)
ny=(5,4,3,2,1)
t=np.linspace(0, 2*np.pi,200)
desfase=0
for i in range(0,):
    x=A*np.sin(nx[i]*t)
    for j in range(0,4):
        y=A*np.sin((ny[j]*t)+desfase)
        fig=plt.figure(figsize=(5,5))
        ax=plt.plot(nx,ny,k)
        k+=1
        ax.scatter(x,y)
        plt.show()

