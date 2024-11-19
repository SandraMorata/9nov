

# Escribe un programa que pida la edad del usuario y clasifique a las personas en diferentes categorías (niño, adolescente, adulto, adulto mayor). Supón los siguientes rangos de edad:

# Niño: Menos de 13 años.
# Adolescente: De 13 a 19 años.
# Adulto: De 20 a 64 años.
# Adulto mayor: 65 años o más.

edad = int(input("Introduce tu edad: "))
if edad < 13:
    print("Eres un niño.")
else:
    if edad < 20:
        print("Eres un adolescente.")
    else:
        if edad < 65:
            print("Eres un adulto.")
        else:
            print("Eres un adulto mayor.")

#yo
edad = int(input("Introduce tu edad:"))
if edad < 13: 
    print ("Nino")
elif 13 <= edad <= 19:
    print ("Adolescente")
elif 20 <= edad <= 64:
    print ("Adulto")
else:
    print ("Adulto mayor")