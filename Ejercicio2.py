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
class Ornitorrinco: #hereda tanto de oviparo como de mamifero(ver UML)
     def __init__(self, familia, origen):
         oviparo.__init__(self, familia, origen)
         mamifero.__init__(self, familia, origen)

#implementar objentos que heredan de dos clases que a su vez heredan de una común es confuso para python y generará problemas
#En este caso ornitorrinco que trata de heredar tanto de mamifero como de oviparo que a su vez heredan de animal tendrá el doble de atributos(repetidos de animal)
#la conclusión es que este tipo de herencias no debe hacerse y se puede solucionar definiendo una clase paralela a las comunes pero individual(poco práctico pero sin errores) que solo herede de la incial
class ornitorrinco:
    def __init__(self, familia, origen):
        animal.__init__(self, familia, origen)
        self.reproduccionsexual = True
        self.ponehuevos = True