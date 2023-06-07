from ClaseEmpleado import Empleado

class Contratado(Empleado):
    __fecha_inicio: str
    __fecha_fin: str
    __cant_horas: int
    __valor_porhora: float

    def __init__ (self,dni,nom,dir,tel,fi,ff,c,v):
        super().__init__(dni,nom,dir,tel)
        self.__fecha_inicio=fi
        self.__fecha_fin=ff
        self.__cant_horas=c
        self.__valor_porhora=v

    def __str__ (self):
        return "DNI:{} - NOMBRE:{} - DIRECCION:{} - TELEFONO:{} -- Fecha Inicio:{} - Fecha Fin:{} - Cantidad de horas:{} - Valor por hora:{}\n ".format(self.get_dni(),self.get_nombre(),self.get_direccion(),self.get_telefono(),self.__fecha_inicio,self.__fecha_fin,self.__cant_horas,self.__valor_porhora)    

    def calculo_sueldo(self):
        sueldo=int(self.__cant_horas) * float(self.__valor_porhora)
        
        return sueldo 
    
    def horas_trabajadas(self,horas):
        actualizado=int(horas)+int(self.__cant_horas)
        self.__cant_horas=actualizado
        print("Horas actualizadas con exito:",self.__cant_horas)