
class Empleado:
    __dni: str
    __nombre: str
    __direccion: str
    __telefono: str

    def __init__(self,dni,n,d,t):
        self.__dni=dni
        self.__nombre=n
        self.__direccion=d
        self.__telefono=t

    def __str__(self):
        return "DNI:{} - NOMBRE:{} - DIRECCION:{} - TELEFONO:{}".format(self.__dni,self.__nombre,self.__direccion,self.__telefono)    

    def get_dni(self):
        return self.__dni
    def get_nombre(self):
        return self.__nombre
    def get_direccion(self):
        return self.__direccion
    def get_telefono(self):
        return self.__telefono
    