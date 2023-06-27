# ° Para crear un arreglo o un vector en Python usamos la funcion Array() de la biblioteca Numpy.

import numpy as np # ESTA LINEA NO HAY QUE COMENTARLA
import random 





#       -- ¿Qué es un Arreglo en programación? --

# ° Es un conjunto de datos que se almacenan temporalmente, además, cumplen con ciertas características, tales como:

#   - Colección finita
#   - Homogénea
#   - Elementos Ordenados

# ° Recibe varios nombres, entre ellos:

#   - Vector
#   - Array
#   - Matriz





#       -- DECLARAR UN ARREGLO --

#   Para declarar un arreglo podemos hacer lo siguiente: 


arreglo = np.array([1, 3, 5, 7])

print(f"""Arreglo = {arreglo}
Dimensiones del Arreglo = {arreglo.ndim}
Largo del Arreglo = {len(arreglo)}
Estructura de la dimension del Arreglo = {arreglo.shape}
Elementos en el intervalo [1:3] (DESDE LA POSICION 1 HASTA ANTES DE LA POSICION 3) = {arreglo[1:3]} 
Elementos en el intervalo [1:3:2] (DESDE LA POSICION 1 HASTA ANTES DE LA POSICION 3, DE 2 EN 2)= {arreglo[1:3:2]}
Elementos en el intervalo [::2] (DESDE LA POSICION 0 HASTA EL FINAL, DE 2 EN 2)= {arreglo[::2]}
Elementos en el intervalo [2::2] (DESDE LA POSICION 2 HASTA EL FINAL, DE 1 EN 1)= {arreglo[2::1]}
Elementos en el intervalo [-2] = {arreglo[-2]}
""")

#   Otras funciones:

# ESTE CREA UN ARRAY DESDE EL O AL 4

c = [i for i in range(0,5)] 
print(c) # [0, 1, 2, 3, 4]

# MUESTRA LOS ELEMENTOS DEL ARREGLO UTILIZANDO CICLO FOR
for i in range(len(arreglo)):
    print(arreglo[i]) # 1 3 5 7

# SE CREA ARREGLO CON 4 ELEMENTOS ENTEROS
print(np.arange(4)) # [0, 1, 2, 3]

# SE CREA ARREGLO CON ELEMENTOS ENTRE 4 Y EL 7, CON UN INTERVALO DE 1 Y SE EXCLUYE EL ULTIMO ELEMENTO
print(np.arange(4,7)) # [4, 5, 6]

# SE CREA ARREGLO CON 4 ELEMENTOS DECIMALES
print(np.arange(4.0)) # [0., 1., 2., 3.]

# SE CREA ARREGLO CON ELEMENTOS ENTRE 3 Y EL 7, CON UN INTERVALO DE 2 Y SE EXCLUYE EL ULTIMO ELEMENTO
print(np.arange(3,7,2)) # [3, 5]





#       -- Copia de arreglos --

# CASO 1:
# Genera la copia del arreglo1 en arreglo2, sin embargo, al realizar cambios en el arreglo original, éstos se pantienen en el segundo arreglo

arreglo1 = np.array([1, 2, 3])
arreglo2 = arreglo1[:]
print(arreglo2) # [1 2 3]
arreglo2[0] = 100
print(arreglo1) # [100 2 3]
print(arreglo2) # [100 2 3]

# CASO 2:
# Genera la copia del arreglo1 en arreglo2,sin embargo lo fuerza con la función copy,de esta forma los cambios sólo se reflejanen el arreglo original

arreglo3 = np.array([1, 2, 3])
arreglo4 = arreglo3[:].copy
print(arreglo4) # [1 2 3]
arreglo2[0] = 100
print(arreglo3) # # [100 2 3]
print(arreglo4) # [1 2 3]


# ACTIVIDAD 2

# 1.1
# Crear un arreglo unidimensional de tamaño 10, conelementos aleatorios de números enteros del 0 al 100,
# paraello deberá investigar la función que permita crear númerosaleatorios


lista = []

for i in range(10):
    lista.append(random.randint(1, 100))

array = np.array(lista)
print(array)

# 1.2
# Crear una copia del arreglo y muestre:

#   - Elemento mayoro Elemento menor
#   - Suma de los elementos
#   - Promedio de los elementos
#   - Mostrar todos los elementos

array2 = array[:]

print(f"""Elemento Mayor: {array2.max()} 
Elemento Menor: {array2.min()}
Suma de los Elemento: {array2.sum()} 
Promedio de los elementos: {array2.mean()}
Elementos del array: {array2}
""")