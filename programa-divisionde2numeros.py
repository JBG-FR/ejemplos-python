# Calculo de IMC , comunica su nivel de salud y envía recomendacion.


nume = int(input("Ingrese un numero entero 1: "))
deno = int(input("Ingrese un numero entero 2: "))
coci = int(nume / deno)
rest = int(nume % deno)
print("La division del numero " + str(nume)+ " entre el numero " + str(deno) + " da como cociente " + str(coci) + " y residuo " + str(rest))
