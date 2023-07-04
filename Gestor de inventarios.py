print("Bienvenido al Programa de Gestión de Inventarios: ")
cantidades = []
productos = []
precios = []

while True:
    print("""
    (1) Añadir productos
    (2) Buscar productos
    (3) Modificar productos
    (4) Ver productos
    (5) Salir
    """)

    respuesta = int(input("Ingresa una de las opciones: "))

    if respuesta == 1:
        cantidad = int(input("Ingresa la cantidad del producto: "))
        producto = input("Ingresa el nombre del producto: ")
        precio = int(input("Ingresa el precio del producto: "))

        cantidades.append(cantidad)
        productos.append(producto)
        precios.append(precio)
    elif respuesta == 2:
        buscador = input("Ingresa el nombre del producto que deseas buscar: ")
        posicion = productos.index(buscador)
        print("La cantidad del producto es: ", cantidades[posicion])
        print("El nombre del producto es: ", productos[posicion])
        print("El precio del producto es: ", precios[posicion])
    elif respuesta == 3:
        buscador = input("Ingresa el nombre del producto que deseas modificar: ")
        posicion = productos.index(buscador)
        cantidad = int(input("Ingresa la cantidad del producto: "))
        producto = input("Ingresa el nombre del producto: ")
        precio = int(input("Ingresa el precio del producto: "))
        cantidades[posicion] = cantidad
        productos[posicion] = producto
        precios[posicion] = precio
    elif respuesta == 4:
        print("La cantidad es: ", cantidades)
        print("El nombre es: ", productos)
        print("El precio es: ", precios)
    else:
        break
