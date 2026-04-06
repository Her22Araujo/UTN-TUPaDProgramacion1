###Cada día tiene cupos fijos:
###Hay 2 días de atención: Lunes y Martes.
###• Lunes: 4 turnos
###• Martes: 3 turnos
###Reglas
###1. Pedir nombre del operador (solo letras).
###2. Menú repetitivo hasta salir:
###1. Reservar turno
###2. Cancelar turno (por nombre)
###3. Ver agenda del día
###4. Ver resumen general
###5. Cerrar sistema
###3. Reservar:
###o Elegir día (1=Lunes, 2=Martes).
###o Pedir nombre del paciente (solo letras).
###o Verificar que no esté repetido en ese día (comparando con las variables
###ya cargadas).
###o Guardar en el primer espacio libre (ej. lunes1, lunes2…).
###4. Cancelar:
###o Elegir día.
###o Pedir nombre del paciente (solo letras).
###o Si existe, cancelar y dejar el espacio vacío ("").
###5. Ver agenda del día:
###4
###Programación 1
###TECNICATURA UNIVERSITARIA
###EN PROGRAMACIÓN
###o Mostrar los turnos del día en orden (Turno 1..N), indicando “(libre)” si
###está vacío.
###6. Resumen general:
###o Turnos ocupados y disponibles por día.
###o Día con más turnos (o empate)



lunes1 =""
lunes2=""
lunes3=""
lunes4=""
martes1=""
martes2=""
martes3=""


while True:
        
        name_op = input("Hola, Ingresa tu nombre: ").strip()

        if name_op.isalpha():
            print(f"Bienvenido {name_op}! \U0000270B")
            break
        else:
            print("Error, solo ingresa letras \U0000274C")

while True:

    print("Elige una opcion")
    opc = input("""
        1-Reservar Turno \U00002705
        2-Cancelar Turno \U0000274C
        3-Ver agenda del dia \U0000270D
        4-Ver resumen \U000023F3
        5-Salir del sistema \U0001F519
            """)
    if opc == "1":
        print("Reservar Turno")

        while True:
            elegir_dia = input("1- Lunes O 2- Martes: ")
            if elegir_dia in ("1","2"):
                break
            else:
                print("El dia seleccionado es incorrecto \U0000274C")
        
        while True:
            nomb_pct = input("Ingrese el nombre del paciente: ").strip()
            if nomb_pct.isalpha():
                break
            else:
                print("Error, ingrese solo letras \U0000274C")

        if elegir_dia == "1":
            if(nomb_pct == lunes1 or nomb_pct == lunes2 or nomb_pct == lunes3 or nomb_pct == lunes4):
                print("El paciente ya tiene turno (El turno asignado fue para el dia Lunes) \U0000274C")
            elif lunes1 =="":
                lunes1 = nomb_pct
                print("Turno agendado con exito, para dia Lunes 1° Turno \U00002705")
            elif lunes2 =="":
                lunes2 = nomb_pct
                print("Turno agendado con exito, para dia Lunes 2° Turno \U00002705")
            elif lunes3 =="":
                lunes3 = nomb_pct
                print("Turno agendado con exito, para dia Lunes 3° Turno \U00002705")
            elif lunes4 =="":
                lunes4 = nomb_pct
                print("Turno agendado con exito, para dia Lunes 4° Turno \U00002705")
            else:
                print("El Dia seleccionado tiene cupo completo \U0000274C")

        if elegir_dia == "2":
            if(nomb_pct == martes1 or nomb_pct == martes2 or nomb_pct == martes3):
                print("El paciente ya tiene turno (El turno asignado fue para el dia Martes) \U0000274C")
            elif martes1 =="":
                martes1 = nomb_pct
                print("Turno agendado con exito, para dia Martes 1° Turno \U00002705")
            elif martes2 =="":
                martes2 = nomb_pct
                print("Turno agendado con exito, para dia Martes 2° Turno \U00002705")
            elif martes3 =="":
                martes3 = nomb_pct
                print("Turno agendado con exito, para dia Martes 3° Turno \U00002705")    
            else:
                print("El Dia seleccionado tiene cupo completo \U0000274C")

    elif opc == "2":
        print("Cancelar Turno")

        while True:
            elegir_dia = input("1- Lunes O 2- Martes: ")
            if elegir_dia in ("1","2"):
                break
            else:
                print("El dia seleccionado es incorrecto \U0000274C")
        
        while True:
            nomb_pct = input("Ingrese el nombre del paciente: ").strip()
            if nomb_pct.isalpha():
                break
            else:
                print("Error, ingrese solo letras \U0000274C")

        verificacion = False
        
        if elegir_dia == "1":
            if lunes1 == nomb_pct:
                lunes1 = ""
                verificacion= True
            elif lunes2 == nomb_pct:
                lunes2 = ""
                verificacion= True
            elif lunes3 == nomb_pct:
                lunes3 = ""
                verificacion= True
            elif lunes4 == nomb_pct:
                lunes4 = ""
                verificacion= True

        else:
            if martes1 == nomb_pct:
                martes1 = ""
                verificacion = True
            elif martes1 == nomb_pct:
                martes1 = ""
                verificacion = True
            elif martes1 == nomb_pct:
                martes1 = ""
                verificacion = True
        
        if verificacion == True:
            print(f"Turno Cancelado paciente {nomb_pct}")
        else:
            print(f"Error el paciente {nomb_pct}, no se encuentra")


    elif  opc == "3":
        print("Ver agenda")
        
        while True:
            elegir_dia = input("1- Lunes O 2- Martes: ")
            if elegir_dia in ("1","2"):
                break
            else:
                print("El dia seleccionado es incorrecto \U0000274C")

        if elegir_dia == "1":
            print("----------DIA LUNES----------")
            print("Turno 1 :", lunes1 if lunes1 != "" else "(Dia Disponible)")
            print("Turno 2 :", lunes2 if lunes2 != "" else "(Dia Disponible)")
            print("Turno 3 :", lunes3 if lunes3 != "" else "(Dia Disponible)")
            print("Turno 4 :", lunes4 if lunes4 != "" else "(Dia Disponible)")

        else:
            print("----------DIA MARTES----------")
            print("Turno 1 :", martes1 if martes1 != "" else "(Dia Disponible)")
            print("Turno 2 :", martes2 if martes2 != "" else "(Dia Disponible)")
            print("Turno 3 :", martes3 if martes3 != "" else "(Dia Disponible)")
            



    elif  opc == "4":
        print("Ver resumen")

        oc_lun = 0
        if lunes1 !="": oc_lun +=1
        if lunes2 !="": oc_lun +=1
        if lunes3 !="": oc_lun +=1
        if lunes4 !="": oc_lun +=1

        oc_mart = 0 

        if martes1 !="": oc_mart +=1
        if martes2 !="": oc_mart +=1
        if martes3 !="": oc_mart +=1

        print(f"""
        ----------RESUMEN----------
        Lunes: {oc_lun} ocupados, {4 - oc_lun} Disponbles     
        Martes: {oc_mart} ocupados, {3 - oc_mart} Disponibles
                """)
        
        if oc_lun > oc_mart :
            print("El dia con mas turnos es el dia Lunes")
        elif oc_mart> oc_lun:
            print("El dia con mas turnos es el dia Martes")
        else:
            print("Ambos dias tiene la misma cantidad de turnos")
    elif  opc == "5":
        print("Salir del sistema")
        break
    else:
                print("Error opcion invalida \U0000274C")
    