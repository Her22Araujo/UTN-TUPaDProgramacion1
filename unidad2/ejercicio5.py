alumnos_presentes= []
cont = 0
while True:

    op= input("Ingrese los nombres de los alumnos presentes ")

    if op.isalpha() and cont < 8:
        alumnos_presentes.append(op)
        cont = cont+1
        print(alumnos_presentes)
        print(cont)

    else:
        print("Desea agregar o quitar algun alumno de la lista? (Agregar/quitar o salir)")
        op2 = input("")

        if op2.lower() == "agregar":
            alum= input("Ingresa el nombre que deseas agregar: ")
            alumnos_presentes.append(alum)

        elif op2.lower() == "quitar":
            alum= input("Que alumno desea quitar ?")

            if alum in alumnos_presentes:
                alumnos_presentes.remove(alum)
                print(f"Lista actualizada {alumnos_presentes}")
            else:
                print("Alumno no encontrado, reintentarlo")
        elif op2.lower() == "salir":
            print("Saliendo del sistema")
            break
        else:
            print("Error, el dato ingresado no es valido")