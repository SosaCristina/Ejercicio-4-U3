from ClaseEmpleado import Empleado


class Planta (Empleado):
    __sueldo_basico: float
    __antiguedad: int

    def __init__(self,dni,nom,dir,tel,s,a):
        super().__init__(dni,nom,dir,tel)
        self.__sueldo_basico=s
        self.__antiguedad=a

    def __str__ (self):

        return "DNI:{} - NOMBRE:{} - DIRECCION:{} - TELEFONO:{} -- Sueldo basico:{} - Antiguedad:{}\n ".format(self.get_dni(),self.get_nombre(),self.get_direccion(),self.get_telefono(),self.__sueldo_basico,self.__antiguedad)    

    def calculo_sueldo(self):
        s=float((float(self.__sueldo_basico)/float(100))) * int( self.__antiguedad)
        sueldo= float(self.__sueldo_basico )+ float(s)
        
        return sueldo