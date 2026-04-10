lista_nombres = ["Ana", "Luis", "Carlos", "Maria", "Sofia", "Jorge", "Lucia", "Diego", "Valentina", "Martin"]


while True:
    buscar_nombre = input("ingrese el nombre del alumno a buscar: ")
    
    for i in range(1):
        if buscar_nombre not in lista_nombres:
                print("El nombre ingresado no esta en la lista !")
        elif buscar_nombre.lower() in lista_nombres.lower():
            posicion= lista_nombres.index(buscar_nombre)
            print(f"Nombre encontrado, se encuentra en la posicion {posicion}")