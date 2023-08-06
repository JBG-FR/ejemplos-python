def es_primo(numero):
    # Función que verifica si un número es primo
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def obtener_primos(N):
    # Función que obtiene los primeros N números primos
    primos = []
    numero = 2
    while len(primos) < N:
        if es_primo(numero):
            primos.append(numero)
        numero += 1
    return primos

def main():
    # Función principal del programa
    try:
        N = int(input("Ingresa un número para obtener los primeros N números primos: "))
        if N <= 0:
            print("El número debe ser mayor que cero.")
        else:
            primos = obtener_primos(N)
            print(f"Los primeros {N} números primos son: {primos}")
    except ValueError:
        print("Por favor, ingresa un número válido.")

# Llamamos a la función 'main' para ejecutar el programa
if __name__ == "__main__":
    main()
