# Calculo de IMC , comunica su nivel de salud y envía recomendacion.

peso = float(input("Ingrese su peso en KG : "))
stat = float(input("Ingrese su statura en metros: "))
imc = peso / (stat ** 2)
print("su indice de masa corporal es : " + str(round(imc,2)))
msj = "Usted esta categorizado en el nivel: "
if imc <= 18.5:
    print(msj + "Desnutición" + " Se recomienta Alimentarse mejor")
elif 18.5 < imc <= 24.9:
    print(msj + "Normal" + " Felcitaciones !!!")
elif 24.9 < imc <= 29.9:
    print(msj + "sobrepeso" + " Mejore su alimentación")
elif 29.90 < imc <= 34.9:
    print(msj + "Obesidad CAT I , Mejor su alimentación visite al medico")
elif 34.9 < imc <= 39.9:
    print(msj + "Obesidad CAT II Mejor su alimentación, vaya al medico con cierta urgencia")
else :
    print(msj + "Obesidad patologica extrema mejore su alimentaión urgente!!!")
