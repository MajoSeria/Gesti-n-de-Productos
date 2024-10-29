import os

productos = []

def cargar_datos():
    if os.path.exists("productos.txt"):
        with open("productos.txt", "r") as file:
            for linea in file:
                nombre, precio, cantidad = linea.strip().split(",")
                productos.append({
                    "nombre": nombre,
                    "precio": float(precio),
                    "cantidad": int(cantidad)
                })
    else:
        print("El archivo 'productos.txt' no existe. Se creará cuando se guarden los productos.")

def guardar_datos():
    with open("productos.txt", "w") as file:
        for producto in productos:
            file.write(f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n")
    print("Datos guardados correctamente en 'productos.txt'.")

def añadir_producto():
    nombre = input("Introduce el nombre del producto: ")
    
    while True:
        try:
            precio = float(input("Introduce el precio del producto: "))
            break
        except ValueError:
            print("Por favor, introduce un número válido para el precio.")

    while True:
        try:
            cantidad = int(input("Introduce la cantidad del producto: "))
            break
        except ValueError:
            print("Por favor, introduce un número entero válido para la cantidad.")

    productos.append({
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    })
    print(f"Producto '{nombre}' añadido correctamente.")

def ver_productos():
    if productos:
        print("\nLista de productos:")
        for producto in productos:
            print(f"Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")
    else:
        print("No hay productos en el inventario.")

def actualizar_producto():
    nombre = input("Introduce el nombre del producto a actualizar: ")
    for producto in productos:
        if producto['nombre'] == nombre:
            print(f"Producto encontrado: {producto}")
            nuevo_nombre = input(f"Nuevo nombre (deja en blanco para mantener '{producto['nombre']}'): ") or producto['nombre']
            
            while True:
                nuevo_precio = input(f"Nuevo precio (deja en blanco para mantener {producto['precio']}): ")
                if nuevo_precio == "":
                    nuevo_precio = producto['precio']
                    break
                try:
                    nuevo_precio = float(nuevo_precio)
                    break
                except ValueError:
                    print("Por favor, introduce un número válido para el precio.")

            while True:
                nuevo_cantidad = input(f"Nueva cantidad (deja en blanco para mantener {producto['cantidad']}): ")
                if nuevo_cantidad == "":
                    nuevo_cantidad = producto['cantidad']
                    break
                try:
                    nuevo_cantidad = int(nuevo_cantidad)
                    break
                except ValueError:
                    print("Por favor, introduce un número entero válido para la cantidad.")

            producto['nombre'] = nuevo_nombre
            producto['precio'] = nuevo_precio
            producto['cantidad'] = nuevo_cantidad
            
            print(f"Producto '{nombre}' actualizado correctamente.")
            return
    print(f"Producto '{nombre}' no encontrado.")

def eliminar_producto():
    nombre = input("Introduce el nombre del producto a eliminar: ")
    for producto in productos:
        if producto['nombre'] == nombre:
            productos.remove(producto)
            print(f"Producto '{nombre}' eliminado correctamente.")
            return
    print(f"Producto '{nombre}' no encontrado.")

def menu():
    cargar_datos()
    while True:
        print("\n1: Añadir producto")
        print("2: Ver productos")
        print("3: Actualizar producto")
        print("4: Eliminar producto")
        print("5: Guardar datos y salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            añadir_producto()
        elif opcion == '2':
            ver_productos()
        elif opcion == '3':
            actualizar_producto()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            guardar_datos()
            break
        else:
            print("Por favor, selecciona una opción válida.")

menu()
