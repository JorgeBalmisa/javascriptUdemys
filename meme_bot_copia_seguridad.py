import os
import random
import pygame
from twitchio.ext import commands

# Ruta de la carpeta donde están los videos
VIDEO_FOLDER = r"E:\MemesTwitch"

# Configuración del bot de Twitch
class MemeBot(commands.Bot):
    def __init__(self):
        super().__init__(token="6fo492bzgi5lwh3t80rdiphq0zea6d",  # Token del usuario
                         prefix="!",  # Prefijo del bot (opcional)
                         initial_channels=["neosylux"])  # Canal de Twitch

    async def event_ready(self):
        print(f"Conectado como {self.nick}")

    async def event_raw_reward_redeem(self, payload):
        if payload.reward.title == "GenMemes":  # Nombre exacto de la recompensa
            print("¡Recompensa GenMemes canjeada!")
            display_random_video()  # Llama a la función para mostrar un video

# Función para seleccionar un video aleatorio de la carpeta
def get_random_video(folder):
    try:
        files = [f for f in os.listdir(folder) if f.endswith(".mp4")]
        if not files:
            print("No se encontraron videos en la carpeta.")
            return None
        selected_video = random.choice(files)
        print(f"Video seleccionado: {selected_video}")
        return os.path.join(folder, selected_video)
    except Exception as e:
        print(f"Error al acceder a la carpeta de videos: {e}")
        return None

# Función para mostrar el video en una ventana usando pygame
def display_random_video():
    print("Generando meme...")
    filepath = get_random_video(VIDEO_FOLDER)
    if filepath:
        print(f"Reproduciendo video: {filepath}")
        try:
            # Inicializa pygame
            pygame.init()
            screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)  # Tamaño de la ventana
            pygame.display.set_caption("Meme Generator")
            print("Ventana de pygame creada")  # Esto confirmará si pygame está funcionando

            # Cargar y reproducir el video
            clock = pygame.time.Clock()
            movie = pygame.movie.Movie(filepath)  # Reemplaza con tu video
            movie_screen = pygame.Surface(movie.get_size()).convert()
            movie.set_display(screen)

            movie.play()

            # Bucle para mostrar el video
            running = True
            while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:  # Cerrar ventana
                        running = False

                screen.blit(movie_screen, (0, 0))
                pygame.display.update()
                clock.tick(30)

                if not movie.get_busy():
                    running = False

            movie.stop()
            pygame.quit()
        except Exception as e:
            print(f"Error al reproducir el video: {e}")
    else:
        print("No se pudo seleccionar un video.")

# Inicia el bot
if __name__ == "__main__":
    bot = MemeBot()
    bot.run()
