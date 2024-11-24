class Rectangulo:
    def __init__ (self,largo,ancho):
        self.largo = largo
        self.ancho = ancho

    def calcular_area (self):
        return (self.largo * self.ancho)
    
    def calcular_perimetro (self):
        return (2*(self.largo+self.ancho))
    
Rectangulo1 =  Rectangulo(100,50)
print(Rectangulo1.calcular_area())
print(Rectangulo1.calcular_perimetro())

Rectangulo2=Rectangulo(20,40)
print(Rectangulo2.calcular_area())
print(Rectangulo2.calcular_perimetro())

print(f"---------------otro ejercicio-------------------")
#simulador cuenta bancaria
class CuentaBancaria:
    def __init__ (self,saldo=0):
        self.saldo = saldo
    
    def depositar(self,cantidad):
        if cantidad > 0:
            self.saldo += cantidad #sumar al saldo
        else:
            raise ValueError("La cantidad a depositar debe ser positiva")

    def retirar(self,cantidad):
        if cantidad > 0:
            if self.saldo >= cantidad:
                self.saldo -= cantidad
            else:
                raise ValueError("Fondos insufientes")
        else:
            raise ValueError("La cantidad a sacar debe ser positiva")
        
    def mostrar_saldo(self):
        print(f"El saldo actual es {self.saldo}")

Micuenta=CuentaBancaria(100)
Micuenta.depositar(50)
#Micuenta.retirar(200)
Micuenta.retirar(50)
Micuenta.mostrar_saldo()

print(f"---------------otro ejercicio-------------------")

class Persona:
    def __init__ (self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def saludar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} anos.")

class Agenda:
    def __init__(self):
        self.contactos = []

    def agregar_contacto (self,contacto):
        self.contactos.append (contacto)
        print(f"Se ha agregado a {contacto.nombre} a la agenda.")
    def mostrar_contactos (self):
        if self.contactos:
            print("Los contactos que hay en aesta agenda son:")
            for contact in self.contactos:
                print(f"- {contacto.nombre}, {contacto.edad} anos.")
        else:
           print("La agenda esta vacia.") 

Persona1=Persona("Desire",30)
Persona2=Persona("Pulgosa",8)
Persona3=Persona("Daniela",40)


Agenda1=Agenda()
Agenda1.agregrar_contacto(Persona1)
Persona2.agrerar_contacto(Persona2)
Persona3.agrerar_contacto(Persona3)

Agenda1.mostrar_contactos()


