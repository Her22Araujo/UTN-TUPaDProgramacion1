import random
lista_al_azar = []
lista_pares = []
lista_impares = []

for i in range(15):
    num = random.randint(1, 100)
    lista_al_azar.append(num)
    
    if num % 2 == 0:
        lista_pares.append(num)
    else:
        lista_impares.append(num)
print(f"""  La lista original es {lista_al_azar}
            la contidad de numeros pares es {len(lista_pares)} 
            y la cantidad de numeros impares es {len(lista_impares)} """)