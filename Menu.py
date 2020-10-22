from Finanzas import Finanzas

while True:
    print("-------------------------------------------------")
    print("Elija la opcion que desea:")
    print("Iniciar una cuenta --1")
    print("Ingresar una cantidad a la cuenta --2")
    print("Sustraer una cantidad a la cuenta --3")
    print("Ver reporte de ingresos--4")
    print("Ver reporte de egresos --5")
    print("Ver todas las transacciones --6")
    print("Ver la cantidad total --7")
    print("Terminar de usar la app --8")
    print("-------------------------------------------------")

    x = int(input())

    if x == 1:
        print("Ingrese el Numero de la cuenta a crear:")
        num = int(input())
        cantidad = 0.0
        cuentacreada = Finanzas(num, cantidad)
    elif x == 2:
        print("Inserte el numero de cuenta:")
        numcuenta = int(input())
        print("Inserte la cantidad:")
        cant = float(input())
        cuentacreada.RegistrarIng(numcuenta, cant)
    elif x == 3:
        print("Inserte el numero de cuenta:")
        numcuenta = int(input())
        print("Inserte la cantidad:")
        cant = float(input())
        cuentacreada.RegistrarEg(numcuenta, cant)
    elif x == 4:
        cuentacreada.mostrarIng()
    elif x == 5:
        cuentacreada.mostarEg()
    elif x == 6:
        cuentacreada.MostrarTrans()
    elif x == 7:
        cuentacreada.Cantotal()
    elif x == 8:
        break
