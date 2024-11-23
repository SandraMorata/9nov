class Persona:
    def __init__ (self, nombre, apellido, edad):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__edad = edad

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        if nuevo_nombre.strip():
            self.__nombre = nuevo_nombre
        else:
            raise ValueError("Nombre no puede quedar vacio")
                             
    @property
    def edad (self):
        return self.__edad
    
    @edad.setter
    def edad (self, nueva_edad):
        if nueva_edad > 0:
            self.__edad = nueva_edad
        else:
            raise ValueError ("Debe ser un numero positivo")
        
    def mostrar_detalles(self):
        #print("{} {} {} a;os".format(self__nombre, self__apellido, self_edad))
        print(f"{self.__nombre} {self.__apellido}, {self.__edad} a;os")

persona1 = Persona("Juan", "Perez", 30)
print(persona1.nombre)
print(persona1.edad)
persona1.nombre = "Juan Carlos"
persona1.edad=35
print(persona1.mostrar_detalles())
        
    