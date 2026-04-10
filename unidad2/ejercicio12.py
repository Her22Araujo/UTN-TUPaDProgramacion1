num_enteros = []
for i in range(8):
    num=int(input(f"Ingrese el numero {i+1}°: "))
    num_enteros.append(num)
    


print(f"""
            los numeros ingresados son: {num_enteros}
            los numeros ordenados de menor a mayor: {sorted(num_enteros)}
            los numeros ordenados de mayor a menor: {sorted(num_enteros, reverse=True)}
            """)    