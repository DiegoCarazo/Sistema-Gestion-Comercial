# Librerías
from inventario import *
from datosUsuarios import *


# ----- Gestión de Información -----
# Registro de usuarios
def Gestión_de_Información():
    clase = input('Selecciones "personal", "cliente o "proovedor": ')
    nombre = input('Nombre: ')
    correo = input('Correo: ')
    direccion = input('Dirección: ')
    telefono = int(input('Numero de teléfono: '))
    lista_datos = [nombre, correo, direccion, telefono]
    temp_dic= {clase: lista_datos}
    return temp_dic

# Gestión_de_Información_dic = {'Tipo': ['Nombre', 'Correo', 'Direccion', Telefono]}
Gestión_de_Información_dic.update(Gestión_de_Información())
print(Gestión_de_Información_dic)


# ----- Catálogo de Productos -----
def catalogo_de_productos():
    producto = input('Nombre del producto: ')
    precio = int(input('Precio: '))
    proveedor = input('Proovedor: ')
    iva = float(input('IVA a aplicar: '))
    descripcion = input('Descripcion: ')
    lista_datos = [precio, proveedor, iva, descripcion]
    temp_dic = {producto: lista_datos}
    return temp_dic
 

# articulo : [Precio, proveedor, IVA, Descripcion]
inventario.update(catalogo_de_productos())


# ----- Cálculo del IVA -----
# Valores de IVA configurables | IVA localizado en el inventario
def calculo_iva():
    print(inventario)
    articulo = input('Escriba el nombre: ')
    iva = inventario[articulo][2]
    precio = inventario[articulo][0]
    calculo = precio + precio * iva
    print('El precio final con el iva del', iva *100, 'es de: ', calculo)


calculo_iva()

# ----- Gestión de Inventarios de Ventas -----
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


# ----- Generación de Informes ----- 
def generar_informe_ventas():
#imprimir encabezado del informe de ventas
    print("Informe de Ventas")
#buscar la venta en la lista de ventas
    for venta in ventas:
#obtener los valores de cada venta 
        producto = venta["producto"]
        cantidad = venta["cantidad"]
        precio = venta["precio"]
        monto_total = cantidad * precio
#imprimir el informe        
print("Producto:", producto)
print("Cantidad vendida:", cantidad)
print("Monto total:", monto_total)

# ----- Sistema de Pagos -----

# ----- Sistema de gráficos -----
