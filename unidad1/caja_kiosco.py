total_desc = 0
total_sin_desc = 0
total_ahorro = 0
total_con_desc = 0
productos=[]
while True:
    nombre_cl = input("Hola ingresa tu nombre: ").strip()
    if(nombre_cl.isalpha()):
        print(f"Bienvenido {nombre_cl}!")
        break
    else:
        print("Error, el nombre ingresado no es valido") 
    
while True:
    cont_produc = input("¿Cuantos productos desea ingresar?").strip()
    if (cont_produc.isdigit() and cont_produc !="" and int(cont_produc) >0):
        cont_prod = int(cont_produc)
        print(f"Vas a ingresar {cont_prod}")
        break
    else:
        print("Error, cantidad de productos ingresados invalido")

for i in range (cont_prod):
    while True:
        prec_prod = input(f"Ingrese el precio del producto {i + 1 }: ").strip()
        if (prec_prod.replace(".","").isdigit() and prec_prod!= "" and float(prec_prod) > 0 ):
            precio= float(prec_prod)
            print("Carga Exitosa")
            total_sin_desc += precio
            break
        else:
            print("Error en la lectura de precio")
    
    
    descuento = 0 

    while True:
        desc = input("¿El producto tiene descuento? (S/N)").lower()
        if(desc == "s"):
            descuento = (precio*10)/100
            break
        elif (desc == "n" and desc.replace(" ","") != ""):
            print("Elemento sin descuento")
            break
        else: 
            print("opcion invalida, vuelva a intentarlo")

    total_desc+=descuento
    productos.append((precio, desc))
    
        

###total con descuento
total_con_desc = total_sin_desc - total_desc
promedio= total_con_desc / cont_prod
print("")
print("=======TICKET=======")
print(f"""
cliente : {nombre_cl}
cantidad de productos: {cont_prod}
""")
print("-"*40)
for i, (precio, desc) in enumerate(productos):
    print(f"Producto {i+1} - precio: {precio:.2f} Descuento : {desc}")
print("-"*40)
print(f"""        
Total sin descuentos : ${total_sin_desc:.2f}
Total con descuentos : ${total_con_desc:.2f}
Ahorro total: ${total_desc:.2f}
Promedio por producto comprado: ${promedio:.2f}
""")
print("="*40)