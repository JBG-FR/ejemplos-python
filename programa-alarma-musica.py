
import time
import pygame


def alarma(tiempo):
    # Función que establece una alarma y muestra un mensaje
    print("La alarma está configurada para sonar en", tiempo, "segundos.")
    time.sleep(tiempo)
    print("¡¡¡ALERTA!!! ¡¡¡Es hora de despertar!!!")
    
def reproducir_musica(ruta_archivo):
    pygame.mixer.init()
    pygame.mixer.music.load(ruta_archivo)
    pygame.mixer.music.play()

def main():
    try:
        segundos = int(input("Ingresa la cantidad de segundos para la alarma: "))
        print("Por favor, ingresa un número válido de segundos.")
    archivo_musica = "musica.mpeg.mpeg"  # Reemplaza con la ruta de tu archivo de música
    reproducir_musica(archivo_musica)
    input("Presiona Enter para detener la música...")  # Pausa el programa hasta que presiones Enter
    pygame.mixer.music.stop()

if __name__ == "__main__":
    main()


#def main():
#   try:
#        segundos = int(input("Ingresa la cantidad de segundos para la alarma: "))
#        if segundos <= 0:
#            print("Por favor, ingresa un valor mayor que cero.")
#        else:
#            alarma(segundos)
#    except ValueError:
#        print("Por favor, ingresa un número válido de segundos.")
#
#if __name__ == "__main__":
#    main()

