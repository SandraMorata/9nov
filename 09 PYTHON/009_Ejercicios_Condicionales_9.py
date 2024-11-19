

# Programa un sistema que categorice los ingresos anuales de una persona 
# como 'bajo', 'medio' o 'alto'. Define tú mismo los límites de cada categoría.

ingresos = float(input("Introduce tus ingresos anuales: "))
if ingresos < 20000:
    print("Tus ingresos son bajos.")
else:
    if ingresos < 50000:
        print("Tus ingresos son medios.")
    else:
        print("Tus ingresos son altos.")

#yo
ingresos = float(input("Introduce aqui tus ingresos en Euros:"))
if ingresos > 100000:
    print("tus ingresos son altos")
elif 30000 <= ingresos <= 100000:
    print("Tus ingesos son medios")
else:
    print("tus ingresos son bajos")