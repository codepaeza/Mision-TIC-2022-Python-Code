var1=10
var2=35
var3=46
var4=67
var5=156
maximo=max(var1,var2,var3,var4,var5)
print(maximo)

minimo=min(var1,var2,var3,var4,var5)
print(minimo)

x=range(5)
print(x)

y=len(x)
print(y)

#Creación de Funciones

def imprimeCosas(x):
    cadenaUno="Mi nombre es:"
    cadenaDos="Edwin Páez Alonso"
    semana=x
    universidad="UTP"
    print(cadenaUno)
    print(cadenaDos+" y estoy cursando la semana:"+str(semana)+" en la "+universidad)

imprimeCosas(1)
imprimeCosas(2)
imprimeCosas(3)
  
#Función suma

def suma(a,b):
    resultado=a+b
    print(resultado)
suma(23,45)
suma(2,6)
suma(12,9)
suma(3,8)


def prince_twice(nombre):
    print(nombre)
    print(nombre)
    print(nombre)
prince_twice("Edwin")
prince_twice("Carlos")
prince_twice("Alberto")

#Cálulo de distancia básico
print("---Programa para Calcular la Distancia Recorrida---")
velocidad=float(input("Ingrese la velocidad en m/s: "))
tiempo=float(input("Ingrese el tiempo que tardó el desplazamiento en segundos: "))

distancia=velocidad*tiempo
print("La distancia recorrida es: "+ str(distancia)+" metros")

#Cálculo de distancia utilizando función
print("Cálculo de distancia utilizando la definición de función en Python")

def calculaDistancia(veloc,tiem):
    distan=veloc*tiem
    print(distan)

calculaDistancia(6,4)
calculaDistancia(45,31)


#Uso de condicionales y control de flujo
x=-52

if x>0:
    print("x es un número positivo")
elif x==0:
    print("x es igual a cero")
else:
    print("x es un número negativo")


#Condicionales anidadas
y=45

if x==y:
    print("x y y son iguales")
else:
    if x<y:
        print("x es menor que y")
    else:
        print("x es mayor que y")



#Decisiones anidadas ó en cascada

num=int(input("Ingrese un número entero:"))

if num<0:
    num=num*(-1)
 
if num>=1 and num<=9:
    print("El número tiene un dígito")
else:
    if num>=10 and num<=99:
        print("El número tiene dos dígitos")
    else:
        if num>=100 and num<=999:
            print("El número tiene tres dígitos")
        else:
            if num>=1000 and num<=9999:
                print("El número tiene cuatro dígitos")
            else:
               if num>=10000:
                   print("El número tiene 5 o más digitos")


#Decisiones en cascada utilizando elif

num=int(input("Ingrese un número entero:"))

if num<0:
    num=num*(-1)
 
if num>=1 and num<=9:
    print("El número tiene un dígito")
elif num>=10 and num<=99:
        print("El número tiene dos dígitos")
elif num>=100 and num<=999:
        print("El número tiene tres dígitos")
elif num>=1000 and num<=9999:
        print("El número tiene cuatro dígitos")
else:
        print("El número tiene 5 o más digitos")
    

#Try y Except

temperatura_farh=input("Escriba la temperatura en grados °F:")
try:
    farh=float(temperatura_farh)
    cel=(farh-32.0)*5.0/9.0
    print(cel)
except:
    print("Por favor ingrese un número con decimales")


    #


