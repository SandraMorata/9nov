

# Desarrolla un programa que solicite la calificación de un examen (0 a 100) 
# y devuelva el rango de desempeño basado en la puntuación: insuficiente, 
# suficiente, bien, muy bien, o excelente.

calificacion = int(input("Introduce la calificación del examen (0-100): "))
if calificacion < 60:
    print("Insuficiente")
else:
    if calificacion < 70:
        print("Suficiente")
    else:
        if calificacion < 80:
            print("Bien")
        else:
            if calificacion < 90:
                print("Muy bien")
            else:
                print("Excelente")

#yo
nota = int(input("Introduce tu nota:"))
if nota < 0 or nota > 100:
    print("Nota no valida. Introduce tu nota (del 0 al 100):")
else:
    if nota < 50:
        print ("insuficiente")
    elif 50 <= nota < 60:
        print ("bien")
    else:
        print ("excelente")