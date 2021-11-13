arreglo = [0, "Eduardo", 2, 3, True, False, 5, 6, 7, "Angel"]
flag = False #Variable bandera 
numero = int(input("Ingesa un numero"))

for buscar in arreglo:
   if (numero == buscar):
      flag = True
      break  
   else:
      flag = False
      
if (flag == True):
      print("Numero encontrado")
else:
      print("No se encuentra el numero")