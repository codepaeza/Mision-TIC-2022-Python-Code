#Reto 5 Edwin Páez Alonso - Misión TIC 2022 Grupo 60 UTP

import pandas as pd

rutaArchivo= 'https://github.com/luisguillermomolero/MisionTIC2022/blob/3f3847bbf2dbe4b2cf4dcceb96a455d92c88f9c5/movies.csv?raw=true'

def listaPeliculas(rutaArchivo:str)->str:
    if rutaArchivo.split('.')[-1]!='csv':
        try:
            csv=pd.read_csv(rutaArchivo)

            columnas= pd.read_csv(rutaArchivo, usecols=[1,2,3,4,5,6,7])

            csv["Net Earnings"]=csv["Gross Earnings"]- csv["Budget"]

            ordenaListaPeliculas= csv[['Net Earnings']].sort_values(['Net Earnings'], ascending=[False])
            print(ordenaListaPeliculas)
        except:
            print('Error al leer el archivo de datos.')
    else:
        print('Extensión inválida.')
    return
print(listaPeliculas(rutaArchivo))
