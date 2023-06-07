from ClaseEmpleado import Empleado

class Externo(Empleado):
    __tarea: str
    __fecha_i: str
    __fecha_f: str
    __monto_viatico: float
    __costo_obra: float
    __monto_seguro: float

    def __init__(self,dni,nom,dir,tel,t,fi,ff,mv,c,ms):
        super().__init__(dni,nom,dir,tel)
        self.__tarea=t
        self.__fecha_i=fi
        self.__fecha_f=ff
        self.__monto_viatico=mv
        self.__costo_obra=c
        self.__monto_seguro=ms

    def __str__ (self):
        return "DNI:{} - NOMBRE:{} - DIRECCION:{} - TELEFONO:{} -- Tarea:{} - Fecha inicio:{} - Fecha Fin:{} - Monto viaticos:{} - Costo Obra:{} - Monto seguro:{}\n  ".format(self.get_dni(),self.get_nombre(),self.get_direccion(),self.get_telefono(),self.__tarea,self.__fecha_i,self.__fecha_f,self.__monto_viatico,self.__costo_obra,self.__monto_seguro)    
    
    def calculo_sueldo(self):
        sueldo=float(self.__costo_obra) - float(self.__monto_viatico) - float(self.__monto_seguro)
        
        return sueldo
    
    def get_fechafin(self):
        return self.__fecha_f
    def get_costoobra(self):
        return self.__costo_obra

    def get_tarea(self):
        return self.__tarea

    