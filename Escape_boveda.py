### VARIABLES DEL PROGRAMA

energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
ant_spam = 3

###AGENTE

print("¡¡Identifíquese!!")

name_us = input("Ingrese su nombre: ").strip()

while not name_us.isalpha():
    name_us = input("Error. Ingrese solo letras: ").strip()

print(f"Bienvenido {name_us}, tenemos una nueva misión para ti.")


while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:

    print(f"""
Agente {name_us}, necesitamos desbloquear 3 cerraduras.

ENERGIA: {energia}
TIEMPO: {tiempo}
CERRADURAS ABIERTAS: {cerraduras_abiertas}
ALARMA: {alarma}
""")

    menu = input("""
1- FORZAR LA CERRADURA
2- HACKEAR EL PANEL
3- DESCANSAR

Elige una opción: """)

    while menu.isdigit() == False or menu not in ["1", "2", "3"]:
        menu = input("Error. Ingresa 1, 2 o 3: ")

    ###FORZAR CERRADURA
    if menu == "1":

        energia -= 20
        tiempo -= 2
        ant_spam -= 1

        print("Estas forzando la cerradura...")


        if ant_spam == 0:
            print("¡ALARMA ACTIVADA!")
            print("Forzaste la cerradura 3 veces seguidas.")
            alarma = True

        else:

            
            if energia < 40:

                print("""
RIESGO DE ALARMA
Debes ingresar un número del 1 al 3
""")

                num = input("Número: ")

                while num.isdigit() == False or num not in ["1", "2", "3"]:
                    num = input("Error. Ingresa 1, 2 o 3: ")

                if num == "3":
                    print("¡¡ALARMA ACTIVADA!!")
                    alarma = True

                elif num == "1":
                    print("¡CERRADURA ABIERTA!")
                    cerraduras_abiertas += 1

                else:
                    print("Casi... vuelve a intentarlo.")

            else:
                print("¡CERRADURA ABIERTA!")
                cerraduras_abiertas += 1

    ###HACKEAR
    elif menu == "2":

        ant_spam = 3
        energia -= 10
        tiempo -= 3

        print("Hackeando panel...")

        for paso in range(1, 5):
            print(f"Paso {paso}/4 completado")
            codigo_parcial += "A"

        print(f"Código parcial: {codigo_parcial}")

        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            codigo_parcial = ""
            print("¡Eres todo un hacker! Se abrió una cerradura.")

    ###DESCANSAR
    elif menu == "3":

        ant_spam = 3
        tiempo -= 1
        energia += 15

        if energia > 100:
            energia = 100

        if alarma == True:
            energia -= 10
            print("La alarma está activada. Pierdes 10 de energía extra.")

        print("Descansaste y recuperaste energía.")

    
    if cerraduras_abiertas == 3:
        print(f"""
¡¡Ganaste {name_us}!!
Abriste las 3 cerraduras y escapaste de la bóveda.
""")
        break

    if alarma == True and tiempo <= 3 and cerraduras_abiertas < 3:
        print("""
¡¡Perdiste!!
La alarma bloqueó la bóveda.
""")
        break

    if energia <= 0 or tiempo <= 0:
        print("""
¡¡Perdiste!!
Te quedaste sin energía o sin tiempo.
""")
        break