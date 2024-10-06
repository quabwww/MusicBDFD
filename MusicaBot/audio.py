import yt_dlp
#s
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
                formats = info_dict.get('formats', None)
                if formats:
                    for f in formats:
                        # En lugar de filtrar solo por mp3, toma cualquier formato de audio
                        if f.get('vcodec') == 'none':  # Asegura que es solo audio
                            audio_url = f.get('url')
                            break

            return audio_url
    except yt_dlp.utils.DownloadError as e:
        if "captcha" in str(e).lower():
            print("Se requiere captcha para este video. No se puede obtener el audio.")
        else:
            print(f"Error inesperado: {e}")
        return None
    except Exception as e:
        print(f"Error al extraer la URL: {e}")
        return None

