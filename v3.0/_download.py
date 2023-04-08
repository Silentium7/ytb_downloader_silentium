from os import getlogin
from pytube import YouTube

def download_video_mp4(url):
    path = "C:/Users/"+str(getlogin())+"/Desktop"
    yt = YouTube(url)
    yt.streams.get_highest_resolution().download(path)
def download_video_mp3(url):pass

# download_video_mp4("https://www.youtube.com/watch?v=vIs6AWjhVv0")