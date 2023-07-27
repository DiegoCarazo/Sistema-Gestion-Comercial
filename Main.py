import json
from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry('800x600')
root.config(background='white')


def gestionar_info():
    Label(text="Sistema de gestion de usuarios", background="white", font=("Arial", 12)).grid(row=1, column=2)

    def agregar_personal():
        # La información se guarda en un archivo "Json"
        def guardar_personal(nombre_dato, correo_dato, direccion_dato, telefono_dato, puesto_dato):
            proovedor = {nombre_dato: [correo_dato, direccion_dato, telefono_dato, puesto_dato]}
            with open("DB_Personal.json", "a") as fp:
                json.dump(proovedor, fp, indent=4)

        Label(text="Nombre: ", background="white", font=("Arial", 12)).grid(row=3, column=1)
        Label(text="Correo: ", background="white", font=("Arial", 12)).grid(row=4, column=1)
        Label(text="Dirección: ", background="white", font=("Arial", 12)).grid(row=5, column=1)
        Label(text="Teléfono: ", background="white", font=("Arial", 12)).grid(row=6, column=1)
        Label(text="Puesto", background="white", font=("Arial", 12)).grid(row=7, column=1)

        # Introducción de información
        nombre = ttk.Entry(root)
        correo = ttk.Entry(root)
        direccion = ttk.Entry(root)
        telefono = ttk.Entry(root)
        puesto = ttk.Entry(root)

        # Parte visual de las Entry
        nombre.grid(row=3, column=2)
        correo.grid(row=4, column=2)
        direccion.grid(row=5, column=2)
        telefono.grid(row=6, column=2)
        puesto.grid(row=7, column=2)

        ttk.Button(root, text="Guardar",
                   command=lambda: guardar_personal(nombre.get(), correo.get(), direccion.get(), telefono.get(),
                                                    puesto.get())).grid(row=8, column=3)

    def agregar_cliente():
        #  La información se guarda en un archivo "Json"
        def guardar_cliente(nombre_dato, correo_dato, telefono_dato, empresa_dato):
            cliente = {nombre_dato: [correo_dato, telefono_dato, empresa_dato]}
            with open("DB_Cliente.json", "a") as fp:
                json.dump(cliente, fp, indent=4)

        Label(text="Nombre: ", background="white", font=("Arial", 12)).grid(row=3, column=1)
        Label(text="Correo: ", background="white", font=("Arial", 12)).grid(row=4, column=1)
        Label(text="Teléfono: ", background="white", font=("Arial", 12)).grid(row=5, column=1)
        Label(text="Empresa: ", background="white", font=("Arial", 12)).grid(row=6, column=1)

        # Introducción de información
        nombre = ttk.Entry(root)
        correo = ttk.Entry(root)
        telefono = ttk.Entry(root)
        empresa = ttk.Entry(root)

        # Parte visual de las Entry
        nombre.grid(row=3, column=2)
        correo.grid(row=4, column=2)
        telefono.grid(row=5, column=2)
        empresa.grid(row=6, column=2)

        ttk.Button(root, text="Guardar",
                   command=lambda: guardar_cliente(nombre.get(), correo.get(), telefono.get(), empresa.get())).grid(
            row=7, column=3)

    def agregar_proovedor():
        # La información se guarda en un archivo "Json"
        def guardar_proovedor(empresa_dato, marca_dato, producto_dato):
            trabajador = {empresa_dato: {marca_dato: producto_dato}}
            with open("DB_Proovedor.json", "a") as fp:
                json.dump(trabajador, fp, indent=4)

        Label(text="Empresa: ", background="white", font=("Arial", 12)).grid(row=3, column=1)
        Label(text="Marca: ", background="white", font=("Arial", 12)).grid(row=4, column=1)
        Label(text="Producto: ", background="white", font=("Arial", 12)).grid(row=5, column=1)

        # Introducción de información
        empresa = ttk.Entry(root)
        marca = ttk.Entry(root)
        producto = ttk.Entry(root)

        # Parte visual de las Entry
        empresa.grid(row=3, column=2)
        marca.grid(row=4, column=2)
        producto.grid(row=5, column=2)

        ttk.Button(root, text="Guardar",
                   command=lambda: guardar_proovedor(empresa.get(), marca.get(), producto.get())).grid(row=8, column=3)

    ttk.Button(root, text="Personal", command=agregar_personal).grid(row=2, column=1)
    ttk.Button(root, text="Cliente", command=agregar_cliente).grid(row=2, column=2)
    ttk.Button(root, text="Proveedor", command=agregar_proovedor).grid(row=2, column=3)


