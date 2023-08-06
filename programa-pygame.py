
import pygame

def reproducir_musica(ruta_archivo):
    pygame.mixer.init()
    pygame.mixer.music.load(ruta_archivo)
    pygame.mixer.music.play()

def main():
    archivo_musica = "musica.mpeg.mpeg"
    reproducir_musica(archivo_musica)
    input("Presiona Enter para detener la música...")  # Pausa el programa hasta que presiones Enter
    pygame.mixer.music.stop()

if __name__ == "__main__":
    main()
