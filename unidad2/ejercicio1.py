notas_estudiantes = []
cont = 10

for i in range(cont):
    nota= int(input(f"Por favor ingrese la nota del alumno: {i+1} "))
    notas_estudiantes.append(nota)  


nota_alta = notas_estudiantes[0]
nota_baja = notas_estudiantes[0]
suma=0
for nota in notas_estudiantes:
    suma = suma + nota
    if nota >= nota_alta:
        nota_alta = nota
        
    elif nota <= nota_baja:
        nota_baja = nota
        
promedio = suma / cont 

print(f"La nota mas alta fue {nota_alta}, la nota mas baja fue {nota_baja}, y el promedio de notas fue {promedio}")