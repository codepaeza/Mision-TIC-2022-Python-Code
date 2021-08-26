#Cargar 5 nombres de personas y sus edades respectivas.
#Luego de realizar la carga por teclado de todos los datos, imprimir los nombres 
#de las personas mayores de edad (mayores o iguales a 18 años).
"""
nombres = []
edades= []

for x in range(5):
    nom=input('Ingrese el nombre de la persona: ')
    nombres.append(nom)
    print(nombres)
    ed=int(input('Ingrese la edad: '))
    edades.append(ed)
    print(edades)
print('Monbre de las personas mayores de edad: ')

for x in range(5):
    if edades[x]>=18:
        print(nombres[x])
"""

#Listas Compuestas
lista=[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
print(lista) #Imprime la lista completa
print(lista[0]) #Imprime la primera sublista
print(lista[2][1]) #Imprime el indice 1 (segunda posicion) de la tercera lista (indice 2)

#Para acceder a cada sublista
for f in range(len(lista)):
    print(lista[f])


#Para acceder a cada lista y cada elemento
for f in range(len(lista)):
    for c in range(len(lista[f])):
        print(lista[f][c])


print('-------Ejemplo 1-------')
array=[[21,22,23],[24,25,26],[27,28,29],[30,31,32]]
print(array) #Imprime la lista completa
print(array[0]) #Imprime el índice 0 de la lista
print(array[0][0]) #Imprime el primer componente de la primera sublista

for x in range(len(array[1])):
    print(array[1][x]) # Imprime las componentes de la segunda sublista(indice 1)
    

