from Ingresos import Ingreso
from Egresos import Egreso

ing = Ingreso()
eg = Egreso()


class Finanzas:
    def __init__(self, numcuenta, cantidad):
        self.numcuenta = numcuenta
        self.cantidad = cantidad

    # LLama a un metodo de la clase ingresos para agregar cantidades
    def RegistrarIng(self, numcuenta, cantidad):
        ing.IngresoN(numcuenta, cantidad)

    # LLama a un metodo de la clase egresos para restar cantidades
    def RegistrarEg(self, numcuenta, cantidad):
        eg.EgresoN(numcuenta, cantidad)

    # LLama a un metodo de clase ingresos para mostrar los ingresos hechos por la cuenta
    def mostrarIng(self):
        ing.MuestraIng()

    # LLama a un metodo de clase egresos para mostrar los egresos hechos por la cuenta
    def mostarEg(self):
        eg.Muestra()

    # Presenta la cantidad total en la cuenta
    def Cantotal(self):
        Total = float(ing.IngresoTotal() - eg.EgresoTotal())
        return Total

    # Hace un listado de todos los egresos e ingresos de una cuenta
    def MostrarTrans(self):
        ing.MuestraIng()
        eg.Muestra()
