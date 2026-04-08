while True:
    nombre_cliente = input("Bienvenido, escriba su nombre aquí: ").strip()

    if nombre_cliente == "":
        print("Error: no puede estar vacio.")
    elif not nombre_cliente.replace(" ", "").isalpha():
        print("Error: el nombre solo debe contener letras.")
    else:
        break

while True:
    cantidad_productos = input("Escriba la cantidad de productos que quiere comprar: ")

    if cantidad_productos == "":
        print("Error: tienes que ingresar la cantidad de productos que quiere comprar.")
    elif not cantidad_productos.isdigit():
        print("Error: debe ser un numero entero positivo.")
    else:
        cantidad_productos = int(cantidad_productos)

        if cantidad_productos > 0:
            break
        else:
            print("Error: debe ser mayor que 0.")

total_sin_descuento = 0
total_con_descuento = 0

precios = []
descuentos = []

for productos in range(cantidad_productos):
    while True:
        precio = input(f"Escriba el precio del producto {productos + 1}: ")
            
        if precio == "":
            print("Error: tienes que escribir el precio.")
        elif not precio.isdigit():
            print("Error: debe ser un numero entero positivo.")
        else:
            precio = int(precio)

            if precio > 0:
                break
            else:
                print("Error: debe ser mayor que 0.")

    while True:
        descuento = input("¿Su producto tiene descuento? S/N ").strip().upper()
        
        if descuento == "":
            print("Error: no puede estar vacío.")
        elif descuento not in ["S", "N"]:
            print("Error: opción inválida.")
        else:
            break

    precios.append(precio)
    descuentos.append(descuento)

    total_sin_descuento += precio

    if descuento == "S":
        print("Descuento aplicado.")
        total_con_descuento += precio * 0.9
    else:
        print("No se aplicó descuento.")
        total_con_descuento += precio

print(f"\nCliente: {nombre_cliente}")
print(f"Cantidad de productos: {cantidad_productos}")

for i in range(cantidad_productos):
    print(f"Producto {i + 1} - Precio: {precios[i]} Descuento (S/N): {descuentos[i]}")

print(f"Total con descuentos: ${total_con_descuento:.2f}")
print(f"Total sin descuentos: ${total_sin_descuento:.2f}")

print("")

ahorro = total_sin_descuento - total_con_descuento
promedio = total_con_descuento / cantidad_productos

print(f"Ahorro: ${ahorro:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")

