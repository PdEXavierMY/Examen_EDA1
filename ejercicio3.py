import random
from datetime import datetime
class Cuenta:
    def __init__(self, id_cuenta, nombre, apertura, numero, saldo, modo):
        self.id = id_cuenta
        self.nombre = nombre
        self.apertura = apertura
        self.numero = numero
        self.saldo = saldo
        self.modo = modo

    def retiro(self):
        dretirado = int(input("Ha seleccionado usted la opción de retirar dinero de su cuenta.\n ¿Cuánto dinero desea retirar?:\n"))
        if 0 < dretirado <= self.saldo:
            self.saldo = self.saldo - dretirado
            print("Ha retirado " + str(dretirado) + "€ y su saldo actualmente es de " + str(self.saldo) + "€.")
            decision = int(input("¿Desea continuar realizando operaciones?(Sí = 1): "))
            if decision == 1:
                operacion()
            else:
                exit()

        else:
            print("Usted no puede retirar más dinero del que contiene el saldo de su cuenta, por favor, introduzca correctamente la cantidad a retirar de su cuenta.")
            Cuenta.retiro(A)