def catalogo_de_productos():
    # articulo : [Precio, proveedor, IVA, Descripción]
    def subir_datos(producto_datos, precios_datos, proveedores_datos, iva_datos, descripcion_datos):
        items = {producto_datos: [precios_datos, proveedores_datos, iva_datos, descripcion_datos]}
        with open("DB_Inventario.json", "a") as fp:
            json.dump(items, fp, indent=4)

    # Labels de la sección
    Label(text="Catalogo de productos", background="white", font=("Arial", 12)).grid(row=1, column=2)
    Label(text="Ingrese el producto y la cantidad a agregar", background="white", font=("Arial", 10)).grid(row=2,
                                                                                                           column=1,
                                                                                                           columnspan=4,
                                                                                                           sticky=W)
    Label(text="Producto: ", background="white", font=("Arial", 12)).grid(row=3, column=1, sticky=W)
    Label(text="Precio: ", background="white", font=("Arial", 12)).grid(row=4, column=1, sticky=W)
    Label(text="Proveedor: ", background="white", font=("Arial", 12)).grid(row=5, column=1, sticky=W)
    Label(text="Cantidad:  ", background="white", font=("Arial", 12)).grid(row=6, column=1, sticky=W)
    Label(text="IVA: ", background="white", font=("Arial", 12)).grid(row=7, column=1, sticky=W)

    Label(text="Descripción: ", background="white", font=("Arial", 12)).grid(row=8, column=1, sticky=W)

    # Botón de subir
    btn = ttk.Button(root, text="Subir", command=lambda: subir_datos(producto.get(), precio.get(), proveedor.get(), iva.get(), descripcion.get()))
    btn.grid(row=9, column=3)

    # Introducción de información
    producto = ttk.Entry(root)
    precio = ttk.Entry(root)
    proveedor = ttk.Entry(root)
    iva = ttk.Entry(root)
    cantidad = ttk.Entry(root)
    descripcion = ttk.Entry(root)

    # Parte visual de las Entry
    producto.grid(row=3, column=2)
    precio.grid(row=4, column=2)
    proveedor.grid(row=5, column=2)
    iva.grid(row=6, column=2)
    cantidad.grid(row=7, column=2)
    descripcion.grid(row=8, column=2)


