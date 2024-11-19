

# Una tienda ofrece descuentos basados en el total de compra. 
# Si la compra es mayor a $100, el descuento es del 10%. Si es mayor a $500, 
# el descuento es del 20%. Crea un programa que calcule el total a pagar 
# después del descuento.

compra = float(input("Introduce el total de la compra: $"))
if compra > 500:
    total = compra * 0.8
    print(f"El total después del descuento es: ${total:.2f}")
else:
    if compra > 100:
        total = compra * 0.9
        print(f"El total después del descuento es: ${total:.2f}")
    else:
        print(f"No hay descuento. El total es: ${compra:.2f}")


#yo
√compra = float(input("Introduce el precio de tu compra en dolares:"))
if compra > 500:
    descuento = compra * 0.20
    compra_total = compra - descuento
    print("congrats, tu compra tiene un descuento de ${:.2f} y se queda en ${:.2f}.".format(descuento,compra_total))
elif compra > 100:
    descuento = compra * 0.10
    compra_total = compra - descuento
    print("congrats, tu compra tiene un descuento de ${:.2f} y se queda en ${:.2f}.".format(descuento,compra_total))
else:
    print("no hay descuento")