import random

def jugar_adivina_numero(intentos, numero_secreto):
    for intento in range(1, intentos + 1):
        intento_usuario = int(input(f"Intento {intento}/{intentos}. Ingresa un número: "))
        if intento_usuario == numero_secreto:
            print(f"¡Felicitaciones! ¡Adivinaste el número {numero_secreto} en {intento} intentos!")
            return True
        elif intento_usuario < numero_secreto:
            print("El número es mayor.")
        else:
            print("El número es menor.")
    print(f"Agotaste tus {intentos} intentos. El número secreto era {numero_secreto}. ¡Inténtalo nuevamente!")
    return False

def main():
    print("Bienvenido al juego de adivinar el número.")
    print("Estoy pensando en un número del 1 al 100.")
    numero_secreto = random.randint(1, 100)
    intentos = 7

    if jugar_adivina_numero(intentos, numero_secreto):
        print("Gracias por jugar. ¡Hasta la próxima!")
    else:
        print("¡Inténtalo nuevamente!")

if __name__ == "__main__":
    main()
