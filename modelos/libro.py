class Libro:
    def __init__(self, isbn, titulo, autor, genero, anio=None, disponible=True):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.anio = anio
        self.disponible = disponible

    def __str__(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"{self.isbn} - {self.titulo} - {self.autor} ({estado})"
    
    def __repr__(self):
        return (
            f"Libro(isbn={self.isbn!r}, "
            f"titulo={self.titulo!r}, "
            f"autor={self.autor!r}, "
            f"anio={self.anio!r}, "
            f"disponible={self.disponible!r})"
        )
    
    def __eq__(self, __value: object) -> bool:
        return self.isbn == __value.isbn
