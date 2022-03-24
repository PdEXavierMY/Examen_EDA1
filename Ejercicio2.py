#Animal
#Mamífero
#Ovíparo
#Pollo
#Gato
#Ornitorrinco
class animal:
    def __init__(self, familia, origen):
        self.familia = str(familia)
        self.origen = str(origen)

class oviparo:
    def __init__(self, familia, origen):
        animal.__init__(self, familia, origen)
        self.ponehuevos = True

class mamifero:
    def __init__(self, familia, origen):
        animal.__init__(self, familia, origen)
        self.reproduccionsexual = True

Pollo = oviparo("Phasianidae", "Asia")
Gato = mamifero("Felidae", "Mundo")
#Ornitorrinco = mamifero y oviparo 