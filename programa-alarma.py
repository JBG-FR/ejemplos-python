
import time
import winsound

def alarma(tiempo):
    # Función que establece una alarma y muestra un mensaje
    print("La alarma está configurada para sonar en", tiempo, "segundos.")
    time.sleep(tiempo)
    print("¡¡¡ALERTA!!! ¡¡¡Es hora de despertar!!!")
    winsound.Beep(500, 3000)  # Reproducir un sonido de 1000 Hz durante 2 segundos

def main():
    try:
        segundos = int(input("Ingresa la cantidad de segundos para la alarma: "))
        if segundos <= 0:
            print("Por favor, ingresa un valor mayor que cero.")
        else:
            alarma(segundos)
    except ValueError:
        print("Por favor, ingresa un número válido de segundos.")

if __name__ == "__main__":
    main()
