class Libro:
    def __init__(self, titulo, autor, anio):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio

class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)
        print(f"Se ha agregado el libro '{libro.titulo}' a la biblioteca.")

    def mostrar_libros(self):
        if self.libros:
            print("Libros en la biblioteca:")
            for libro in self.libros:
                print(f"Libro: {libro.titulo}, {libro.autor}, {libro.anio}")
        else:
            print("No hay libros en la biblioteca.")

    def buscar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower():
                print(f"Libro encontrado: '{libro.titulo}' por {libro.autor} ({libro.anio})")
                return  # Salir del método si se encuentra el libro
        else:
            print(f"El libro '{titulo}' no está en la biblioteca.")

# Crear instancias de libros
libro1 = Libro("1984", "George Orwell", 1949)
libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", 1967)
libro3 = Libro("Los 3 cerditos", "Desire Diez", 2024)

# Crear biblioteca e interactuar con ella
biblioteca_centro = Biblioteca()
biblioteca_centro.agregar_libro(libro1)
biblioteca_centro.agregar_libro(libro2)
biblioteca_centro.agregar_libro(libro3)

biblioteca_centro.mostrar_libros()

# Buscar libros
biblioteca_centro.buscar_libro("1984")
biblioteca_centro.buscar_libro("El principito")
