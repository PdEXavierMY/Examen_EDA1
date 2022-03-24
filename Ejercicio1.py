class libro:
    def __init__(self, titulo, genero, autor, isbn, editorial):
        self.titulo = str(titulo)
        self.genero = str(genero)
        self.autor = str(autor)
        self.isbn = bool(isbn)
        self.editorial = bool(editorial)

    def get_titulo(self):
        return self.titulo

    def get_genero(self):
        return self.genero

    def get_autor(self):
        return self.autor

    def get_isb(self):
        return self.isbn

    def get_editorial(self):
        return self.editorial

    def set_titulo(self, titulo):
        self.titulo = titulo
    
    def set_genero(self, genero):
        self.genero = genero

    def set_autor(self, autor):
        self.titulo = autor

    def set_titulo(self, isbn):
        self.isbn = isbn

    def set_titulo(self, editorial):
        self.editorial = editorial