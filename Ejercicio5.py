#Declarar variables 
grados = int(input("Ingresa los grados: "))

#Proceso 
gradosc = grados - 273.15
gradosk = grados + 273.15
gradosf = 1.8 * grados + 32

#Resultados

print("Grados celsius= ", round(gradosc, 2))
print("Grados kelvin= ", round(gradosk, 2))
print("Grados fahrenheit= ", round(gradosf, 2))