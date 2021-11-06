# Entradas: Declarar variables
calificacion1 = float(input("Escribe la 1er calificacion: "))
calificacion2 = float(input("Escribe la 2da calificacion: "))
calificacion3 = float(input("Escribe la 3er calificacion: "))


 #Procesos: Calculo de las operaciones basicas

suma = calificacion1 + calificacion2 + calificacion3
promedio = suma / 3

print("Promedio= ", round(promedio, 2))

if (promedio > 5):
    print ("Aprobado")
else:
    print("Reprobado")