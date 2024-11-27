class Producto:
    """
    Clase que representa un producto en el inventario.
    
    Atributos privados:
    - _nombre: Nombre del producto
    - _categoria: Categoría del producto
    - _precio: Precio del producto
    - _cantidad: Cantidad en stock
    """
    def __init__(self, nombre: str, categoria: str, precio: float, cantidad: int):
        """
        Constructor de la clase Producto con validaciones.
        
        Args:
            nombre (str): Nombre del producto
            categoria (str): Categoría del producto
            precio (float): Precio del producto
            cantidad (int): Cantidad en stock
        
        Raises:
            ValueError: Si los valores no cumplen con las validaciones
        """
        # Validaciones de entrada
        if not nombre or not categoria:
            raise ValueError("El nombre y la categoría no pueden estar vacíos")
        
        if precio <= 0:
            raise ValueError("El precio debe ser mayor que 0")
        
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa")
        
        # Atributos privados
        self._nombre = nombre
        self._categoria = categoria
        self._precio = precio
        self._cantidad = cantidad
    
    # Getters
    def get_nombre(self) -> str:
        """Obtener el nombre del producto"""
        return self._nombre
    
    def get_categoria(self) -> str:
        """Obtener la categoría del producto"""
        return self._categoria
    
    def get_precio(self) -> float:
        """Obtener el precio del producto"""
        return self._precio
    
    def get_cantidad(self) -> int:
        """Obtener la cantidad en stock"""
        return self._cantidad
    
    # Setters
    def set_precio(self, nuevo_precio: float):
        """
        Establecer un nuevo precio con validación
        
        Args:
            nuevo_precio (float): Nuevo precio del producto
        
        Raises:
            ValueError: Si el precio no es válido
        """
        if nuevo_precio <= 0:
            raise ValueError("El precio debe ser mayor que 0")
        self._precio = nuevo_precio
    
    def set_cantidad(self, nueva_cantidad: int):
        """
        Establecer una nueva cantidad con validación
        
        Args:
            nueva_cantidad (int): Nueva cantidad en stock
        
        Raises:
            ValueError: Si la cantidad no es válida
        """
        if nueva_cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa")
        self._cantidad = nueva_cantidad
    
    def __str__(self) -> str:
        """
        Representación en cadena del producto
        
        Returns:
            str: Información del producto
        """
        return (f"Producto: {self._nombre} | "
                f"Categoría: {self._categoria} | "
                f"Precio: €{self._precio:.2f} | "
                f"Cantidad: {self._cantidad}")


class Inventario:
    """
    Clase que gestiona el inventario de productos.
    
    Atributos privados:
    - _productos: Lista de productos en el inventario
    """
    def __init__(self):
        """
        Constructor de la clase Inventario.
        Inicializa la lista de productos vacía.
        """
        self._productos = []
    
    def agregar_producto(self, producto: Producto):
        """
        Agregar un nuevo producto al inventario.
        
        Args:
            producto (Producto): Producto a agregar
        
        Raises:
            ValueError: Si el producto ya existe
        """
        # Verificar si el producto ya existe
        for p in self._productos:
            if p.get_nombre() == producto.get_nombre():
                raise ValueError(f"El producto {producto.get_nombre()} ya existe en el inventario")
        
        self._productos.append(producto)
        print(f"Producto {producto.get_nombre()} agregado exitosamente")
    
    def actualizar_producto(self, nombre: str, nuevo_precio: float = None, nueva_cantidad: int = None):
        """
        Actualizar precio o cantidad de un producto existente.
        
        Args:
            nombre (str): Nombre del producto a actualizar
            nuevo_precio (float, optional): Nuevo precio del producto
            nueva_cantidad (int, optional): Nueva cantidad del producto
        
        Raises:
            ValueError: Si el producto no existe
        """
        for producto in self._productos:
            if producto.get_nombre() == nombre:
                if nuevo_precio is not None:
                    producto.set_precio(nuevo_precio)
                if nueva_cantidad is not None:
                    producto.set_cantidad(nueva_cantidad)
                print(f"Producto {nombre} actualizado exitosamente")
                return
        
        raise ValueError(f"Producto {nombre} no encontrado en el inventario")
    
    def eliminar_producto(self, nombre: str):
        """
        Eliminar un producto del inventario.
        
        Args:
            nombre (str): Nombre del producto a eliminar
        
        Raises:
            ValueError: Si el producto no existe
        """
        for i, producto in enumerate(self._productos):
            if producto.get_nombre() == nombre:
                del self._productos[i]
                print(f"Producto {nombre} eliminado exitosamente")
                return
        
        raise ValueError(f"Producto {nombre} no encontrado en el inventario")
    
    def mostrar_inventario(self):
        """
        Mostrar todos los productos del inventario.
        """
        if not self._productos:
            print("El inventario está vacío")
            return
        
        print("--- INVENTARIO ACTUAL ---")
        for producto in self._productos:
            print(producto)
    
    def buscar_producto(self, nombre: str) -> Producto:
        """
        Buscar un producto por nombre.
        
        Args:
            nombre (str): Nombre del producto a buscar
        
        Returns:
            Producto: Producto encontrado
        
        Raises:
            ValueError: Si el producto no existe
        """
        for producto in self._productos:
            if producto.get_nombre() == nombre:
                return producto
        
        raise ValueError(f"Producto {nombre} no encontrado en el inventario")


def main():
    """
    Función principal para demostrar el funcionamiento del inventario.
    """
    # Crear un inventario
    inventario = Inventario()
    
    try:
        # Agregar productos
        p1 = Producto("Laptop", "Electrónica", 899.99, 10)
        p2 = Producto("Smartphone", "Electrónica", 599.99, 15)
        
        inventario.agregar_producto(p1)
        inventario.agregar_producto(p2)
        
        # Mostrar inventario
        inventario.mostrar_inventario()
        
        # Actualizar producto
        inventario.actualizar_producto("Laptop", nuevo_precio=799.99, nueva_cantidad=8)
        
        # Buscar producto
        producto_buscado = inventario.buscar_producto("Smartphone")
        print("\nProducto buscado:")
        print(producto_buscado)
        
        # Eliminar producto
        inventario.eliminar_producto("Smartphone")
        
        # Mostrar inventario actualizado
        inventario.mostrar_inventario()
    
    except ValueError as e:
        print(f"Error: {e}")


# Ejecutar el script
if __name__ == "__main__":
    main()