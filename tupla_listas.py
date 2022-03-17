#Las tuplas son elementos inmtables, no se les puede añadir nuevos elementos.
"""
t1 = (5.24,) # tupla de un solo elemento
t2 = (3.67, 'hola', 4, True)
t3 = (t2, 4, False) # tupla como elemento de otra tupla
t4 = t3 + t2 # concatenación
#print(t4)
#print(t4[2]) # indexación
#print(t4[0])
#print(t4[2:4]) # segmentación
"""

#Estamos modificando una tupla, pero tomando el valor antes dado y almacenandolo otra vez en la misma variable tupla.
"""
tup = (4, 'free', 8.4)
name = 'Fernando'

# intento incorrecto de modificación de una tupla y una cadena
#tup[1] = 'locked'
#name[4] = '-'

# forma correcta
tup = tup[0:2] + (7,) #Indexamos hasta el elemento 2, y le contatenamos la tupla (7,)
name = name[:4] + '-' + name[5:] # Indexamos ambos valores y los contatenamos.
print(tup, name)
"""

#En las listas, los elementos se pueden modificar, ademas se les puede añadir.
"""
list1 = [9]
list2 = [4, 'free', 8.4]
list3 = [list2, True]
list4 = list3 + [4, -7.8]
print(list4)
list2[1] = 6.34  # indexación de un elemento para modificar su valor
print(list4[2])
print(list4[0])
print(list4[2:4])
"""

#Listas y su conjunto de metodos.

list_1 = [1, 6, 7, 8, 9, 12, 11, 10, 6, 13, 6,]
list_2 = [21, 25, 26]

list_1.append(5) #Agrega el objeto al final de la lista.
print(list_1)

x = list_1.count(6) #Rotorna el número de veces que el objeto se encuetra en la lista.
print(x)

list_1.insert(2, 3), #Inserta el objeto 3, en la posición 2 de la lista.
print(list_1)

list_1.extend(list_2) #Agrega todos los elementos al final de la lista.
print(list_1)

list_1.remove(6) #Borra el primer elemento 6 que encuentre.
print(list_1)

list_1.index(6) #Retorna la posición del primer elemento 6 que encuentre.
print(list_1)

list_1.pop(2) #Borra el elemento de la posición 2.
print(list_1)

list_1.sort() #Ordena la lista.
print(list_1)

list_1.reverse() #Invierte el orden de la lista.
print(list_1)