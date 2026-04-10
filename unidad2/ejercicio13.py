puntajes = [450, 1200, 875, 990, 300, 1500, 640]
maxim = puntajes[0]
minim = puntajes[0]

for i in range(len(puntajes)):
    
    if puntajes[i] < maxim:
        maxim = puntajes[i]
        
    elif puntajes[i] > minim:
            minim = puntajes[i]


puntajes.sort()

num = 990

if num in puntajes:
    posicion=puntajes.index(num)

            
print(f"Ranking :")
print(*puntajes)
print(f"El {num} que buscas esta en la {posicion}")
print(f"{maxim} and {minim}")
