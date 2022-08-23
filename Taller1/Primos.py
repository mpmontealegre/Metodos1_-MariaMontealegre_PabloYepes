# -*- coding: utf-8 -*-
def numeros_primos(cantidad:int):
    r=range(2,1000)
    primos=[]
    lst=[]
    for i in r:
        check=0
        for n in range(1,i+1):
            if i%n==0:
                check +=1
        if check==2:
             primos.append(i)   
        lst=primos[0:cantidad]
    return lst

print(numeros_primos(10))