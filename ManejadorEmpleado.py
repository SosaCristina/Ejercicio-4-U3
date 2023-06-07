from ClaseEmpleado import Empleado
from ClaseEmpleadoPlanta import Planta
from ClaseEmpleadoContratado import Contratado
from ClaseEmpleadoExterno import Externo
import numpy as np
import csv

class ManejadorE:
    __cantidad=0
    __dimension=0
    __incremento=5

    def __init__(self,dimension,incremento=5):
        self.__empleados=np.empty(dimension,dtype=Empleado)
        self.__cantidad=0
        self.__dimension=dimension

    def __str__(self):
        s=""
        for i in range(self.__cantidad):
            s+= str(i) + "\n"
        return s
        
    

    def agregar (self,unEmpleado):
        if self.__cantidad==self.__dimension:
            self.__dimension +=self.__incremento
            self.__empleados.resize(self.__dimension)
        self.__empleados[self.__cantidad]=unEmpleado
        self.__cantidad+=1    

    def crear_empleado(self):
        self.crear_planta()
        self.crear_externo()
        self.crear_contratado()

    def crear_planta(self):
        archivo1=open("C:\\Users\\chili\\POO archivos\\planta.csv")
        reader=csv.reader(archivo1,delimiter=",")
        for fila in reader:
            dni=fila[0]
            nom=fila[1]
            dir=fila[2]
            tel=fila[3]
            sueldo_b=fila[4]
            antig=int(fila[5])
            unPlanta=Planta(dni,nom,dir,tel,sueldo_b,antig)
            self.agregar(unPlanta)
        archivo1.close    
          
    def crear_externo(self):       
        archivo2=open("C:\\Users\\chili\\POO archivos\\externos.csv")
        reader=csv.reader(archivo2,delimiter=",")
        for fila in reader:
            dni=fila[0]
            nom=fila[1]
            dom=fila[2]
            tel=fila[3]
            tarea=fila[4]
            f_i=fila[5]
            f_f=fila[6]
            mv=fila[7]
            cost=fila[8]
            ms=fila[9]
            unExterno=Externo(dni,nom,dom,tel,tarea,f_i,f_f,mv,cost,ms)
            self.agregar(unExterno)
        archivo2.close
        
    def crear_contratado(self):
        archivo3=open("C:\\Users\\chili\\POO archivos\\contratados.csv")
        reader=csv.reader(archivo3,delimiter=",")
        for fila in reader:
            dni=fila[0]
            nom=fila[1]
            dom=fila[2]
            tel=fila[3]
            f_i=fila[4]
            f_f=fila[5]
            cant=fila[6]
            valor=fila[7]
            unContratado=Contratado(dni,nom,dom,tel,f_i,f_f,cant,valor)
            self.agregar(unContratado)
        archivo3.close    
            
    def mostrar(self):
        for i in self.__empleados:
            print(i)
            

    def buscar_empleado(self,dni):
        i=0
        indice=0
        bandera=False
        while i<len(self.__empleados) and not bandera:
            if (self.__empleados[i].get_dni() == dni):
                indice=i
                bandera=True
            else: i+=1
        return self.__empleados[indice]
            
    def modificar_horas(self,empleado):
        horas=int(input("Ingrese cantidad de horas trabajadas al dia de la fecha:"))
        empleado.horas_trabajadas(horas)

    def buscar_tarea(self,tarea):
        i=0
        indice=0
        bandera=False
        while i<len(self.__empleados) and not bandera:
            if isinstance(self.__empleados[i],Externo):
                if(self.__empleados[i].get_tarea() == tarea):
                    bandera=True
                    indice=i
                else: i+=1    
            else: 
                i+=1
        return self.__empleados[indice]

    def ver_monto(self,empleado):
        
        if empleado.get_fechafin()>"01/06/23":
            print("El monto a pagar es:{}".format(empleado.get_costoobra()))     
        else:
            print("La tarea ya fue finalizada")               
        
    

    def ayuda_economica(self):
        for i in self.__empleados:
            if isinstance(i, Planta):
                sueldo=i.calculo_sueldo()
                if sueldo < float(150000):
                    print("{} - {} - {}".format(i.get_nombre(),i.get_direccion(),i.get_dni()))
            else:
                if isinstance(i, Externo):
                    sueldo=i.calculo_sueldo()
                    if sueldo < float(150000):
                        print("{} - {} - {}".format(i.get_nombre(),i.get_direccion(),i.get_dni()))       
                else:
                    if isinstance(i, Contratado):
                        sueldo=i.calculo_sueldo()
                        if sueldo < float(150000):
                            print("{} - {} - {}".format(i.get_nombre(),i.get_direccion(),i.get_dni()))

    def mostrar_sueldos(self):
        print("NOMBRE de empleado - TELEFONO - SUELDO")
        for i in self.__empleados:
            if isinstance(i, Planta):
                sueldo=i.calculo_sueldo()
                print("{}       -    {}  -   {}".format(i.get_nombre(),i.get_telefono(),sueldo))
            else:
                if isinstance(i, Externo):
                    sueldo=i.calculo_sueldo()
                    print("{}       -    {}  -   {}".format(i.get_nombre(),i.get_telefono(),sueldo))       
                else:
                    if isinstance(i, Contratado):
                        sueldo=i.calculo_sueldo()
                        print("{}       -    {}  -   {}".format(i.get_nombre(),i.get_telefono(),sueldo))