class Event():        #CamelCase
    def __init__ (self):  #constructor de mi clase. dando estado inicial

        self.artista = "artista"       #Atributo que cambia
        self.__promotor = "LiveNation"     #Atributo que no cambia, encapsulado para evitar cambio fuera de la clase
        self.aforo = "aforo" #cuantos tickets totales hay a la venta 
        self.onsale=False #no esta a la venta todavia
        self.categoria = "categoria" #categoria musica, arte, teatro y deportes

    def en_venta(self,arrancamos):               #creo el metodo (funcion(self))
        self.onsale=True              #Tourbonito.enventa=True
        self.onsale=arrancamos        #self va a ser lo que le  pongamos en arrancamos
        if (self.en_venta):         #si la variable true es true, x eso no ponemos nada
            return" "
        
    def activado(self):               #
        if(self.onsale):
            return "El evento ya ha salido a la venta"
        else:
            return "El evento todavia no ha salido a la venta"
        
    def __chequeo_interno(self):
            print("realizando chequeo interno")

        self.gasolina="ok"
        self.aceite="ok"
        self.puertas="cerradas"
    
        if(self.gasolina=="ok" and self.aceite=="ok" and self puertas=="cerradas")


tour_bonito=Event()    #intancio la clase Event

print("El promotor es " ,tour_bonito.promotor)
print("El promotor es ", tour_bonito, " como todos")  #borrar
tour_bonito.en_venta()
print(tour_bonito.activado())

print("------------------A continuacion creamos el segundo objeto -----------")

tour_oxigeno=Event() #Creo el segundo objeto
print("El promotor es " ,tour_oxigeno.promotor)
print("El promotor es ", tour_oxigeno, " como todos")

print(tour_bonito.activado())
