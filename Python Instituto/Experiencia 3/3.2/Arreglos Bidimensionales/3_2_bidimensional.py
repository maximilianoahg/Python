import numpy as np
import random

# Una matriz está compuesta por filas y columnas

#  OPERACIONES CON UN ARREGLO DE DOS DIMENSIONES

# TRADICIONAL
matriz = np.array([[0, 1, 2], [3, 4, 5]])
for f in range(2):
    for c in range(3):
        print(matriz[f][c])

print(f'ELEMENTO 1,1: {matriz[1, 1]}')

# USANDO LISTAS
lista = [[1, 2, 3],
         [4, 5, 6]]

matriz = np.array(lista)
print(matriz)
print(f'ELEMENTO O,1: {matriz[0][1]}')

# MOSTRAR ELEMENTOS DE LA MATRIZ

lista = [[1, 2, 3],
         [4, 5, 6]]
matriz = np.array(lista)

print(matriz[1, 1]) # 5
print(matriz[:,2]) # [3 6]
print(matriz[0, :]) # [1 2 3]
print(matriz[0,::-1]) # [3 2 1]


# GENERAR MATRIZ CON CEROS
matriz = np.zeros((3, 3))
print(matriz) #[[0. 0. 0.] [0. 0. 0.] [0. 0. 0.]]

# GENERAR MATRIZ CON UNOS
matriz = np.ones((3, 3))
print(matriz) #[[1. 1. 1.] [1. 1. 1.] [1. 1. 1.]]

# GENERAR MATRIZ CON DIAGONAL PRINCIPAL CON 1
matriz = np.diag([1, 1, 1])
print(matriz) #[[1 0 0] [0 1 0] [0 0 1]]

# SUMAR LOS ELEMENTOS

lista = [[1, 2, 3],
         [4, 5, 6]]
matriz = np.array(lista)

print(matriz.sum()) # 21

# SUMAR LOS ELEMENTOS POR FILA

lista = [[1, 2, 3],
         [4, 5, 6]]
matriz = np.array(lista)

print('Suma de los elementos de la fila 0: ', matriz[0:].sum()) # 6
print('Suma de los elementos de la fila 1: ', matriz[1:].sum()) # 15
print('Suma de los elementos de la columna 0: ', matriz[:,0].sum()) # 5
print('Suma de los elementos de la columna 1: ', matriz[:,1].sum()) # 7
print('Suma de los elementos de la columna 1: ', matriz[:,2].sum()) # 9

print(matriz.ndim) # 2 => MUESTRA LAS DIMENSIONES DE LA MATRIZ
print(matriz.shape) # (2, 3) => MUESTRA LAS FILAS Y COLUMNAS (FILAS, COLUMNAS)
print(matriz.size) # 6 => CUENTA CUANTOS ELEMENTOS HAY

# CONCATENAR DOS MATRICES

m1 = np.array([[1, 2, 3], [1, 2, 3]])
m2 = np.array([[4, 5, 6], [7, 8, 9]])

print(np.concatenate((m1, m2), axis=0))


# EJERCICIOS

# 1. Crear un arreglo de dos dimensiones de tamaño 3 x 3, con elementos aleatorios de números enteros del 0 al 100.

lista1 = []
lista2 = []
lista3 = []

for i in range(3):
    lista1.append(random.randint(0,100))
    lista2.append(random.randint(0,100))
    lista3.append(random.randint(0,100))



array = np.array([[lista1], [lista2], [lista3]])
print(array)

# 2. Utilice las siguientes funciones en el arreglo creado en el punto 1

#   • Promedio de los elementos.
#   • Suma de los elementos.
#   • Mostrar el elemento mayor.
#   • Mostrar el elemento menor.
#   • Mostrar sólo los elementos de la diagonal principal.

print(f"""Elemento Mayor: {array.max()} 
Elemento Menor: {array.min()}
Suma de los Elemento: {array.sum()} 
Promedio de los elementos: {array.mean()}
Elementos del array: {array}
Elementos en diagonal: {array.diagonal()}
""")

# 3. Crear un arreglo de dos dimensiones de 3 x 3 con números ceros,
# excepto la diagonal principal que debe contener en el mismo orden los
# siguientes elementos 1, 2 y 3.

matriz = np.diag([1, 2, 3])
print(matriz)