class Animal:

    def __init__ (self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

    def descripcion(self):
        print(f"{self.nombre}, {self.especie}, {self.edad}")

Animal1=Animal("Marisa","Elefante",10)
Animal1.descripcion()

class Coche:
    def __init__ (self,marca,modelo,ano):
        self.__marca = marca
        self.__modelo = modelo
        self.__ano = ano

    #getter de marca
    @property
    def marca(self):
        return self.__marca

    #setter de marca
    @marca.setter
    def marca(self,valor):
        self.__marca=valor

    @property
    def modelo(self):
        return self.__modelo

    @modelo.setter
    def modelo(self,valor):
        self.__modelo=valor

    @property
    def ano(self):
        return self.__ano

    @ano.setter 
    def ano(self,valor):
        self.__ano=valor

    def mostrar_informacion(self):
        print(f"Las caracteristicas del coche son {self.__marca}, {self.__modelio}, {self.ano}")

coche5=Coche("Toyota","Corolla",2008)
coche5.marca = "Honda"
coche5.modelo = "Civic"
coche5.ano = 2022

coche5.mostrar_informacion()

class Concierto:
    def __init__(self, nombre, artista, fecha, precio):
        self.__nombre = nombre
        self.__artista = artista
        self.__fecha = fecha
        self.__precio = precio

class Ticketera:
    def __init__(self,nombre_empresa):
        self.__nombre_empresa = nombre_empresa
        self.__conciertos = []

    def agregar_concierto(self, concierto):
        self.__conciertos.append(concierto)

    def eliminar_concierto(self):
        self.conciertos.remove(concierto)

    def mostrar_conciertos():
        for i in range(self.conciertos)
        print (f"Los conciertos que actualmente tenemos a la ventas son: {conciertos}")