# Crear clase egreso
class Egreso:
    def __init__(self):
        self.ListaEg = []

    # Funcion que recibe las cantidades y las resta
    def EgresoN(self, numcuenta, cantidad):
        Egreso = (numcuenta, cantidad)
        result = self.ListaEg.append(Egreso)
        return result

    # Devuelve la cantidad total de egresos
    def EgresoTotal(self):
        total = 0
        for egreso in self.ListaEg:
            total = total + float(egreso[1])
        return total

    # Muestra todos los egresos de la cuenta
    def Muestra(self):
        for egreso in self.ListaEg:
            print(f"Numero de Cuenta: {egreso[0]} Cantidad: {egreso[1]}")