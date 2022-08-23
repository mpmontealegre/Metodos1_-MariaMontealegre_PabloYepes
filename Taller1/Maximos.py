# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from scipy.signal import find_peaks

df=pd.read_csv('EstrellaEspectro.csv')
a=df.iloc[:,-1].str.split()
x1=[]
y1=[]
x2=[]
y2=[]
posiciones=[]
r=range(0,len(a))

for i in r:
    x=float(a[i][0])
    y=float(a[i][1])
    x1.append((x))
    y1.append(y)

peaks, _ = find_peaks(np.array(y1), height=0)

for i in range(0, len(peaks)):
    posiciones.append(peaks[i])
    x=x1[posiciones[i]]
    y=y1[posiciones[i]]
    x2.append(x)
    y2.append(y)














