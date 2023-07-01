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

# ----- Generación de Informes ----- 

# ----- Sistema de Pagos -----

# ----- Sistema de gráficos -----
