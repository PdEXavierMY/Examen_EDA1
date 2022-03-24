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