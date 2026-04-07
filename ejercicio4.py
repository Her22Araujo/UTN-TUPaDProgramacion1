lista_rep = []
lista_sin_rep = []

for i in range(20):
        
        add = input("Ingrese un numero a la lista ")
        
        if add.isdigit():
            lista_rep.append(add)
            
            if add.isdigit() and add not in lista_sin_rep:    
                lista_sin_rep.append(add)
            
        else:
            print("ingrese un valor valido")
            
print(f"Lista con repeticiones: {lista_rep}")    
print(f"Lista sin repeticiones: {lista_sin_rep}")
