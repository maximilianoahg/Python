#                               -- Listas --



# la imagen muestra que en cada caja podemos guardar un valor, sea este una variable númerica, cadenas de caracteres, incluso una lista.abs

# lista = [1, 'Hola', 3.67, [1, 2, 3]]

# Se asemejan bastante a los Arrays, so consideramos otros lenguajes de programacion.
# Si necesitamos incluir más de un valor dentro de la lista, sólo los separamos por una coma.abs

# listas = [1, 2, 3, 4]

# -- Crear Listas --

# nombre_lista = []

# nombre_lista --> NOMBRE DE LA LISTA
# [] --> ESTOS PARÉNTESIS DE CORCHETE INDICAN QUE ES UNA LISTA





#                               -- Elementos de una lista --



# El ejemplo muestra que posee 3 elementos y que para acceder a ellos, solo se utiliza un índice

# a = [12, 'Python', 3.1416]

# print(a[0]) #[12]       -->  El elemento 1 está en la posición 0
# print(a[1]) #[Python]   -->  El elemento 2 esta en la posicion 1
# print(a[2]) #[3.1416]   -->  El elemento 3 esta en la posicion 2

# Para acceder al último elemento de la lista, sólo se utiliza el índice -1

# a = [90, 'Python', 3.87]

# print(a[-1]) #[3.87]   -->  Accede al ultimo elemento de la lista


# -----------------------------------------------------------------

#                     --|| Append(<obj>) ||--

# El metodo .Append() permite agregar elementos al final de la lista

# lista = [1, 2]
# lista.append(3)
# print(lista) # -> [1, 2, 3, 4]

# -----------------------------------------------------------------

#                    --||Extend(<iterable>)||--

# El metodo extend() permite añadir una lista a una lista inicial

# lista = [1, 2]
# lista.extend([3,4])
# print(lista) # -> [1, 2, 3, 4]

# -----------------------------------------------------------------

#                  --||Insert(<index>, <obj>)||--

# El metodo insert() permite añadir un elemento en una posicion determinada

# lista = [1, 3]
# lista.insert(1, 2)
# print(lista) -> [1, 2, 3]

# -----------------------------------------------------------------

#                         --||Pop()||--

# El metodo .pop() elimina el ultimo elemento de la lista

# lista = [1, 2, 3]
# lista.pop()
# print(lista) # -> [1, 2]

#                       --||Pop(<index>)||--

# El metodo .pop(<index>) elimina el elemento que se encuentra en la posicion ingresada

# lista = [1, 2, 3]
# lista.pop(1)
# print(lista) # -> [1, 3]

# -----------------------------------------------------------------

#                        --||Reverse()||--

# El metodo .reverse() permite invertir el orden de la lista

# lista = [1, 2, 3]
# lista.reverse()
# print(lista) # -> [3, 2, 1]

# -----------------------------------------------------------------

#                         --||Sort()||--

# El metodo .sort() permite ordenar los elementos de menor a mayor

# lista = [3, 2, 1]
# lista.sort()
# print(lista) # -> [1, 2, 3]

# El metodo .sort tambien permite ordenar los elementos de mayor a menor

# lista = [3, 1, 2]
# lista.sort(reverse=True)
# print(lista) # -> [1, 2, 3]

# -----------------------------------------------------------------



# -----------------------------------------------------------------
# |                       ACTIVIDAD 1                             |
# |                                                               |
# |     Investiga con tus compañeros sobre otras operaciones      |
# |                     con las listas                            |
# -----------------------------------------------------------------

#                 --||Tamaño de la lista||--

# lista = [1, 2, 3]
# print(len(lista)) # -> 3


#                   --||Copiar una lista||--

# lista1 = ['Maximiliano','Hernandez']
# lista2 = lista1.copy()
# print(lista2) # -> ['Maximiliano','Hernandez']  