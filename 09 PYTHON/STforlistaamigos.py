#lista de amigis
nombres=["Sandra","Desi","Iris","Ro","Carolina"]
#imprimir los nombres de amigis
for nombre in nombres:
    print(nombre)
#imprimir los numeros de 1 al 10
for i in range(1,11):   
    print(i)
#imprimir los numeros del 1 al 20 y decir si es par o impar
for i in range(1,21):
    if i % 2 == 0:
        print(f"{i} es par")
    else:
        print(f"{i} es impar")
#usar un buble for para recorrer del 1 al 10 y sumarlos, imprimir el resultado

suma = 0
for i in range(1, 11):
    suma += i
print(f"La suma de los primeros 10 números es {suma}")
#tabla de multiplicar del 5 (del 5*1 al 5*10)
for i in range(1,11):
    print(f"5 x {i} = {5 * i}")
#contar cuantos numeros negativos en una lista
numeros = [-1,3,5,2,4,-3]
contador_negativos = 0
for num in numeros:
    if num < 0:
        contador_negativos += 1
print(f"Hay {contador_negativos} numeros negativos en la lista")
