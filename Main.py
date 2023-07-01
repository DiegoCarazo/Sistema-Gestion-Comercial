# Librerías
import json


# Gestión de Información

# Registro de usuarios
def personal():
    nombre = input('Nombre: ')
    correo = input('Correo: ')
    direccion = input('Dirección: ')
    telefono = int(input('Numero de teléfono: '))

    lista_datos = [correo, direccion, telefono]

    temp_dic = {}
    temp_dic.update({nombre: lista_datos})

    return temp_dic


# Gestión de clientes
def clientes():
    nombre = input('Nombre: ')
    correo = input('Correo: ')
    direccion = input('Direccion: ')
    telefono = int(input('Numero de teléfono: '))
    lista_datos = [correo, direccion, telefono]

    temp_dic = {}
    temp_dic.update({nombre: lista_datos})

    return temp_dic


# Registro de proveedores 
def proveedores():
    nombre = input('Nombre: ')
    correo = input('Correo: ')
    direccion = input('Direccion: ')
    telefono = int(input('Numero de teléfono: '))
    lista_datos = [correo, direccion, telefono]

    temp_dic = {}
    temp_dic.update({nombre: lista_datos})

    return temp_dic


dic_personal = personal()

# uso del gestion de información
with open('Datos personal.jason', 'a') as f:
    json.dump(dic_personal, f, indent=4)

# Gestión de Inventarios de Ventas:
# Registro de ventas

# Actualización de inventario

# Control de stock
inventario = {
    # articulo : [Precio, proveedor, IVA]
    'Camiseta': [5500, 'Nike', 0.13],
    'Pantalones': [12000, 'Adidas', 0.04],
    'Proteína': [35000, 'Builder', 0.02],
    'Pesas': [40000, 'Builder', 0.01]
}


# Cálculo del IVA:
# Valores de IVA configurables | IVA localizado en el inventario
def calculo_iva():
    print(inventario)
    articulo = input('Escriba el nombre: ')
    iva = inventario[articulo][2]
    precio = inventario[articulo][0]
    calculo = precio + precio * iva
    print(calculo)


calculo_iva()

# Generación de Informes:
# Informes de ventas

# Informes de inventario

# Informes de clientes

# Registro de productos

# Sistema de Pagos
# Registro de métodos de pago

# Selección de método de pago

# Integración de correo electrónico
