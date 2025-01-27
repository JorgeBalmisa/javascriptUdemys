import random
import pygame
from twitchio.ext import commands
import os
import threading

# Ruta de la carpeta donde están los videos
VIDEO_FOLDER = r"E:\MemesTwitch"  # Cambia esta ruta a la de tus videos

# Configuración del bot de Twitch
class MemeBot(commands.Bot):
    def __init__(self):
        super().__init__(token="6fo492bzgi5lwh3t80rdiphq0zea6d",  # Tu token
                         prefix="!",  # Prefijo del bot
                         initial_channels=["neosylux"])  # Canal de Twitch

    async def event_ready(self):
        print(f"Conectado como {self.nick}")

    async def event_raw_reward_redeem(self, payload):
        if payload.reward.title == "GenMemes":  # Nombre de la recompensa exacta
            print("¡Recompensa GenMemes canjeada!")
            # Crear un hilo para ejecutar el video sin bloquear el bot
            threading.Thread(target=open_test_window).start()  # Llama a la función en un hilo separado

def open_test_window():
    # Test: Crear ventana de pygame y mantenerla abierta
    print("Generando ventana...")
    pygame.init()
    screen = pygame.display.set_mode((800, 600))  # Tamaño de la ventana
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

# Inicia el bot
if __name__ == "__main__":
    bot = MemeBot()
    bot.run()