def sistema_pagos():
    def tarjeta_pago():
        # Usada al presionar el botón
        def subir_datos():
            nombre_datos = nombre.get()
            numero_datos = numero.get()
            fecha_mes_datos = fecha_mes.get()
            fecha_ano_datos = fecha_ano.get()
            codigo_datos = codigo.get()
            monto_pago_datos = monto_pago.get()
            item_datos = item.get()
            cantidad_item_datos = cantidad_item.get()

            tarjeta_usada = {
                nombre_datos: [monto_pago_datos, item_datos, cantidad_item_datos, numero_datos, fecha_mes_datos,
                               fecha_ano_datos, codigo_datos]}
            print(tarjeta_usada)
            return tarjeta_usada

        # Labels de la sección
        Label(root, text="Ingrese los datos de la tarjeta", background="white", font=("Arial", 12)).grid(row=2,
                                                                                                         column=3,
                                                                                                         stick=W,
                                                                                                         columnspan=2)
        Label(root, text="Nombre del titular: ", background="white").grid(row=3, column=3, stick=W)
        Label(root, text="Numero de tarjeta: ", background="white").grid(row=4, column=3, stick=W)
        Label(root, text="Expiración(Mes): ", background="white").grid(row=5, column=3, stick=W)
        Label(root, text="Expiración(Año): ", background="white").grid(row=6, column=3, stick=W)
        Label(root, text="Código de seguridad: ", background="white").grid(row=7, column=3, stick=W)
        Label(root, text="Monto del pago: ", background="white").grid(row=8, column=3, stick=W)
        Label(root, text="Item comprado: ", background="white").grid(row=9, column=3, stick=W)
        Label(root, text="Cantidad comprada: ", background="white").grid(row=10, column=3, stick=W)

        # Entry de la sección
        nombre = ttk.Entry(root)
        numero = ttk.Entry(root)
        fecha_mes = ttk.Entry(root)
        fecha_ano = ttk.Entry(root)
        codigo = ttk.Entry(root)
        monto_pago = ttk.Entry(root)
        item = ttk.Entry(root)
        cantidad_item = ttk.Entry(root)

        # Entry visuales
        nombre.grid(row=3, column=4, stick=W)
        numero.grid(row=4, column=4, stick=W)
        fecha_mes.grid(row=5, column=4, stick=W)
        fecha_ano.grid(row=6, column=4, stick=W)
        codigo.grid(row=7, column=4, stick=W)
        monto_pago.grid(row=8, column=4, stick=W)
        item.grid(row=9, column=4, stick=W)
        cantidad_item.grid(row=10, column=4, stick=W)

        btn_subir = ttk.Button(root, text="Pagar", command=subir_datos)
        btn_subir.grid(row=11, column=5)

    def transferencia_pago():
        # Usada al presionar el botón
        def subir_datos():
            numero_recibo_datos = numero_recibo.get()
            monto_pago_datos = monto_pago.get()
            item_datos = item.get()
            cantidad_item_datos = cantidad_item.get()
            lista_datos = {numero_recibo_datos: [monto_pago_datos, item_datos, cantidad_item_datos]}
            print(lista_datos)
            return lista_datos

        # Labels de la sección
        Label(root, text="Cuenta a transferir: 0123456789", background="white", font=("Arial", 12)).grid(row=2,
                                                                                                         column=3,
                                                                                                         stick=W,
                                                                                                         columnspan=2)
        Label(root, text="Ingrese los datos", background="white", font=("Arial", 12)).grid(row=3,
                                                                                           column=3,
                                                                                           stick=W,
                                                                                           columnspan=2)
        Label(root, text="Numero de recibo ", background="white", font=("Arial", 12)).grid(row=4, column=3, stick=W)
        Label(root, text="Monto: ", background="white", font=("Arial", 12)).grid(row=5, column=3, stick=W)
        Label(root, text="Item: ", background="white", font=("Arial", 12)).grid(row=6, column=3, stick=W)
        Label(root, text="Cantidad: ", background="white", font=("Arial", 12)).grid(row=7, column=3, stick=W)

        # Entry para la sección
        numero_recibo = ttk.Entry(root)
        monto_pago = ttk.Entry(root)
        item = ttk.Entry(root)
        cantidad_item = ttk.Entry(root)

        # Visual para Entry
        numero_recibo.grid(row=4, column=4, stick=W)
        monto_pago.grid(row=5, column=4, stick=W)
        item.grid(row=6, column=4, stick=W)
        cantidad_item.grid(row=7, column=4, stick=W)

        btn_subir = ttk.Button(root, text="Pagar", command=subir_datos)
        btn_subir.grid(row=8, column=5)

    def efectivo_pago():
        def subir_datos(monto_pago_datos, item_datos, cantidad_item_datos):
            lista_pago = {"Efectivo": [monto_pago_datos, item_datos, cantidad_item_datos]}
            print(lista_pago)
            return lista_pago

        # Labels de la sección
        Label(root, text="Pago en efectivo", background="white", font=("Arial", 12)).grid(row=2, column=3,
                                                                                          stick=W, columnspan=2)
        Label(root, text="Monto: ", background="white", font=("Arial", 12)).grid(row=3, column=3, stick=W)
        Label(root, text="Item: ", background="white", font=("Arial", 12)).grid(row=4, column=3, stick=W)
        Label(root, text="Cantidad: ", background="white", font=("Arial", 12)).grid(row=5, column=3, stick=W)

        # sección de Entry
        monto_pago = ttk.Entry(root)
        item = ttk.Entry(root)
        cantidad_item = ttk.Entry(root)

        # Visual Entry
        monto_pago.grid(row=3, column=4, stick=W)
        item.grid(row=4, column=4, stick=W)
        cantidad_item.grid(row=5, column=4, stick=W)

        btn_subir = ttk.Button(root, text="Pagar",
                               command=lambda: subir_datos(monto_pago.get(), item.get(), cantidad_item.get()))
        btn_subir.grid(row=6, column=5)

    # Labels de la sección
    Label(root, text="Seleccione un método de pago", background="white", font=("Arial", 12)).grid(row=1, column=2)

    # Botones para los usuarios
    tarjeta = Button(root, text="Tarjeta de crédito", font=("Arial", 12), height=1, width=18, command=tarjeta_pago)
    transferencia = Button(root, text="Transferencia bancaria", font=("Arial", 12), height=1, width=18,
                           command=transferencia_pago)
    efectivo = Button(root, text="Efectivo", font=("Arial", 12), height=1, width=18, command=efectivo_pago)

    # Botones visuales
    tarjeta.grid(row=2, column=2, sticky=W)
    transferencia.grid(row=3, column=2, sticky=W)
    efectivo.grid(row=4, column=2, sticky=W)


# interfaz grafica menu principal
bienvenido = ttk.Label(root, text="Bienvenido al centro de servicio", background='white', font=("Arial", 15))
bienvenido.grid(row=0, columnspan=4, sticky=W)

usuarios = ttk.Button(root, text="Gestion de usuarios", command=gestionar_info, width=20)
usuarios.grid(row=1, column=0, sticky=W)

productos = ttk.Button(root, text="Catalogo de productos", command=catalogo_de_productos, width=20)
productos.grid(row=2, column=0, sticky=W)

pagos = ttk.Button(root, text="Sistema pagos", command=sistema_pagos, width=20)
pagos.grid(row=3, column=0, sticky=W)

root.mainloop()
