#Declarar variables
a = float(input("Ingresa un valor para a= "))
b = float(input("Ingresa un valor para b= "))
c = float(input("Ingresa un valor para c= "))

#Proceso
x1 = (-b + pow(b ** 2 - 4 * a * c, 1/2)) / (2 * a)
x2 = (-b - pow(b ** 2 - 4 * a * c, 1/2)) / (2 * a)

#Resultados 

print ("X1= ", round(x1, 2))
print ("X2= ", round(x2, 2))