# -*- coding: utf-8 -*-
import Fibonacci as Fibonacci
import Primos as Primos
import Maximos as Maximos
from matplotlib import pyplot as plt
import numpy as np

#Gráfica maximos

plt.plot(Maximos.x1, Maximos.y1)
plt.scatter(Maximos.x2, Maximos.y2, c="red")
plt.title("Serie de datos y sus máximos locales")
plt.show()

#Gráfica sucesion Fibonacci

plt.plot(Fibonacci.sucesion_fibonacci(21),color='black')
plt.title("Sucesión de Fibonacci")
plt.show()

#Gráfica comparativa número aureo y sucesión Fibonacci

r=range(2,20)

x1=[Fibonacci.aureo_fibonacci(i) for i in r]
x2=[Fibonacci.aureo(i) for i in r]
fig, ax=plt.subplots()
ax.plot(x1, label= "Estimación usando la sucesion")
ax.plot(x2, label="Número aureo")
ax.legend()
plt.show()

#Gráfica numeros primos en funcion de posicion

plt.plot(Primos.numeros_primos(1000),color="red")
plt.title("Primeros 1000 números primos")
plt.show()

#Gráfica espiral de Arquímedes
theta = np.linspace(0., 2*np.pi, 500)
a, b = 0, 1.
plt.polar(theta, a+b*theta)
plt.title("Espiral de Arquímedes")
plt.show()