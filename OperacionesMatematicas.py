#Ejercicio 1
#Importar la libreria math 
import math
# Entradas: Declarar variables
print("Escribe el 1er numero: ")
numero1 = int(input())
numero2 = int(input("Escribe el 2do numero: "))

# Procesos: Calculo de las operaciones basicas 
suma = numero1 + numero2
resta  = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2
potencia1 = numero1 ** 2
potencia2 = pow(numero2, 3)
raiz_cuadrada1 = pow(numero1, 1/2)
raiz_cuadrada2 = math.sqrt(numero1)
raiz_cubica = pow(numero1, 1/3)
modulo = numero1 % numero2

# Salidas: Resultados de operaciones
print("Suma: ", suma)
print("Resta: ", resta)
print("Multiplicacion: ", multiplicacion)
print("Division: ", division)
print("Potencia1: ", potencia1)
print("Potencia2: ", potencia2)
print("Raiz cuadrada1: ", round(raiz_cuadrada1, 2))
print("Raiz cuadrada2: ", round(raiz_cuadrada2, 2))
print("Raiz cubica: ", round(raiz_cubica, 2))
print("Modulo: ", modulo)

print(f"Suma: {suma}")

#Contacatenacion (Union de textos)
#Casteo: Convertir un tipo de dato en otro tipo de dato
print("Suma: " + str(suma))