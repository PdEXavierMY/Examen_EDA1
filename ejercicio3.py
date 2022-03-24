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
        if A.modo == 1:
            dretirado = int(input("Ha seleccionado usted la opción de retirar dinero de su cuenta.\n¿Cuánto dinero desea retirar?: "))
            if 0 < dretirado <= self.saldo:
                self.saldo = self.saldo - dretirado
                print("Ha retirado " + str(dretirado) + "€ y su saldo es de " + str(self.saldo) + "€.")
                decision = int(input("¿Desea continuar realizando operaciones?(Sí = 1): "))
                if decision == 1:
                    Cuenta.operacion()
                else:
                    exit()
            else:
                print("No puede retirar más dinero del que contiene el saldo, por favor, introduzca correctamente la cantidad a retirar.")
                Cuenta.retirar(A)
        elif A.modo != 1:
            print("Su banco le proporciona la opción de quedarse en números negativos(máximo -2500).")
            dretirado = int(input("Ha seleccionado usted la opción de retirar dinero de su cuenta.\n¿Cuánto dinero desea retirar?: "))
            if 0 < dretirado <= self.saldo+2500:
                self.saldo = self.saldo - dretirado
                print("Ha retirado " + str(dretirado) + "€ y su saldo es de " + str(self.saldo) + "€.")
                if self.saldo < 0:
                    print("Saldo negativo, no se pueden realizar más operaciones.")
                    exit()
                else:
                    decision = int(input("¿Desea continuar realizando operaciones?(Sí = 1): "))
                    if decision == 1:
                        Cuenta.operacion()
                    else:
                        exit()

            else:
                print("No puede retirar más dinero del negativo permitido, por favor, introduzca correctamente la cantidad a retirar.")
                Cuenta.retirar(A)

    def ingresar(self):
        dingresado = int(input("Ha seleccionado la opción de ingresar dinero a su cuenta. ¿Cuánto dinero desea ingresar?: "))
        if dingresado > 0:
            self.saldo += dingresado
            print("Ha ingresado " + str(dingresado) + "€ y su saldo es de " + str(self.saldo) + "€.")
            decision = int(input("¿Desea continuar realizando operaciones?(Sí = 1): "))
            if decision == 1:
                Cuenta.operacion()
            else:
                exit()
        else:
            print("No puede ingresar números negativos.")
            exit()

    def transferencia(self):
        if A.modo != 1:    
            dtransferido = int(input("Ha seleccionado la opción de transferir dinero a otra cuenta. ¿Cuánto desea transferir?: "))
            if 0 < dtransferido <= self.saldo*2:    
                A.saldo -= dtransferido
                B.saldo += dtransferido
                print("Ha transferido " + str(dtransferido) + "€ y su saldo es de " + str(self.saldo) + "€.")
                print("El saldo de la cuenta B es de " + str(B.saldo) + "€.")
            else:
                print("No posee esa cantidad de dinero en su cuenta. Operación denegada.")
            decision = int(input("¿Desea continuar realizando operaciones?(Sí = 1): "))
            if decision == 1:
                Cuenta.operacion()
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
                    Cuenta.operacion()
                else:
                    exit()
            else:
                print("No posee esa cantidad de dinero en su cuenta. Operación denegada.")

    def creacioncuenta():
            nombre = str(input("Ha seleccionado la opción de crear una cuenta. Introduzca su nombre: "))
            global A, B
            modo = int(input("¿Qué tipo de cuenta desea(Plazo fijo = 1, VIP = (cualquier entero excepto 1))?: "))
            n = str(random.randint(100000000000, 999999999999))
            A = Cuenta(str(random.randint(100000, 999999)), nombre, datetime.today(),n, 10000, modo)
            print(nombre + " ha creado una cuenta bancaria el " + str(datetime.today()) + " con el número de cuenta: " + n + ".")
            B = Cuenta(str(random.randint(100000, 999999)), "Persona B", datetime.today(), str(random.randint(100000000000, 999999999999)), 10000, 5)
            print("La segunda cuenta B(VIP) con un saldo de 10000 euros con la que va a operar se creó por defecto el 17/07/2017.")

    def operacion():
        elegir = int(input("Introduzca la operación que va a realizar(Ingersar dinero = 1, Retirar dinero = 2, Transferir dinero = 3): "))
        if elegir == 1:
            Cuenta.ingresar(A)
        if elegir == 2:
            Cuenta.retirar(A)
        if elegir == 3:
            Cuenta.transferencia(A)

#iniciar código
Cuenta.creacioncuenta()
Cuenta.operacion()