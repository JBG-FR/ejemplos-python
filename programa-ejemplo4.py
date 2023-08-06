
paya = int(input("Ingrese el numero de payasos: "))
mune = int(input("Ingrese el numero de muñecas: "))
pato = (paya * 112) + (mune * 75)
patk = round(pato / 1000, 2)            
print("El peso total es: " + str(patk) + " KG")
