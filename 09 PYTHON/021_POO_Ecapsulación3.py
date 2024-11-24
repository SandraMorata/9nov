# POO

# CREACIÓN DE UNA CLASE

class Persona:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self.apellido = apellido
        self.edad = edad

    @property
    def nombre(self):
        print('Llamando método get nombre')
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        print('Llamando método set nombre')
        self._nombre = nombre

    def mostrar_detalle(self):
        print(f'Persona: {self._nombre} {self.apellido} {self.edad}')

    #Sin decoradores


    #def mostrar_detalle(self):
    #    print(f'Persona: {self.nombre()} {self.apellido} {self.edad}')


persona1 = Persona('Juan', 'Perez', 28)
persona1.nombre = 'Juan Carlos'
print(persona1.nombre)
# persona1._nombre = 'Cambio'
# print(persona1._nombre)







class Persona

    def __init__ (self,nombre,apellido,edad):
        self.__nombre = nombre
        self.apellido = apellido
        self.edad = edad
    
    @property
    def get_nombre(self):
        return self.__nombre

    @nombre.setter
    def setter_nombre(self, self.__nombre):
        self.__nombre = otro nombre

    def mostrar_detalles(self):
        print(f"Persona: {self.__nombre}, {self.apellido}, {self.edad}")

    Yo = Persona("Sandra","Morata",45)
    Yo.nombre + "Nani"
    print(Yo.nombre)    
