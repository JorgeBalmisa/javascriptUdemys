import pygame
from twitchio.ext import commands
import os
import threading

# Ruta de la carpeta donde están los videos
VIDEO_FOLDER = r"E:\MemesTwitch"  # Cambia esta ruta a la de tus videos

TWITCH_TOKEN = "6fo492bzgi5lwh3t80rdiphq0zea6d"  # Token de Twitch

# Verificar si la carpeta de videos existe
if not os.path.exists(VIDEO_FOLDER):
    print(f"ADVERTENCIA: La carpeta {VIDEO_FOLDER} no existe.")
else:
    print(f"Carpeta de videos encontrada: {VIDEO_FOLDER}")

class MemeBot(commands.Bot):
    def __init__(self):
        super().__init__(
            token=TWITCH_TOKEN,  # Usa el token directamente
            prefix="!",  # Prefijo del bot
            initial_channels=["neosylux"]  # Canal de Twitch
        )
        print("Bot inicializado correctamente.")

    async def event_ready(self):
        print(f"Conectado como {self.nick}")
        print(f"Conectado a los canales: {self.connected_channels}")

    async def event_channel_points_redemption(self, payload):
        # Depuración: Verifica el contenido del payload
        print(f"Payload recibido: {payload}")

        if payload.reward.title == "GenMemes":  # Verifica el título de la recompensa
            print("¡Recompensa GenMemes canjeada!")
            # Crear un hilo para ejecutar el video sin bloquear el bot
            threading.Thread(target=open_test_window, daemon=True).start()
        else:
            print("El título de la recompensa no coincide.")

def open_test_window():
    print("Generando ventana...")
    pygame.init()

    # Crear la ventana
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Ventana de Test del Bot")
    screen.fill((0, 255, 0))  # Fondo verde
    pygame.display.update()

    # Bucle para mantener la ventana abierta
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()
    print("Ventana cerrada.")


# Inicia el bot
if __name__ == "__main__":
    try:
        print("Iniciando el bot...")
        bot = MemeBot()
        bot.run()
    except Exception as e:
        print(f"Error al iniciar el bot: {e}")