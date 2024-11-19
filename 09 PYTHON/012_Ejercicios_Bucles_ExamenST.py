# Escribe un programa que sume todos los números enteros del 1 al 100 usando un bucle for.
suma = 0
for numero in range (1,101):
    suma += numero
print("La suma de los numeros de 1 al 100 es:", suma)



# Utiliza un bucle for para generar e imprimir la lista de los cuadrados 
# de los primeros 10 números enteros (1 al 10).
cuadrados = []
for numero in range (1,11):
    cuadrados.append (numero **2)
print("Los cuadrados de los numeros del 1 al 10 es" , cuadrados)

# Dado un string, utiliza un bucle for para contar cuántas veces aparece la 
# letra 'a' en el string.
palabra = "trabajo"
count = 0
for letra in palabra:
    if letra == "a":
     count += 1
print(f"La letra a en la palabra {palabra} aparece {count} veces.")


# Escribe un programa que imprima la tabla de multiplicar del número 7, 
# desde el 7x1 hasta el 7x10, usando un bucle for.
numero = 7
numero8 = 8
for i in range(0,11):
    resultado = (i*numero)
    print(f"{numero} * {i} = {resultado}")

    resultado8 = (i*numero8)
    print(f"La tabla del 8 es:n\ {numero8}) * {i} = {resultado8}")
    
# Escribe un script que cuente desde 1 hasta un número n proporcionado por 
# el usuario, imprimiendo cada número.

n = int(input("Introduce un numero:"))
contador = 1
while contador <=n:
    print (contador)
    contador += 1



# Crea un programa que sume números introducidos por el usuario hasta que el 
# usuario introduzca 0. Al final, el programa debe mostrar la suma total.
suma = 0
numero = int(input("Ingresa un numero (0 para terminar:"))
while numero != 0:
    suma += numero
    numero = int(input("Ingresa un numero (0 para terminar:"))
print("La suma de los numeros introducidos es:", suma)


# Implementa un programa que le pida al usuario introducir números hasta que 
# introduzca el número 5. Cuando eso ocurra, el programa debe imprimir un 
# mensaje indicando que se encontró el número 5
numero = int(input("Introduce un numero:"))
while numero !=5:
    numero = int(input("Introduce un numero:"))
print("Numero 5 encontrado")


# Escribe un script que solicite al usuario su edad y asegúrate de que el 
# número proporcionado esté entre 1 y 100. Si el número está fuera de ese rango, 
# pídele que lo introduzca nuevamente.
edad = int(input("Introduce tu edad:"))
while edad < 1 or edad > 100:
    print("La edad introducida no es valida.") 
    edad = int(input("Introduce tu edad:"))
else:
    print("Gracias, tu edad ha sido validada")


#Escribe un programa que sume todos los números enteros del 1 al 100 utilizando un bucle for.

suma = 0
for i in range (1,101):
    suma += i
    print("la suma de los numeros del 1 al 100 es", suma)


#Usa un bucle for para generar e imprimir la lista de los cuadrados de los primeros 10 números enteros (del 1 al 10).
lista = []
for i in range (1,11):
    lista.append(i ** 2)
print("la lista de los cuadrados del 1 al 10 es:", lista)

#Dado un string, utiliza un bucle for para contar cuántas veces aparece la letra 'a' en el string.

palabra = "banana"
contador = 0
letra = "a"
for i in palabra:
    if i == "a":
        contador +=1
print("La {} aparece {} veces en {}.".format(letra,contador,palabra))

#tabla del 10
numero = 10
for i in range (1,11):
    resultado = (i*numero)
    print(f"{numero} * {i} = {resultado}")