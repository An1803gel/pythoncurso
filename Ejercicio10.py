num = float(input("Ingresa un numero: "))
suma = 0
contador = 0
resultado = 0

while (num > 0):
    if (num > 0):
        suma = suma + num  
        contador = contador + 1
        num = float(input("Ingresa otro numero: "))

        
        
resultado = suma / contador      
print("Promedio es ", resultado)