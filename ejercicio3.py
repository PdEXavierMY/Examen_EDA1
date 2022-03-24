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

    def creacioncuenta():
            nombre = str(input("Ha seleccionado la opción de crear una cuenta. Introduzca su nombre: "))
            global A, B
            modo = int(input("¿Qué tipo de cuenta desea(Plazo fijo = 1, VIP = 2)?: "))
            n = str(random.randint(100000000000, 999999999999))
            A = Cuenta(str(random.randint(100000, 999999)), nombre, datetime.today(),n, 10000, modo)
            print(nombre + " ha creado una cuenta bancaria el " + str(datetime.today()) + " con el número de cuenta: " + n)
            B = Cuenta(str(random.randint(100000, 999999)), "Persona B", datetime.today(), str(random.randint(100000000000, 999999999999)), 10000, 5)
            print("la cuenta B(VIP) a nombre de Professor.X, con un saldo de 1000 euros, con la que va a operar se creó el 17/07/2017.")