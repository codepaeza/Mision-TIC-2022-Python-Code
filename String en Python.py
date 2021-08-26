#Práctica de tratamiento de String en Python

fruta="fresa" #la palabra fresa tiene [0 1 2 3 4] posiciones de caracter
letra=fruta[0] #Selecciona el caracter en posición 0 - Letra f
print(letra)

#Uso de función len() para obtener la longitud de una cadena
palabra="esternocleidomastoideo"
longitud=len(palabra)
print(longitud) #El resultado para esta función es 22-Pero se debe recordar que los indices de caracteres van de 0 a 21

#Obtener el último caracter de palabra
ultimo=palabra[longitud-1]
print(ultimo)

#Obtener segmentos de cadenas de texto
nombre="Edwin Páez Alonso"
largo=len(nombre)
print(largo)
nom1=nombre[0:5]  #La función tiene la forma [n,m) incluyendo el primero pero excluyendo el último,por esto se debe sumar uno al final
ape1=nombre[6:10]
ape2=nombre[11:17]

nom2=nombre[:11] #Dejando el primer indice vacío y marcando el final, la función toma la cadena desde el comienzo (indce 0) hasta el indice definido
ape3=nombre[6:] ##Dejando el último indice vacío y marcando el inicial, la función toma la cadena desde el definido hasta el indice final

print(nom1)
print(ape1)
print(ape2)
print(nom2)
print(ape3)

#Ciclos con Strings

prefijos="JKLMNOPQ"
sufijo="ack"

for letra in prefijos:
    print(letra + sufijo)

#Ordenamiento de palabras comparación por orden alfabético
palab=input("Escriba una fruta:")
if palab=="banana":
    print("La fruta es una banana")
else:
    print("La fruta es diferente a banana")


palab1=input("Ingrese una palabra:")
if palab1<"banana":
    print("Su palabra " +palab1+ " va antes que banana")
elif palab1>"banana":
    print("Su palabra "+palab1+" va después de banana")
else:
    print("No hay información de donde está su palabra") #Es importante saber que en Python las mayúsculas van primero

#Cambios en cadenas
cadena="Hola Mundo"
print(cadena)

nuevaCadena="Nuevo "+cadena[5:]
print(nuevaCadena)

#Buscar carateres en una cadena

def buscar(cad, c):
    indice=0
    while indice<len(cad):
        if cad[indice]==c:
            print("El indice número: "+str(indice)+" es la letra buscada")
        else:
            print("El índice número: "+str(indice)+" y no corresponde a la letra buscada")
        indice=indice+1
buscar("morales", "o")

#Cambio minúsculas a mayúsculas

palabra1="Edwin"
print(palabra1)
palabra1Mayuscula=palabra1.upper()
print(palabra1Mayuscula)

#Cambio mayúsculas a minúsculas

palabra2="PAEZ"
print(palabra2)
palabra2Minuscula=palabra2.lower()
print(palabra2Minuscula)

#Búsqueda de una cadena dentro de otra
cadena1="palabra"
cadena2="br"
index=cadena1.find(cadena2)
print(index)





