#Reto 2 - Edwin Páez Alonso
#UTP - Grupo 60

def gananciasVentas(Productos:dict)-> dict:
    
    pass
    if Productos['dProducto']=='Camisa':

        if (Productos['tProducto']=='S' or Productos['tProducto']=='s') and 0<=Productos['vArticulo']<=100000:
            cProducto=round(float(Productos['vArticulo']*0.05),2)
            gServicios=round(float(Productos['vArticulo']*0.15),2)
            rCompra=round(float(Productos['vArticulo']*0.40),2)
            
        elif (Productos['tProducto']=='S' or Productos['tProducto']=='s') and 101000<=Productos['vArticulo']<=180000:
            cProducto=round(float(Productos['vArticulo']*0.08),2)
            gServicios=round(float(Productos['vArticulo']*0.15),2)
            rCompra=round(float(Productos['vArticulo']*0.40),2)
           
        elif (Productos['tProducto']=='S' or Productos['tProducto']=='s') and 181000<=Productos['vArticulo']<=230000:
            cProducto=round(float(Productos['vArticulo']*0.11),2)
            gServicios=round(float(Productos['vArticulo']*0.15),2)
            rCompra=round(float(Productos['vArticulo']*0.40),2)
            
        elif (Productos['tProducto']=='M' or Productos['tProducto']=='m') and 0<=Productos['vArticulo']<=100000:
             cProducto=round(float(Productos['vArticulo']*0.05),2)
             gServicios=round(float(Productos['vArticulo']*0.15),2)
             rCompra=round(float(Productos['vArticulo']*0.40),2)
            
        elif (Productos['tProducto']=='M' or Productos['tProducto']=='m') and 101000<=Productos['vArticulo']<=180000:
             cProducto=round(float(Productos['vArticulo']*0.08),2)
             gServicios=round(float(Productos['vArticulo']*0.15),2)
             rCompra=round(float(Productos['vArticulo']*0.40),2)
            
        elif (Productos['tProducto']=='M' or Productos['tProducto']=='m') and 181000<=Productos['vArticulo']<=230000:
             cProducto=round(float(Productos['vArticulo']*0.11),2)
             gServicios=round(float(Productos['vArticulo']*0.15),2)
             rCompra=round(float(Productos['vArticulo']*0.40),2)
            
        elif (Productos['tProducto']=='L' or Productos['tProducto']=='l') and 0<=Productos['vArticulo']<=100000:
             cProducto=round(float(Productos['vArticulo']*0.05),2)
             gServicios=round(float(Productos['vArticulo']*0.15),2)
             rCompra=round(float(Productos['vArticulo']*0.40),2)
            
        elif (Productos['tProducto']=='L' or Productos['tProducto']=='l') and 101000<=Productos['vArticulo']<=180000:
             cProducto=round(float(Productos['vArticulo']*0.08),2)
             gServicios=round(float(Productos['vArticulo']*0.15),2)
             rCompra=round(float(Productos['vArticulo']*0.40),2)
            
        elif (Productos['tProducto']=='L' or Productos['tProducto']=='l') and 181000<=Productos['vArticulo']<=230000:
             cProducto=round(float(Productos['vArticulo']*0.11),2)
             gServicios=round(float(Productos['vArticulo']*0.15),2)
             rCompra=round(float(Productos['vArticulo']*0.40),2)
                 
    if Productos['dProducto']=='Pantalon':
        if (Productos['tProducto']=='S' or Productos['tProducto']=='s') and 0<=Productos['vArticulo']<=100000:
            cProducto=round(float(Productos['vArticulo']*0.06),2)
            gServicios=round(float(Productos['vArticulo']*0.25),2)
            rCompra=round(float(Productos['vArticulo']*0.50),2)
            
        elif (Productos['tProducto']=='S' or Productos['tProducto']=='s') and 101000<=Productos['vArticulo']<=180000:
            cProducto=round(float(Productos['vArticulo']*0.09),2)
            gServicios=round(float(Productos['vArticulo']*0.25),2)
            rCompra=round(float(Productos['vArticulo']*0.50),2)
            
        elif (Productos['tProducto']=='S' or Productos['tProducto']=='s') and 181000<=Productos['vArticulo']<=230000:
            cProducto=round(float(Productos['vArticulo']*0.12),2)
            gServicios=round(float(Productos['vArticulo']*0.25),2)
            rCompra=round(float(Productos['vArticulo']*0.50),2)
                       
        elif (Productos['tProducto']=='M' or Productos['tProducto']=='m') and 0<=Productos['vArticulo']<=100000:
            cProducto=round(float(Productos['vArticulo']*0.06),2)
            gServicios=round(float(Productos['vArticulo']*0.25),2)
            rCompra=round(float(Productos['vArticulo']*0.50),2)
                
        elif (Productos['tProducto']=='M' or Productos['tProducto']=='m') and 101000<=Productos['vArticulo']<=180000:
            cProducto=round(float(Productos['vArticulo']*0.09),2)
            gServicios=round(float(Productos['vArticulo']*0.25),2)
            rCompra=round(float(Productos['vArticulo']*0.50),2)
                
        elif (Productos['tProducto']=='M' or Productos['tProducto']=='m') and 181000<=Productos['vArticulo']<=230000:
            cProducto=round(float(Productos['vArticulo']*0.12),2)
            gServicios=round(float(Productos['vArticulo']*0.25),2)
            rCompra=round(float(Productos['vArticulo']*0.50),2)
                
        elif (Productos['tProducto']=='L' or Productos['tProducto']=='l') and 0<=Productos['vArticulo']<=100000:
            cProducto=round(float(Productos['vArticulo']*0.06),2)
            gServicios=round(float(Productos['vArticulo']*0.25),2)
            rCompra=round(float(Productos['vArticulo']*0.50),2)
            
        elif (Productos['tProducto']=='L' or Productos['tProducto']=='l') and 101000<=Productos['vArticulo']<=180000:
            cProducto=round(float(Productos['vArticulo']*0.09),2)
            gServicios=round(float(Productos['vArticulo']*0.25),2)
            rCompra=round(float(Productos['vArticulo']*0.50),2)
            
        elif (Productos['tProducto']=='L' or Productos['tProducto']=='l') and 181000<=Productos['vArticulo']<=230000:
            cProducto=round(float(Productos['vArticulo']*0.12),2)
            gServicios=round(float(Productos['vArticulo']*0.25),2)
            rCompra=round(float(Productos['vArticulo']*0.50),2)
            

    if Productos['dProducto']=='Chaqueta':

        if (Productos['tProducto']=='S' or Productos['tProducto']=='s') and 0<=Productos['vArticulo']<=100000:
            cProducto=round(float(Productos['vArticulo']*0.07),2)
            gServicios=round(float(Productos['vArticulo']*0.20),2)
            rCompra=round(float(Productos['vArticulo']*0.45),2)
                    
        elif (Productos['tProducto']=='S' or Productos['tProducto']=='s') and 101000<=Productos['vArticulo']<=180000:
            cProducto=round(float(Productos['vArticulo']*0.10),2)
            gServicios=round(float(Productos['vArticulo']*0.20),2)
            rCompra=round(float(Productos['vArticulo']*0.45),2)
            
        elif (Productos['tProducto']=='S' or Productos['tProducto']=='s') and 181000<=Productos['vArticulo']<=230000:
            cProducto=round(float(Productos['vArticulo']*0.12),2)
            gServicios=round(float(Productos['vArticulo']*0.20),2)
            rCompra=round(float(Productos['vArticulo']*0.45),2)
                    
        elif (Productos['tProducto']=='M' or Productos['tProducto']=='m') and 0<=Productos['vArticulo']<=100000:
            cProducto=round(float(Productos['vArticulo']*0.07),2)
            gServicios=round(float(Productos['vArticulo']*0.20),2)
            rCompra=round(float(Productos['vArticulo']*0.45),2)
            
        elif (Productos['tProducto']=='M' or Productos['tProducto']=='m') and 101000<=Productos['vArticulo']<=180000: 
            cProducto=round(float(Productos['vArticulo']*0.10),2)
            gServicios=round(float(Productos['vArticulo']*0.20),2)
            rCompra=round(float(Productos['vArticulo']*0.45),2)
            
        elif (Productos['tProducto']=='M' or Productos['tProducto']=='m') and 181000<=Productos['vArticulo']<=230000:
            cProducto=round(float(Productos['vArticulo']*0.12),2)
            gServicios=round(float(Productos['vArticulo']*0.20),2)
            rCompra=round(float(Productos['vArticulo']*0.45),2)
            
        elif (Productos['tProducto']=='L' or Productos['tProducto']=='l') and 0<=Productos['vArticulo']<=100000:
            cProducto=round(float(Productos['vArticulo']*0.07),2)
            gServicios=round(float(Productos['vArticulo']*0.20),2)
            rCompra=round(float(Productos['vArticulo']*0.45),2)
            
        elif (Productos['tProducto']=='L' or Productos['tProducto']=='l') and 101000<=Productos['vArticulo']<=180000:
            cProducto=round(float(Productos['vArticulo']*0.10),2)
            gServicios=round(float(Productos['vArticulo']*0.20),2)
            rCompra=round(float(Productos['vArticulo']*0.45),2)
            
        elif (Productos['tProducto']=='L' or Productos['tProducto']=='l') and 181000<=Productos['vArticulo']<=230000:
            cProducto=round(float(Productos['vArticulo']*0.12),2)
            gServicios=round(float(Productos['vArticulo']*0.20),2)
            rCompra=round(float(Productos['vArticulo']*0.45),2)


    dicSalida={'idVenta':Productos['idVenta'],'vArticulo':Productos['vArticulo'], 'cProducto':cProducto,'gServicios':gServicios, 'rCompra':rCompra}
    return(dicSalida)


Productos = {
    'idVenta': 1001,
    'vArticulo': 85125.65,
    'dProducto': 'Camisa',
    'tProducto': 's'
    }
print(gananciasVentas(Productos))

Productos = {
    'idVenta': 1002,
    'vArticulo': 210500,
    'dProducto': 'Pantalon',
    'tProducto': 'm'
}
print(gananciasVentas(Productos))

Productos = {
    'idVenta': 1003,
    'vArticulo': 145954.63,
    'dProducto': 'Chaqueta',
    'tProducto': 'l'
}
print(gananciasVentas(Productos))

Productos = {
    'idVenta': 1004,
    'vArticulo': 214874.32,
    'dProducto': 'Chaqueta',
    'tProducto': 's'
}
print(gananciasVentas(Productos))

Productos = {
    'idVenta': 1005,
    'vArticulo': 115263.23,
    'dProducto': 'Chaqueta',
    'tProducto': 'm'
}
print(gananciasVentas(Productos))


Productos = {
    'idVenta': 1006,
    'vArticulo': 58698.23,
    'dProducto': 'Chaqueta',
    'tProducto': 'l'
}
print(gananciasVentas(Productos))


