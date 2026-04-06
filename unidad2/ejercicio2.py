productos =[]
for i in range(5):
    produ=input(f"Ingrese el {i+1}° producto a cargar ")   
    productos.append(produ)
    
productos.sort()

while True:
    print(f"Estos con los productos cargados {productos}")
    
    op = input("Desea eliminar alguno producto de la lista?")
    
    if op.lower() == "si":
        print("Que elemento desea eliminar ? ")
        delt= input("").lower()
        if delt not in productos:
            print("elemento no encontrado")
        else:
            productos.remove(delt)
    else:
        print("elemento ingresado es invalido")
        break
        
    print(productos)