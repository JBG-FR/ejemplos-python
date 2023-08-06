# Programa para medir la temperatura

temt = input("Ingrese la temperatura en celsius: ")
temp = int (temt)
if temp <= 0:
    print ("muy frio")
elif 0 < temp < 15:
    print ("frio")
else:
    print ("calor")
