from tkinter import *
from pytube import YouTube
import urllib.request
import requests
from os import mkdir,remove, listdir

def get_videos_info_by_url(lien):
    miniature_path = YouTube(lien).thumbnail_url[23:34]
    number_views = str(YouTube(lien).views)
    if len(number_views) > 6 : number_views = number_views[0:len(number_views)-6] + "M"
    elif len(number_views) > 4 : number_views = number_views[0:len(number_views)-3] + "k"
    chaine_informations = "Video by " + str(YouTube(lien).author)+", "+str(number_views)+" views"
    infos = [[YouTube(lien).title, lien, miniature_path,chaine_informations]]
    return infos


def get_videos_info(keywords):
    # suppression des miniatures précédentes
    miniatures = listdir("miniatures")
    for i in miniatures:
        chaine = "miniatures/"+str(i)
        remove(chaine)

    # recherche
    recherche = keywords
    recherche_finale = ""
    for i in range(len(recherche)):
        if recherche[i] == " ":
            recherche_finale += "+"
        else : recherche_finale += recherche[i]
    url = 'https://www.youtube.com/results?search_query=' + recherche_finale

    # recupère le coude source
    fp = urllib.request.urlopen(url)
    mybytes = fp.read()
    HTML_code = mybytes.decode("utf8")
    fp.close()

    liens = []
    ids = []
    
    for i in range(len(HTML_code)):
        if HTML_code[i:i+10] == 'videoIds":':
            if not HTML_code[i+12:i+23] in ids:
                ids.append(HTML_code[i+12:i+23])
                #print(int(100*i/len(HTML_code)),"%")
                lien = "https://www.youtube.com/watch?v="+HTML_code[i+12:i+23]
                miniature_path = HTML_code[i+12:i+23]
                number_views = str(YouTube(lien).views)
                if len(number_views) > 6 : number_views = number_views[0:len(number_views)-6] + "M"
                elif len(number_views) > 4 : number_views = number_views[0:len(number_views)-3] + "k"
                chaine_informations = "Video by " + str(YouTube(lien).author)+", "+str(number_views)+" views"
                infos = [YouTube(lien).title, lien, miniature_path,chaine_informations]
                liens.append(infos)


    #print(liens)
    return liens
