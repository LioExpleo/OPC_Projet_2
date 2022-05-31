import requests
from bs4 import BeautifulSoup
import re #import de regular expression
import time
import csv

#fonction qui recherche la position précédente de ce que l'on veut récupérer avec charcherch et
#récupère jusqu'au caractere à ne pas récupéré défini en entrée EndChar
def Projet2Chaine(chaine, charCherch, EndChar):
    OutChaine =""
    req=""
    req = re.search(charCherch, chaine, re.I)
    index = req.end()
    while (((chaine[index]) != (EndChar)) and (index < req.endpos)):
        OutChaine = OutChaine + (chaine[index])
        # print(chaine[index])
        index = index + 1
    return(OutChaine)

def CherchPosit(chaine,charDeb,charFin):
    PositDeb = chaine.find(charDeb)
    PositFin = chaine.find(charFin)
    return (PositDeb, PositFin  )

def TelechFichier(urlsrc):
    #urlsrc = 'http://example.com/source'
    rsrc = requests.get(urlsrc)
    urldst = 'http://example.com/dest'
    rdst = requests.post(urldst, files={'file': rsrc.content})

def ErrTelechImgUrl(NbrError,ListName,ListUrl):
    for i in range(NbrError):
        NameImage = ListName[i]
        ImgUrl = ListUrl[i]
        print("Téléchargement des images suite erreur")
        print (NameImage)
        print(ImgUrl)

        try:  # télécharger les images
            # cheminFichier = ("\home\lionel\openclassrooms\projet2\Image\" + str(NameImage))
            urllib.request.urlretrieve(ImgUrl, NameImage)
            print ("Erreur téléchargement " + ImgUrl + "traitée ")
        # time.slepp(0.1)

        except:
            print("Image à télécharger de façon manuelle " + ImgUrl + " Url : " +ImgUrl)
            # print(Category)

