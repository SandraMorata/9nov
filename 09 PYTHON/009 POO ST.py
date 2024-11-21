class Event():        #CamelCase
    artista = "artista"       #Atributo que cambia
    promotor = "LiveNation"     #Atributo que no cambia
    aforo = "aforo" #cuantos tickets totales hay a la venta 
    onsale=False #no esta a la venta todavia
    categoria = "categoria" #categoria musica, arte, teatro y deportes

    def en_venta(self):               #creo el metodo (funcion(self))
        self.onsale=True              #Tourbonito.enmarcha=True


    def activado(self):               #
        if(self.onsale):
            return "El evento ya ha salido a la venta"
        else:
            return "El evento todavia no ha salido a la venta"

tour_bonito=Event()    #intancio la clase Event

print("El promotor es " ,tour_bonito.promotor)
print("El promotor es ", tour_bonito, " como todos")
tour_bonito.en_venta()
print(tour_bonito.activado())


