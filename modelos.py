class Pelicula:

    def __init__(self,nombre,duracion,genero) -> None:
        self.nombre = nombre
        self.duracion = duracion
        self.genero = genero


class Genero:

    def __init__(self, nombre) -> None:
        self.nombre = nombre


class Catalogo:

    def __init__(self,nombre) -> None:
        self.nombre = nombre
        self.pelicula = []