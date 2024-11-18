

# Un almacén da un descuento del 15% si la compra del cliente supera los 1000 Euros. 
# Escribe un programa que pida el total de la compra y calcule el descuento 
# (si aplica) y el total a pagar.

# Solicita al usuario que ingrese el total de la compra
total_compra = float(input("Ingresa el total de la compra: $"))

# Verifica si el total de la compra supera los 1000 dólares
if total_compra > 1000:
    # Calcula el descuento
    descuento = total_compra * 0.15
    # Redondea el descuento a dos decimales
    descuento_redondeado = round(descuento, 2)
    # Calcula el total final aplicando el descuento redondeado
    total_final = total_compra - descuento_redondeado
    # Redondea el total final a pagar a dos decimales
    total_final_redondeado = round(total_final, 2)
    # Imprime el total final a pagar y el descuento aplicado
    print(f"Se aplicó un descuento de ${descuento_redondeado}, total a pagar: ${total_final_redondeado}")
else:
    # Si no se aplica descuento, el total a pagar es el mismo que el total de la compra
    # Redondea el total de la compra a dos decimales
    total_compra_redondeado = round(total_compra, 2)
    print(f"No se aplicó descuento, total a pagar: ${total_compra_redondeado}")

#yo
total_compra = float(input("Ingrese el total de su compra:"))
if total_compra > 1000:
    descuento = total_compra * 0.15
    total_con_descuento = total_compra - descuento
    print("Congrats! Tu compra supera los 1000euros y tiene un descuento del 15%, es decir, de {}. Por lo que su compra es {} euros.".format(descuento,total_con_descuento))
else:
    print("Tienes que comprar mas. si superas los 1000euros tendras un descuento del 15%. Lo sentimos, tu compra no tiene descuento")