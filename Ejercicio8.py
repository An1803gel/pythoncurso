#Declarar variable
numero = int(input("Ingesa un numero"))

#Procedimiento
if (numero < 0 and numero > -100):
    j = -1
    while (j >= -99):
       print(j)
       j = j - 2
elif (numero > 0 and numero < 100):
    j = 2
    while (j <= 100):
       print(j)
       j = j + 2
else :
    print("NO VALIDO")
