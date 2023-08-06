
num1 = int(input("Ingresa numero a: "))
num2 = int(input("Ingresa numero b: "))
num3 = int(input("Ingresa numero c: "))

def suma(num1,num2,num3):
    """Función que SUMA"""
    sum = num1 + num2 + num3
    print("La suma es: " + str(sum))
    return
def mult(num1,num2,num3):
    """Función que MULTIPLICA"""
    mul = num1 * num2 * num3
    print("La multiplicacion es: " + str(mul))
    return
def algmate(num1,num2,num3):
    alg = num1 ** num2 - num3
    print("el algoritnmo es: " + str(alg))
    return
suma(num1,num2,num3)
mult(num1,num2,num3)
algmate(num1,num2,num3)
suma(2,4,5)
mult(4,5,6)
algmate(2,3,3)
