# Escribir un programa que lea un entero positivo, 
#, introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta 
#. La suma de los 
# primeros enteros positivos puede ser calculada de la siguiente forma:

peso = float(input("Ingrese su peso en KG : "))
stat = float(input("Ingrese su statura en metros: "))
imc = peso / (stat ** 2)
print("su indice de masa corporal es : " + str(imc))
msj = print("Usted esta categorizado en el nivel: ")
if imc < 18.5:
    print(msj + "Desnutición" + " Se recomienta Alimentarse mejor")
elif 18.5 < imc < 24.9:
    print(msj + "Normal" + " Felcitaciones !!")
elif 24.9 < imc < 24.9:
    print(msj + "sobrepeso" + " Mejore su alimentación")
elif 30.0 < imc < 34.9:
    print(msj + "Obesidad CAT I" + "Mejor su alimentación")
elif 35.0 < imc < 39.9:
    print(msj + "Obesidad CAT II" + "Mejor su alimentación, vaya al medico")
else 49 < imc:
    print(msj + "Obesidad patologica extrema" + "mejore su alimentaión urgente!!!")





    sobrepeso")   
print("Ustes esta categorizado en el nivel; "
