
#Solicitar números al usuario hasta que ingrese el cero.
#Por cada uno, mostrar la suma de sus dígitos.
#Al finalizar, mostrar la sumatoria
#de todos los números ingresados y la suma de sus dígitos.
#Reutilizar la misma función realizada en el ejercicio 2.

numero=int(input("Números a procesar: "))


def sumaDigitos(numero):
    suma=0
    while numero!=0:
        digito=numero%10
        suma=suma+digito
        numero=numero//10
    return suma

def sumaNumeros(numero):
    sumanum=0
    while numero!=0:
        sumanum=sumanum+numero
    return sumanum

while numero!=0:
    print("Suma de digitos es :" + str(sumaDigitos(numero)))
    print("Suma de Numeros es :" + str(sumaNumeros(numero)))
