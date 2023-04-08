#Le A - Secteur feat. SCH (Clip Officiel)

from tkinter import *
from _get_videos_info import get_videos_info, get_videos_info_by_url
from _download import download_video_mp4,download_video_mp3
from time import sleep
from os import listdir, remove, startfile
import requests
from PIL import ImageTk, Image

videos_disponibles = False
numero_image = 0
liens = []

def download_mp4():
    global numero_image
    global liens
    global screen
    #####print("mp4")
    download_video_mp4(liens[numero_image][1])
    screen.destroy()

def download_mp3():
    global numero_image
    global liens
    global screen
    #####print("mp3")
    download_video_mp3(liens[numero_image][1])
    screen.destroy()

def get_videos_info_launch():
    global numero_image
    global liens
    
    numero_image = 0
    liens = []
    videos_disponibles = False
    if search_bar.get() != "":
        liens = get_videos_info(search_bar.get())
        videos_disponibles = True
                
        show_video_info(numero_image)

def get_videos_info_launch_by_url():
    global numero_image
    global liens
    
    numero_image = 0
    liens = []
    videos_disponibles = False
    if search_bar.get() != "":
        liens = get_videos_info_by_url(search_bar.get())
        #####print(liens)
        videos_disponibles = True
                
        show_video_info(numero_image)

def download_miniature(extrait):
    try :
        a = listdir("miniatures")[0]
        chaine = "miniatures/" + a
        remove(chaine)
    except IndexError : pass
    
    miniature = "https://i.ytimg.com/vi/"+extrait+"/sddefault.jpg"
    img_data = requests.get(miniature).content
    chaine2 = 'miniatures/'+extrait+".jpg"
    with open(chaine2, 'wb') as handler:
        handler.write(img_data)

def show_video_info(numero_image):
    
    global screen
    
    video_name = liens[numero_image][0]
    download_miniature(liens[numero_image][2])
    # affiche la miniature
    
    global bouton_left
    global bouton_right
    global miniature
    global miniature_img
    global text_video_range
    global text_numero_video
    global text_info_video
    global space2
    global bouton_download_mp4
    global bouton_download_mp3
    
    bouton_left.pack(side=LEFT)
    bouton_right.pack(side=RIGHT)
    
    try : text_video_range.pack_forget()
    except : pass
    text_video_range = "vidéo "+str(numero_image+1)+"/"+str(len(liens))
    text_video_range = Label(screen, text = text_video_range)
    text_video_range.configure(font=("Arial", 10))
    text_video_range.pack(side=TOP,pady=10)
    
    try : miniature.pack_forget()
    except : pass
    chaine = "miniatures/" + liens[numero_image][2] + ".jpg"
    miniature_img = ImageTk.PhotoImage(Image.open(chaine).resize((200,int(200*0.75))))
    miniature = Label(screen, image = miniature_img)
    miniature.pack(side = TOP,pady = 10)
    
    try : text_numero_video.pack_forget()
    except : pass
    text_numero_video = video_name
    text_numero_video = Label(screen, text = text_numero_video)
    text_numero_video.configure(font=("Arial", 10))
    text_numero_video.pack(side=TOP)
    
    try : text_info_video.pack_forget()
    except : pass
    text_info_video = liens[numero_image][3]
    text_info_video = Label(screen, text = text_info_video)
    text_info_video.configure(font=("Arial", 10))
    text_info_video.pack(side=TOP)
    
    try : space2.pack_forget()
    except : pass
    space2 = Label(screen, text = ".                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ")
    space2.configure(font=("Arial", 2))
    space2.pack(side=TOP,pady=10)
    try : bouton_download_mp4.pack_forget()
    except : pass
    bouton_download_mp4 = Button(screen,text="DOWNLOAD MP4 (max resolution, it may take some time (a lot))", command=download_mp4, padx=254, pady=5)
    bouton_download_mp4.pack(side=TOP, pady=10)
    try : bouton_download_mp3.pack_forget()
    except : pass
    bouton_download_mp3 = Button(screen,text="DOWNLOAD MP3 (it may take less time)", command=download_mp3, padx=284, pady=5)
    bouton_download_mp3.pack(side=TOP, pady=00)


def put_right_image():
    global numero_image
    try :
        numero_image += 1
        show_video_info(numero_image)
    except IndexError :
        numero_image -= 1
        #####print("error")

def put_left_image():
    global numero_image
    try :
        if numero_image != 0 :
            numero_image -= 1
            show_video_info(numero_image)
    except IndexError :
        numero_image += 1

screen = Tk()
screen.title("Download yt videos (by Silentium)")
screen.geometry("700x650")
screen.resizable(width=False, height=False)
screen.configure(background="#c8c8c8")

title = Label(screen, text = "DOWNLOAD YT VIDEO")
title.configure(font=("Arial", 20))
title.pack(side=TOP,pady=10)

indication_msg = Label(screen, text = "Enter a keywords or URL : ")
indication_msg.configure(font=("Arial", 10))
indication_msg.pack(side=TOP,pady=10)

text_video_range = ()
text_video_name = ()

search_bar = Entry(screen, width=60, font=('Arial 15'))
search_bar.pack(side=TOP)

bouton_research = Button(screen,text="SEARCH (that will take few time)", command=get_videos_info_launch, padx=244, pady=5)
bouton_research.pack(side=TOP, pady=10)
bouton_URL = Button(screen,text="I ENTERED A URL (that will take no time)", command=get_videos_info_launch_by_url, padx=224, pady=5)
bouton_URL.pack(side=TOP, pady=00)

space = Label(screen, text = "                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       ")
space.configure(font=("Arial", 2))
space.pack(side=TOP,pady=10)

bouton_left = Button(screen,text="<--", command=put_left_image, padx=5, pady=5)
bouton_right = Button(screen,text="-->", command=put_right_image, padx=5, pady=5)

try :
    a = listdir("miniatures")
    chaine = "miniatures/" + a[0]
    miniature_img = ImageTk.PhotoImage(Image.open(chaine).resize((50,50)))
    miniature = Label(screen, image = miniature_img)
except IndexError : pass


if videos_disponibles :
    numero_image = 0
    bouton_left.pack(side=LEFT)
    bouton_right.pack(side=RIGHT)
    
    chaine = "miniatures/" + 'KGM_2z4GW-8' + ".jpg"
    miniature_img = ImageTk.PhotoImage(Image.open(chaine).resize((50,50)))
    miniature = Label(screen, image = miniature_img)
    miniature.pack(side = TOP)

screen.mainloop()