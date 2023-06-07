from ManejadorEmpleado import ManejadorE
from ClaseEmpleado import Empleado
from ClaseEmpleadoContratado import Contratado
from ClaseEmpleadoExterno import Externo
from ClaseEmpleadoPlanta import Planta

if __name__=="__main__":
    cant=int(input("Ingresar cantidad de empleados: "))
    unEmpleado=ManejadorE(cant)
    unEmpleado.crear_empleado()
    unEmpleado.mostrar()
    dni=input("Ingresar DNI de empleado:")
    e=unEmpleado.buscar_empleado(dni)
    unEmpleado.modificar_horas(e)
    tarea=input("Ingresar Tarea:")
    e=unEmpleado.buscar_tarea(tarea)
    unEmpleado.ver_monto(e)
    unEmpleado.ayuda_economica()
    unEmpleado.mostrar_sueldos()