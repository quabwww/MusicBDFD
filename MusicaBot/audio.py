import yt_dlp
from pytube import YouTube
#s
def get_youtube_audio_url(video_url):
    yt = YouTube(video_url)
    audio_stream = yt.streams.filter(only_audio=True).first()
    print(audio_stream)
    return audio_stream.url

