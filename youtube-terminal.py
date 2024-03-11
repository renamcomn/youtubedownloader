from pytube import YouTube
import os
import ssl
import sys

ssl._create_default_https_context = ssl._create_unverified_context

print("")
print("__  ______  __  __________  ______  ______   ____  ____ _       ___   ____    ____  ___    ____  __________ ")
print("\ \/ / __ \/ / / /_  __/ / / / __ )/ ____/  / __ \/ __ \ |     / / | / / /   / __ \/   |  / __ \/ ____/ __ \ ")
print("\  / / / / / / / / / / / / / __  / __/    / / / / / / / | /| / /  |/ / /   / / / / /| | / / / / __/ / /_/ / ");
print(" / / /_/ / /_/ / / / / /_/ / /_/ / /___   / /_/ / /_/ /| |/ |/ / /|  / /___/ /_/ / ___ |/ /_/ / /___/ _, _/ ")
print("/_/\____/\____/ /_/  \____/_____/_____/  /_____/\____/ |__/|__/_/ |_/_____/\____/_/  |_/_____/_____/_/ |_| ")
print("                                                                              by Renan Henrique @renamcomn")
print("")

print("[*] usage: python3 youtube-terminar.py W345dz mp3");

link = 'https://www.youtube.com/watch?v='
folder = '/Downloads'

def main(video, option):
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


if __name__ == "__main__":
    if len(sys.argv)<2:
        exit(1)
    else:
        video = sys.argv[1]
        option = sys.argv[2]
        main(video, option)
    
       

    

        
