#Prácticas de lenguaje Python

#Variables
var= "3.7.1"
print("La versión de Python es: ",var)
print("La versión de Python es: " + var)


#Python trata el signo = no como igual a, sino como asigna un valor
var1=1
print(var1)
var1=var1+1
print(var1)

#Cálculo Teorema de Pitágoras
a=5
b=10
c=(a**2+b**2)**0.5
print("c=: ",c)

a=float(input("Ingrese valor lado a:"))
b=float(input("Ingrese valor lado b:"))
c=(a**2+b**2)**0.5
print("La hipotenusa c es: ",c)


#Pruebas variables
juan=3
maria=5
adan=6

print("Juan tiene",juan, "manzanas")
print("Maria tiene",maria, "manzanas")
print("Adan tiene", adan, "manzanas")
print(juan,",",maria,",",adan)
totalManzanas=juan+maria+adan
print("En total tienen",totalManzanas,"manzanas")


#Ejercicios Unidad 2
#Ejercicio1: Leer un número entero y determinar si termina en 4

numero1=int(input("Ingrese un número entero: "))
numero1_4=numero1-4
numero1str=str(numero1_4)
print(numero1str)
cadenaNum1=[numero1str]
num4=numero1str[-1]
print(num4)

if num4=="0":
    print("El número termina en 4")
else:
    print("El número no termina en 4")

#Ejercicio2: Leer un número entero y determinar si tiene tres dígitos

numero2=int(input(("Ingrese un número entero para validar si tiene tres dígitos")))
numero2Str=str(numero2)
print(numero2Str)
num2Lon=len(numero2Str)
print(num2Lon)

if num2Lon==3:
    print("El número entero tiene tres dígitos")
else:
    print("El número entero no tiene tres dígitos")





