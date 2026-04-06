
###2. Permitir máximo 3 intentos para ingresar usuario y clave.
###3. Si falla 3 veces: mostrar “Cuenta bloqueada” y terminar.
###4. Si ingresa bien: mostrar un menú repetitivo (usar while) hasta elegir salir:
###1. Ver estado de inscripción (mostrar “Inscripto”)
###2. Cambiar clave (pedir nueva clave y confirmación; deben
###coincidir)
###3. Mostrar mensaje motivacional (1 frase)
###4. Salir

###CREDENCIALES CORRECTAS###
us = "alumno"
passw = "python123"

validacion = 3

for i in range(3):
        usuario=input("Bienvnido ingresa tu usuario: ").strip()
        contraseña = input("Ingresa la contraseña: ")

        if (validacion <= 3 and usuario == us and contraseña == passw):
            print("Ingreso Correcto")
            while True:
                eleccion = input("""
                     1-Estado de inscripcion \U00002705
                      2-Cambiar clave \U0001F511 
                       3-Mostrar mensaje \U0001F4E7
                        4-Salir del sistema \U0000274C
                    """)
                if (eleccion.isdigit() and eleccion == "1"):

                    print("Estas inscripto \U00002705")

                elif(eleccion.isdigit() and eleccion == "2"):

                    print("ingresa la nueva clave \U0001F511 ")
                    print("la contraseña debe tener minimo 6 digitos")
                    newpass = input("")
                    if len(newpass)> 6:
                        passw=newpass
                        print("se genero la nueva clave exitosamente")
                        print(f"Tu nueva clave es : {passw} ")
                    else:
                        print("\U0000274C Error datos ingresados invalidos \U0000274C")

                elif(eleccion.isdigit() and eleccion == "3"):
                    
                    print("El secreto del éxito verdadero es el CONOCIMIENTO unido a la ACCIÓN. \U0001F618") 

                elif(eleccion.isdigit() and eleccion == "4"):

                    print("Gracias por usar este sistema. \U0001F642")
                    break

                else:

                    print("\U000026A0 Error eleccion invalida \U000026A0")
        else:
            validacion -=1
            print(f"Error al ingresar los datos, te quedan {validacion} intentos.")
print("\U000026A0 Sistema bloqueado \U000026A0")
        