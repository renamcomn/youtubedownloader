from pytube import YouTube
import os
import ssl
import sys

ssl._create_default_https_context = ssl._create_unverified_context

link = 'https://www.youtube.com/watch?v='
folder = '/Downloads'

video = sys.argv[1]
option = sys.argv[2]

#Iniciar download
try:
    yt = YouTube(link+video)
    if option == "mp3":
        stream = yt.streams.filter(only_audio=True, file_extension='mp4').first()
        fl = stream.filesize
        filename = stream.download(folder)
        os.rename(filename, filename[:-4] + ".mp3")
    else:
        stream = yt.streams.filter(file_extension='mp4').get_highest_resolution()
        filename = stream.download(folder)
    
    print("Download completo")
except Exception as e:
    print("Erro ao fazer o download")