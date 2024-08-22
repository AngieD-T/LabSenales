# Practica 1 Introducción a Python 
# Angie Tovar 1000603915

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Item a 
a = np.array([67.1, 1, -0.3, 5.2, -6])
b = np.array([1, 3, 2.2, 5.1, 1])

# Item b
Pescalar = np.dot(a,b)

# Item c
Mpuntoapunto = a * b

# Item d
A = np.array([[2, -1, -3 ],[4, -1.5, -2.5],[7.3, -0.9, -0.2]])

# Item e
AT = np.transpose(A)

# Item f
Mones = np.ones((2, 3)) # crea una matriz llena de unos en este caso con dimensiones de 2 x 3
Redondear = np.round(12.814,) # Redondea el valor decimal de un número a su entero más cercano, en este caso 13
Redondear_Mayor = np.ceil(22.23) # Devuelve el número entero más próximo que sea mayor a él.
Redondear_Menor = np.floor(32.68) # Devuelve el número entero más próximo que sea menor a él.

# Item g
ubicacion1 = A[0,2]
print('Valor de la primera fila y tercera columna de la matriz A:',ubicacion1)

# Item h
ubicacion2 = A[1,:]
print('Valores de la segunda fila de la matriz A:',ubicacion2)

# Item i
dimensiones = A.shape
print('Las dimensiones (filas, columnas) de la matriz A son:', dimensiones)

# Item j
n_valores = np.arange(0,81)
y = np.sin(np.pi * 0.18 * n_valores)

# Item k
y2 = np.cos(2 * np.pi * 0.03 * n_valores)

# Item l
s = y + y2
t = y * y2

# Item m
plt.figure(1)

plt.plot(n_valores, y, label = 'y(n) = sin(π * 0.18n)', color = '#98FF98')
plt.plot(n_valores, y2, label = 'y2(n) = cos(2π * 0.03n)', color = '#FFC0CB')

plt.title('Señales seno y coseno')
plt.xlabel('n')
plt.ylabel('y(n) - y2(n)')
plt.legend()
plt.grid(True)
plt.show()

# Item n
plt.figure(2)

plt.plot(n_valores, s, label = 's(n) = y(n) + y2(n)', color = '#D8BFD8')
plt.plot(n_valores, t, label = 't(n) = y(n) * y2(n)', color = '#FFC0CB')

plt.title('Operaciones entre señales')
plt.xlabel('n')
plt.ylabel('s(n) - t(n)')
plt.legend()
plt.grid(True)
plt.show()

# Reto 

def notas_alumnos(diccionario_notas):
    notas = list(diccionario_notas.values())

    min_notas = np.min(notas)
    max_notas = np.max(notas)
    media_notas = np.mean(notas)
    desviacion_notas = np.std(notas)

    Estadistica = pd.Series({
        'Nota minima': min_notas,
        'Nota máxima' : max_notas,
        'Media' : media_notas,
        'Desviación tipica' : desviacion_notas
    })

    return Estadistica




