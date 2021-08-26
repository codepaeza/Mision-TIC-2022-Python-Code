"""
class Empleado:

    #Define el metodo inicial (constructor)

    def __init__(self):
        self.nombre=input("Escriba el nombre: ")
        self.sueldo=float(input("Ingrese el suledo: "))
    def imprimir(self):
        print("Nombre: ", self.nombre)
        print("Suledo:", self.sueldo)
    def paga_impuestos(self):
        if self.sueldo>3000:
            print("Debe pagar impuestos")
        else:
            print("No debe pagar impuestos")


empleado1 = Empleado()  #Instancia, declarar la variable "empleado1" como tipo "clase".
empleado1.imprimir()
empleado1.paga_impuestos()
"""
#Calcula la potencia eléctrica consumida a partir de la cantidad de fases y las mediciones
# de corriente y voltaje

#Misión TIC 2022 - UTP Grupo 60
#Edwin Páez Alonso

class potenciaConsumida:

    def __init__(self):
        self.fases=int(input("Ingrese la cantidad de fases: "))
        self.corriente=float(input("Ingrese la corriente medida en Amperios: "))
        self.voltaje=float(input("Ingrese el voltaje medido en Voltios: "))

    def calculaPotencia(self):
        if self.fases==1:
           potencia=round(float(self.corriente*self.voltaje),1)
           print("La potencia consumida monofásica es: "+str(potencia)+" Wattios")

        if self.fases==2:
           potencia=round(float(self.corriente*self.voltaje),1)
           print("La potencia consumida bifásica es: "+str(potencia)+" Wattios")

        if self.fases==3:
            potencia=round(float((3**1/2)*self.corriente*self.voltaje),1)
            print("La potencia consumida trifásica es: "+str(potencia)+" Wattios")
        if self.fases>3:
            print("La cantidad de fases no es válida")


potenciaConsumida1=potenciaConsumida()
potenciaConsumida1.calculaPotencia()