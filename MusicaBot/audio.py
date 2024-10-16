import yt_dlp

def get_youtube_audio_url(video_url):
    try:
        # Configuración de opciones para yt-dlp
        ydl_opts = {
            'format': 'bestaudio/best',  # Selecciona el mejor formato de audio
            'noplaylist': True,          # Evitar descargar listas de reproducción enteras
            'quiet': True,               # Silenciar la salida
            'skip_download': True,       # Solo extraer URL
            'no_warnings': True,         # Evitar mostrar advertencias
            'ignoreerrors': True         # Continuar aunque haya errores
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Extraer información del video (sin descargar)
            info_dict = ydl.extract_info(video_url, download=False)
            if 'url' in info_dict:
                audio_url = info_dict['url']
                print(f"Audio URL: {audio_url}")
                return audio_url
            else:
                print("No se encontró una URL de audio válida.")
                return None

    except Exception as e:
        print(f"Error al obtener el audio: {e}")
        return None

