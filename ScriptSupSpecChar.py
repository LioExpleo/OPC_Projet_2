import os
import time

import requests
from bs4 import BeautifulSoup
import re #import de regular expression
from FctProjet2 import*
from FctScrapLivre import*
from Fct_Ecrire_CSV import*
import csv
import shutil
import re
import time

#Suppression des caractères spéciaux pour zipper les livres.

# Pour toutes les catégories
# 1-1 Récupérer un nom de catégorie pour nommer le fichier csv

    # Création du répertoire Csv si absent
    # Création des répertoires pour ranger les images et fichiers Csv
    #Recherche du dossier de travail
wd = os.getcwd()

WorkingDirectory = ("working directory is ", wd)
WorkingDirectory = str(wd)
WorkingDirectoryImage = WorkingDirectory + "/Image/"

#Création du répertoire ImageNew si inexistant
WorkingDirectoryImageNew = WorkingDirectory + "/ImageNew/"


DirSource = WorkingDirectoryImage
DirDest = WorkingDirectoryImageNew
src_files = os.listdir(DirSource)
dest_files = os.listdir(DirDest) #liste des fichiers dans le répertoire de destination

if not os.path.exists(WorkingDirectoryImageNew): # s'il n'existe pas de directory imageNew, on le créé
    os.makedirs(WorkingDirectoryImageNew)
    #Si le répertoire était existant, effacer son contenu
else:
    for fil_name in dest_files:
        FileOld = (str(DirDest) + str(fil_name))
        os.remove(FileOld)
        #print("relancer le script pour renommer les fichiers")
        #exit()

#print ("attente")
#time.sleep(2)

#récupérer la liste des fichiers du répertoire source
src_files = os.listdir(DirSource)
for fil_name in src_files: #pour chaque fichier du répertoire source
    full_file_name = os.path.join(DirSource,fil_name)
    if os.path.isfile(full_file_name): #
        shutil.copy(full_file_name,DirDest) #copy

for fil_name in dest_files:
        if fil_name.isalnum(): #Si pas de caractères spéciaux dans le fichier
            pass
        else:

        #if ("#" in fil_name):
            print(fil_name)
            fil_nameNew = re.sub("#"," ", fil_name)
            fil_nameNew = re.sub("\(", "_", fil_nameNew)
            fil_nameNew = re.sub("\)", "_", fil_nameNew)
            fil_nameNew = re.sub("\,", "_", fil_nameNew)
            fil_nameNew = re.sub(r"[^a-z+A-Z+0-9+-+.]", "", fil_nameNew)
            #fil_nameNew = re.sub(r"(\w|\d|\.\-)", "", fil_nameNew)

            file_oldname = os.path.join(DirDest, fil_name)
            file_newname_newfile = os.path.join(DirDest, fil_nameNew)
            #time.sleep(0.1)
            try:
            #if file_newname_newfile !="":
                os.rename(file_oldname,file_newname_newfile)
                print(fil_nameNew)
            except:
                print("")



#listimage = os.listdir(DirectoryDestination)

#for filename in files :
#        string = "Hey! What's up bro?"
 #       new_string = re.sub(r"[^a-zA-Z0-9]", "", string)
  #      print(new_string)

