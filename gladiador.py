juego = True

while juego == True:

    print("Bienvenido a la lucha de Gladiadores!!")
    name = str(input("Ingresa tu nombre de guerrero!: \U0001F977  " ))
    if name.isalpha():
        break
    else:    
        print("Error de novato! ingresa solo letras Guerrero!!")

print(f"Ese es el verdadero nombre de un Guerrero!")
print(f"Estas listo para la batalla {name}?")
print("\U0001FA93 COMIENZA LA BATALLA \U0001FA93")

vida_gladiador = 100
vida_enemigo = 100
pociones = 3
daño_atack_pesado = 15
daño_enemigo = 12

#Combate
while vida_enemigo >0 and vida_gladiador >0 :
    print(f""" {name} TU VIDA : {vida_gladiador}  \U0001F499  VIDA DEL ENEMIGO: {vida_enemigo} \U0001F5A4  TUS POCIONES: {pociones} \U0001FAD9
        """)
    print("Elige tu ataque! \U000100C9 ")
    atack = input("""
                \U00002488 Ataque Pesado    
                \U00002489 Rafaga Veloz
                \U0000248A Curar  
                """).strip()
    if atack.isdigit() and atack == "1": #and vida_enemigo>20:
        print("Ataque Pesado \U0000274C")
        if vida_enemigo <=20:
            print("Ataque Critico \U00002757 ")
            daño_critico = daño_atack_pesado * 1.5
            vida_enemigo = vida_enemigo - daño_critico
            print(f"vida enemigo: {vida_enemigo}")
        
        else:

            vida_enemigo = vida_enemigo - daño_atack_pesado
            print(f"{vida_enemigo}")

    elif atack.isdigit() and atack == "2":
        print("Rafaga Veloz \U0001F343") 
        for i in range (3):
            rafaga = 5 
            vida_enemigo = vida_enemigo - rafaga
            print(f"Golpe conectado por 5 de daño!")
            print(f"vida del enemigo {vida_enemigo}")
            if vida_enemigo == 0:
                break


    elif atack.isdigit() and atack == "3":
        print("Curar \U0001F90D")
        if pociones != 0:
            poty = 30
            vida_gladiador = vida_gladiador + poty
            pociones = pociones - 1 
            print(f"Te quedan {pociones} \U00002757")
            print (f"Te estas curando.. resiste + HP{vida_gladiador} \U0001F496")
        else: 
            print("\U0000274C No te quedan pociones Guerrero \U0000274C \U00002757")    

    else:
        print("Error, ingresa un numero valido ")

    if vida_enemigo < 0:

        vida_enemigo = 0
    
    if vida_gladiador < 0:

        vida_gladiador = 0
    
    if vida_enemigo > 0:
        vida_gladiador = vida_gladiador - daño_enemigo
        print("El enemigo te a atacado! \U0001F916 ")

if vida_gladiador>0:
    print("Felicidades Guerrero! GANASTE\U00002757 \U00002757 ")
else:
    print("\U0000274C Has caido en batalla, PERDISTE\U0000274C \U00002757")