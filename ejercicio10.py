dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

productos = []
precios = []
ventas = []

for i in range(4):
    nombre = input(f"Ingrese el nombre del producto {i+1}: ")
    productos.append(nombre)

    precio = float(input(f"Ingrese el precio de {nombre}: "))
    precios.append(precio)

# Cargar ventas
for i in range(4):
    fila = []
    print(f"\nIngrese las ventas de {productos[i]}:")

    for j in range(7):
        cantidad = int(input(f"{dias[j]}: "))
        fila.append(cantidad)

    ventas.append(fila) 

print("\nMatriz de ventas:")
for i in range(4):
    print(productos[i], ventas[i])

print("\nTotal vendido y recaudado por cada producto:")

mayor_producto = 0
nombre_producto = ""

for i in range(4):
    total = sum(ventas[i])
    recaudado = total * precios[i]

    print(f"""
Producto: {productos[i]}
Total vendido: {total}
Total recaudado: ${recaudado}
""")

    if total > mayor_producto:
        mayor_producto = total
        nombre_producto = productos[i]

mayor_dia = 0
nombre_dia = ""

for j in range(7):
    total_dia = 0

    for i in range(4):
        total_dia += ventas[i][j]

    if total_dia > mayor_dia:
        mayor_dia = total_dia
        nombre_dia = dias[j]

print(f"\nEl día con mayores ventas fue {nombre_dia} con {mayor_dia} ventas")
print(f"El producto más vendido de la semana fue {nombre_producto} con {mayor_producto} ventas")