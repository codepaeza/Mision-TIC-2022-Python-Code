#Ejercicios en Python - Semana 2

#1.	Leer un número entero y determinar si es un número terminado en 4

numero=int(input("Ingrese número para evaluar si termina en 4: ")) #Entrada de teclado de número a evaluar
cadena=str(numero)
c=len(cadena)
print("El número ingresado tiene: "+str(c)+" dígitos")

ultimo=cadena[c-1]
print("El último digito del número ingresado es: "+ultimo)

if ultimo=="4":
    print("El número: "+cadena+" termina en 4")
else:
    print("El número: "+cadena+" no termina en 4")


#2.	Leer un número entero y determinar si tiene 3 dígitos.
num=int(input("Ingrese un número entero de tres dígitos: "))
cad=str(num)
lon=len(cad)

if lon=="3":
    print("El número ingresado tiene tres dígitos")
else:
    print("Intente de nuevo, el número NO tiene tres dígitos")

