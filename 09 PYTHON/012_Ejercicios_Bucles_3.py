



# Dado un string, utiliza un bucle for para contar cuántas veces aparece la 
# letra 'a' en el string.

texto = "banana"
contador = 0
for caracter in texto:
    if caracter == 'a':
        contador += 1
print(f"La letra 'a' aparece {contador} veces en la palabra {texto}.")


#yo
palabra = "banana"
count = 0
for caracter in palabra:
    if caracter == "a":
        count +=1
print(f"El caracter a en la palabra {palabra} se encuentra {count} veces.")