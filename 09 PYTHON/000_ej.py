class Producto:
    """
    Clase que representa un producto en el inventario.
    Contiene atributos privados para nombre, categoría, precio y cantidad.
    """
    def __init__(self, nombre, categoria, precio, cantidad):
        # Atributos privados
        self.__nombre = nombre
        self.__categoria = categoria
        self.__precio = precio
        self.__cantidad = cantidad

    # Métodos para obtener los valores de los atributos (getters)
    def get_nombre(self):
        return self.__nombre

    def get_categoria(self):
        return self.__categoria

    def get_precio(self):
        return self.__precio

    def get_cantidad(self):
        return self.__cantidad

    # Métodos para modificar los valores de los atributos (setters) con validaciones
    def set_precio(self, precio):
        # El precio debe ser mayor que 0
        if precio > 0:
            self.__precio = precio
        else:
            raise ValueError("El precio debe ser mayor que 0.")

    def set_cantidad(self, cantidad):
        # La cantidad debe ser mayor o igual a 0
        if cantidad >= 0:
            self.__cantidad = cantidad
        else:
            raise ValueError("La cantidad debe ser mayor o igual que 0.")


class Inventario:
    """
    Clase que representa un inventario de productos.
    Permite realizar operaciones como agregar, actualizar, eliminar, buscar y mostrar productos.
    """
    def __init__(self):
        # Lista privada que almacena los productos
        self.__productos = []

    def agregar_producto(self, nombre, categoria, precio, cantidad):
        """
        Agrega un nuevo producto al inventario.
        Verifica que el producto no exista previamente.
        """
        # Verificar si el producto ya existe
        for producto in self.__productos:
            if producto.get_nombre().lower() == nombre.lower():
                print("El producto ya existe en el inventario.")
                return
        
        # Crear un nuevo producto y agregarlo a la lista
        nuevo_producto = Producto(nombre, categoria, precio, cantidad)
        self.__productos.append(nuevo_producto)
        print(f"Producto '{nombre}' agregado exitosamente.")

    def actualizar_producto(self, nombre, nuevo_precio=None, nueva_cantidad=None):
        """
        Actualiza el precio y/o la cantidad de un producto existente.
        Incluye validaciones para evitar datos inválidos.
        """
        for producto in self.__productos:
            if producto.get_nombre().lower() == nombre.lower():
                # Validar y actualizar el precio, si se proporciona
                if nuevo_precio is not None:
                    if nuevo_precio > 0:
                        producto.set_precio(nuevo_precio)
                    else:
                        print("El precio debe ser mayor que 0. No se realizaron cambios en el precio.")

                # Validar y actualizar la cantidad, si se proporciona
                if nueva_cantidad is not None:
                    if nueva_cantidad >= 0:
                        producto.set_cantidad(nueva_cantidad)
                    else:
                        print("La cantidad debe ser mayor o igual que 0. No se realizaron cambios en la cantidad.")

                print(f"Producto '{nombre}' actualizado correctamente.")
                return
        
        # Si el producto no se encuentra
        print(f"Producto '{nombre}' no encontrado.")

    def eliminar_producto(self, nombre):
        """
        Elimina un producto del inventario.
        """
        for producto in self.__productos:
            if producto.get_nombre().lower() == nombre.lower():
                self.__productos.remove(producto)
                print(f"Producto '{nombre}' eliminado del inventario.")
                return
        print(f"Producto '{nombre}' no encontrado.")

    def mostrar_inventario(self):
        """
        Muestra todos los productos disponibles en el inventario.
        """
        if not self.__productos:
            print("El inventario está vacío.")
        else:
            print("\n--- Inventario ---")
            for producto in self.__productos:
                print(f"Nombre: {producto.get_nombre()}, Categoría: {producto.get_categoria()}, "
                      f"Precio: {producto.get_precio()}, Cantidad: {producto.get_cantidad()}")

    def buscar_producto(self, nombre):
        """
        Busca un producto por su nombre y muestra sus detalles si existe.
        """
        for producto in self.__productos:
            if producto.get_nombre().lower() == nombre.lower():
                print(f"Producto encontrado: Nombre: {producto.get_nombre()}, Categoría: {producto.get_categoria()}, "
                      f"Precio: {producto.get_precio()}, Cantidad: {producto.get_cantidad()}")
                return
        print(f"Producto '{nombre}' no encontrado.")


def menu ():
    """
    Función principal que muestra el menú de opciones para interactuar con el inventario.
    """
    inventario = Inventario()  # Crear una instancia del inventario
    
    while True:
        print("\n------ Menú de Inventario ------")
        print("1. Agregar producto")
        print("2. Actualizar producto")
        print("3. Eliminar producto")
        print("4. Mostrar inventario")
        print("5. Buscar producto")
        print("6. Salir")

        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue

        if opcion == 1:  # Agregar producto
            nombre = input("Introduce el nombre del producto: ")
            categoria = input("Introduce la categoría del producto: ")
            try:
                precio = float(input("Introduce el precio del producto: "))
                cantidad = int(input("Introduce la cantidad del producto: "))
                if precio <= 0 or cantidad < 0:
                    print("El precio debe ser mayor que 0 y la cantidad mayor o igual que 0.")
                else:
                    inventario.agregar_producto(nombre, categoria, precio, cantidad)
            except ValueError:
                print("Por favor, ingresa valores válidos para el precio y la cantidad.")

        elif opcion == 2:  # Actualizar producto
            nombre = input("Introduce el nombre del producto a actualizar: ")
            try:
                nuevo_precio = float(input("Introduce el nuevo precio (deja en blanco para no modificar): ") or None)
                nueva_cantidad = int(input("Introduce la nueva cantidad (deja en blanco para no modificar): ") or None)
                if nuevo_precio is not None and nuevo_precio <= 0:
                    print("El precio debe ser mayor que 0.")
                    nuevo_precio = None  # Ignorar cambio inválido
                if nueva_cantidad is not None and nueva_cantidad < 0:
                    print("La cantidad debe ser mayor o igual que 0.")
                    nueva_cantidad = None  # Ignorar cambio inválido
                inventario.actualizar_producto(nombre, nuevo_precio, nueva_cantidad)
            except ValueError:
                print("Por favor, ingresa valores válidos para el precio y la cantidad.")

        elif opcion == 3:  # Eliminar producto
            nombre = input("Introduce el nombre del producto a eliminar: ")
            inventario.eliminar_producto(nombre)

        elif opcion == 4:  # Mostrar inventario
            inventario.mostrar_inventario()

        elif opcion == 5:  # Buscar producto
            nombre = input("Introduce el nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)

        elif opcion == 6:  # Salir
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Inténtalo de nuevo.")
if __name__ == "__main__":
    menu()
