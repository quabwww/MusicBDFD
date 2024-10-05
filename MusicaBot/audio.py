import yt_dlp

def get_youtube_audio_url(video_url):
    ydl_opts = {
        'format': 'bestaudio[ext=m4a]/best',  # Selecciona el mejor audio disponible
        'extractaudio': True,  # Extrae solo el audio
        'audioformat': 'mp3',  # Convierte el audio a mp3 si es posible
        'quiet': True,  # Para evitar que imprima información innecesaria
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(video_url, download=False)

            # Intenta obtener la URL del audio
            audio_url = info_dict.get("url", None)

            if not audio_url:
                # Si no se encuentra la URL, lista los formatos disponibles
                formats = info_dict.get('formats', None)
                if formats:
                    for f in formats:
                        if f.get('ext') == 'mp3':  # Filtra por mp3
                            audio_url = f.get('url')
                            break  # Sal del bucle una vez que encuentres el primer mp3

            return audio_url
    except Exception as e:
        print(f"Error al extraer la URL: {e}")
        return None

