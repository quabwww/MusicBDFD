import discord
from discord.ext import commands
import asyncio
import ffmpeg
from MusicaBot.buscar import search_youtube
from MusicaBot.audio import get_youtube_audio_url
import os
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

class MusicBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=discord.Intents().all())
        self.voice_client = None
        self.music_queue = []  # Cola para almacenar las URLs de música

    async def play_music(self, user_id, channel_id, guild_id, query):
        try:
            print(f"Buscando audio para la consulta: {query}")
            guild = self.get_guild(int(guild_id))
            if guild is None:
                print("No se pudo encontrar el servidor.")
                raise ValueError("El bot no está en el servidor especificado.")

            member = guild.get_member(int(user_id))
            if member is None:
                print("No se pudo encontrar el miembro.")
                raise ValueError("El usuario no se encuentra en el servidor.")

            # Verifica si el usuario está en un canal de voz
            if member.voice is None or member.voice.channel.id != int(channel_id):
                raise ValueError("El usuario no está en el canal de voz correcto.")

            # Busca el audio de YouTube basado en la consulta
            extract = search_youtube(query)
            url = get_youtube_audio_url(extract)

            if not url:
                raise ValueError("No se pudo obtener la URL del audio.")

            # Agrega la URL a la cola de música
            self.music_queue.append(url)
            print(f"Agregada a la cola: {url}. Cola actual: {self.music_queue}")

            # Conectar al canal de voz si no está conectado
            if self.voice_client is None:
                self.voice_client = await member.voice.channel.connect()

            # Iniciar la reproducción si no hay música sonando
            if not self.voice_client.is_playing():
                asyncio.create_task(self.start_playing())  # Reproducción en segundo plano

            # Enviar respuesta JSON inmediatamente
            return {"status": "success", "message": "Canción agregada a la cola", "queue": self.music_queue}

        except Exception as e:
            print(f"Error al reproducir música: {e}")
            return {"status": "error", "message": str(e)}

    async def start_playing(self):
        while self.music_queue:
            url = self.music_queue.pop(0)  # Obtiene la siguiente URL de la cola
            ffmpeg_options = {
                'options': '-vn'
            }

            try:
                # Reproducir el audio
                self.voice_client.play(discord.FFmpegPCMAudio(url, **ffmpeg_options))

                # Espera hasta que termine la reproducción
                while self.voice_client.is_playing():
                    await asyncio.sleep(1)

            except Exception as e:
                print(f"Error durante la reproducción: {e}")
                continue  # Continúa a la siguiente canción en la cola

        # Desconectar después de que se haya terminado la cola
        if self.voice_client and not self.music_queue:
            await self.voice_client.disconnect()
            self.voice_client = None

    async def show_queue(self):
        return self.music_queue  # Devuelve la cola actual

    async def on_ready(self):
        print(f"Bot conectado como {self.user} en el servidor.")

    async def start_bot(self):
        # Inicia el bot
        TOKEN = os.getenv("DISCORD_TOKEN")
        await self.start(TOKEN)
