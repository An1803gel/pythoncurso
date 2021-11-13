#Declarar
agua = int(input("¿Cual es el nivel del agua?"))

if (agua > 6):
    print("Desbordamiento de agua en cisterna")
elif(agua == 6):
    print("Apagar bomba")
elif (4 <= agua < 6):
    print("Desacelerar bomba")
elif (2 <= agua < 4):
    print("Bomba trabajando")
elif (0 < agua < 2):
    print("Acelerar bomba de agua")
elif (agua == 0):
    print("Encender bomba de agua")
#elif (agua < 0):
    #print("Fuga en cisterna")
else :
    print("Fuga en cisterna")