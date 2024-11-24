"""Ejercicio: Gestión de Atributos en una Clase con Getters y Setters
Descripción:
En este ejercicio, crearás una clase llamada Libro para gestionar los atributos privados titulo, autor y precio de un libro. Utilizarás propiedades (@property) para implementar los getters y setters de estos atributos. Al final, deberás mostrar los detalles del libro utilizando un método.

Requisitos:
Definir la Clase Libro:

La clase debe tener un constructor (__init__) que acepte tres parámetros: titulo, autor y precio.

Dentro del constructor, asigna estos parámetros a los atributos privados de la clase.

Crear Getters y Setters Utilizando Decoradores:

Define un método getter y un método setter para el atributo titulo utilizando el decorador @property y @titulo.setter.

Define un método getter y un método setter para el atributo precio utilizando el decorador @property y @precio.setter.

Los setters deben incluir validaciones:

titulo no puede estar vacío.

precio debe ser un número positivo.

Método para Mostrar Detalles:

Crea un método llamado mostrar_detalles que devuelva una cadena con los detalles del libro en el formato: Libro: titulo, autor, precio €.

Instanciación y Uso de la Clase:

Crea una instancia de la clase Libro con los valores titulo="Cien Años de Soledad", autor="Gabriel García Márquez", y precio=20.

Usa los métodos getters para obtener los valores de titulo y precio.

Usa los métodos setters para cambiar los valores de titulo a El Amor en los Tiempos del Cólera y precio a 25.

Muestra los detalles del libro utilizando el método mostrar_detalles.""""

class Libro:
    def __init__ (self, titulo, autor, precio): #constructor de clase
        self.__titulo = titulo
        self.__autor = autor 
        self.__precio = precio

    @property
    def titulo(self):
        return (self.__titulo)

    @titulo.setter
    def titulo(self,nuevo_titulo):
        if nuevo_titulo.strip():
           self.__titulo = nuevo_titulo
        else:
            raise ValueError("El titulo no puede quedar vacio")
        
    @property
    def precio(self):
        return (self.__precio)

    @precio.setter
    def precio(self,precio_nuevo):
        if precio_nuevo > 0:
            self.__precio = precio_nuevo
        else:
            raise ValueError("El precio tiene que ser mayor que 0")
        
    def mostrar_detalles (self):
        return f"Libro: {self.__titulo}, {self.__autor}, {self.__precio}$."

Libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", 20)
print(Libro1.titulo)
print(Libro1.precio)
Libro1.titulo="El Amor en los Tiempos del Cólera"
Libro1.precio=25
print(Libro1.mostrar_detalles())


# Crea una clase CuentaBancaria que tenga un atributo privado __saldo. 
# Implementa un método getter llamado get_saldo que devuelva el saldo actual. 
# Crea una instancia de CuentaBancaria y muestra el saldo usando el método getter.

class CuentaBancaria:
    def __init__ (self,saldo):
        self.__saldo = saldo
    
    def get_saldo(self):
     return self.__saldo



mi_cuenta = CuentaBancaria(1000)
        
# Crear una instancia de CuentaBancaria


# Mostrar el saldo usando el método getter
print("Saldo inicial: ", mi_cuenta.get_saldo())





# Modifica la clase CuentaBancaria para que tenga un método setter llamado set_saldo 
# que permita modificar el saldo solo si el nuevo saldo es positivo. 
# Usa este método para intentar establecer un saldo negativo y observa el resultado.

    def set_saldo(self, nuevo_saldo):
        if nuevo_saldo > 0:
            self.__saldo = nuevo_saldo
        else:
            print(f"El saldo no puede ser negativo.")
    




# Crear una instancia de CuentaBancaria

# Intentar establecer un saldo negativo

# Mostrar el saldo después del intento







# Crea una clase Empleado que tenga un atributo protegido _sueldo y un método 
# público mostrar_sueldo que imprima el sueldo. Crea una instancia de Empleado 
# y llama al método mostrar_sueldo.









# Crea una clase Estudiante con atributos privados __nombre y __nota. 
# Implementa métodos getter para ambos atributos y un método setter para __nota 
# que solo permita valores entre 0 y 10. Crea una instancia de Estudiante, 
# establece y muestra sus valores usando los métodos adecuados.

class Estudiante:
    def __init__ (self,__nombre, __nota):
        self.__nombre = nombre
        self.__nota = nota

    def 

# Crear una instancia de Estudiante


# Mostrar el nombre y la nota


# Intentar establecer una nueva nota válida e inválida
