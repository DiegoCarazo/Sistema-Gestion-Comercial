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

