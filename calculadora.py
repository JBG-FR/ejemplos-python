def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: No se puede dividir por cero"

def main():
    print("Calculadora básica")
    print("Operaciones disponibles:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")

    opcion = int(input("Selecciona una opción (1/2/3/4): "))

    if opcion in [1, 2, 3, 4]:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))

        if opcion == 1:
            resultado = sumar(num1, num2)
        elif opcion == 2:
            resultado = restar(num1, num2)
        elif opcion == 3:
            resultado = multiplicar(num1, num2)
        else:
            resultado = dividir(num1, num2)

        print("El resultado es:", resultado)
    else:
        print("Opción no válida. Por favor, selecciona una opción válida (1/2/3/4).")

if __name__ == "__main__":
    main()
