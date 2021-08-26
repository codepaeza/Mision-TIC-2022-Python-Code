#Reto 1 Grupo 60 UTP - Edwin Páez Alonso - CC 79742331

#Cálculo de Área y Perímetro Terreno Centro Comercial


def Logica(lado):  #Calcula el área y perímetro de un terreno en forma de triángulo equilátero

  perimetroTerreno=round((lado*3),4) #Formula para el calculo del perímetro de un terreno de forma triángulo equilátero
  hTerreno=round((((3**0.5)*(lado))/2),4)  #Formula para el cálculo de la altura de un terreno de forma triángulo equilátero 
  areaTerreno=round(((lado*hTerreno)/2),4)#Formula para el cálculo del área de un terreno de forma triángulo equilátero 
  return(" El perímetro del terreno es: " + str(perimetroTerreno) + " kilómetros, y su área de: " + str(areaTerreno))

 
Logica(1.25)
Logica(33.25)
Logica(254.256)


    
"""
#Ejemplos salidas:

lado=1.25  #El perímetro del terreno es: 3.75 kilómetros, y su área de: 0.6051
lado=33.25 #El perímetro del terreno es: 99.75 kilómetros, y su área de: 83.0203
lado=254.256 #El perímetro del terreno es: 762.768 kilómetros, y su área de: 1755.5233 
"""
