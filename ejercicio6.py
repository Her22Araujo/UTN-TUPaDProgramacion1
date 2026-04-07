num = []

while True:
        for i in range (7):
                numeros =input(f"Ingresa el {i+1}° un numero ")
                if numeros.isdigit() and numeros != 0:
                    num.append(numeros)
                else:
                    print("Error en el ingreso de los datos")
        
        print(f"Los numeros ingresados son: {num}")
        num.reverse()
        print(f"Con el orden alterado es: {num}")