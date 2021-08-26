#Reto 1 Grupo 60 UTP - CC 79742331

#Cálculo de Área y Perímetro Terreno Centro Comercial

# La variable a es la longitud de un lado del terreno (en metros)

a=float(input("Ingrese la longitud del lado a e metros: "))

b= 2 * a

print("a=",a)
print("b=",b)

#La forma del terreno se compone de cuatro bloques:

# El bloque 1 es un rectángulo de dimensiones a y b
area1=a*b
print("El área del rectángulo 1 es: ",area1)

perimetro1=(2*a)+(2*b)
print("El perímetro del rectángulo 1 es: ",perimetro1)

# El bloque 2 es un rectángulo de dimensiones b y a
area2=b*a
print("El área del rectángulo 2 es: ",area2)

perimetro2=(2*b)+(2*a)
print("El perímetro del rectángulo 2 es: ",perimetro2)

# El bloque 3 es un cuadrado de dimensiones a y a
area3=a*a
print("El área del rectángulo 3 es: ",area3)

perimetro3=4*a
print("El perímetro del rectángulo 3 es: ",perimetro3)

# El bloque 4 es un rectángulo de dimensiones b y a
area4=b*a
print("El área del rectángulo 4 es: ",area4)

perimetro4=(2*b)+(2*a)
print("El perímetro del rectángulo 4 es: ",perimetro4)


#Se calcula el área total del terreno:
areaTerreno= area1 + area2 + area3 + area4
print("El área total del terreno es: ",areaTerreno)

#Se calcula el perímetro del terreno:
perimetroTerreno= (perimetro1-a) + (perimetro2-(2*(b/2))) + (perimetro3-(2*a)) + (perimetro4-(b/2))
print("El perímetro total del terreno es: ",perimetroTerreno)