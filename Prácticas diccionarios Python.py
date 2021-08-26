#Prácticas diccionarios Python

#Definición básica diccionario con llaves{}
diccionario={"total":55, "elemento": "poste"}

print(diccionario)


#Definición básica de diccionario con funcion dict()
diccionario1=dict(total=120, elemento="aisladores")

print(diccionario1)


#Diccionario dentro de otro diccionario
usuario = {
    'nombre': 'Edwin Páez Alonso',
    'edad' : 44, 
    'curso': 'Curso de Python',
    'skills':{
        'programacion' : True,
        'base_de_datos': False
    },
    'No medallas' : 1
}

print(usuario)
print(usuario['nombre'])
print(usuario['curso'])
print(usuario['skills'])
print(usuario['skills']['base_de_datos'])
