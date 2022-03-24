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

    def retirar(self):
        dretirado = int(input("Ha seleccionado usted la opción de retirar dinero de su cuenta.\n ¿Cuánto dinero desea retirar?:\n"))
        if 0 < dretirado <= self.saldo:
            self.saldo = self.saldo - dretirado
            print("Ha retirado " + str(dretirado) + "€ y su saldo es de " + str(self.saldo) + "€.")
            decision = int(input("¿Desea continuar realizando operaciones?(Sí = 1): "))
            if decision == 1:
                operacion()
            else:
                exit()

        else:
            print("Usted no puede retirar más dinero del que contiene el saldo de su cuenta, por favor, introduzca correctamente la cantidad a retirar de su cuenta.")
            Cuenta.retirar(A)

    def ingresar(self):
        dingresado = int(input("Ha seleccionado la opción de ingresar dinero a su cuenta. ¿Cuánto dinero desea ingresar?"))
        self.saldo += dingresado
        print("Ha ingresado " + str(dingresado) + "€ y su saldo es de " + str(self.saldo) + "€.")
        decision = int(input("¿Desea continuar realizando operaciones?(Sí = 1): "))
        if decision == 1:
            operacion()
        else:
            exit()

    def transferencia(self):
        if A.modo != 1:    
            dtransferido = int(input("Ha seleccionado la opción de transferir dinero a otra cuenta. ¿Cuánto desea transferir?: "))
            if 0 < dtransferido <= self.saldo*2:    
                A.saldo -= dtransferido
                B.saldo += dtransferido
                print("Ha transferido " + str(dtransferido) + "€ y su saldo es de " + str(self.saldo) + "€.")
                print("El saldo de la cuenta B es de " + str(B.saldo) + "€.")
            decision = int(input("¿Desea continuar realizando operaciones?(Sí = 1): "))
            if decision == 1:
                operacion()
            else:
                exit()
        else:
            dtransferido = int(input("Ha seleccionado la opción de transferir dinero a otra cuenta. ¿Cuánto dinero desea transferir?: "))

            if 0 < (dtransferido + dtransferido * 0.05) <= self.saldo:        
                A.saldo -= dtransferido + dtransferido * 0.05
                B.saldo += dtransferido #cuenta a transferir
                print("a transferido " + str(dtransferido) + "€ y su saldo es de " + str(self.saldo) + "€.")
                print("El saldo de la cuenta B es de " + str(B.saldo) + "€.")
                decision = int(input("¿Desea continuar realizando operaciones?(Sí = 1): "))
                if decision == 1:
                    operacion()
                else:
                    exit()