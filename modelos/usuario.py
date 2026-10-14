class Usuario:
    def __init__(self, id, nombre, apellidos, email):
        self.id = id
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email

    def __str__(self):
        return f"{self.id} - {self.nombre} {self.apellidos} <{self.email}>"

    def __repr__(self):
        return (
            f"Usuario(Id={self.id!r}, "
            f"nombre={self.nombre!r}, "
            f"apellidos={self.apellidos!r}, "
            f"email={self.email!r})"
        )
    
