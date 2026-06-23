# Sistema de Ventas - Paso 2
# Estudiante: Nicol
# Fecha: 22/06/2026

while True:  # Bucle para vender varios productos
    # Entrada de datos
    Precio = float(input("Precio del producto: $"))
    cantidad = int(input("Cantidad: "))
    
    # Proceso: calcular subtotal
    subtotal = Precio * cantidad
    
    # Condicional: descuento por cantidad
    if cantidad >= 10:
        descuento = subtotal * 0.10
        total = subtotal - descuento
        print(f"Subtotal: ${subtotal}")
        print(f"Descuento 10%: -${descuento}")
        print(f"Total a pagar: ${total}")
    else:
        total = subtotal
        print(f"Total a pagar: ${total}")
    
    # Preguntar si sigue
    seguir = input("¿Otro producto? s/n: ")
    if seguir != "s":
        print("Gracias por tu compra!")
        break
