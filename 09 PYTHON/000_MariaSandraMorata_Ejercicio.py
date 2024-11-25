class Producto:        #nombramos la clase Producto
    def __init__(self,nombre,categoria,precio,cantidad): #contructor de atributos
        self.__nombre = nombre #creamos los atributos con __ para que sean privados
        self.__categoria = categoria
        self.__precio = precio
        self.__cantidad = cantidad

    def get_nombre(self):  #getter de nombre
        return self.__nombre
    
    def get_categoria(self):   #getter de categoria
        return self.__categoria
    
    def get_precio(self):
        return self.__precio

    def get_cantidad(self):
        return self.__cantidad
    
    def set_precio(self,precio):     #setter.precio
        if precio >0:               #validacion
            self.__precio = precio
        else:
            raise ValueError("El precio debe ser mayor a 0.")   

    def set_cantidad(self,cantidad):    #setter.cantidad
        if cantidad > 0:                #validacion
            self.cantidad = cantidad
        else:
            raise ValueError("Introduce una cantidad mayor a 0.")


class Inventario:                  #creamos la clase inventario q tendra una lista de productos y funciones
    def __init__(self):            #contructor
        self.__productos = []      #creamos una lista privada y vacia donde se guardaran los productos

    def agregar_producto(self,nombre,categoria,precio,cantidad):     #funcion para agregar producto (con sus atributos)
        for producto in self.__productos:                            #verificamos que el producto no exista ya
            if producto.get__nombre().lower() == nombre.lower():     #transformamos nombres a minusculas 
                print("El producto ya existe.")
                return
        nuevo_producto = Producto(nombre,categoria,precio,cantidad)   #nombramos nuevo producto con sus atributos     
        self.__productos.append(nuevo_producto)                       #agregamos nuevo producto
        print(f"Producto '{nombre}' ha sido agregado exitosamente.")
            
    def modificar_producto(self,nuevo_precio,nueva_cantidad):       #funcion para modificar el precio o la cantidad de un producto existente
        for product in self.__productos:                            #bucle para buscar nombre de producto en la lista donde almacenamos productos
            if product.get_nombre().lower() == nombre.lower():      #cuando los nombres del producto sean iguales
                if nuevo_precio is not None:                        #validacion para que inserte un precio nuevo o no (solo cantidad)
                    if nuevo_precio >0:                             #validacion para que el precio sea mayor que 0
                        producto.set_precio(nuevo_precio)           #se cambia el precio
                        print(f"El precio se ha actualizado a {nuevo_precio}.")
                    else:
                        print("El precio debe ser mayor a cero. No se ha realizado el cambio.")
                 if nueva_cantidad is not None:
                    if nueva_cantidad>=0:
                        product.set_cantidad(nueva_cantidad)
                        print(f"La cantidad se ha actualizado a {nueva_cantidad}.")
                    else:
                        print("La cantidad debe ser mayor o igual a cero. No se ha realizado el cambio.")
                print("Producto {nombre} modificado correctamente.")
                return
        print(f:"Producto {nombre} no ha sido encontrado.")

    def eliminar_producto(self,nombre):                 #funcion para eliminar un producto
        for producto in self.__productos:
            if producto.get_nombre().lower() == nombre.lower():
                self.__productos.remove(producto)
                print(f"Producto {nombre} ha sido eliminado del inventario.")
                return
        print(f"Producto '{nombre}' no encontrado.")

    def mostrar_inventario (self):                      #funcion para mostrar los elementos del inventario
        if not self.__productos:
            print("El inventario esta vacio.")
        else:
            print("\n---- Inventario ----")
            for product in self.__productos:
                print(f"Nombre: {producto.get_nombre()}, Categoría: {producto.get_categoria()}, "
                      f"Precio: {producto.get_precio()}, Cantidad: {producto.get_cantidad()}")





        
def menu():     #creamos el menu con un modelo
    while True: #con utilizamos un bucle while
        print("\n------ Menu de Inventario ------")  #titulo del menu
        print("1. Agregar producto")    #print las diferentes funciones
        print("2. Actualizar producto")
        print("3. Eliminar producto")
        print("4. Mostrar inventario")
        print("5. Buscar producto")
        print("6. Salir")

        opcion = input("Seleccione una opcion: ") #mostramos al usuario un mensaje para q elija una opcion del menu

        if opcion == 1:  #si el usuario elige uno
            print("Has seleccionado agregar producto. Por favor, ingresa los siguientes datos:") #le imprimos mensaje
                    __nombre = input("Introduce el nombre del producto: ")
                                            #Verificar que el producto no exista previamente en el inventario.

        elif opcion == 2 #si el usuario elige la opcion dos
            print("Has seleccionado actualizar producto. Introduce los datos que quieras cambiar:")
            def actualizar.producto(self,productos)
                self.productos.update(productos)
            
    
