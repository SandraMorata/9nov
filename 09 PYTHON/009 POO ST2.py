class Vehiculos():
    def __init__(self,marca, modelo): #constructor
        
        self.marca=marca #se lo tenemos que pasar
        self.modelo=modelo
        self.enmarcha=False #x defecto no esta en marcha
        self.acelera=False
        self.frena=False

    def arrancar(self):
        self.enmarcha=True

    def acelerar(self):
        self.acelera=True

    def frenar(self):
        self.frena=True

    def estado(self): #recibe por parametro self
        print ("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ", self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: " , self.frena)

class Moto(Vehiculos): #nuestra clase moto hereda de vehiculos
    pass

miMoto=Moto("Honda", "CBR")
miMoto.estado()