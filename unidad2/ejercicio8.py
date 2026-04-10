alumnos = []
materia_lengua = []
materia_matematica = []
materia_ingles = []
promed_estudiante = 0
promed_leng=0
promed_ingle=0
promed_mat=0

while True:
    cont=int(input("ingrese la cantidad de alumnos: (ingrese solo numeros): "))
    if cont:
        for i in range(cont):
            nombre = input(f"Ingrese el nombre del alumnos {i+1}: ")
            alumnos.append(nombre)
            for i in range (1):
            
                lengua  = int(input("Ingrese la nota de Lengua: "))
                matematica  = int(input("Ingrese la nota de Matematicas: "))
                ingles  = int(input("ingrese la nota de Ingles: "))
                materia_lengua.append(lengua)
                materia_matematica.append(matematica)
                materia_ingles.append(ingles)
                promed_estudiante =(materia_ingles[i]+
                                    materia_lengua[i]+
                                    materia_matematica[i]) / 3
                
                
                promed_leng= sum(materia_lengua) / len(materia_lengua)
                promed_ingle= sum(materia_ingles) / len(materia_ingles)
                promed_mat= sum(materia_matematica) / len(materia_matematica) 
            
    
        for i in range(cont):
            promedio = (materia_lengua[i] + materia_matematica[i] +  materia_ingles[i]) / 3

            print(f"""
                        PROMEDIO POR ALUMNO
                        Alumno: {alumnos[i]}
                        Lengua: {materia_lengua[i]}
                        Matemática: {materia_matematica[i]}
                        Inglés: {materia_ingles[i]}
                        Promedio: {promedio:.2f}
                """)
            print(f"""
                        PROMEDIO POR MATERIA
                        Lengua: {promed_leng:.2f}
                        Matemática: {promed_mat:.2f}
                        Inglés: {promed_ingle:.2f}
                    """)