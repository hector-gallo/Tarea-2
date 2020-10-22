# Crear clase egreso
class Ingreso:
    def __init__(self):
        self.ListaIng = []

    # Funcion que recibe las cantidades y las inserta
    def IngresoN(self, numcuenta, cantidad):
        Ingreso = (numcuenta, cantidad)
        result = self.ListaIng.append(Ingreso)
        return result

    # Devuelve la cantidad total de ingresos
    def IngresoTotal(self):
        total = 0
        for ingreso in self.ListaIng:
            total = total + float(ingreso[1])
        return total

    # Muestra todos los ingresos de la cuenta
    def MuestraIng(self):
        for ingreso in self.ListaIng:
            print(f"Numero de Cuenta: {ingreso[0]} Cantidad: {ingreso[1]}")
