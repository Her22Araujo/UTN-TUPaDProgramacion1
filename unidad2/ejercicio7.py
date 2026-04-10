temp_max=[]
temp_min=[]
suma_max=0        
suma_min=0   
temperatura_maxima = 0
temperatura_minima = 0

for i in range(7):
    temp = int(input(f"ingresa las temperaturas deseadas para almacenar {i+1}: "))

    if temp <20:
        print("temperatura minima")
        suma_min=suma_min+int(temp)
        temp_min.append(temp)
        if temperatura_minima == 0 or temp < temperatura_minima or temperatura_minima < -100:
            temperatura_minima= temp
        
    elif temp >=20:
        
        print("temperatura maxima")  
        suma_max=suma_max + temp  
        temp_max.append(temp)
        if temp > temperatura_maxima:
            temperatura_maxima= temp
        
    else:
        print("dato ingresado erroneo")
        
promedio_max = suma_max / 7 
promedio_min = suma_min / 7 


print(f"""  temperaturas maximas {temp_max}
            temperaturas minimas {temp_min}
            
            los promedio:
                        temperatura Maximas: {promedio_max}
                        temperaturas Minimas: {promedio_min}
                        temperatura mas Alta: {temperatura_maxima}
                        temperatura mas baja: {temperatura_minima}
            """)