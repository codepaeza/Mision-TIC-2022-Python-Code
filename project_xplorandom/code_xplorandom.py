import pandas as pd
from firebase import firebase

#Lee el archivo excel base xplorandom.xlsx y lo asigna a un DataFrame
xplorandom=pd.ExcelFile('D:\Mi nuevo camino/bd_xplorandom/estructura_info.xlsx') #Tener cuidado con las formas\literal, ya que pueden generar error para Python
df=pd.read_excel(xplorandom,'xplorandom',usecols=['Id', 'Pais', 'Departamento', 'Ciudad',
 'Razon', 'Direccion', 'TelefonoFijo', 'Celular', 'Whatsapp', 'email', 'facebook', 'instagram',
  'twitter', 'tiktok', 'SectorCadena', 'Plan', 'CantidadPersonas', 'DetallePlan', 'Precio','Dia',
   'HoraInicio', 'HoraFin', 'Edad'], dtype={"Celular":str}) #(variable de la ruta, Nombrn("https://events-e3ea4-default-rtdb.firebaseio.com/",None) #Conecta con la base de datos en Firebase
#precio=df.loc[df['Precio']<=5000]
#print(precio)

#Evalúa la condición de planes meores o iguales a $5.000
menor_cinco_lucas=df.loc[lambda df:df['Precio']<=5000,:]
print(menor_cinco_lucas)

#Evalúa la condición de planes meores o iguales a $10.000
menor_diez_lucas=df.loc[lambda df:df['Precio']<=10000,:]
print(menor_diez_lucas)

#Evalúa la condición de planes meores o iguales a $20.000
menor_veinte_lucas=df.loc[lambda df:df['Precio']<=20000,:]
print(menor_veinte_lucas)

#Evalúa la condición de planes meores o iguales a $50.000
menor_cincuenta_lucas=df.loc[lambda df:df['Precio']<=50000,:]
print(menor_cincuenta_lucas)

#Evalúa la condición de planes meores o iguales a $100.000
menor_cien_lucas=df.loc[lambda df:df['Precio']<=100000,:]
print(menor_cien_lucas)

#Evalúa la condición de planes meores o iguales a $200.000
menor_doscientas_lucas=df.loc[lambda df:df['Precio']<=200000,:]
print(menor_doscientas_lucas)

#Evalúa la condición de planes meores o iguales a $300.000
menor_trescientas_lucas=df.loc[lambda df:df['Precio']<=300000,:]
print(menor_trescientas_lucas)

#Evalúa la condición de planes meores o iguales a $400.000
menor_cuatrocientas_lucas=df.loc[lambda df:df['Precio']<=400000,:]
print(menor_cuatrocientas_lucas)

#Evalúa la condición de planes meores o iguales a $500.000
menor_quinientas_lucas=df.loc[lambda df:df['Precio']<=500000,:]
print(menor_quinientas_lucas)

#Evalúa la condición de planes meores o iguales a $600.000
menor_seiscientas_lucas=df.loc[lambda df:df['Precio']<=600000,:]
print(menor_seiscientas_lucas)

#Evalúa la condición de planes meores o iguales a $700.000
menor_setecientas_lucas=df.loc[lambda df:df['Precio']<=700000,:]
print(menor_setecientas_lucas)

#Evalúa la condición de planes meores o iguales a $800.000
menor_ochocientas_lucas=df.loc[lambda df:df['Precio']<=800000,:]
print(menor_ochocientas_lucas)

#Evalúa la condición de planes meores o iguales a $900.000
menor_novecientas_lucas=df.loc[lambda df:df['Precio']<=900000,:]
print(menor_novecientas_lucas)

#Evalúa la condición de planes meores o iguales a $1.000.000
menor_unmillon_lucas=df.loc[lambda df:df['Precio']<=1000000,:]
print(menor_unmillon_lucas)

#precio=df['Precio']
#print(precio)

#Establece la conexión con la bases de datos en Firebase
firebase=firebase.FirebaseApplication("https://xplorandom-default-rtdb.firebaseio.com/",None)

#Asigna a la varable data el DataFrame y lo convierte a JSON
data5=menor_cinco_lucas.to_json(orient='records')
data10=menor_diez_lucas.to_json(orient='records')
data20=menor_veinte_lucas.to_json(orient='records')
data50=menor_cincuenta_lucas.to_json(orient='records')
data100=menor_cien_lucas.to_json(orient='records')
data200=menor_doscientas_lucas.to_json(orient='records')
data300=menor_trescientas_lucas.to_json(orient='records')
data400=menor_cuatrocientas_lucas.to_json(orient='records')
data500=menor_doscientas_lucas.to_json(orient='records')
data600=menor_seiscientas_lucas.to_json(orient='records')
data700=menor_setecientas_lucas.to_json(orient='records')
data800=menor_ochocientas_lucas.to_json(orient='records')
data900=menor_novecientas_lucas.to_json(orient='records')
data1000=menor_unmillon_lucas.to_json(orient='records')

#Envía a la base de datos Firebase el objeto girardot con el archivo JSON de la tabla asignada al DataFrame
result5=firebase.post('/girardot5',data5)#Envia el JSON a la base de datos en Firebase
result10=firebase.post('/girardot10',data10)
result20=firebase.post('/girardot20',data20)
result50=firebase.post('girardot50',data50)
result100=firebase.post('/girardot100',data100)
result200=firebase.post('/girardot200',data200)
result300=firebase.post('/girardot300',data300)
result400=firebase.post('/girardot400',data400)
result500=firebase.post('(girardot500',data500)
result600=firebase.post('/girardot600',data600)
result700=firebase.post('/girardot700',data700)
result800=firebase.post('/girardot800',data800)
result900=firebase.post('/girardot900',data900)
result1000=firebase.post('/girardot1000',data1000)


print(result5) #Muestra el registro 
print(result10)
print(result20)
print(result50)
print(result100)
print(result200)
print(result300)
print(result400)
print(result500)
print(result600)
print(result700)
print(result800)
print(result900)
print(result1000)



""""
import openpyxl
excel_document=openpyxl.load_workbook('D:\Mi nuevo camino/bd_xplorandom/estructura_info.xlsx')
print (type(excel_document)) #Resultado: <class 'openpyxl.workbook.workbook.Workbook'>
print(excel_document.get_sheet_names()) #Resultado: ['xplorandom']

#Accediendo a las celdas en el libro
dato=excel_document.get_sheet_by_name('xplorandom')
print(dato['R4'].value)
"""
"""
import sys
from openpyxl import workbook
from xlrd import open_workbook
archivo=open_workbook('D:\Mi nuevo camino/bd_xplorandom/estructura_info.xlsx')
print("Número de hojas: ",workbook.nsheets)
"""